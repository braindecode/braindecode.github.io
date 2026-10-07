Braindecode package version: 1.8.1

Documentation scope: https://braindecode.org/dev/

Source commit: [f86998476aaf86ea56b4c913e37fb243f6926e1b](https://github.com/braindecode/braindecode/tree/f86998476aaf86ea56b4c913e37fb243f6926e1b)

Canonical HTML: [ShallowFBCSPNet model reference](https://braindecode.org/dev/generated/braindecode.models.ShallowFBCSPNet.html)

---

<a id="braindecode-models-shallowfbcspnet"></a>

# braindecode.models.ShallowFBCSPNet

### *class* braindecode.models.ShallowFBCSPNet(n_chans=None, n_outputs=None, n_times=None, n_filters_time=40, filter_time_length=25, n_filters_spat=40, pool_time_length=75, pool_time_stride=15, final_conv_length='auto', conv_nonlin=<class 'braindecode.modules.activation.Square'>, pool_mode='mean', activation_pool_nonlin=<class 'braindecode.modules.activation.SafeLog'>, split_first_layer=True, batch_norm=True, batch_norm_alpha=0.1, drop_prob=0.5, chs_info=None, input_window_seconds=None, sfreq=None)

Shallow ConvNet model from Schirrmeister et al (2017) [[Schirrmeister2017]](#r9432a19f6121-schirrmeister2017).

Convolution

![ShallowNet Architecture](https://onlinelibrary.wiley.com/cms/asset/221ea375-6701-40d3-ab3f-e411aad62d9e/hbm23730-fig-0002-m.jpg)

Model described in [[Schirrmeister2017]](#r9432a19f6121-schirrmeister2017).

* **Parameters:**
  * **n_chans** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Number of EEG channels.
  * **n_outputs** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Number of outputs of the model. This is the number of classes
    in the case of classification.
  * **n_times** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Number of time samples of the input window.
  * **n_filters_time** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Number of temporal filters.
  * **filter_time_length** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Length of the temporal filter.
  * **n_filters_spat** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Number of spatial filters.
  * **pool_time_length** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Length of temporal pooling filter.
  * **pool_time_stride** ([*int*](https://docs.python.org/3/builtins/functions.html#int)) – Length of stride between temporal pooling filters.
  * **final_conv_length** ([*int*](https://docs.python.org/3/builtins/functions.html#int) *|* [*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) – Length of the final convolution layer.
    If set to “auto”, length of the input signal must be specified.
  * **conv_nonlin** ([`type`](https://docs.python.org/3/builtins/functions.html#type)[[`Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)] | [`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)) – Non-linear module class to be used after convolution layers.
    For backward compatibility, callables are also accepted and wrapped
    with [`Expression`](wrapper/braindecode.modules.Expression.html#braindecode.modules.Expression).
  * **pool_mode** ([*str*](https://docs.python.org/3/builtins/stdtypes.html#str)) – Method to use on pooling layers. “max” or “mean”.
  * **activation_pool_nonlin** ([`type`](https://docs.python.org/3/builtins/functions.html#type)[[`Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)]) – Non-linear module class to be used after pooling layers.
  * **split_first_layer** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) – Split first layer into temporal and spatial layers (True) or just use temporal (False).
    There would be no non-linearity between the split layers.
  * **batch_norm** ([*bool*](https://docs.python.org/3/builtins/functions.html#bool)) – Whether to use batch normalisation.
  * **batch_norm_alpha** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) – Momentum for BatchNorm2d.
  * **drop_prob** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) – Dropout probability.
  * **chs_info** ([*list*](https://docs.python.org/3/builtins/stdtypes.html#list) *of* [*dict*](https://docs.python.org/3/builtins/stdtypes.html#dict)) – Information about each individual EEG channel. This should be filled with
    `info["chs"]`. Refer to [`mne.Info`](https://mne.tools/stable/generated/mne.Info.html#mne.Info) for more details.
  * **input_window_seconds** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) – Length of the input window in seconds.
  * **sfreq** ([*float*](https://docs.python.org/3/builtins/functions.html#float)) – Sampling frequency of the EEG recordings.
* **Raises:**
  [**ValueError**](https://docs.python.org/3/builtins/exceptions.html#ValueError) – If some input signal-related parameters are not specified: and can not be inferred.

### Notes

If some input signal-related parameters are not specified,
there will be an attempt to infer them from the other parameters.

### References

<a id="r9432a19f6121-schirrmeister2017"></a>
[Schirrmeister2017] 

Schirrmeister, R. T., Springenberg, J. T., Fiederer,
L. D. J., Glasstetter, M., Eggensperger, K., Tangermann, M., Hutter, F.
& Ball, T. (2017).
Deep learning with convolutional neural networks for EEG decoding and
visualization.
Human Brain Mapping , Aug. 2017.
Online: [http://dx.doi.org/10.1002/hbm.23730](http://dx.doi.org/10.1002/hbm.23730)



### Hugging Face Hub integration

When the optional `huggingface_hub` package is installed, all models
automatically gain the ability to be pushed to and loaded from the
Hugging Face Hub. Install with:

```default
pip install braindecode[hub]
```

**Pushing a model to the Hub:**

```default
from braindecode.models import ShallowFBCSPNet

# Train your model
model = ShallowFBCSPNet(n_chans=22, n_outputs=4, n_times=1000)
# ... training code ...

# Push to the Hub
model.push_to_hub(
    repo_id="username/my-shallowfbcspnet-model",
    commit_message="Initial model upload",
)
```

**Loading a model from the Hub:**

```default
from braindecode.models import ShallowFBCSPNet

# Load pretrained model
model = ShallowFBCSPNet.from_pretrained("username/my-shallowfbcspnet-model")

# Load with a different number of outputs (head is rebuilt automatically)
model = ShallowFBCSPNet.from_pretrained("username/my-shallowfbcspnet-model", n_outputs=4)
```

**Extracting features and replacing the head:**

```default
import torch

x = torch.randn(1, model.n_chans, model.n_times)
# Extract encoder features (consistent dict across all models)
out = model(x, return_features=True)
features = out["features"]

# Replace the classification head
model.reset_head(n_outputs=10)
```

**Saving and restoring full configuration:**

```default
import json

config = model.get_config()            # all __init__ params
with open("config.json", "w") as f:
    json.dump(config, f)

model2 = ShallowFBCSPNet.from_config(config)    # reconstruct (no weights)
```

All model parameters (both EEG-specific and model-specific such as
dropout rates, activation functions, number of filters) are automatically
saved to the Hub and restored when loading.

See [Loading and Adapting Pretrained Foundation Models](../auto_examples/model_building/plot_load_pretrained_models.html#load-pretrained-models) for a complete tutorial.

<!-- !! processed by numpydoc !! -->

<a id="examples-using-braindecode-models-shallowfbcspnet"></a>

## Examples using `braindecode.models.ShallowFBCSPNet`

<!-- start-sphx-glr-thumbnails -->
<!-- thumbnail-parent-div-open -->
* [Simple training on MNE epochs](../auto_examples/model_building/plot_basic_training_epochs.html)

* [Cropped Decoding on BCIC IV 2a Dataset](../auto_examples/model_building/plot_bcic_iv_2a_moabb_cropped.html)

* [Basic Brain Decoding on EEG Data](../auto_examples/model_building/plot_bcic_iv_2a_moabb_trial.html)

* [How to train, test and tune your model?](../auto_examples/model_building/plot_how_train_test_and_tune.html)

* [Hyperparameter tuning with scikit-learn](../auto_examples/model_building/plot_hyperparameter_tuning_with_scikit-learn.html)

* [Convolutional neural network regression model on fake data.](../auto_examples/model_building/plot_regression.html)

* [Training a Braindecode model in PyTorch](../auto_examples/model_building/plot_train_in_pure_pytorch_and_pytorch_lightning.html)

* [Benchmarking eager and lazy loading](../auto_examples/datasets_io/benchmark_lazy_eager_loading.html)

* [Fingers flexion cropped decoding on BCIC IV 4 ECoG Dataset](../auto_examples/advanced_training/bcic_iv_4_ecog_cropped.html)

* [Data Augmentation on BCIC IV 2a Dataset](../auto_examples/advanced_training/plot_data_augmentation.html)

* [Searching the best data augmentation on BCIC IV 2a Dataset](../auto_examples/advanced_training/plot_data_augmentation_search.html)

* [Interpretability of EEG Decoders](../auto_examples/advanced_training/plot_interpretability.html)

* [Sparse autoencoders on the activations of a motor-imagery decoder](../auto_examples/advanced_training/plot_sae_activation_analysis.html)

* [Fingers flexion decoding on BCIC IV 4 ECoG Dataset](../auto_examples/applied_examples/bcic_iv_4_ecog_trial.html)

<!-- thumbnail-parent-div-close -->
