Braindecode package version: 1.8.1

Documentation scope: https://braindecode.org/dev/

Source commit: [cb1ca885d1bf7860fa0d74f87c8f46ad274e1646](https://github.com/braindecode/braindecode/tree/cb1ca885d1bf7860fa0d74f87c8f46ad274e1646)

Canonical HTML: [Installation from PyPI](https://braindecode.org/dev/install/install_pip.html)

---

<a id="install-pip"></a>

<a id="installing-from-pypi"></a>

# Installing from PyPI

Braincode can be installed via pip from [PyPI](https://pypi.org/project/braindecode).

#### NOTE
We recommend the most updated version of pip to install from PyPI.

Below are the installation commands for the most common use cases.

```console
pip install braindecode
```

Braindecode can also be installed along [MOABB](https://moabb.neurotechx.com) to download open datasets:

```bash
pip install braindecode[moabb]
```

Braindecode can also be installed with all optional dependencies for testing and
documentation building:

```bash
pip install braindecode[all]
```

To use the potential of the deep learning modules PyTorch with GPU, we recommend the
following sequence before installing the braindecode:

1. Install the latest NVIDIA driver.
2. Check [PyTorch’s](https://pytorch.org) official guide, for the recommended CUDA versions. For
   the Pip package, the user must download the CUDA manually, install it on the system,
   and ensure CUDA_PATH is appropriately set and working!
3. Continue to follow the guide and install PyTorch.

See the [Frequently Asked Questions (FAQ)](../help.html) section if you have a problem.

<!-- This (-*- rst -*-) format file contains commonly used link targets
and name substitutions.  It may be included in many files,
therefore it should only contain link targets and name
substitutions.  Try grepping for "^\.\. _" to find plausible
candidates for this list. -->
<!-- NOTE: reST targets are
__not_case_sensitive__, so only one target definition is needed for
nipy, NIPY, Nipy, etc... -->
<!-- braindecode -->
<!-- mne -->
<!-- moabb -->
<!-- main dependencies -->
<!-- git stuff -->
<!-- other stuff -->
<!-- spd_learn -->
<!-- vim: ft=rst -->
