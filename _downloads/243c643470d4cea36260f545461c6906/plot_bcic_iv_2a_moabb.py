"""
Cropped Decoding on BCIC IV 2a Competition Set with skorch and moabb.
==============================================

"""

# Authors: Maciej Sliwowski
#          Robin Tibor Schirrmeister
#          Lukas Gemein
#          Hubert Banville
#
# License: BSD-3


import numpy as np
import torch
from torch import optim

from braindecode.datautil.windowers import create_windows_from_events
from braindecode.classifier import EEGClassifier
from braindecode.datasets import MOABBDataset
from braindecode.losses import CroppedNLLLoss
from braindecode.models.deep4 import Deep4Net
from braindecode.models.shallow_fbcsp import ShallowFBCSPNet
from braindecode.models.util import to_dense_prediction_model
from braindecode.scoring import CroppedTrialEpochScoring
from braindecode.util import set_random_seeds

model_name = "shallow"  # 'shallow' or 'deep'
cuda = torch.cuda.is_available()
device = 'cuda' if cuda else 'cpu'

set_random_seeds(seed=20190706, cuda=cuda)

input_time_length = 1000
n_classes = 4
n_chans = 26 # TODO: should be 22 of course
if model_name == "shallow":
    model = ShallowFBCSPNet(
        n_chans,
        n_classes,
        input_time_length=input_time_length,
        final_conv_length=30,
    )
elif model_name == "deep":
    model = Deep4Net(
        n_chans,
        n_classes,
        input_time_length=input_time_length,
        final_conv_length=2,
    )

to_dense_prediction_model(model)

if cuda:
    model.cuda()

with torch.no_grad():
    dummy_input = torch.tensor(
        np.ones((1, n_chans, input_time_length, 1), dtype=np.float32),
        device=device,
    )
    n_preds_per_input = model(dummy_input).shape[2]


dataset = MOABBDataset(dataset_name="BNCI2014001", subject_ids=[1])

windows_dataset = create_windows_from_events(
    dataset, trial_start_offset_samples=-125, trial_stop_offset_samples=1000,
    supercrop_size_samples=1000, supercrop_stride_samples=n_preds_per_input,
    drop_samples=False, mapping={1:0, 2:1, 3:2, 4:3})


class TrainTestBCICIV2aSplit(object):
    def __call__(self, dataset, y, **kwargs):
        splitted = dataset.split('session')
        return splitted['session_T'], splitted['session_E']


cropped_cb_train = CroppedTrialEpochScoring(
    "accuracy",
    name="train_trial_accuracy",
    lower_is_better=False,
    on_train=True,
    input_time_length=input_time_length,
)
cropped_cb_train_f1_score = CroppedTrialEpochScoring(
    "f1_macro",
    name="train_f1_score",
    lower_is_better=False,
    on_train=True,
    input_time_length=input_time_length,
)
cropped_cb_valid = CroppedTrialEpochScoring(
    "accuracy",
    on_train=False,
    name="valid_trial_accuracy",
    lower_is_better=False,
    input_time_length=input_time_length,
)
cropped_cb_valid_f1_score = CroppedTrialEpochScoring(
    "f1_macro",
    name="valid_f1_score",
    lower_is_better=False,
    on_train=False,
    input_time_length=input_time_length,
)
# MaxNormDefaultConstraint and early stopping should be added to repeat previous braindecode

clf = EEGClassifier(
    model,
    criterion=CroppedNLLLoss,
    optimizer=optim.AdamW,
    train_split=TrainTestBCICIV2aSplit(),
    optimizer__lr=0.0625 * 0.01,
    optimizer__weight_decay=0,
    batch_size=32,
    callbacks=[
        ("train_trial_accuracy", cropped_cb_train),
        ("train_trial_f1_score", cropped_cb_train_f1_score),
        ("valid_trial_accuracy", cropped_cb_valid),
    ],
    device=device,
)

clf.fit(windows_dataset, y=None, epochs=1)
