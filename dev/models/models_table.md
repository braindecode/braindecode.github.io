Braindecode package version: 1.8.1

Documentation scope: https://braindecode.org/dev/

Source commit: [31bb32c62b90a7f75fe332a2cc524d1756a068b6](https://github.com/braindecode/braindecode/tree/31bb32c62b90a7f75fe332a2cc524d1756a068b6)

Canonical HTML: [Model selection (interactive table in HTML)](https://braindecode.org/dev/models/models_table.html)

---

<a id="models-summary"></a>

# Models Summary

This page offers a summary of all [`braindecode`](../api.html#module-braindecode) implemented models. For more
information on each model, please consult the API.

Columns definitions:

> - **Model**: The name of the model.
> - **Application**: The application(s) the model is typically used for (e.g., Motor
>   Imagery, P300, Sleep Staging). ‘General’ indicates applicability across multiple
>   applications or no specific application focus.
> - **Modality**: The recording modality (bio-signal type) the model is designed and
>   validated for, e.g. EEG, MEG, or sEMG. Most Braindecode models target EEG; a few
>   support more than one modality (e.g. EEG, MEG).
> - **Type**: The model’s output interface. `Prediction` indicates a supervised head
>   that can be used for classification or regression, depending on the wrapper, loss,
>   and target. `Embedding` indicates a model that exposes an embedding
>   representation through its documented public interface.
> - **Sampling Frequency**: The data sampling rate (in Hertz) the model is designed
>   for. Note that this might be adaptable depending on the specific dataset and
>   application.
> - **Categorization**: models categorization based on the main building blocks used
>   in the architecture. See Models Categorization page for more details.
> - **Hyperparameters**: The mandatory hyperparameters required for instantiating the model class. These may include:
>   : -  **n_chans**, number of channels/electrodes/sensors,
>     -  **n_outputs**, number of output classes or regression targets,
>     -  **n_times**, number of time points in the input window,
>     -  **freq (Hz)**, sampling frequency,
>     -  **chs_info**, information about each individual EEG
>       channel. Refer to [`mne.Info`](https://mne.tools/stable/generated/mne.Info.html#mne.Info) (see its “chs” field for details)

> Also, n_times can be derived implicitly by providing both sfreq and
> input_window_seconds.

> - **#Parameters**: The approximate total number of trainable parameters in the
>   model, calculated using a consistent configuration (see note below).

The parameter counts shown in the table were calculated using consistent hyperparameters
for models within the same paradigm, based largely on Braindecode’s default
implementation values. These counts provide a relative comparison but may differ from
those reported in the original publications due to variations in specific architectural
details, input dimensions used in the paper, or calculation methods.

We are continually expanding this collection and welcome contributions! If you have
implemented a model relevant to EEG, EcoG, or MEG analysis, consider adding it to
Braindecode.

 [Next: Models Parameter Visualization](models_visualization.html)
