Braindecode package version: 1.8.1

Documentation scope: https://braindecode.org/dev/

Source commit: [2426ddc34f182a71959defab75f5585d6832c659](https://github.com/braindecode/braindecode/tree/2426ddc34f182a71959defab75f5585d6832c659)

Canonical HTML: [API and model input conventions](https://braindecode.org/dev/api.html)

---

<a id="api-reference"></a>

<a id="module-braindecode"></a>

<a id="braindecode-api-reference"></a>

# Braindecode API Reference

<!-- !! processed by numpydoc !! -->

<a id="models"></a>

## Models

Model zoo availables in braindecode. The models are implemented as `PyTorch`
[`torch.nn.Module`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module) and can be used for various EEG decoding ways tasks.

All the models have the convention of having the signal related parameters named the
same way, following the braindecode’s standards:

-  `n_outputs`: Number of labels or outputs of the model.
-  `n_chans`: Number of EEG channels.
-  `n_times`: Number of time points of the input window.
-  `sfreq`: Sampling frequency of the EEG recordings.
- (/ ) `input_window_seconds`: Length of the input window in
  seconds.
-  `chs_info`: Information about each individual EEG channel. Refer
  to [`mne.Info`](https://mne.tools/stable/generated/mne.Info.html#mne.Info) (see its `"chs"` field for details).

All the models assume that the input data is a 3D tensor of shape `(batch_size,
n_chans, n_times)`, and some models also accept a 4D tensor of shape `(batch_size,
n_chans, n_times, n_epochs)`, in case of cropped model.

All the models are implemented as subclasses of
[`EEGModuleMixin`](generated/braindecode.models.EEGModuleMixin.html#braindecode.models.EEGModuleMixin), which is a base class for all EEG models
in Braindecode. The [`EEGModuleMixin`](generated/braindecode.models.EEGModuleMixin.html#braindecode.models.EEGModuleMixin) class provides a common
interface for all EEG models and can derive variable names when needed.

#### IMPORTANT
**Hugging Face Hub Integration**

All models in braindecode naturally possess the capability to push and pull from the
Hugging Face Hub through inheritance from
[`PyTorchModelHubMixin`](https://huggingface.co/docs/huggingface_hub/main/en/package_reference/mixins#huggingface_hub.PyTorchModelHubMixin). This allows you to:

- **Load pre-trained models** from the Hub using
  `Model.from_pretrained("repo_id")`
- **Share your trained models** with the community using
  `model.push_to_hub("repo_id")`
- **Version control your models** with git-like versioning on the Hub

To enable this functionality, install braindecode with Hub support:

```default
pip install braindecode[hug]
```

**Available pre-trained models:**

Some models have pre-trained weights available on the Hugging Face BrainDecode
organization:

- [`BIOT`](generated/braindecode.models.BIOT.html#braindecode.models.BIOT) - Foundation model with pre-trained weights
- [`BrainBERT`](generated/braindecode.models.BrainBERT.html#braindecode.models.BrainBERT) - Intracranial (sEEG/iEEG) foundation model with pre-trained
  weights
- [`CBraMod`](generated/braindecode.models.CBraMod.html#braindecode.models.CBraMod) - Criss-Cross Transformer model with pre-trained weights
- [`CodeBrain`](generated/braindecode.models.CodeBrain.html#braindecode.models.CodeBrain) - Scalable EEG pre-training with temporal and spectral code
  prediction
- [`Labram`](generated/braindecode.models.Labram.html#braindecode.models.Labram) - Large Brain Model with pre-trained weights
- [`REVE`](generated/braindecode.models.REVE.html#braindecode.models.REVE) - EEG foundation model with pre-trained weights
- [`LUNA`](generated/braindecode.models.LUNA.html#braindecode.models.LUNA) - Universal EEG embedding model with pre-trained weights
- `MIRepNet` - Motor-imagery pre-trained model
- [`BENDR`](generated/braindecode.models.BENDR.html#braindecode.models.BENDR) - Foundation model with pre-trained weights
- [`SignalJEPA`](generated/braindecode.models.SignalJEPA.html#braindecode.models.SignalJEPA) - Self-supervised learning model with pre-trained weights
- [`EEGPT`](generated/braindecode.models.EEGPT.html#braindecode.models.EEGPT) - Pretrained transformer for universal EEG
- [`STEEGFormer`](generated/braindecode.models.STEEGFormer.html#braindecode.models.STEEGFormer) - ViT-MAE EEG foundation model with braindecode-format
  re-hosted weights

**Example - Loading a pre-trained model:**

```python
from braindecode.models import BIOT

# Load pre-trained BIOT model from Hugging Face Hub
model = BIOT.from_pretrained("braindecode/biot-pretrained-prest-16chs")

# Use for your EEG classification task
# ... your code here ...
```

**Example - Pushing your trained model:**

```python
from braindecode.models import EEGNeX

# Train your model
model = EEGNeX(n_chans=22, n_outputs=4, n_times=1000)
# ... training code ...

# Push to the Hub (requires huggingface-cli login)
model.push_to_hub(
    repo_id="username/my-eegnex-model", commit_message="Initial model upload"
)
```

For more details, see the [`EEGModuleMixin`](generated/braindecode.models.EEGModuleMixin.html#braindecode.models.EEGModuleMixin) documentation
and the [Uploading and downloading datasets to Hugging Face Hub](auto_examples/datasets_io/plot_hub_integration.html#hub-integration) tutorial.

* **note:**
  Auto-generated Pydantic configs are available when the optional
  `braindecode[pydantic]` extra (which installs `pydantic` and `numpydantic`) is
  installed; otherwise config generation is skipped.

`braindecode.models.base`:

| [`EEGModuleMixin`](generated/braindecode.models.EEGModuleMixin.html#braindecode.models.EEGModuleMixin)([n_outputs, n_chans, ...])   | Mixin class for all EEG models in braindecode.   |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|

`braindecode.models`:

| [`ATCNet`](generated/braindecode.models.ATCNet.html#braindecode.models.ATCNet)([n_chans, n_outputs, ...])                                              | ATCNet from Altaheri et al   (2022) [[R2ecdb73d6ab9-1]](generated/braindecode.models.ATCNet.html#r2ecdb73d6ab9-1).                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`AttentionBaseNet`](generated/braindecode.models.AttentionBaseNet.html#braindecode.models.AttentionBaseNet)([n_times, n_chans, ...])                  | AttentionBaseNet from Wimpff M et al (2023) [[R523d6c831d64-Martin2023]](generated/braindecode.models.AttentionBaseNet.html#r523d6c831d64-martin2023).                                               |
| [`AttnSleep`](generated/braindecode.models.AttnSleep.html#braindecode.models.AttnSleep)([sfreq, n_tce, d_model, d_ff, ...])                            | Sleep Staging Architecture from Eldele et al  (2021) [[Re40f69d9f16e-Eldele2021]](generated/braindecode.models.AttnSleep.html#re40f69d9f16e-eldele2021).                                             |
| [`BaRISTA`](generated/braindecode.models.BaRISTA.html#braindecode.models.BaRISTA)([n_outputs, n_chans, chs_info, ...])                                 | BaRISTA from Oganesian et al (2025) [[Rf66e33847fc0-Oganesian2025]](generated/braindecode.models.BaRISTA.html#rf66e33847fc0-oganesian2025).                                                          |
| [`BDTCN`](generated/braindecode.models.BDTCN.html#braindecode.models.BDTCN)([n_chans, n_outputs, chs_info, ...])                                       | Braindecode TCN from Gemein, L et al (2020) [[Rd56781dc6fcb-gemein2020]](generated/braindecode.models.BDTCN.html#rd56781dc6fcb-gemein2020).                                                          |
| [`BENDR`](generated/braindecode.models.BENDR.html#braindecode.models.BENDR)([n_chans, n_outputs, n_times, ...])                                        | BENDR (BErt-inspired Neural Data Representations) from Kostas et al (2021) [[R26ccbd70a49a-bendr]](generated/braindecode.models.BENDR.html#r26ccbd70a49a-bendr).                                     |
| [`BIOT`](generated/braindecode.models.BIOT.html#braindecode.models.BIOT)([embed_dim, num_heads, num_layers, ...])                                      | BIOT from Yang et al (2023) [[R606e26b38fe6-Yang2023]](generated/braindecode.models.BIOT.html#r606e26b38fe6-yang2023)                                                                                |
| [`BrainBERT`](generated/braindecode.models.BrainBERT.html#braindecode.models.BrainBERT)([hidden_dim, ffn_dim, n_layers, ...])                          | BrainBERT from Wang et al. (2023) [[Rf54fa634480e-BrainBERT2023]](generated/braindecode.models.BrainBERT.html#rf54fa634480e-brainbert2023).                                                          |
| [`BrainModule`](generated/braindecode.models.BrainModule.html#braindecode.models.BrainModule)([n_chans, n_outputs, n_times, ...])                      | BrainModule from [[Rf869b8ed6368-brainmagick]](generated/braindecode.models.BrainModule.html#rf869b8ed6368-brainmagick), also known as SimpleConv.                                                   |
| [`CBraMod`](generated/braindecode.models.CBraMod.html#braindecode.models.CBraMod)([n_outputs, n_chans, chs_info, ...])                                 | **C**riss-**C**ross **Bra**in **Mod**el for EEG Decoding from Wang et al. (2025) [[Rdb05ba1b4969-cbramod]](generated/braindecode.models.CBraMod.html#rdb05ba1b4969-cbramod).                         |
| [`CodeBrain`](generated/braindecode.models.CodeBrain.html#braindecode.models.CodeBrain)([n_outputs, n_chans, chs_info, ...])                           | CodeBrain: Scalable Code EEG Pre-Training for Unified Downstream BCI Tasks.                                                                                                                          |
| [`ContraWR`](generated/braindecode.models.ContraWR.html#braindecode.models.ContraWR)([n_chans, n_outputs, sfreq, ...])                                 | Contrast with the World Representation ContraWR from Yang et al (2021) [[Ra71465cb6797-Yang2021]](generated/braindecode.models.ContraWR.html#ra71465cb6797-yang2021).                                |
| [`CTNet`](generated/braindecode.models.CTNet.html#braindecode.models.CTNet)([n_outputs, n_chans, sfreq, chs_info, ...])                                | CTNet from Zhao, W et al (2024) [[Rc7f1d6cec70c-ctnet]](generated/braindecode.models.CTNet.html#rc7f1d6cec70c-ctnet).                                                                                |
| [`DGCNN`](generated/braindecode.models.DGCNN.html#braindecode.models.DGCNN)([n_outputs, n_chans, chs_info, ...])                                       | DGCNN for EEG classification from Song et al. (2018) [[Rff991d0fb90b-dgcnn]](generated/braindecode.models.DGCNN.html#rff991d0fb90b-dgcnn).                                                           |
| [`DIVER1`](generated/braindecode.models.DIVER1.html#braindecode.models.DIVER1)([n_outputs, n_chans, chs_info, ...])                                    | DIVER-1 from Han et al. (2025) [[Raa6ac0ab42e7-Han2025]](generated/braindecode.models.DIVER1.html#raa6ac0ab42e7-han2025).                                                                            |
| [`Deep4Net`](generated/braindecode.models.Deep4Net.html#braindecode.models.Deep4Net)([n_chans, n_outputs, n_times, ...])                               | Deep ConvNet model from Schirrmeister et al (2017) [[Rb8ef6c2733ce-Schirrmeister2017]](generated/braindecode.models.Deep4Net.html#rb8ef6c2733ce-schirrmeister2017).                                  |
| [`DeepSleepNet`](generated/braindecode.models.DeepSleepNet.html#braindecode.models.DeepSleepNet)([n_outputs, return_feats, ...])                       | DeepSleepNet from Supratak et al (2017) [[R28b528aca953-Supratak2017]](generated/braindecode.models.DeepSleepNet.html#r28b528aca953-supratak2017).                                                   |
| [`EEGConformer`](generated/braindecode.models.EEGConformer.html#braindecode.models.EEGConformer)([n_outputs, n_chans, ...])                            | EEG Conformer from Song et al (2022) [[Rd6c0fefc356a-song2022]](generated/braindecode.models.EEGConformer.html#rd6c0fefc356a-song2022).                                                              |
| [`EEGDINO`](generated/braindecode.models.EEGDINO.html#braindecode.models.EEGDINO)([n_outputs, n_chans, chs_info, ...])                                 | EEG-DINO from Wang et al. (2025) [[R8a8c4f990233-eegdino]](generated/braindecode.models.EEGDINO.html#r8a8c4f990233-eegdino).                                                                         |
| [`EEGInceptionERP`](generated/braindecode.models.EEGInceptionERP.html#braindecode.models.EEGInceptionERP)([n_chans, n_outputs, ...])                   | EEG Inception for ERP-based from Santamaria-Vazquez et al (2020) [[R37c4761d4e92-santamaria2020]](generated/braindecode.models.EEGInceptionERP.html#r37c4761d4e92-santamaria2020).                   |
| [`EEGInceptionMI`](generated/braindecode.models.EEGInceptionMI.html#braindecode.models.EEGInceptionMI)([n_chans, n_outputs, ...])                      | EEG Inception for Motor Imagery, as proposed in Zhang et al. (2021) [[Rc36ed781f4f5-1]](generated/braindecode.models.EEGInceptionMI.html#rc36ed781f4f5-1).                                           |
| [`EEGITNet`](generated/braindecode.models.EEGITNet.html#braindecode.models.EEGITNet)([n_outputs, n_chans, n_times, ...])                               | EEG-ITNet from Salami, et al (2022) [[R7fe571f46200-Salami2022]](generated/braindecode.models.EEGITNet.html#r7fe571f46200-salami2022)                                                                |
| [`EEGMiner`](generated/braindecode.models.EEGMiner.html#braindecode.models.EEGMiner)([method, n_chans, n_outputs, ...])                                | EEGMiner from Ludwig et al (2024) [[R66a8789ab6ed-eegminer]](generated/braindecode.models.EEGMiner.html#r66a8789ab6ed-eegminer).                                                                     |
| [`EEGNet`](generated/braindecode.models.EEGNet.html#braindecode.models.EEGNet)([n_chans, n_outputs, n_times, ...])                                     | EEGNet model from Lawhern et al (2018) [[Rffa56cc934a8-Lawhern2018]](generated/braindecode.models.EEGNet.html#rffa56cc934a8-lawhern2018).                                                            |
| [`EEGPT`](generated/braindecode.models.EEGPT.html#braindecode.models.EEGPT)([n_outputs, n_chans, chs_info, ...])                                       | EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals from Wang et al. (2024) [[R025fd21f633e-eegpt]](generated/braindecode.models.EEGPT.html#r025fd21f633e-eegpt). |
| [`EEGNeX`](generated/braindecode.models.EEGNeX.html#braindecode.models.EEGNeX)([n_chans, n_outputs, n_times, ...])                                     | EEGNeX model from Chen et al (2024) [[R60f8df15fd80-eegnex]](generated/braindecode.models.EEGNeX.html#r60f8df15fd80-eegnex).                                                                         |
| [`EEGSimpleConv`](generated/braindecode.models.EEGSimpleConv.html#braindecode.models.EEGSimpleConv)([n_outputs, n_chans, sfreq, ...])                  | EEGSimpleConv from Ouahidi, YE et al (2023) [[R5661533ddc63-Yassine2023]](generated/braindecode.models.EEGSimpleConv.html#r5661533ddc63-yassine2023).                                                |
| [`EEGSym`](generated/braindecode.models.EEGSym.html#braindecode.models.EEGSym)([n_chans, n_outputs, n_times, ...])                                     | EEGSym from Pérez-Velasco et al (2022) [[R871bea9be1d1-eegsym2022]](generated/braindecode.models.EEGSym.html#r871bea9be1d1-eegsym2022).                                                              |
| [`EEGTCNet`](generated/braindecode.models.EEGTCNet.html#braindecode.models.EEGTCNet)([n_chans, n_outputs, n_times, ...])                               | EEGTCNet model from Ingolfsson et al (2020) [[Rc25b3d8a3a40-ingolfsson2020]](generated/braindecode.models.EEGTCNet.html#rc25b3d8a3a40-ingolfsson2020).                                               |
| [`EMG2QwertyNet`](generated/braindecode.models.EMG2QwertyNet.html#braindecode.models.EMG2QwertyNet)([n_outputs, n_chans, sfreq, ...])                  | Decoder mapping surface electromyography (sEMG) to keystrokes (emg2qwerty) [[R6311dcb4571d-emg2qwerty2024]](generated/braindecode.models.EMG2QwertyNet.html#r6311dcb4571d-emg2qwerty2024).           |
| [`FBCNet`](generated/braindecode.models.FBCNet.html#braindecode.models.FBCNet)([n_chans, n_outputs, chs_info, ...])                                    | FBCNet from Mane, R et al (2021) [[R9769c9f8e3f7-fbcnet2021]](generated/braindecode.models.FBCNet.html#r9769c9f8e3f7-fbcnet2021).                                                                    |
| [`FBLightConvNet`](generated/braindecode.models.FBLightConvNet.html#braindecode.models.FBLightConvNet)([n_chans, n_outputs, ...])                      | LightConvNet from Ma, X et al (2023) [[R501137d6e8c9-lightconvnet]](generated/braindecode.models.FBLightConvNet.html#r501137d6e8c9-lightconvnet).                                                    |
| [`FBMSNet`](generated/braindecode.models.FBMSNet.html#braindecode.models.FBMSNet)([n_chans, n_outputs, chs_info, ...])                                 | FBMSNet from Liu et al (2022) [[Re7850041dabd-fbmsnet]](generated/braindecode.models.FBMSNet.html#re7850041dabd-fbmsnet).                                                                            |
| [`IFNet`](generated/braindecode.models.IFNet.html#braindecode.models.IFNet)([n_chans, n_outputs, n_times, ...])                                        | IFNetV2 from Wang J et al (2023) [[Rd9f3b242e751-ifnet]](generated/braindecode.models.IFNet.html#rd9f3b242e751-ifnet).                                                                               |
| [`InterpolatedBENDR`](generated/braindecode.models.InterpolatedBENDR.html#braindecode.models.InterpolatedBENDR)(chs_info[, n_outputs, ...])            | Channel-interpolating wrapper around [`BENDR`](generated/braindecode.models.BENDR.html#braindecode.models.BENDR).                                                                                    |
| [`InterpolatedBIOT`](generated/braindecode.models.InterpolatedBIOT.html#braindecode.models.InterpolatedBIOT)(chs_info[, n_outputs, ...])               | Channel-interpolating wrapper around [`BIOT`](generated/braindecode.models.BIOT.html#braindecode.models.BIOT).                                                                                       |
| [`InterpolatedEEGPT`](generated/braindecode.models.InterpolatedEEGPT.html#braindecode.models.InterpolatedEEGPT)(chs_info[, n_outputs, ...])            | Channel-interpolating wrapper around [`EEGPT`](generated/braindecode.models.EEGPT.html#braindecode.models.EEGPT).                                                                                    |
| [`InterpolatedLaBraM`](generated/braindecode.models.InterpolatedLaBraM.html#braindecode.models.InterpolatedLaBraM)(chs_info[, n_outputs, ...])         | Channel-interpolating wrapper around [`Labram`](generated/braindecode.models.Labram.html#braindecode.models.Labram).                                                                                 |
| [`InterpolatedModel`](generated/braindecode.models.InterpolatedModel.html#braindecode.models.InterpolatedModel)(model_cls, target_chs_info)            | Return a subclass of `model_cls` that interpolates channels to `target_chs_info`.                                                                                                                    |
| [`InterpolatedSignalJEPA`](generated/braindecode.models.InterpolatedSignalJEPA.html#braindecode.models.InterpolatedSignalJEPA)(chs_info[, ...])        | Channel-interpolating wrapper around [`SignalJEPA`](generated/braindecode.models.SignalJEPA.html#braindecode.models.SignalJEPA).                                                                     |
| [`Labram`](generated/braindecode.models.Labram.html#braindecode.models.Labram)([n_times, n_outputs, chs_info, ...])                                    | Labram from Jiang, W B et al (2024) [[Rb5cdfc6ea4fe-Jiang2024]](generated/braindecode.models.Labram.html#rb5cdfc6ea4fe-jiang2024).                                                                   |
| [`LUNA`](generated/braindecode.models.LUNA.html#braindecode.models.LUNA)([n_outputs, n_chans, n_times, sfreq, ...])                                    | LUNA from Döner et al [[Ra888573a1c66-LUNA]](generated/braindecode.models.LUNA.html#ra888573a1c66-luna).                                                                                             |
| [`MEDFormer`](generated/braindecode.models.MEDFormer.html#braindecode.models.MEDFormer)([n_chans, n_outputs, n_times, ...])                            | Medformer from Wang et al (2024) [[Rf62d33a1206f-Medformer2024]](generated/braindecode.models.MEDFormer.html#rf62d33a1206f-medformer2024).                                                           |
| [`MetaNeuromotorHand`](generated/braindecode.models.MetaNeuromotorHand.html#braindecode.models.MetaNeuromotorHand)([n_outputs, n_chans, ...])          | Generic neuromotor interface for handwriting from Meta (2025) [[R56528df87fac-gni2025]](generated/braindecode.models.MetaNeuromotorHand.html#r56528df87fac-gni2025).                                 |
| [`MSCFormer`](generated/braindecode.models.MSCFormer.html#braindecode.models.MSCFormer)([n_outputs, n_chans, sfreq, ...])                              | MSCFormer from Zhao, W et al (2025) [[R145bcee8b1ba-mscformer]](generated/braindecode.models.MSCFormer.html#r145bcee8b1ba-mscformer).                                                                |
| [`MSVTNet`](generated/braindecode.models.MSVTNet.html#braindecode.models.MSVTNet)([n_chans, n_outputs, n_times, ...])                                  | MSVTNet model from Liu K et al (2024) from [[R0733e66fed6d-msvt2024]](generated/braindecode.models.MSVTNet.html#r0733e66fed6d-msvt2024).                                                             |
| [`PBT`](generated/braindecode.models.PBT.html#braindecode.models.PBT)([n_chans, n_outputs, n_times, chs_info, ...])                                    | Patched Brain Transformer (PBT) model from Klein et al (2025) [[Re7f840f86627-pbt]](generated/braindecode.models.PBT.html#re7f840f86627-pbt).                                                        |
| [`PopulationTransformer`](generated/braindecode.models.PopulationTransformer.html#braindecode.models.PopulationTransformer)([n_outputs, n_chans, ...]) | PopulationTransformer (PopT) from Chau et al. (2024) [[R1b4476d13843-PopT2024]](generated/braindecode.models.PopulationTransformer.html#r1b4476d13843-popt2024).                                     |
| [`REVE`](generated/braindecode.models.REVE.html#braindecode.models.REVE)([n_outputs, n_chans, chs_info, ...])                                          | **R**epresentation for **E**EG with **V**ersatile **E**mbeddings (REVE) from El Ouahidi et al. (2025) [[Rfc92bf36d5c3-reve]](generated/braindecode.models.REVE.html#rfc92bf36d5c3-reve).             |
| [`SCCNet`](generated/braindecode.models.SCCNet.html#braindecode.models.SCCNet)([n_chans, n_outputs, n_times, ...])                                     | SCCNet from Wei, C S (2019) [[Rbd95e5cdbbde-sccnet]](generated/braindecode.models.SCCNet.html#rbd95e5cdbbde-sccnet).                                                                                 |
| [`ShallowFBCSPNet`](generated/braindecode.models.ShallowFBCSPNet.html#braindecode.models.ShallowFBCSPNet)([n_chans, n_outputs, ...])                   | Shallow ConvNet model from Schirrmeister et al (2017) [[R9432a19f6121-Schirrmeister2017]](generated/braindecode.models.ShallowFBCSPNet.html#r9432a19f6121-schirrmeister2017).                        |
| [`SignalJEPA`](generated/braindecode.models.SignalJEPA.html#braindecode.models.SignalJEPA)([n_outputs, n_chans, chs_info, ...])                        | Architecture introduced in signal-JEPA for self-supervised pre-training, Guetschel, P et al (2024) [[R62b31c4b9b52-1]](generated/braindecode.models.SignalJEPA.html#r62b31c4b9b52-1)                 |
| [`SignalJEPA_Contextual`](generated/braindecode.models.SignalJEPA_Contextual.html#braindecode.models.SignalJEPA_Contextual)([n_outputs, n_chans, ...]) | Contextual downstream architecture introduced in signal-JEPA Guetschel, P et al (2024) [[Rb25bb9e753a8-1]](generated/braindecode.models.SignalJEPA_Contextual.html#rb25bb9e753a8-1).                 |
| [`SignalJEPA_PostLocal`](generated/braindecode.models.SignalJEPA_PostLocal.html#braindecode.models.SignalJEPA_PostLocal)([n_outputs, n_chans, ...])    | Post-local downstream architecture introduced in signal-JEPA Guetschel, P et al (2024) [[R29e8e87440e5-1]](generated/braindecode.models.SignalJEPA_PostLocal.html#r29e8e87440e5-1).                  |
| [`SignalJEPA_PreLocal`](generated/braindecode.models.SignalJEPA_PreLocal.html#braindecode.models.SignalJEPA_PreLocal)([n_outputs, n_chans, ...])       | Pre-local downstream architecture introduced in signal-JEPA Guetschel, P et al (2024) [[R795e75e58da6-1]](generated/braindecode.models.SignalJEPA_PreLocal.html#r795e75e58da6-1).                    |
| [`SincShallowNet`](generated/braindecode.models.SincShallowNet.html#braindecode.models.SincShallowNet)([num_time_filters, ...])                        | Sinc-ShallowNet from Borra, D et al (2020) [[R4fd1ba6a7153-borra2020]](generated/braindecode.models.SincShallowNet.html#r4fd1ba6a7153-borra2020).                                                    |
| [`SleepStagerBlanco2020`](generated/braindecode.models.SleepStagerBlanco2020.html#braindecode.models.SleepStagerBlanco2020)([n_chans, sfreq, ...])     | Sleep staging architecture from Blanco et al (2020) from [[Rb3eee9d9e81a-Blanco2020]](generated/braindecode.models.SleepStagerBlanco2020.html#rb3eee9d9e81a-blanco2020)                              |
| [`SleepStagerChambon2018`](generated/braindecode.models.SleepStagerChambon2018.html#braindecode.models.SleepStagerChambon2018)([n_chans, sfreq, ...])  | Sleep staging architecture from Chambon et al. (2018) [[R89163c5eab6a-Chambon2018]](generated/braindecode.models.SleepStagerChambon2018.html#r89163c5eab6a-chambon2018).                             |
| [`SPARCNet`](generated/braindecode.models.SPARCNet.html#braindecode.models.SPARCNet)([n_chans, n_times, n_outputs, ...])                               | Seizures, Periodic and Rhythmic pattern Continuum Neural Network (SPaRCNet) from Jing et al (2023) [[Rf8eed20f8ca2-jing2023]](generated/braindecode.models.SPARCNet.html#rf8eed20f8ca2-jing2023).    |
| [`SSTDPN`](generated/braindecode.models.SSTDPN.html#braindecode.models.SSTDPN)([n_chans, n_times, n_outputs, ...])                                     | SSTDPN from Can Han et al (2025) [[R15c5a176a51e-Han2025]](generated/braindecode.models.SSTDPN.html#r15c5a176a51e-han2025).                                                                          |
| [`STEEGFormer`](generated/braindecode.models.STEEGFormer.html#braindecode.models.STEEGFormer)([n_outputs, n_chans, chs_info, ...])                     | STEEGFormer from Yang et al. (2026) [[R2168339d6ac8-Yang2026]](generated/braindecode.models.STEEGFormer.html#r2168339d6ac8-yang2026).                                                                |
| [`SyncNet`](generated/braindecode.models.SyncNet.html#braindecode.models.SyncNet)([n_chans, n_times, n_outputs, ...])                                  | Synchronization Network (SyncNet) from Li, Y et al (2017) [[R5cdbe961b734-Li2017]](generated/braindecode.models.SyncNet.html#r5cdbe961b734-li2017).                                                  |
| [`TCFormer`](generated/braindecode.models.TCFormer.html#braindecode.models.TCFormer)([n_outputs, n_chans, chs_info, ...])                              | TCFormer from Altaheri et al (2025) [[Rd79f90b7998b-tcformer]](generated/braindecode.models.TCFormer.html#rd79f90b7998b-tcformer).                                                                   |
| [`TIDNet`](generated/braindecode.models.TIDNet.html#braindecode.models.TIDNet)([n_chans, n_outputs, n_times, ...])                                     | Thinker Invariance DenseNet model from Kostas et al (2020) [[Re74dd80418c9-TIDNet]](generated/braindecode.models.TIDNet.html#re74dd80418c9-tidnet).                                                  |
| [`TSception`](generated/braindecode.models.TSception.html#braindecode.models.TSception)([n_chans, n_outputs, ...])                                     | TSception model from Ding et al. (2020) from [[R576865d14b94-ding2020]](generated/braindecode.models.TSception.html#r576865d14b94-ding2020).                                                         |
| [`USleep`](generated/braindecode.models.USleep.html#braindecode.models.USleep)([n_chans, sfreq, depth, ...])                                           | Sleep staging architecture from Perslev et al (2021) [[R58a5e8182f0a-1]](generated/braindecode.models.USleep.html#r58a5e8182f0a-1).                                                                  |
| [`ZUNA`](generated/braindecode.models.ZUNA.html#braindecode.models.ZUNA)([n_outputs, n_chans, chs_info, ...])                                          | ZUNA from Warner et al. (2026) [[Rc751ab0dc940-Warner2026ZUNA]](generated/braindecode.models.ZUNA.html#rc751ab0dc940-warner2026zuna).                                                                |

<a id="diver-1-recording-metadata"></a>

### DIVER-1 recording metadata

### braindecode.models.diver1.channel_metadata_from_chs_info(chs_info)

Build DIVER-1 coordinate and electrode-type metadata from MNE channel info.

* **Parameters:**
  **chs_info** ([`list`](https://docs.python.org/3/builtins/stdtypes.html#list)[[`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)]) – One MNE `info["chs"]` entry per channel, with `kind` and `loc`.
* **Returns:**
  Float32 `(n_chans, 5)` tensor: xyz in millimetres, modality
  (EEG=0, intracranial=1), and subtype (grid=0, strip=1, depth=2,
  unknown=-1). MNE cannot identify strips. Missing coordinates are NaN.
  These slots follow DIVER-1’s vocabulary, not MNE kind codes.
* **Return type:**
  [`Tensor`](https://docs.pytorch.org/docs/stable/tensors.html#torch.Tensor)

### Examples

```pycon
>>> import mne
>>> info = mne.create_info(["A1", "A2"], 500.0, "seeg")
>>> channel_metadata_from_chs_info(info["chs"])[:, 3:].tolist()
[[1.0, 2.0], [1.0, 2.0]]
```

<!-- !! processed by numpydoc !! -->

Modules

`braindecode.modules`:

This module contains the building blocks for Braindecode models. It contains activation
functions, convolutional layers, attention mechanisms, filter banks, and other
utilities.

<a id="activation"></a>

### Activation

These modules wrap specialized activation functions—e.g., safe logarithms for numerical
stability.

`braindecode.modules.activation`:

| [`GatedLinearUnit`](generated/activation/braindecode.modules.GatedLinearUnit.html#braindecode.modules.GatedLinearUnit)([activation])   | Generalized gated linear unit (GLU family).   |
|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| [`LogActivation`](generated/activation/braindecode.modules.LogActivation.html#braindecode.modules.LogActivation)([epsilon])            | Logarithm activation function.                |
| [`SafeLog`](generated/activation/braindecode.modules.SafeLog.html#braindecode.modules.SafeLog)([epsilon])                              | Safe logarithm activation function module.    |

<a id="attention"></a>

### Attention

These modules implement various attention mechanisms, including multi’head attention and
squeeze and excitation layers.

`braindecode.modules.attention`:

| [`CAT`](generated/attention/braindecode.modules.CAT.html#braindecode.modules.CAT)(in_channels, reduction_rate, kernel_size)                                       | Attention Mechanism from [[R4b3f3c7c2fe2-Wu2023]](generated/attention/braindecode.modules.CAT.html#r4b3f3c7c2fe2-wu2023).                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`CBAM`](generated/attention/braindecode.modules.CBAM.html#braindecode.modules.CBAM)(in_channels, reduction_rate, kernel_size)                                    | Convolutional Block Attention Module from [[R8389a3af090c-Woo2018]](generated/attention/braindecode.modules.CBAM.html#r8389a3af090c-woo2018).                 |
| [`ECA`](generated/attention/braindecode.modules.ECA.html#braindecode.modules.ECA)(in_channels, kernel_size)                                                       | Efficient Channel Attention [[R18399df6eede-Wang2021]](generated/attention/braindecode.modules.ECA.html#r18399df6eede-wang2021).                              |
| [`FCA`](generated/attention/braindecode.modules.FCA.html#braindecode.modules.FCA)(in_channels[, seq_len, reduction_rate, ...])                                    | Frequency Channel Attention Networks from [[R7a6c40ff4f0b-Qin2021]](generated/attention/braindecode.modules.FCA.html#r7a6c40ff4f0b-qin2021).                  |
| [`GCT`](generated/attention/braindecode.modules.GCT.html#braindecode.modules.GCT)(in_channels)                                                                    | Gated Channel Transformation from [[R977e9a24fcb7-Yang2020]](generated/attention/braindecode.modules.GCT.html#r977e9a24fcb7-yang2020).                        |
| [`SRM`](generated/attention/braindecode.modules.SRM.html#braindecode.modules.SRM)(in_channels[, use_mlp, reduction_rate, bias])                                   | Attention module from [[R94e1b7c716d1-Lee2019]](generated/attention/braindecode.modules.SRM.html#r94e1b7c716d1-lee2019).                                      |
| [`CATLite`](generated/attention/braindecode.modules.CATLite.html#braindecode.modules.CATLite)(in_channels, reduction_rate[, bias])                                | Modification of CAT without the convolutional layer from [[R1d30135f2545-Wu2023]](generated/attention/braindecode.modules.CATLite.html#r1d30135f2545-wu2023). |
| [`EncNet`](generated/attention/braindecode.modules.EncNet.html#braindecode.modules.EncNet)(in_channels, n_codewords)                                              | Context Encoding for Semantic Segmentation from [[R13609999c674-Zhang2018]](generated/attention/braindecode.modules.EncNet.html#r13609999c674-zhang2018).     |
| [`GatherExcite`](generated/attention/braindecode.modules.GatherExcite.html#braindecode.modules.GatherExcite)(in_channels[, seq_len, ...])                         | Gather-Excite Networks from [[Re3d24ebdda8b-Hu2018b]](generated/attention/braindecode.modules.GatherExcite.html#re3d24ebdda8b-hu2018b).                       |
| [`GSoP`](generated/attention/braindecode.modules.GSoP.html#braindecode.modules.GSoP)(in_channels, reduction_rate[, bias])                                         | Global Second-order Pooling Convolutional Networks from [[Reb98cd67024f-Gao2018]](generated/attention/braindecode.modules.GSoP.html#reb98cd67024f-gao2018).   |
| [`MultiHeadAttention`](generated/attention/braindecode.modules.MultiHeadAttention.html#braindecode.modules.MultiHeadAttention)(emb_size, num_heads[, ...])        | Multi-head self-attention block.                                                                                                                              |
| [`SqueezeAndExcitation`](generated/attention/braindecode.modules.SqueezeAndExcitation.html#braindecode.modules.SqueezeAndExcitation)(in_channels, reduction_rate) | Squeeze-and-Excitation Networks from [[R0b6baaf6da0f-Hu2018]](generated/attention/braindecode.modules.SqueezeAndExcitation.html#r0b6baaf6da0f-hu2018).        |

<a id="blocks"></a>

### Blocks

These modules are specialized building blocks for neural networks, including multi’layer
perceptrons (MLPs) and inception blocks.

`braindecode.modules.blocks`:

| [`MLP`](generated/blocks/braindecode.modules.MLP.html#braindecode.modules.MLP)(in_features[, hidden_features, ...])                                | Multilayer Perceptron (MLP) with GELU activation and optional dropout.   |
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [`FeedForwardBlock`](generated/blocks/braindecode.modules.FeedForwardBlock.html#braindecode.modules.FeedForwardBlock)(emb_size, expansion, drop_p) | Feedforward network block.                                               |
| [`InceptionBlock`](generated/blocks/braindecode.modules.InceptionBlock.html#braindecode.modules.InceptionBlock)(branches)                          | Inception block module.                                                  |
| [`PatchTokenizer`](generated/blocks/braindecode.modules.PatchTokenizer.html#braindecode.modules.PatchTokenizer)(patch_size, n_times[, ...])        | Tokenize an EEG signal into non-overlapping temporal patches.            |

<a id="convolution"></a>

### Convolution

These modules implement constraints convolutional layers, including depthwise
convolutions and causal convolutions. They also include convolutional layers with
constraints and pooling layers.

`braindecode.modules.convolution`:

| [`AvgPool2dWithConv`](generated/convolution/braindecode.modules.AvgPool2dWithConv.html#braindecode.modules.AvgPool2dWithConv)(kernel_size, stride[, ...])   | Compute average pooling using a convolution, to have the dilation parameter.    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [`CausalConv1d`](generated/convolution/braindecode.modules.CausalConv1d.html#braindecode.modules.CausalConv1d)(in_channels, out_channels, ...)              | Causal 1-dimensional convolution                                                |
| [`CombinedConv`](generated/convolution/braindecode.modules.CombinedConv.html#braindecode.modules.CombinedConv)(in_chans[, n_filters_time, ...])             | Merged convolutional layer for temporal and spatial convs in Deep4/ShallowFBCSP |
| [`Conv2dWithConstraint`](generated/convolution/braindecode.modules.Conv2dWithConstraint.html#braindecode.modules.Conv2dWithConstraint)(\*args[, max_norm])  | 2D convolution with max-norm constraint on the weights.                         |
| [`DepthwiseConv2d`](generated/convolution/braindecode.modules.DepthwiseConv2d.html#braindecode.modules.DepthwiseConv2d)(in_channels[, ...])                 | Depthwise convolution layer.                                                    |

<a id="filter"></a>

### Filter

These modules implement Filter Bank as Layer and generalizer Gaussian layer.

`braindecode.modules.filter`:

| [`ChannelInterpolationLayer`](generated/filter/braindecode.modules.ChannelInterpolationLayer.html#braindecode.modules.ChannelInterpolationLayer)(src_chs_info, ...)   | Projects an input from one channel set to another via a fixed (or learnable) matrix.                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`FilterBankLayer`](generated/filter/braindecode.modules.FilterBankLayer.html#braindecode.modules.FilterBankLayer)(n_chans, sfreq[, ...])                             | Apply multiple band-pass filters to generate multiview signal representation.                                                                                                |
| [`GeneralizedGaussianFilter`](generated/filter/braindecode.modules.GeneralizedGaussianFilter.html#braindecode.modules.GeneralizedGaussianFilter)(in_channels, ...)    | Generalized Gaussian Filter from Ludwig et al (2024) [[Raf65b68c9f5f-eegminer]](generated/filter/braindecode.modules.GeneralizedGaussianFilter.html#raf65b68c9f5f-eegminer). |

<a id="layers"></a>

### Layers

These modules implement various types of layers, including dropout layers, normalization
layers, and time’distributed layers. They also include layers for handling different
input shapes and dimensions.

`braindecode.modules.layers`:

| [`ChannelMerger`](generated/layers/braindecode.modules.ChannelMerger.html#braindecode.modules.ChannelMerger)([out_channels, pos_dim, ...])   | Spatial Fourier-attention merge: `n_chans` -> `out_channels`.        |
|----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [`Chomp1d`](generated/layers/braindecode.modules.Chomp1d.html#braindecode.modules.Chomp1d)(chomp_size)                                       | Remove samples from the end of a sequence.                           |
| [`DropPath`](generated/layers/braindecode.modules.DropPath.html#braindecode.modules.DropPath)([drop_prob])                                   | Drop paths, also known as Stochastic Depth, per sample.              |
| [`Ensure4d`](generated/layers/braindecode.modules.Ensure4d.html#braindecode.modules.Ensure4d)(\*args, \*\*kwargs)                            | Ensure the input tensor has 4 dimensions.                            |
| [`FourierEmb`](generated/layers/braindecode.modules.FourierEmb.html#braindecode.modules.FourierEmb)([dimension, margin])                     | 2D Fourier positional embedding over electrode `(x, y)` in `[0, 1]`. |
| [`SubjectLayers`](generated/layers/braindecode.modules.SubjectLayers.html#braindecode.modules.SubjectLayers)(in_channels, out_channels, ...) | Per-subject linear transformation layer.                             |
| [`TimeDistributed`](generated/layers/braindecode.modules.TimeDistributed.html#braindecode.modules.TimeDistributed)(module)                   | Apply module on multiple windows.                                    |

<a id="linear"></a>

### Linear

These modules implement linear layers with various constraints and initializations. They
include linear layers with max’norm constraints and linear layers with specific
initializations.

`braindecode.modules.linear`:

| [`LinearWithConstraint`](generated/linear/braindecode.modules.LinearWithConstraint.html#braindecode.modules.LinearWithConstraint)(\*args[, max_norm])   | Linear layer with max-norm constraint on the weights.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| [`MaxNormLinear`](generated/linear/braindecode.modules.MaxNormLinear.html#braindecode.modules.MaxNormLinear)(in_features, out_features[, ...])          | Linear layer with MaxNorm constraining on weights.      |

<a id="stats"></a>

### Stats

These modules implement statistical layers, including layers for calculating the mean,
standard deviation, and variance of input data. They also include layers for calculating
the log power and log variance of input data. Mostly used on FilterBank models.

`braindecode.modules.stats`:

| [`StatLayer`](generated/stats/braindecode.modules.StatLayer.html#braindecode.modules.StatLayer)(stat_fn, dim[, keepdim, ...])   | Generic layer to compute a statistical function along a specified dimension.   |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|

| [`LogPowerLayer`](generated/stats/braindecode.modules.LogPowerLayer.html#braindecode.modules.LogPowerLayer)   | Generic layer to compute a statistical function along a specified dimension.   |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [`LogVarLayer`](generated/stats/braindecode.modules.LogVarLayer.html#braindecode.modules.LogVarLayer)         | Generic layer to compute a statistical function along a specified dimension.   |
| [`MaxLayer`](generated/stats/braindecode.modules.MaxLayer.html#braindecode.modules.MaxLayer)                  | Generic layer to compute a statistical function along a specified dimension.   |
| [`MeanLayer`](generated/stats/braindecode.modules.MeanLayer.html#braindecode.modules.MeanLayer)               | Generic layer to compute a statistical function along a specified dimension.   |
| [`StdLayer`](generated/stats/braindecode.modules.StdLayer.html#braindecode.modules.StdLayer)                  | Generic layer to compute a statistical function along a specified dimension.   |
| [`VarLayer`](generated/stats/braindecode.modules.VarLayer.html#braindecode.modules.VarLayer)                  | Generic layer to compute a statistical function along a specified dimension.   |

<a id="utilities"></a>

### Utilities

These modules implement various utility functions and classes for change to cropped
model.

`braindecode.modules.util`:

| [`aggregate_probas`](generated/util/braindecode.modules.aggregate_probas.html#braindecode.modules.aggregate_probas)(logits[, n_windows_stride])   | Aggregate predicted probabilities with self-ensembling.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|

<a id="wrappers"></a>

### Wrappers

These modules implement wrappers for various types of models, including wrappers for
models with multiple outputs and wrappers for models with intermediate outputs.

`braindecode.modules.wrapper`:

| [`Expression`](generated/wrapper/braindecode.modules.Expression.html#braindecode.modules.Expression)(expression_fn)                                                 | Compute given expression on forward pass.                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [`IntermediateOutputWrapper`](generated/wrapper/braindecode.modules.IntermediateOutputWrapper.html#braindecode.modules.IntermediateOutputWrapper)(to_select, model) | Wraps network model such that outputs of intermediate layers can be returned. |

<a id="functional"></a>

## Functional

`braindecode.functional`:

The functional module contains various functions that can be used like functional API.

| [`drop_path`](generated/braindecode.functional.drop_path.html#braindecode.functional.drop_path)(x[, drop_prob, training, ...])                                                   | Drop paths (Stochastic Depth) per sample.                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [`glorot_weight_zero_bias`](generated/braindecode.functional.glorot_weight_zero_bias.html#braindecode.functional.glorot_weight_zero_bias)(model)                                 | Initialize parameters of all modules by initializing weights with.                    |
| [`hilbert_freq`](generated/braindecode.functional.hilbert_freq.html#braindecode.functional.hilbert_freq)(x[, forward_fourier])                                                   | Compute the Hilbert transform using PyTorch, separating the real and imaginary parts. |
| [`identity`](generated/braindecode.functional.identity.html#braindecode.functional.identity)(x)                                                                                  |                                                                                       |
| [`plv_time`](generated/braindecode.functional.plv_time.html#braindecode.functional.plv_time)(x[, forward_fourier, epsilon])                                                      | Compute the Phase Locking Value (PLV) metric in the time domain.                      |
| [`rescale_parameter`](generated/braindecode.functional.rescale_parameter.html#braindecode.functional.rescale_parameter)(param, layer_id)                                         | Recaling the l-th transformer layer.                                                  |
| [`safe_log`](generated/braindecode.functional.safe_log.html#braindecode.functional.safe_log)(x[, eps])                                                                           | Prevents $log(0)$ by using $log(max(x, eps))$.                                        |
| [`sinusoidal_positional_encoding`](generated/braindecode.functional.sinusoidal_positional_encoding.html#braindecode.functional.sinusoidal_positional_encoding)(n_positions, dim) | Fixed sine/cosine positional-encoding table of shape `(n_positions, dim)`.            |
| [`square`](generated/braindecode.functional.square.html#braindecode.functional.square)(x)                                                                                        |                                                                                       |

<a id="datasets"></a>

## Datasets

`braindecode.datasets`:

Pytorch Datasets structure for common EEG datasets, and function to create the dataset
from several different data formats. The options available are: Numpy Arrays, MNE
Raw and MNE Epochs.

<a id="base-classes"></a>

### Base classes

| [`BaseConcatDataset`](generated/braindecode.datasets.BaseConcatDataset.html#braindecode.datasets.BaseConcatDataset)(list_of_ds[, ...])   | A base class for concatenated datasets.                        |
|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [`RecordDataset`](generated/braindecode.datasets.RecordDataset.html#braindecode.datasets.RecordDataset)([description, transform])        |                                                                |
| [`RawDataset`](generated/braindecode.datasets.RawDataset.html#braindecode.datasets.RawDataset)(raw[, description, target_name, ...])     | Returns samples from an mne.io.Raw object along with a target. |
| [`WindowsDataset`](generated/braindecode.datasets.WindowsDataset.html#braindecode.datasets.WindowsDataset)(windows[, description, ...])  | Returns windows from an mne.Epochs object along with a target. |

<a id="common-datasets"></a>

### Common Datasets

| [`BCICompetitionIVDataset4`](generated/braindecode.datasets.BCICompetitionIVDataset4.html#braindecode.datasets.BCICompetitionIVDataset4)([subject_ids])               | BCI competition IV dataset 4.                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| `BNCI2014_001`                                                                                                                                                        |                                                            |
| [`CHBMIT`](generated/braindecode.datasets.CHBMIT.html#braindecode.datasets.CHBMIT)([root])                                                                            | The Children's Hospital Boston EEG Dataset.                |
| [`HGD`](generated/braindecode.datasets.HGD.html#braindecode.datasets.HGD)(subject_ids)                                                                                | High-gamma dataset described in Schirrmeister et al. 2017. |
| [`MOABBDataset`](generated/braindecode.datasets.MOABBDataset.html#braindecode.datasets.MOABBDataset)(dataset_name[, subject_ids, ...])                                | A class for moabb datasets.                                |
| [`NMT`](generated/braindecode.datasets.NMT.html#braindecode.datasets.NMT)([path, target_name, recording_ids, ...])                                                    | The NMT Scalp EEG Dataset.                                 |
| [`SleepPhysionet`](generated/braindecode.datasets.SleepPhysionet.html#braindecode.datasets.SleepPhysionet)([subject_ids, recording_ids, ...])                         | Sleep Physionet dataset.                                   |
| [`SIENA`](generated/braindecode.datasets.SIENA.html#braindecode.datasets.SIENA)([root])                                                                               | The Siena EEG Dataset.                                     |
| [`SleepPhysionetChallenge2018`](generated/braindecode.datasets.SleepPhysionetChallenge2018.html#braindecode.datasets.SleepPhysionetChallenge2018)([subject_ids, ...]) | Physionet Challenge 2018 polysomnography dataset.          |
| [`TUH`](generated/braindecode.datasets.TUH.html#braindecode.datasets.TUH)(path[, recording_ids, target_name, ...])                                                    | Temple University Hospital (TUH) EEG Corpus.               |
| [`TUHAbnormal`](generated/braindecode.datasets.TUHAbnormal.html#braindecode.datasets.TUHAbnormal)(path[, recording_ids, ...])                                         | Temple University Hospital (TUH) Abnormal EEG Corpus.      |
| [`TUHEvents`](generated/braindecode.datasets.TUHEvents.html#braindecode.datasets.TUHEvents)(path[, recording_ids, ...])                                               | Temple University Hospital (TUH) EEG Event Corpus.         |

<a id="dataset-builders-functions"></a>

### Dataset Builders Functions

Functions to create datasets from different data formats

| [`create_from_X_y`](generated/braindecode.datasets.create_from_X_y.html#braindecode.datasets.create_from_X_y)(X, y, drop_last_window, sfreq)            | Create a BaseConcatDataset of WindowsDatasets from X and y to be used for.   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [`create_from_mne_raw`](generated/braindecode.datasets.create_from_mne_raw.html#braindecode.datasets.create_from_mne_raw)(raws, ...[, ...])             | Create WindowsDatasets from mne.RawArrays.                                   |
| [`create_from_mne_epochs`](generated/braindecode.datasets.create_from_mne_epochs.html#braindecode.datasets.create_from_mne_epochs)(list_of_epochs, ...) | Create WindowsDatasets from mne.Epochs.                                      |

<a id="bids-integration"></a>

#### BIDS Integration

`braindecode.datasets.bids`:

The BIDS subpackage provides tools for working with BIDS-formatted EEG data, including
dataset loading and Hugging Face Hub push/pull functionality.

| [`BIDSDataset`](generated/braindecode.datasets.bids.BIDSDataset.html#braindecode.datasets.bids.BIDSDataset)(root[, subjects, sessions, ...])                     | Dataset for loading BIDS.                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [`BIDSEpochsDataset`](generated/braindecode.datasets.bids.BIDSEpochsDataset.html#braindecode.datasets.bids.BIDSEpochsDataset)(\*args, \*\*kwargs)                | **Experimental** dataset for loading [`mne.Epochs`](https://mne.tools/stable/generated/mne.Epochs.html#mne.Epochs) organised in BIDS. |
| [`BIDSIterableDataset`](generated/braindecode.datasets.bids.BIDSIterableDataset.html#braindecode.datasets.bids.BIDSIterableDataset)(reader_fn[, pool_size, ...]) | Dataset for loading BIDS.                                                                                                             |
| [`HubDatasetMixin`](generated/braindecode.datasets.bids.HubDatasetMixin.html#braindecode.datasets.bids.HubDatasetMixin)()                                        | Mixin class for Hugging Face Hub integration with EEG datasets.                                                                       |

<a id="preprocessing"></a>

### Preprocessing

`braindecode.preprocessing`:

<a id="core-functions"></a>

### Core Functions

| [`preprocess`](generated/braindecode.preprocessing.preprocess.html#braindecode.preprocessing.preprocess)(concat_ds, preprocessors[, ...])                                                      | Apply preprocessors to a concat dataset.                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| [`Preprocessor`](generated/braindecode.preprocessing.Preprocessor.html#braindecode.preprocessing.Preprocessor)(fn, \*[, apply_on_array])                                                       | Preprocessor for an MNE Raw or Epochs object.            |
| [`create_windows_from_events`](generated/braindecode.preprocessing.create_windows_from_events.html#braindecode.preprocessing.create_windows_from_events)(concat_ds[, ...])                     | Create windows based on events in mne.Raw.               |
| [`create_fixed_length_windows`](generated/braindecode.preprocessing.create_fixed_length_windows.html#braindecode.preprocessing.create_fixed_length_windows)(concat_ds[, ...])                  | Windower that creates sliding windows.                   |
| [`create_windows_from_target_channels`](generated/braindecode.preprocessing.create_windows_from_target_channels.html#braindecode.preprocessing.create_windows_from_target_channels)(concat_ds) |                                                          |
| [`exponential_moving_demean`](generated/braindecode.preprocessing.exponential_moving_demean.html#braindecode.preprocessing.exponential_moving_demean)(data[, ...])                             | Perform exponential moving demeaning.                    |
| [`exponential_moving_standardize`](generated/braindecode.preprocessing.exponential_moving_standardize.html#braindecode.preprocessing.exponential_moving_standardize)(data[, ...])              | Perform exponential moving standardization.              |
| [`filterbank`](generated/braindecode.preprocessing.filterbank.html#braindecode.preprocessing.filterbank)(raw, frequency_bands[, ...])                                                          | Applies multiple bandpass filters to the signals in raw. |

<a id="eegprep-pipeline"></a>

### EEGPrep Pipeline

| [`EEGPrep`](generated/braindecode.preprocessing.EEGPrep.html#braindecode.preprocessing.EEGPrep)(\*[, resample_to, flatline_maxdur, ...])                                  | Preprocessor for an MNE Raw object that applies the EEGPrep pipeline.                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [`ReinterpolateRemovedChannels`](generated/braindecode.preprocessing.ReinterpolateRemovedChannels.html#braindecode.preprocessing.ReinterpolateRemovedChannels)(\*[, ...]) | Reinterpolate previously removed EEG channels to restore original channel set.                    |
| [`RemoveBadChannels`](generated/braindecode.preprocessing.RemoveBadChannels.html#braindecode.preprocessing.RemoveBadChannels)(\*[, corr_threshold, ...])                  | Removes EEG channels with problematic data; variant that uses channel locations.                  |
| [`RemoveBadChannelsNoLocs`](generated/braindecode.preprocessing.RemoveBadChannelsNoLocs.html#braindecode.preprocessing.RemoveBadChannelsNoLocs)(\*[, min_corr, ...])      | Remove EEG channels with problematic data; variant that does not use channel locations.           |
| [`RemoveBadWindows`](generated/braindecode.preprocessing.RemoveBadWindows.html#braindecode.preprocessing.RemoveBadWindows)(\*[, max_bad_channels, ...])                   | Remove periods with abnormally high-power content from continuous data.                           |
| [`RemoveBursts`](generated/braindecode.preprocessing.RemoveBursts.html#braindecode.preprocessing.RemoveBursts)(\*[, cutoff, window_len, ...])                             | Run the Artifact Subspace Reconstruction (ASR) method on EEG data to remove burst-type artifacts. |
| [`RemoveCommonAverageReference`](generated/braindecode.preprocessing.RemoveCommonAverageReference.html#braindecode.preprocessing.RemoveCommonAverageReference)(\*[, ...]) | Subtracts the common average reference from the EEG data (EEGPrep version).                       |
| [`RemoveDCOffset`](generated/braindecode.preprocessing.RemoveDCOffset.html#braindecode.preprocessing.RemoveDCOffset)(\*[, can_change_duration, ...])                      | Remove the DC offset from the EEG data by subtracting the per-channel median.                     |
| [`RemoveDrifts`](generated/braindecode.preprocessing.RemoveDrifts.html#braindecode.preprocessing.RemoveDrifts)([transition, attenuation, method])                         | Remove drifts from the EEG data using a forward-backward high-pass filter.                        |
| [`RemoveFlatChannels`](generated/braindecode.preprocessing.RemoveFlatChannels.html#braindecode.preprocessing.RemoveFlatChannels)(\*[, ...])                               | Removes EEG channels that flat-line for extended periods of time.                                 |

<a id="signal-processing"></a>

### Signal Processing

| [`Resample`](generated/braindecode.preprocessing.Resample.html#braindecode.preprocessing.Resample)(sfreq, \*[, npad, window, ...])                                                 | Braindecode preprocessor wrapper for [`resample()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.resample).                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`Resampling`](generated/braindecode.preprocessing.Resampling.html#braindecode.preprocessing.Resampling)(sfreq)                                                                    | Resample the data to a specified rate (EEGPrep version).                                                                                                                                                                 |
| [`Filter`](generated/braindecode.preprocessing.Filter.html#braindecode.preprocessing.Filter)(l_freq, h_freq[, picks, ...])                                                         | Braindecode preprocessor wrapper for [`filter()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.filter).                                                                                                 |
| [`FilterData`](generated/braindecode.preprocessing.FilterData.html#braindecode.preprocessing.FilterData)(sfreq, l_freq, h_freq[, picks, ...])                                      | Braindecode preprocessor wrapper for [`filter_data()`](https://mne.tools/stable/generated/mne.filter.filter_data.html#mne.filter.filter_data).                                                                           |
| [`NotchFilter`](generated/braindecode.preprocessing.NotchFilter.html#braindecode.preprocessing.NotchFilter)(freqs[, picks, filter_length, ...])                                    | Braindecode preprocessor wrapper for [`notch_filter()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.notch_filter).                                                                                     |
| [`SavgolFilter`](generated/braindecode.preprocessing.SavgolFilter.html#braindecode.preprocessing.SavgolFilter)(h_freq[, verbose])                                                  | Braindecode preprocessor wrapper for [`savgol_filter()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.savgol_filter).                                                                                   |
| [`ApplyHilbert`](generated/braindecode.preprocessing.ApplyHilbert.html#braindecode.preprocessing.ApplyHilbert)([picks, envelope, n_jobs, ...])                                     | Braindecode preprocessor wrapper for [`apply_hilbert()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.apply_hilbert).                                                                                   |
| [`Rescale`](generated/braindecode.preprocessing.Rescale.html#braindecode.preprocessing.Rescale)(scalings, \*[, verbose])                                                           | Braindecode preprocessor wrapper for [`rescale()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.rescale).                                                                                               |
| [`OversampledTemporalProjection`](generated/braindecode.preprocessing.OversampledTemporalProjection.html#braindecode.preprocessing.OversampledTemporalProjection)([duration, ...]) | Braindecode preprocessor wrapper for [`oversampled_temporal_projection()`](https://mne.tools/stable/generated/mne.preprocessing.oversampled_temporal_projection.html#mne.preprocessing.oversampled_temporal_projection). |

<a id="channel-management"></a>

### Channel Management

| [`Pick`](generated/braindecode.preprocessing.Pick.html#braindecode.preprocessing.Pick)(picks[, exclude, verbose])                                                                  | Braindecode preprocessor wrapper for [`pick()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.pick).                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`PickChannels`](generated/braindecode.preprocessing.PickChannels.html#braindecode.preprocessing.PickChannels)(ch_names[, ordered, verbose])                                       | Braindecode preprocessor wrapper for [`pick_channels()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.pick_channels).                                                                                |
| [`PickTypes`](generated/braindecode.preprocessing.PickTypes.html#braindecode.preprocessing.PickTypes)([meg, eeg, stim, eog, ecg, emg, ...])                                        | Braindecode preprocessor wrapper for [`pick_types()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.pick_types).                                                                                      |
| [`DropChannels`](generated/braindecode.preprocessing.DropChannels.html#braindecode.preprocessing.DropChannels)(ch_names[, on_missing])                                             | Braindecode preprocessor wrapper for [`drop_channels()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.drop_channels).                                                                                |
| [`AddChannels`](generated/braindecode.preprocessing.AddChannels.html#braindecode.preprocessing.AddChannels)(add_list[, force_update_info])                                         | Braindecode preprocessor wrapper for [`add_channels()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.add_channels).                                                                                  |
| [`CombineChannels`](generated/braindecode.preprocessing.CombineChannels.html#braindecode.preprocessing.CombineChannels)(groups[, method, keep_stim, ...])                          | Braindecode preprocessor wrapper for [`combine_channels()`](https://mne.tools/stable/generated/mne.channels.combine_channels.html#mne.channels.combine_channels).                                                     |
| [`RenameChannels`](generated/braindecode.preprocessing.RenameChannels.html#braindecode.preprocessing.RenameChannels)(mapping[, allow_duplicates, ...])                             | Braindecode preprocessor wrapper for [`rename_channels()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.rename_channels).                                                                            |
| [`ReorderChannels`](generated/braindecode.preprocessing.ReorderChannels.html#braindecode.preprocessing.ReorderChannels)(ch_names)                                                  | Braindecode preprocessor wrapper for [`reorder_channels()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.reorder_channels).                                                                          |
| [`SetChannelTypes`](generated/braindecode.preprocessing.SetChannelTypes.html#braindecode.preprocessing.SetChannelTypes)(mapping, \*[, ...])                                        | Braindecode preprocessor wrapper for [`set_channel_types()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.set_channel_types).                                                                        |
| [`InterpolateBads`](generated/braindecode.preprocessing.InterpolateBads.html#braindecode.preprocessing.InterpolateBads)([reset_bads, mode, origin, ...])                           | Braindecode preprocessor wrapper for [`interpolate_bads()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.interpolate_bads).                                                                          |
| [`InterpolateTo`](generated/braindecode.preprocessing.InterpolateTo.html#braindecode.preprocessing.InterpolateTo)(sensors[, origin, method, ...])                                  | Braindecode preprocessor wrapper for [`interpolate_to()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.interpolate_to).                                                                              |
| [`InterpolateBridgedElectrodes`](generated/braindecode.preprocessing.InterpolateBridgedElectrodes.html#braindecode.preprocessing.InterpolateBridgedElectrodes)(bridged_idx[, ...]) | Braindecode preprocessor wrapper for [`interpolate_bridged_electrodes()`](https://mne.tools/stable/generated/mne.preprocessing.interpolate_bridged_electrodes.html#mne.preprocessing.interpolate_bridged_electrodes). |
| [`ComputeBridgedElectrodes`](generated/braindecode.preprocessing.ComputeBridgedElectrodes.html#braindecode.preprocessing.ComputeBridgedElectrodes)([lm_cutoff, ...])               | Braindecode preprocessor wrapper for [`compute_bridged_electrodes()`](https://mne.tools/stable/generated/mne.preprocessing.compute_bridged_electrodes.html#mne.preprocessing.compute_bridged_electrodes).             |
| [`EqualizeChannels`](generated/braindecode.preprocessing.EqualizeChannels.html#braindecode.preprocessing.EqualizeChannels)([copy, verbose])                                        | Braindecode preprocessor wrapper for [`equalize_channels()`](https://mne.tools/stable/generated/mne.channels.equalize_channels.html#mne.channels.equalize_channels).                                                  |
| [`EqualizeBads`](generated/braindecode.preprocessing.EqualizeBads.html#braindecode.preprocessing.EqualizeBads)([interp_thresh, copy])                                              | Braindecode preprocessor wrapper for [`equalize_bads()`](https://mne.tools/stable/generated/mne.preprocessing.equalize_bads.html#mne.preprocessing.equalize_bads).                                                    |
| [`FindBadChannelsLof`](generated/braindecode.preprocessing.FindBadChannelsLof.html#braindecode.preprocessing.FindBadChannelsLof)([n_neighbors, picks, ...])                        | Braindecode preprocessor wrapper for [`find_bad_channels_lof()`](https://mne.tools/stable/generated/mne.preprocessing.find_bad_channels_lof.html#mne.preprocessing.find_bad_channels_lof).                            |

<a id="reference-montage"></a>

### Reference & Montage

| [`SetEEGReference`](generated/braindecode.preprocessing.SetEEGReference.html#braindecode.preprocessing.SetEEGReference)([ref_channels, copy, ...])           | Braindecode preprocessor wrapper for [`set_eeg_reference()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.set_eeg_reference).           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`SetBipolarReference`](generated/braindecode.preprocessing.SetBipolarReference.html#braindecode.preprocessing.SetBipolarReference)(anode, cathode[, ...])   | Braindecode preprocessor wrapper for `set_bipolar_reference()`.                                                                                          |
| [`AddReferenceChannels`](generated/braindecode.preprocessing.AddReferenceChannels.html#braindecode.preprocessing.AddReferenceChannels)(ref_channels[, copy]) | Braindecode preprocessor wrapper for [`add_reference_channels()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.add_reference_channels). |
| [`SetMontage`](generated/braindecode.preprocessing.SetMontage.html#braindecode.preprocessing.SetMontage)(montage[, match_case, ...])                         | Braindecode preprocessor wrapper for [`set_montage()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.set_montage).                       |

<a id="ssp-projections"></a>

### SSP Projections

| [`AddProj`](generated/braindecode.preprocessing.AddProj.html#braindecode.preprocessing.AddProj)(projs[, remove_existing, verbose])   | Braindecode preprocessor wrapper for [`add_proj()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.add_proj).     |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [`ApplyProj`](generated/braindecode.preprocessing.ApplyProj.html#braindecode.preprocessing.ApplyProj)(\*[, projs, verbose])          | Braindecode preprocessor wrapper for [`apply_proj()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.apply_proj). |
| [`DelProj`](generated/braindecode.preprocessing.DelProj.html#braindecode.preprocessing.DelProj)([idx])                               | Braindecode preprocessor wrapper for [`del_proj()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.del_proj).     |

<a id="data-transformation"></a>

### Data Transformation

| [`Crop`](generated/braindecode.preprocessing.Crop.html#braindecode.preprocessing.Crop)([tmin, tmax, include_tmax, ...])                                                    | Braindecode preprocessor wrapper for [`crop()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.crop).                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`CropByAnnotations`](generated/braindecode.preprocessing.CropByAnnotations.html#braindecode.preprocessing.CropByAnnotations)([annotations, verbose])                      | Braindecode preprocessor wrapper for [`crop_by_annotations()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.crop_by_annotations).                                                                    |
| [`ComputeCurrentSourceDensity`](generated/braindecode.preprocessing.ComputeCurrentSourceDensity.html#braindecode.preprocessing.ComputeCurrentSourceDensity)([sphere, ...]) | Braindecode preprocessor wrapper for [`compute_current_source_density()`](https://mne.tools/stable/generated/mne.preprocessing.compute_current_source_density.html#mne.preprocessing.compute_current_source_density). |
| [`FixStimArtifact`](generated/braindecode.preprocessing.FixStimArtifact.html#braindecode.preprocessing.FixStimArtifact)([events, event_id, tmin, ...])                     | Braindecode preprocessor wrapper for [`fix_stim_artifact()`](https://mne.tools/stable/generated/mne.preprocessing.fix_stim_artifact.html#mne.preprocessing.fix_stim_artifact).                                        |
| [`MaxwellFilter`](generated/braindecode.preprocessing.MaxwellFilter.html#braindecode.preprocessing.MaxwellFilter)([origin, int_order, ...])                                | Braindecode preprocessor wrapper for [`maxwell_filter()`](https://mne.tools/stable/generated/mne.preprocessing.maxwell_filter.html#mne.preprocessing.maxwell_filter).                                                 |
| [`RealignRaw`](generated/braindecode.preprocessing.RealignRaw.html#braindecode.preprocessing.RealignRaw)(other, t_raw, t_other, \*[, verbose])                             | Braindecode preprocessor wrapper for [`realign_raw()`](https://mne.tools/stable/generated/mne.preprocessing.realign_raw.html#mne.preprocessing.realign_raw).                                                          |
| [`RegressArtifact`](generated/braindecode.preprocessing.RegressArtifact.html#braindecode.preprocessing.RegressArtifact)([picks, exclude, ...])                             | Braindecode preprocessor wrapper for [`regress_artifact()`](https://mne.tools/stable/generated/mne.preprocessing.regress_artifact.html#mne.preprocessing.regress_artifact).                                           |

<a id="artifact-detection-annotation"></a>

### Artifact Detection & Annotation

| [`AnnotateAmplitude`](generated/braindecode.preprocessing.AnnotateAmplitude.html#braindecode.preprocessing.AnnotateAmplitude)([peak, flat, bad_percent, ...])     | Braindecode preprocessor wrapper for [`annotate_amplitude()`](https://mne.tools/stable/generated/mne.preprocessing.annotate_amplitude.html#mne.preprocessing.annotate_amplitude).             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`AnnotateBreak`](generated/braindecode.preprocessing.AnnotateBreak.html#braindecode.preprocessing.AnnotateBreak)([events, min_break_duration, ...])              | Braindecode preprocessor wrapper for [`annotate_break()`](https://mne.tools/stable/generated/mne.preprocessing.annotate_break.html#mne.preprocessing.annotate_break).                         |
| [`AnnotateMovement`](generated/braindecode.preprocessing.AnnotateMovement.html#braindecode.preprocessing.AnnotateMovement)(pos[, ...])                            | Braindecode preprocessor wrapper for [`annotate_movement()`](https://mne.tools/stable/generated/mne.preprocessing.annotate_movement.html#mne.preprocessing.annotate_movement).                |
| [`AnnotateMuscleZscore`](generated/braindecode.preprocessing.AnnotateMuscleZscore.html#braindecode.preprocessing.AnnotateMuscleZscore)([threshold, ch_type, ...]) | Braindecode preprocessor wrapper for [`annotate_muscle_zscore()`](https://mne.tools/stable/generated/mne.preprocessing.annotate_muscle_zscore.html#mne.preprocessing.annotate_muscle_zscore). |
| [`AnnotateNan`](generated/braindecode.preprocessing.AnnotateNan.html#braindecode.preprocessing.AnnotateNan)(\*[, verbose])                                        | Braindecode preprocessor wrapper for [`annotate_nan()`](https://mne.tools/stable/generated/mne.preprocessing.annotate_nan.html#mne.preprocessing.annotate_nan).                               |

<a id="metadata-configuration"></a>

### Metadata & Configuration

| [`Anonymize`](generated/braindecode.preprocessing.Anonymize.html#braindecode.preprocessing.Anonymize)([daysback, keep_his, verbose])                                    | Braindecode preprocessor wrapper for [`anonymize()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.anonymize).                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`SetAnnotations`](generated/braindecode.preprocessing.SetAnnotations.html#braindecode.preprocessing.SetAnnotations)(annotations[, emit_warning, ...])                  | Braindecode preprocessor wrapper for [`set_annotations()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.set_annotations).                         |
| [`SetMeasDate`](generated/braindecode.preprocessing.SetMeasDate.html#braindecode.preprocessing.SetMeasDate)(meas_date)                                                  | Braindecode preprocessor wrapper for [`set_meas_date()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.set_meas_date).                             |
| [`AddEvents`](generated/braindecode.preprocessing.AddEvents.html#braindecode.preprocessing.AddEvents)(events[, stim_channel, replace])                                  | Braindecode preprocessor wrapper for [`add_events()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.add_events).                                   |
| [`FixMagCoilTypes`](generated/braindecode.preprocessing.FixMagCoilTypes.html#braindecode.preprocessing.FixMagCoilTypes)()                                               | Braindecode preprocessor wrapper for [`fix_mag_coil_types()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.fix_mag_coil_types).                   |
| [`ApplyGradientCompensation`](generated/braindecode.preprocessing.ApplyGradientCompensation.html#braindecode.preprocessing.ApplyGradientCompensation)(grade[, verbose]) | Braindecode preprocessor wrapper for [`apply_gradient_compensation()`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.apply_gradient_compensation). |

<a id="data-utils"></a>

## Data Utils

`braindecode.datautil`:

| [`save_concat_dataset`](generated/braindecode.datautil.save_concat_dataset.html#braindecode.datautil.save_concat_dataset)(path, concat_dataset[, ...])       |                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| [`load_concat_dataset`](generated/braindecode.datautil.load_concat_dataset.html#braindecode.datautil.load_concat_dataset)(path, preload[, ...])              | Load a stored BaseConcatDataset from.   |
| [`infer_signal_properties`](generated/braindecode.datautil.infer_signal_properties.html#braindecode.datautil.infer_signal_properties)(X[, y, mode, classes]) | Infers signal properties from the data. |

<a id="samplers"></a>

## Samplers

Samplers that can used to sample EEG data for training and testing and to create batches
of data, used on Self’Supervised Learning and other tasks.

`braindecode.samplers`:

| [`RecordingSampler`](generated/braindecode.samplers.RecordingSampler.html#braindecode.samplers.RecordingSampler)(metadata[, random_state])                                                  | Base sampler simplifying sampling from recordings.                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`DistributedRecordingSampler`](generated/braindecode.samplers.DistributedRecordingSampler.html#braindecode.samplers.DistributedRecordingSampler)(metadata[, ...])                          | Base sampler simplifying sampling from recordings in distributed setting.                                                                                                                                        |
| [`SequenceSampler`](generated/braindecode.samplers.SequenceSampler.html#braindecode.samplers.SequenceSampler)(metadata, n_windows, ...[, ...])                                              | Sample sequences of consecutive windows.                                                                                                                                                                         |
| [`RelativePositioningSampler`](generated/braindecode.samplers.RelativePositioningSampler.html#braindecode.samplers.RelativePositioningSampler)(metadata, ...[, ...])                        | Sample examples for the relative positioning task from [[R0467437a2408-Banville2020]](generated/braindecode.samplers.RelativePositioningSampler.html#r0467437a2408-banville2020).                                |
| [`DistributedRelativePositioningSampler`](generated/braindecode.samplers.DistributedRelativePositioningSampler.html#braindecode.samplers.DistributedRelativePositioningSampler)(...[, ...]) | Sample examples for the relative positioning task from [[Rc4a232d8b33d-Banville2020]](generated/braindecode.samplers.DistributedRelativePositioningSampler.html#rc4a232d8b33d-banville2020) in distributed mode. |
| [`BalancedSequenceSampler`](generated/braindecode.samplers.BalancedSequenceSampler.html#braindecode.samplers.BalancedSequenceSampler)(metadata, n_windows)                                  | Balanced sampling of sequences of consecutive windows with categorical targets.                                                                                                                                  |

<a id="augmentation-api"></a>

<a id="augmentation"></a>

## Augmentation

The augmentation module follow the pytorch transforms API. It contains transformations
that can be applied to EEG data. The transformations can be used to augment the data
during training, which can help improve the performance of the model. The
transformations can be applied to the data in a variety of ways, including time’domain
transformations, frequency’domain transformations, and spatial transformations.

`braindecode.augmentation`:

| [`Transform`](generated/braindecode.augmentation.Transform.html#braindecode.augmentation.Transform)([probability, random_state])                                           | Basic transform class used for implementing data augmentation.                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`IdentityTransform`](generated/braindecode.augmentation.IdentityTransform.html#braindecode.augmentation.IdentityTransform)([probability, random_state])                   | Identity transform.                                                                                                                                                    |
| [`Compose`](generated/braindecode.augmentation.Compose.html#braindecode.augmentation.Compose)(transforms)                                                                  | Transform composition.                                                                                                                                                 |
| [`AugmentedDataLoader`](generated/braindecode.augmentation.AugmentedDataLoader.html#braindecode.augmentation.AugmentedDataLoader)(dataset[, transforms, ...])              | A base dataloader class customized to applying augmentation Transforms.                                                                                                |
| [`TimeReverse`](generated/braindecode.augmentation.TimeReverse.html#braindecode.augmentation.TimeReverse)(probability[, random_state])                                     | Flip the time axis of each input with a given probability.                                                                                                             |
| [`SignFlip`](generated/braindecode.augmentation.SignFlip.html#braindecode.augmentation.SignFlip)(probability[, random_state])                                              | Flip the sign axis of each input with a given probability.                                                                                                             |
| [`FTSurrogate`](generated/braindecode.augmentation.FTSurrogate.html#braindecode.augmentation.FTSurrogate)(probability[, ...])                                              | FT surrogate augmentation of a single EEG channel, as proposed in [[Ra7c6c14d9bd9-1]](generated/braindecode.augmentation.FTSurrogate.html#ra7c6c14d9bd9-1).            |
| [`ChannelsShuffle`](generated/braindecode.augmentation.ChannelsShuffle.html#braindecode.augmentation.ChannelsShuffle)(probability[, p_shuffle, ...])                       | Randomly shuffle channels in EEG data matrix.                                                                                                                          |
| [`ChannelsDropout`](generated/braindecode.augmentation.ChannelsDropout.html#braindecode.augmentation.ChannelsDropout)(probability[, p_drop, ...])                          | Randomly set channels to flat signal.                                                                                                                                  |
| [`GaussianNoise`](generated/braindecode.augmentation.GaussianNoise.html#braindecode.augmentation.GaussianNoise)(probability[, std, random_state])                          | Randomly add white noise to all channels.                                                                                                                              |
| [`ChannelsSymmetry`](generated/braindecode.augmentation.ChannelsSymmetry.html#braindecode.augmentation.ChannelsSymmetry)(probability, ordered_ch_names)                    | Permute EEG channels inverting left and right-side sensors.                                                                                                            |
| [`SmoothTimeMask`](generated/braindecode.augmentation.SmoothTimeMask.html#braindecode.augmentation.SmoothTimeMask)(probability[, ...])                                     | Smoothly replace a randomly chosen contiguous part of all channels by.                                                                                                 |
| [`BandstopFilter`](generated/braindecode.augmentation.BandstopFilter.html#braindecode.augmentation.BandstopFilter)(probability, sfreq[, ...])                              | Apply a band-stop filter with desired bandwidth at a randomly selected.                                                                                                |
| [`FrequencyShift`](generated/braindecode.augmentation.FrequencyShift.html#braindecode.augmentation.FrequencyShift)(probability, sfreq[, ...])                              | Add a random shift in the frequency domain to all channels.                                                                                                            |
| [`SensorsRotation`](generated/braindecode.augmentation.SensorsRotation.html#braindecode.augmentation.SensorsRotation)(probability, ...[, axis, ...])                       | Interpolates EEG signals over sensors rotated around the desired axis.                                                                                                 |
| [`SensorsZRotation`](generated/braindecode.augmentation.SensorsZRotation.html#braindecode.augmentation.SensorsZRotation)(probability, ordered_ch_names)                    | Interpolates EEG signals over sensors rotated around the Z axis.                                                                                                       |
| [`SensorsYRotation`](generated/braindecode.augmentation.SensorsYRotation.html#braindecode.augmentation.SensorsYRotation)(probability, ordered_ch_names)                    | Interpolates EEG signals over sensors rotated around the Y axis.                                                                                                       |
| [`SensorsXRotation`](generated/braindecode.augmentation.SensorsXRotation.html#braindecode.augmentation.SensorsXRotation)(probability, ordered_ch_names)                    | Interpolates EEG signals over sensors rotated around the X axis.                                                                                                       |
| [`Mixup`](generated/braindecode.augmentation.Mixup.html#braindecode.augmentation.Mixup)(alpha[, beta_per_sample, random_state])                                            | Implements Iterator for Mixup for EEG data.                                                                                                                            |
| [`SegmentationReconstruction`](generated/braindecode.augmentation.SegmentationReconstruction.html#braindecode.augmentation.SegmentationReconstruction)(probability[, ...]) | Segmentation Reconstruction from Lotte (2015) [[R78e7a66c7d6f-Lotte2015]](generated/braindecode.augmentation.SegmentationReconstruction.html#r78e7a66c7d6f-lotte2015). |
| [`MaskEncoding`](generated/braindecode.augmentation.MaskEncoding.html#braindecode.augmentation.MaskEncoding)(probability[, max_mask_ratio, ...])                           | MaskEncoding from [[R9102599ed233-1]](generated/braindecode.augmentation.MaskEncoding.html#r9102599ed233-1).                                                           |
| [`AmplitudeScale`](generated/braindecode.augmentation.AmplitudeScale.html#braindecode.augmentation.AmplitudeScale)(probability[, interval, ...])                           | Rescale amplitude based on a random sampled scaling value.                                                                                                             |
| [`ChannelsReref`](generated/braindecode.augmentation.ChannelsReref.html#braindecode.augmentation.ChannelsReref)(probability[, random_state])                               | Randomly re-reference channels in EEG data matrix.                                                                                                                     |

The functional augmentation API contains the same transformations as the transforms API,
but they are implemented as functions.

`braindecode.augmentation.functional`:

| [`identity`](generated/braindecode.augmentation.functional.identity.html#braindecode.augmentation.functional.identity)(X, y)                                                               | Identity operation.                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`time_reverse`](generated/braindecode.augmentation.functional.time_reverse.html#braindecode.augmentation.functional.time_reverse)(X, y)                                                   | Flip the time axis of each input.                                                                                                                                       |
| [`sign_flip`](generated/braindecode.augmentation.functional.sign_flip.html#braindecode.augmentation.functional.sign_flip)(X, y)                                                            | Flip the sign axis of each input.                                                                                                                                       |
| [`ft_surrogate`](generated/braindecode.augmentation.functional.ft_surrogate.html#braindecode.augmentation.functional.ft_surrogate)(X, y, phase_noise_magnitude, ...)                       | FT surrogate augmentation of a single EEG channel, as proposed in [[R52a4658fffa7-1]](generated/braindecode.augmentation.functional.ft_surrogate.html#r52a4658fffa7-1). |
| [`channels_dropout`](generated/braindecode.augmentation.functional.channels_dropout.html#braindecode.augmentation.functional.channels_dropout)(X, y, p_drop[, random_state])               | Randomly set channels to flat signal.                                                                                                                                   |
| [`channels_shuffle`](generated/braindecode.augmentation.functional.channels_shuffle.html#braindecode.augmentation.functional.channels_shuffle)(X, y, p_shuffle[, random_state])            | Randomly shuffle channels in EEG data matrix.                                                                                                                           |
| [`channels_permute`](generated/braindecode.augmentation.functional.channels_permute.html#braindecode.augmentation.functional.channels_permute)(X, y, permutation)                          | Permute EEG channels according to fixed permutation matrix.                                                                                                             |
| [`gaussian_noise`](generated/braindecode.augmentation.functional.gaussian_noise.html#braindecode.augmentation.functional.gaussian_noise)(X, y, std[, random_state])                        | Randomly add white Gaussian noise to all channels.                                                                                                                      |
| [`smooth_time_mask`](generated/braindecode.augmentation.functional.smooth_time_mask.html#braindecode.augmentation.functional.smooth_time_mask)(X, y, ...)                                  | Smoothly replace a contiguous part of all channels by zeros.                                                                                                            |
| [`bandstop_filter`](generated/braindecode.augmentation.functional.bandstop_filter.html#braindecode.augmentation.functional.bandstop_filter)(X, y, sfreq, bandwidth, ...)                   | Apply a band-stop filter with desired bandwidth at the desired frequency.                                                                                               |
| [`frequency_shift`](generated/braindecode.augmentation.functional.frequency_shift.html#braindecode.augmentation.functional.frequency_shift)(X, y, delta_freq, sfreq)                       | Adds a shift in the frequency domain to all channels.                                                                                                                   |
| [`sensors_rotation`](generated/braindecode.augmentation.functional.sensors_rotation.html#braindecode.augmentation.functional.sensors_rotation)(X, y, ...)                                  | Interpolates EEG signals over sensors rotated around the desired axis.                                                                                                  |
| [`mixup`](generated/braindecode.augmentation.functional.mixup.html#braindecode.augmentation.functional.mixup)(X, y, lam, idx_perm)                                                         | Mixes two channels of EEG data.                                                                                                                                         |
| [`segmentation_reconstruction`](generated/braindecode.augmentation.functional.segmentation_reconstruction.html#braindecode.augmentation.functional.segmentation_reconstruction)(X, y, ...) | Segment and reconstruct EEG data from [[Rc19448ba78ac-1]](generated/braindecode.augmentation.functional.segmentation_reconstruction.html#rc19448ba78ac-1).              |
| [`mask_encoding`](generated/braindecode.augmentation.functional.mask_encoding.html#braindecode.augmentation.functional.mask_encoding)(X, y, time_start, ...)                               | Mark encoding from Ding et al (2024) from [[Re49696d5b28b-ding2024]](generated/braindecode.augmentation.functional.mask_encoding.html#re49696d5b28b-ding2024).          |
| [`amplitude_scale`](generated/braindecode.augmentation.functional.amplitude_scale.html#braindecode.augmentation.functional.amplitude_scale)(X, y, scale[, random_state])                   | Rescale amplitude of each channel based on a random sampled scaling value.                                                                                              |
| [`channels_rereference`](generated/braindecode.augmentation.functional.channels_rereference.html#braindecode.augmentation.functional.channels_rereference)(X, y[, random_state])           | Randomly re-reference channels in EEG data matrix.                                                                                                                      |

<a id="classifier"></a>

## Classifier

Skorch wrapper for braindecode models. The skorch wrapper allows to use braindecode
models with scikit’learn API.

`braindecode.classifier`:

| [`EEGClassifier`](generated/braindecode.classifier.EEGClassifier.html#braindecode.classifier.EEGClassifier)(module, \*args[, criterion, ...])   | Classifier that does not assume softmax activation.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|

<a id="regressor"></a>

## Regressor

Skorch wrapper for braindecode models focus on regression tasks. The skorch wrapper
allows to use braindecode models with scikit’learn API.

`braindecode.regressor`:

| [`EEGRegressor`](generated/braindecode.regressor.EEGRegressor.html#braindecode.regressor.EEGRegressor)(module, \*args[, cropped, ...])   | Regressor that calls loss function directly.   |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|

<a id="training"></a>

## Training

Training module contains functions and classes for training and evaluating EEG models.
It is inside the Classifier and Regressor skorch classes, and it is used to train the
models and evaluate their performance.

`braindecode.training`:

| [`CroppedLoss`](generated/braindecode.training.CroppedLoss.html#braindecode.training.CroppedLoss)(loss_function)                                                        | Compute Loss after averaging predictions across time.                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [`TimeSeriesLoss`](generated/braindecode.training.TimeSeriesLoss.html#braindecode.training.TimeSeriesLoss)(loss_function)                                               | Compute Loss between timeseries targets and predictions.                                                         |
| [`DanceLoss`](generated/braindecode.training.DanceLoss.html#braindecode.training.DanceLoss)([weight_class, weight_iou, ...])                                            | DANCE criterion: matched DETR (CE + IoU) + dense CE + consistency KL.                                            |
| [`CroppedTrialEpochScoring`](generated/braindecode.training.CroppedTrialEpochScoring.html#braindecode.training.CroppedTrialEpochScoring)(scoring[, ...])                | Class to compute scores for trials from a model that predicts (super)crops.                                      |
| [`CroppedTimeSeriesEpochScoring`](generated/braindecode.training.CroppedTimeSeriesEpochScoring.html#braindecode.training.CroppedTimeSeriesEpochScoring)(scoring[, ...]) | Class to compute scores for trials from a model that predicts (super)crops with time series target.              |
| [`PostEpochTrainScoring`](generated/braindecode.training.PostEpochTrainScoring.html#braindecode.training.PostEpochTrainScoring)(scoring[, ...])                         | Epoch Scoring class that recomputes predictions after the epoch on the training in validation mode.              |
| [`mixup_criterion`](generated/braindecode.training.mixup_criterion.html#braindecode.training.mixup_criterion)(preds, target)                                            | Implements loss for Mixup for EEG data.                                                                          |
| [`trial_preds_from_window_preds`](generated/braindecode.training.trial_preds_from_window_preds.html#braindecode.training.trial_preds_from_window_preds)(preds, ...)     | Assigning window predictions to trials  while removing duplicate predictions.                                    |
| [`predict_trials`](generated/braindecode.training.predict_trials.html#braindecode.training.predict_trials)(module, dataset[, ...])                                      | Create trialwise predictions and optionally also return trialwise targets from a cropped dataset given a module. |
| [`f1_event`](generated/braindecode.training.f1_event.html#braindecode.training.f1_event)(pred_events, gt_events[, iou_threshold])                                       | COCO-style greedy event F1: TP requires IoU > threshold AND class match.                                         |

<a id="utils"></a>

## Utils

Functions available in braindecode util module.

`braindecode.util`:

| [`set_random_seeds`](generated/braindecode.util.set_random_seeds.html#braindecode.util.set_random_seeds)(seed, cuda[, cudnn_benchmark])   | Set seeds for python random module numpy.random and torch.          |
|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [`resolve_montage_name`](generated/braindecode.util.resolve_montage_name.html#braindecode.util.resolve_montage_name)(name)                | Resolve an MNE standard montage name for the installed MNE version. |

<a id="visualization"></a>

## Visualization

Tools for opening up trained EEG decoders: per-trial attribution maps, sanity-check
protocols that probe whether those maps reflect what the model actually learned,
attribution-quality metrics, topographic projection, and confusion-matrix plotting.

The end-to-end workflow tracks the EEG-XAI benchmark of Sujatha Ravindran &
Contreras-Vidal (Sci Rep 2023, DOI [10.1038/s41598-023-43871-8](https://doi.org/10.1038/s41598-023-43871-8)): compute attributions, randomize labels
and weights, score the resulting maps against the trained-model reference, and decide
which methods are trustworthy on your data. See the [interpretability tutorial](auto_examples/advanced_training/plot_interpretability.html#interpretability-tutorial) for a worked example on BCI IV 2a.

`braindecode.visualization`:

<a id="time-domain-attribution"></a>

### Time-domain attribution

Per-trial attribution maps in the input domain. Each function takes `(model, x,
target)` and returns a tensor with the same spatial shape as `x`; all are thin
wrappers around [captum](https://captum.ai/) (a soft dependency installed via `pip
install braindecode[viz]`) and raise [`ImportError`](https://docs.python.org/3/builtins/exceptions.html#ImportError) without it.

| [`saliency`](generated/braindecode.visualization.saliency.html#braindecode.visualization.saliency)(model, x, target)                                            | Vanilla saliency: `|d y[target] / d x|`.                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`input_x_gradient`](generated/braindecode.visualization.input_x_gradient.html#braindecode.visualization.input_x_gradient)(model, x, target)                    | Element-wise input × input-gradient.                                    |
| [`integrated_gradients`](generated/braindecode.visualization.integrated_gradients.html#braindecode.visualization.integrated_gradients)(model, x, target[, ...]) | Integrated Gradients (Sundararajan et al., 2017) via captum.            |
| [`layer_grad_cam`](generated/braindecode.visualization.layer_grad_cam.html#braindecode.visualization.layer_grad_cam)(model, x, target, layer)                   | Layer GradCAM via captum: class-discriminative localization at `layer`. |
| [`guided_backprop`](generated/braindecode.visualization.guided_backprop.html#braindecode.visualization.guided_backprop)(model, x, target)                       | GuidedBackprop attribution (Springenberg et al., 2014) via captum.      |
| [`deconvolution`](generated/braindecode.visualization.deconvolution.html#braindecode.visualization.deconvolution)(model, x, target)                             | DeconvNet-style attribution (Zeiler & Fergus, 2014) via captum.         |
| [`deep_lift`](generated/braindecode.visualization.deep_lift.html#braindecode.visualization.deep_lift)(model, x, target[, baseline])                             | DeepLIFT attribution (Shrikumar et al., 2017) via captum.               |
| [`lrp`](generated/braindecode.visualization.lrp.html#braindecode.visualization.lrp)(model, x, target)                                                           | Layer-wise Relevance Propagation (Bach et al., 2015) via captum.        |

<a id="frequency-domain-attribution"></a>

### Frequency-domain attribution

Gradient of each model output with respect to the **amplitude spectrum** of the input —
a complement to the time-domain methods that makes oscillatory contributions (e.g.
alpha/beta motor imagery) visible directly in the topomap. Implemented in pure PyTorch
via `rfft`/`irfft` round-tripping; no captum needed.

| [`amplitude_gradients`](generated/braindecode.visualization.amplitude_gradients.html#braindecode.visualization.amplitude_gradients)(model, x)                                 | Per-batch amplitude gradients.                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`amplitude_gradients_per_trial`](generated/braindecode.visualization.amplitude_gradients_per_trial.html#braindecode.visualization.amplitude_gradients_per_trial)(model, ...) | Concatenated [`amplitude_gradients()`](generated/braindecode.visualization.amplitude_gradients.html#braindecode.visualization.amplitude_gradients) over every trial in a dataset. |

<a id="sanity-check-protocols"></a>

### Sanity-check protocols

Adebayo et al. (NeurIPS 2018) randomization checks for attribution maps, reused on EEG
decoders by Sujatha Ravindran & Contreras-Vidal. [`random_target()`](generated/braindecode.visualization.random_target.html#braindecode.visualization.random_target) powers the
**label-randomization** check (does the map change when you ask about the wrong class?)
and [`cascading_layer_reset()`](generated/braindecode.visualization.cascading_layer_reset.html#braindecode.visualization.cascading_layer_reset) powers the **weight-randomization** check (does the
map collapse as the trained weights are progressively replaced?). An attribution method
that survives both is suspicious — its output likely reflects architecture rather than
learning.

| [`random_target`](generated/braindecode.visualization.random_target.html#braindecode.visualization.random_target)(target, n_classes[, generator])                  | Return labels uniformly sampled from `{0, ..., n_classes-1} \ target`.   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [`cascading_layer_reset`](generated/braindecode.visualization.cascading_layer_reset.html#braindecode.visualization.cascading_layer_reset)(model[, deepcopy_first]) | Yield model copies with progressively-randomized parameters.             |

<a id="attribution-quality-metrics"></a>

### Attribution-quality metrics

Score how similar two attribution maps are: typically a trained-model attribution
against a randomized-model attribution, or against a ground-truth mask from a simulator.
[`compute_metrics()`](generated/braindecode.visualization.compute_metrics.html#braindecode.visualization.compute_metrics) returns twelve cosine / Pearson / mass-accuracy / rank-accuracy
variants; [`compute_ssim_metrics()`](generated/braindecode.visualization.compute_ssim_metrics.html#braindecode.visualization.compute_ssim_metrics) adds four SSIM-based scores using a pure-torch
reimplementation of skimage’s structural similarity (no extra dependency). Pass
`chs_info=` to score topographic projections instead of raw attribution maps.

| [`compute_metrics`](generated/braindecode.visualization.compute_metrics.html#braindecode.visualization.compute_metrics)(explanations, reference[, ...])         | Compute attribution-quality metrics between explanations and reference.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [`compute_ssim_metrics`](generated/braindecode.visualization.compute_ssim_metrics.html#braindecode.visualization.compute_ssim_metrics)(explanations, reference) | Compute four SSIM-based attribution-quality metrics.                      |
| [`METRIC_NAMES`](generated/braindecode.visualization.METRIC_NAMES.html#braindecode.visualization.METRIC_NAMES)                                                  | Built-in mutable sequence.                                                |
| [`SSIM_METRIC_NAMES`](generated/braindecode.visualization.SSIM_METRIC_NAMES.html#braindecode.visualization.SSIM_METRIC_NAMES)                                   | Built-in mutable sequence.                                                |

<a id="activations"></a>

### Activations

Read or replace a submodule’s output during a forward pass. The temporary hooks are
removed even when the forward pass raises.

| [`capture_activations`](generated/braindecode.visualization.capture_activations.html#braindecode.visualization.capture_activations)(model, x, layer)                                      | Return the output emitted by `layer` during `model(x)`.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [`run_with_activation_substitution`](generated/braindecode.visualization.run_with_activation_substitution.html#braindecode.visualization.run_with_activation_substitution)(model, x, ...) | Run `model(x)` after replacing `layer`'s output.          |

<a id="topography"></a>

### Topography

Project per-channel scalar values onto a 2-D scalp topomap grid via Clough-Tocher
triangulation on MNE-derived sensor coordinates. Returns a plain `ndarray` so callers
can compose with their own plotting stack rather than going through
[`mne.viz.plot_topomap()`](https://mne.tools/stable/generated/mne.viz.plot_topomap.html#mne.viz.plot_topomap) (and its matplotlib roundtrip).

| [`project_to_topomap`](generated/braindecode.visualization.project_to_topomap.html#braindecode.visualization.project_to_topomap)(data, chs_info[, res])   | Project per-channel attribution values onto a 2-D scalp topomap grid.   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|

<a id="plotting"></a>

### Plotting

| [`plot_confusion_matrix`](generated/braindecode.visualization.plot_confusion_matrix.html#braindecode.visualization.plot_confusion_matrix)(confusion_mat[, ...])   | Generates a confusion matrix with additional precision and sensitivity metrics as in [[R8046536b33dd-1]](generated/braindecode.visualization.plot_confusion_matrix.html#r8046536b33dd-1).   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
