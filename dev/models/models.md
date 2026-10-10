Braindecode package version: 1.8.1

Documentation scope: https://braindecode.org/dev/

Source commit: [ceedaa306a0a5a549ae23d16c9b5be0538409d67](https://github.com/braindecode/braindecode/tree/ceedaa306a0a5a549ae23d16c9b5be0538409d67)

Canonical HTML: [The decoding problem](https://braindecode.org/dev/models/models.html)

---

<a id="models"></a>

<a id="the-brain-decode-problem"></a>

# The brain decode problem

All the models in this library tackle the following problem: given time-series signals
$X \in \mathbb{R}^{C \times T}$ and labels $y \in \mathcal{Y}$,
[`braindecode`](../api.html#module-braindecode) implements neural networks $f$ that **decode** brain
activity, i.e., it applies a series of transformations layers (e.g.
[`Conv2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv2d.html#torch.nn.Conv2d), [`Linear`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Linear.html#torch.nn.Linear), [`ELU`](https://docs.pytorch.org/docs/stable/generated/torch.nn.ELU.html#torch.nn.ELU)) to the
data to allow us to filter and extract features that are relevant to what we are
modeling, in other words:

$$
f_{\theta} : X \to y,
$$

where $C$ (`n_chans`) is the number of channels/electrodes and $T$
(`n_times`) is the temporal window length/epoch size over the interval of interest.

The definition of $y$ is broad; it may be anchored in a cognitive stimulus (e.g.,
BCI, ERP, SSVEP, cVEP), mental state (sleep stage), brain age, visual/audio/text/action
inputs, or any target that can be quantized and modeled as a decoding task, see
references
[1](#id4), [2](#id8), [3](#id5), [4](#id9), [5](#id10), [6](#id12), [7](#id13), [8](#id14).

We aim to translate recorded brain activity into its originating stimulus, behavior, or
mental state, King and Dehaene [[2014](#id15)], King *et al.* [[2020](#id16)], again, $f(X) \to y$.

The neural networks model $f$ learns a representation that is useful for the
encoded stimulus in the subject’s brain over time series—also known as *reverse
inference*.

In supervised decoding, we usually learn the network parameters $\theta$ by
minimizing the regularized the average loss over the training set
$\mathcal{D}_{\text{tr}}=\{(x_i,y_i)\}_{i=1}^{N_{\text{tr}}}$.

$$
\begin{aligned}
\theta^{*}
  &= \arg\min_{\theta}\, \hat{\mathcal{R}}(\theta) \\
  &= \arg\min_{\theta}\, \frac{1}{N_{\text{tr}}}\sum_{i=1}^{N_{\text{tr}}}
     \ell\!\left(f_{\theta}(x_i),\, y_i\right) \;+\; \lambda\,\Omega(\theta)\,,
\end{aligned}
$$

where $\ell$ is the task loss (e.g., cross-entropy
[`CrossEntropyLoss`](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html#torch.nn.CrossEntropyLoss)), $\Omega$ is an optional regularizer, and
$\lambda \ge 0$ its weight (e.g. `weight_decay` parameter in
[`Adam`](https://docs.pytorch.org/docs/stable/generated/torch.optim.Adam.html#torch.optim.Adam) is the example of regularization).

Equivalently, the goal is to minimize the expected risk
$\mathcal{R}(\theta)=\mathbb{E}_{(x,y)\sim P_{\text{tr}}}
[\ell(f_{\theta}(x),y)]$, for which the empirical average above is a finite-sample
approximation.

With this, in this model’s sub-pages, we provide:

> - 1. Our definition of the brain decoding problem (here);
> - 1. [The categorization of the neural networks based on what is inside them](models_categorization.html);
> - 1. [A table overview to understand what is inside the models](models_table.html);
> - 1. [A visualization of the common important information from the models](models_visualization.html).

[Browse the models table →](models_table.html)

### References

<a id="id4"></a>
[1] 

Bruno Aristimunha, Alexandre Janoni Bayerlein, M. Jorge Cardoso, Walter Hugo Lopez Pinaya, and Raphael Yokoingawa De Camargo. Sleep-Energy: An Energy Optimization Method to Sleep Stage Scoring. *IEEE Access*, 11:34595–34602, 2023.



<a id="id8"></a>
[2] 

Bruno Aristimunha, Igor Carrara, Pierre Guetschel, Sara Sedlar, Pedro Rodrigues, Jan Sosulski, Divyesh Narayanan, Erik Bjareholt, Barthelemy Quentin, Robin Tibor Schirrmeister, Emmanuel Kalunga, Ludovic Darmet, Cattan Gregoire, Ali Abdul Hussain, Ramiro Gatti, Vladislav Goncharenko, Jordy Thielen, Thomas Moreau, Yannick Roy, Vinay Jayaram, Alexandre Barachant, and Sylvain Chevallier. Mother of all bci benchmarks v1.0. [https://doi.org/10.5281/zenodo.10034223](https://doi.org/10.5281/zenodo.10034223), 2023. DOI: 10.5281/zenodo.10034223.



<a id="id5"></a>
[3] 

Sylvain Chevallier, Igor Carrara, Bruno Aristimunha, Pierre Guetschel, Sara Sedlar, Bruna Lopes, Sebastien Velut, Salim Khazem, and Thomas Moreau. The largest EEG-based BCI reproducibility study for open science: the MOABB benchmark. *arXiv preprint arXiv:2404.15319*, 2024.



<a id="id9"></a>
[4] 

Jarod Lévy, Mingfang Zhang, Svetlana Pinet, Jérémy Rapin, Hubert Banville, Stéphane d'Ascoli, and Jean-Rémi King. Brain-to-text decoding: a non-invasive approach via typing. *arXiv preprint arXiv:2502.17480*, 2025.



<a id="id10"></a>
[5] 

Yohann Benchetrit, Hubert Banville, and Jean-Remi King. Brain decoding: toward real-time reconstruction of visual perception. In *The Twelfth International Conference on Learning Representations*. 2024. URL: [https://openreview.net/forum?id=3y1K6buO8c](https://openreview.net/forum?id=3y1K6buO8c).



<a id="id12"></a>
[6] 

Stéphane d'Ascoli, Corentin Bel, Jérémy Rapin, Hubert Banville, Yohann Benchetrit, Christophe Pallier, and Jean-Rémi King. Decoding individual words from non-invasive brain recordings across 723 participants. *arXiv preprint arXiv:2412.17829*, 2024.



<a id="id13"></a>
[7] 

Denis A Engemann, Apolline Mellot, Richard Höchenberger, Hubert Banville, David Sabbagh, Lukas Gemein, Tonio Ball, and Alexandre Gramfort. A reusable benchmark of brain-age prediction from m/eeg resting-state signals. *Neuroimage*, 262:119521, 2022.



<a id="id14"></a>
[8] 

Jonathan Xu, Bruno Aristimunha, Max Emanuel Feucht, Emma Qian, Charles Liu, Tazik Shahjahan, Martyna Spyra, Steven Zifan Zhang, Nicholas Short, Jioh Kim, Paula Perdomo, Ricky Renfeng Mao, Yashvir Sabharwal, Michael Ahedor Moaz Shoura, and Adrian Nestor. Alljoined – a dataset for EEG-to-image decoding. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), Workshop on Data Curation and Augmentation in Enhancing Medical Imaging Applications*, 1–9. 2024.



<a id="id15"></a>
[9] 

Jean-Rémi King and Stanislas Dehaene. Characterizing the dynamics of mental representations: the temporal generalization method. *Trends in cognitive sciences*, 18(4):203–210, 2014.



<a id="id16"></a>
[10] 

Jean-Rémi King, Laura Gwilliams, Chris Holdgraf, Jona Sassenhagen, Alexandre Barachant, Denis Engemann, Eric Larson, and Alexandre Gramfort. Encoding and Decoding Framework to Uncover the Algorithms of Cognition. In *The Cognitive Neurosciences*. The MIT Press, 05 2020.



<a id="id30"></a>
[11] 

Ravikiran Mane, Effie Chew, Karen Chua, Kai Keng Ang, Neethu Robinson, A Prasad Vinod, Seong-Whan Lee, and Cuntai Guan. Fbcnet: a multi-view convolutional neural network for brain-computer interface. *arXiv preprint arXiv:2104.01233*, 2021.



<a id="id31"></a>
[12] 

Ke Liu, Mingzhao Yang, Zhuliang Yu, Guoyin Wang, and Wei Wu. Fbmsnet: a filter-bank multi-scale convolutional neural network for eeg-based motor imagery decoding. *IEEE Transactions on Biomedical Engineering*, 70(2):436–445, 2022.



<a id="id29"></a>
[13] 

Davide Borra, Silvia Fantozzi, and Elisa Magosso. Interpretable and lightweight convolutional neural network for eeg decoding: application to movement execution and imagination. *Neural Networks*, 129:55–74, 2020.



<a id="id28"></a>
[14] 

Siegfried Ludwig, Stylianos Bakas, Dimitrios A Adamos, Nikolaos Laskaris, Yannis Panagakis, and Stefanos Zafeiriou. Eegminer: discovering interpretable features of brain activity with learnable filters. *Journal of Neural Engineering*, 21(3):036010, 2024.



<a id="id21"></a>
[15] 

Shaojie Bai, J Zico Kolter, and Vladlen Koltun. An empirical evaluation of generic convolutional and recurrent networks for sequence modeling. *arXiv preprint arXiv:1803.01271*, 2018.



<a id="id18"></a>
[16] 

Yonghao Song, Qingqing Zheng, Bingchuan Liu, and Xiaorong Gao. Eeg conformer: convolutional transformer for eeg decoding and visualization. *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 31:710–719, 2022.



<a id="id19"></a>
[17] 

Wei Zhao, Xiaolu Jiang, Baocan Zhang, Shixiao Xiao, and Sujun Weng. CTNet: a convolutional transformer network for EEG-based motor imagery classification. *Scientific reports*, 14(1):20237, 2024.



<a id="id20"></a>
[18] 

Hamdi Altaheri, Ghulam Muhammad, and Mansour Alsulaiman. Physics-informed attention temporal convolutional network for EEG-based motor imagery classification. *IEEE transactions on industrial informatics*, 19(2):2249–2258, 2022.



<a id="id26"></a>
[19] 

Zhiwu Huang and Luc Van Gool. A riemannian network for spd matrix learning. In *Proceedings of the AAAI conference on artificial intelligence*, volume 31. 2017.



<a id="id27"></a>
[20] 

Bruno Aristimunha, Ce Ju, Antoine Collas, Florent Bouchard, Ammar Mian, Bertrand Thirion, Sylvain Chevallier, and Reinmar Kobler. Spd learn: a geometric deep learning python library for neural decoding through trivialization. *arXiv preprint arXiv:2602.22895*, 2026.



<a id="id25"></a>
[21] 

Tengfei Song, Wenming Zheng, Peng Song, and Zhen Cui. Eeg emotion recognition using dynamical graph convolutional neural networks. *IEEE Transactions on Affective Computing*, 11(3):532–541, 2020. [doi:10.1109/TAFFC.2018.2817622](https://doi.org/10.1109/TAFFC.2018.2817622).



<a id="id24"></a>
[22] 

Dominik Klepl, Min Wu, and Fei He. Graph neural network-based eeg classification: a survey. *IEEE Transactions on Neural Systems and Rehabilitation Engineering*, 32:493–503, 2024.



<a id="id23"></a>
[23] 

P. Guetschel, T. Moreau, and M. Tangermann. S-JEPA: towards seamless cross-dataset transfer through dynamic spatial attention. In *Proceedings of the 9th Graz Brain-Computer Interface Conference*. 2024. URL: [https://doi.org/10.3217/978-3-99161-014-4-003](https://doi.org/10.3217/978-3-99161-014-4-003), [doi:10.3217/978-3-99161-014-4-003](https://doi.org/10.3217/978-3-99161-014-4-003).



<a id="id22"></a>
[24] 

Zhige Chen, Rui Yang, Mengjie Huang, Fumin Li, Guoping Lu, and Zidong Wang. Eegprogress: a fast and lightweight progressive convolution architecture for eeg classification. *Computers in Biology and Medicine*, 169:107901, 2024.



<a id="id32"></a>
[25] 

Chaoqi Yang, M Westover, and Jimeng Sun. Biot: biosignal transformer for cross-data learning in the wild. *Advances in Neural Information Processing Systems*, 36:78240–78260, 2023.



<a id="id7"></a>
[26] 

Weibang Jiang, Liming Zhao, and Bao-liang Lu. Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI. In *The Twelfth International Conference on Learning Representations*. 2024. URL: [https://openreview.net/forum?id=QzTpTRVtrP](https://openreview.net/forum?id=QzTpTRVtrP).



<a id="id267"></a>
[27] 

Guangyu Wang, Wenchao Liu, Yuhong He, Cong Xu, Lin Ma, and Haifeng Li. EEGPT: pretrained transformer for universal and reliable representation of EEG signals. In *The Thirty-eighth Annual Conference on Neural Information Processing Systems*. 2024. URL: [https://openreview.net/forum?id=lvS2b8CjG5](https://openreview.net/forum?id=lvS2b8CjG5).



<a id="id271"></a>
[28] 

Jathurshan Pradeepkumar, Xihao Piao, Zheng Chen, and Jimeng Sun. Tokenizing single-channel EEG with time-frequency motif learning. In *The Fourteenth International Conference on Learning Representations*. 2026. URL: [https://openreview.net/forum?id=2sPmWHZ8Ir](https://openreview.net/forum?id=2sPmWHZ8Ir).



<a id="id270"></a>
[29] 

Tidiane Camaret N'dir, Robin Tibor Schirrmeister, and Tonio Ball. EEG-CLIP: learning EEG representations from natural language descriptions. *Frontiers in Robotics and AI*, 12:1625731, 2025. URL: [https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1625731/full](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1625731/full), [doi:10.3389/frobt.2025.1625731](https://doi.org/10.3389/frobt.2025.1625731).



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
