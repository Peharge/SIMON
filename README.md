<p align="center">
    <img src="./img-readme/solution6.ico" width="250"/>
</p>
<br>
<div align="center">

<img alt="SIMON" src="https://img.shields.io/badge/SIMON-blue">
<img alt="Peharge" src="https://img.shields.io/badge/Peharge-8A2BE2">
<br>
<br>

<img alt="python" src="https://img.shields.io/badge/Python-3.11 / 3.12 / 3.13-blue?&logo=Python&logoColor=white%5BPython">
<img alt="c++" src="https://img.shields.io/badge/-C++-blue?logo=cplusplus">
<img alt="c" src="https://img.shields.io/badge/-C-blue?logo=c">
<br>
<br>

<img alt="pytorch" src="https://img.shields.io/badge/PyTorch-EE4C2C?logo=PyTorch&logoColor=white">
<img alt="flask" src="https://img.shields.io/badge/django-092E20?logo=django&logoColor=white">
<img alt="pycharm" src="https://img.shields.io/badge/PyCharm-black?logo=PyCharm&logoColor=white">
<img alt="" src="https://img.shields.io/badge/Jupyter-notebook-brightgreen">
<img alt="" src="https://img.shields.io/badge/Google-Colab-red">
<img alt="github" src="https://img.shields.io/badge/GitHub-black?logo=github">
<img alt="" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue">
<br>
<br>

<img alt="os" src="https://img.shields.io/badge/os-linux%20%7C%20macOS%20%7C%20windows-blue">
<br>
<br>

[![MONAI](https://img.shields.io/badge/-MONAI-blue)](https://monai.io/)
[![PyPI version](https://badge.fury.io/py/monai.svg)](https://badge.fury.io/py/monai)
[![docker](https://img.shields.io/badge/docker-pull-green.svg?logo=docker&logoColor=white)](https://hub.docker.com/r/projectmonai/monai)
[![conda](https://img.shields.io/conda/vn/conda-forge/monai?color=green)](https://anaconda.org/conda-forge/monai)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<br>

</div>

# _SIMON_

> **S** olution **I** ntelligence **M** edical **O** pen **N** etwork

> ⚠️**Still in progress**⚠️

> ⚠️ Important warning: Beware of fake accounts! ⚠️
There is evidence that fake accounts may attempt to misrepresent this project. Please do not share personal information with anyone you do not know and only rely on content coming directly from this repository. Immediately report large activities or accounts to GitHub or the project team.
  
This project works with the GP-LSTM-GRU-T-IQ parameter and aims to obtain images from various imaging techniques such as X-ray (classic X-ray), CT (computed tomography), MRI (magnetic resonance imaging), PET (positron emission tomography), DEXA (dual-energy X-ray absorptiometry) and fluoroscopy (interventional radiology).
The goal is to help diagnose lung cancer, breast cancer, prostate cancer, colon cancer, leukemia, skin cancer, pancreatic cancer, kidney cancer, cervical cancer, brain tumors, liver cancer, esophageal cancer, thyroid cancer, bladder cancer, stomach cancer and other cancers.

## _News_

- **[2024.10.04]** Start ;-)
- **[2024.11.09]** Start on Github ;-)
- **[2025.01.01]** New Updates - aka. new start ;-)

## _Inhaltsverzeichnis_

- [Updates](#updates)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Checklist](#checklist)
- [Transformer](#transformer)
- [Medical information](#medical-information)
- [License](#license)

---

## Updates

### _SIMON 1.0 [soon]_

<p align="center">
    <img src="./img-readme/simon-banner1.png" width="1400"/>
</p>

> 2025.04.01

### _SIMON 2.0 [soon]_

<p align="center">
    <img src="./img-readme/simon-banner2.png" width="1400"/>
</p>

> 2025.10.01

### _SIMON 3.0 [soon]_

<p align="center">
    <img src="./img-readme/simon-banner3.png" width="1400"/>
</p>

> 2026.04.01

### Demo

<img src="./img-readme/Screenshot 2024-10-09 150838.png" width="1400">
<img src="./img-readme/Screenshot 2024-10-15 195936.png" width="1400">
<img src="./img-readme/Screenshot 2024-10-11 171846.png" width="1400">

## Installation

> ⚠️**Still in progress**⚠️

> soon Mac os and Linux

  **MAVIS (aka Xc++ 2)** is currently under development and is not fully available in this repository. Cloning the repository will only give you the README file, some images and already released codes, including the user interface (UI) compatible with **Qwen 2.5 Code** and **Llama 3.2 Vision**.

### Prerequisites

   To successfully install MAVIS, you need the following programs:

1. **Git**<br>
   Download [Git](https://git-scm.com/) from the official website:
   [Git Download](https://git-scm.com)

2. **Python**<br>
   - Download [Python](https://www.python.org/) from [Python Download](https://www.python.org) or via the [Microsoft Store](https://apps.microsoft.com/).<br>
   _Recommended: **Python 3.13** (3.12 or 3.11 are also supported)._

3. **Python development environment (IDE) (but not required)**<br>
   A suitable IDE makes developing and working with Python easier. Recommended options:
   - [Visual Studio Code](https://code.visualstudio.com/) (VS Code for short) is a free source code editor from Microsoft.<br>
   **Download**: [Visual Studio Code Download](https://code.visualstudio.com)
   - [PyCharm](https://www.jetbrains.com/pycharm/) is an integrated development environment (IDE) from the Czech company JetBrains for the Python programming language.<br>
   **Download**: [PyCharm Download](https://www.jetbrains.com/de-de/pycharm/)<br>
   _**Note:** PyCharm offers advanced features for Python development and is particularly suitable for advanced users._

4. **3D Slicer**<br>
    This project uses [3D Slicer](https://www.slicer.org/), which is a free and open source software package for image analysis and scientific visualization.<br>
    **Download**: [3D Slicer Download](https://download.slicer.org/)

### Installation

1. **Clone repository**<br>
   Clone the repository to a local directory:
    ```bash
    git clone https://github.com/Peharge/SIMON
    ```
2. **Change directory**<br>
   Navigate to the project directory:
    ```bash
    cd SIMON
    ```
3. **Create Python virtual environment**<br>
   Set up a virtual environment to install dependencies in isolation:
    ```bash
    python -m venv venv
    ```
   *(You can replace `venv` with any other name.)*

4. **Activate virtual environment**<br>
   Activate the virtual environment:
   - **For CMD**:
       ```bash
       venv\Scripts\activate
       ```
   - **For PowerShell**:
       ```bash
       .\venv\Scripts\Activate
       ```

5. Install the necessary dependencies (if required):<br>
    [MONAI.com](https://monai.io/) - [MONAI GitHub](https://github.com/Project-MONAI/MONAI) - [MONAI Label.com](https://monai.io/label.html) - [MONAI Label GitHub](https://github.com/Project-MONAI/MONAILabel) - [MONAI Model Zoo.com](https://monai.io/model-zoo.html) - [MONAI Model Zoo GitHub](https://github.com/Project-MONAI/model-zoo) - [MONAI Tutorials GitHub](https://github.com/Project-MONAI/tutorials/tree/main)
    ```bash
    pip install monai
    pip install monailabel
    ```
    or
    ```bash
    pip install monai[all]
    pip install monailabel
    ```

## Usage

> ⚠️**Still in progress**⚠️

- Make sure all dependencies are installed.
- Use the following command to run tests:

1. **Radiology** ([Radiology](https://docs.nvidia.com/launchpad/ai/monai-label/latest/monai-radiology-app.html))<br>
    1.1 Deploy MONAI Label Server<br>
    On the local machine follow the commands listed below to install MONAI Label, download a sample application (Radiology), download a sample dataset (MSD heart MRI), and deploy the sample app and standard dataset on the MONAI Label server.<br>
    Download Radiology sample app to local directory
    ```bash
    monailabel apps --name radiology --download --output .
    ```
    Download Task 2 MSD dataset
    ```bach
    monailabel datasets --download --name Task09_Spleen --output .
    ```
    Start the Radiology app in MONAI label server and start annotating the downloaded images using deepedit model
    ```bach
    monailabel start_server --app radiology --studies Task09_Spleen/imagesTr --conf models deepedit
    ```
    1.2 Annotating a Custom Dataset<br>
    To annotate a custom dataset using DeepEdit, we can download the DeepEdit app as above, however, the dataset directory need not be populated. Follow the commands below to setup custom dataset annotation using the empty local directory my_dataset as the image and label storage location.<br>
    Install MONAI Label
    ```bach
    pip install monailabel
    ```

    Download DeepEdit sample app to local directory
    ```bach
    monailabel apps --name radiology --download --output .
    ```

    Create an empty folder for the custom dataset
    ```bach
    mkdir my_dataset
    ```

    Start the DeepEdit app in MONAI label server on the empty dataset folder
    ```bach
    monailabel start_server --app radiology --studies my_dataset --conf models deepedit
    ```
   
2. **Monaibundle** ([Monaibundle](https://github.com/Project-MONAI/tutorials/blob/main/monailabel/monailabel_monaibundle_3dslicer_multiorgan_seg.ipynb))<br>
    
    2.1 Download monaibundle app<br>
    Get and copy the monaibundle app using monailabel API
    ```bash
    monailabel apps --name monaibundle --download --output .
    ```
    2.2 Download sample data<br>
    The multi-organ segmentation task takes CT images as input. The bundle model Swin UNETR pre-trained weights are trained with Beyond The Cranial Vault (BTCV). In this tutorial, some sample CT images from MSD are used (for the purpose of app demonstration on Slicer 3D). Download MSD Task09 dataset as the sample dataset using monailabel API.

    ```bach
    monailabel datasets --download --name Task09_Spleen --output .
    ```
    ```bach
    monailabel datasets --download --name Task09_Spleen --output datasets
    ```
    2.3 Starting MONAI Label Server
    Specify the bundle name in ```--conf models <BUNDLENAME>``` argument.
 
    **Deepedit:**
    ```bach
    monailabel start_server --app monaibundle --studies Task09_Spleen/imagesTr --conf models deepedit
    ```
    **Renal Structures UNEST Segmentationmodel:**
    ```bash
    monailabel start_server --app monaibundle --studies Task09_Spleen/imagesTr --conf models renalStructures_UNEST_segmentation
    ```
    **Spleen CT Segmentation:**
    ```bash
    monailabel start_server --app monaibundle --studies Task09_Spleen/imagesTr --conf models spleen_ct_segmentation
    ```
    **Supported Models:**
    
    | Bundle | Model | Objects | Modality | Note |
    |:----:|:-----:|:-------:|:--------:|:----:|
    | [spleen_ct_segmentation](https://github.com/Project-MONAI/model-zoo/tree/dev/models/spleen_ct_segmentation) | UNet | Spleen | CT | A model for (3D) segmentation of the spleen |
    | [swin_unetr_btcv_segmentation](https://github.com/Project-MONAI/model-zoo/tree/dev/models/swin_unetr_btcv_segmentation) | SwinUNETR | Multi-Organ | CT | A model for (3D) multi-organ segmentation |
    | [prostate_mri_anatomy](https://github.com/Project-MONAI/model-zoo/tree/dev/models/prostate_mri_anatomy) | UNet | Prostate | MRI | A model for (3D) prostate segmentation from MRI image |
    | [pancreas_ct_dints_segmentation](https://github.com/Project-MONAI/model-zoo/tree/dev/models/pancreas_ct_dints_segmentation) | DiNTS | Pancreas/Tumor | CT | An automl method for (3D) pancreas/tumor segmentation |
    | [renalStructures_UNEST_segmentation](https://github.com/Project-MONAI/model-zoo/tree/dev/models/renalStructures_UNEST_segmentation) | UNesT | Kidney Substructure | CT |  A pre-trained for inference (3D) kidney cortex/medulla/pelvis segmentation |
    | [wholeBrainSeg_UNEST_segmentation](https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBrainSeg_Large_UNEST_segmentation) | UNesT | Whole Brain | MRI T1 |  A pre-trained for inference (3D) 133 whole brain structures segmentation |
    | [spleen_deepedit_annotation](https://github.com/Project-MONAI/model-zoo/tree/dev/models/spleen_deepedit_annotation) | DeepEdit | Spleen| CT | An interactive method for 3D spleen Segmentation |
    | [lung_nodule_ct_detection](https://github.com/Project-MONAI/model-zoo/tree/dev/models/lung_nodule_ct_detection) | RetinaNet | Lung Nodule| CT | The detection model for 3D CT images |
    | [wholeBody_ct_segmentation](https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation) | SegResNet | 104 body structures| CT | The segmentation model for 104 tissue from 3D CT images (TotalSegmentator Dataset) |

   
    1.4 (Optional) File Structure for monaibundle app<br>
    To double check and confirm the correct monaibundle app and bundle files structure.

    The directory tree structure should be:
    ```
    └── monaibundle\n
        ├── __init__.py\n
        ├── lib\n
        │   ├── activelearning\n
        │   │   └── __init__.py\n
        │   ├── infers\n
        │   │   └── __init__.py\n
        │   ├── __init__.py\n
        │   └── trainers\n
        │       └── __init__.py\n
        ├── main.py\n
        ├── model\n
        │   └── swin_unetr_btcv_segmentation_v0.3.9\n
        │       ├── configs\n
        │       │   ├── evaluate.json\n
        │       │   ├── inference.json\n
        │       │   ├── logging.conf\n
        │       │   ├── metadata.json\n
        │       │   ├── multi_gpu_train.json\n
        │       │   └── train.json\n
        │       ├── docs\n
        │       │   ├── data_license.txt\n
        │       │   └── README.md\n
        │       ├── eval\n
        │       ├── LICENSE\n
        │       └── models\n
        │           └── model.pt\n
        ├── README.md\n
        └── requirements.txt\n
    ```
    
    1.5 (Optional) + Sandbox (Colorized + SSAO)<br>

    <img src="./img-readme/colorized and ssao demo.jpeg" width="1400">
    <img src="./img-readme/colorized and ssao demo3.jpeg" width="1400">

## Demo

From 2024

<div class="gallery">
    <img src="./img-readme/output.png" alt="Bild 1" width="200">
    <img src="./img-readme/output2.png" alt="Bild 2" width="200">
    <img src="./img-readme/output3.png" alt="Bild 3" width="200">
    <img src="./img-readme/output4.png" alt="Bild 4" width="200">
    <img src="./img-readme/output5.png" alt="Bild 5" width="200">
    <img src="./img-readme/output6.png" alt="Bild 6" width="200">
    <img src="./img-readme/output7.png" alt="Bild 7" width="200">
    <img src="./img-readme/output8.png" alt="Bild 8" width="200">
    <img src="./img-readme/output9.png" alt="Bild 9" width="200">
    <img src="./img-readme/output10.png" alt="Bild 10" width="200">
    <img src="./img-readme/output11.png" alt="Bild 11" width="200">
    <img src="./img-readme/output12.png" alt="Bild 12" width="200">
    <img src="./img-readme/output13.png" alt="Bild 13" width="200">
    <img src="./img-readme/output14.png" alt="Bild 14" width="200">
    <img src="./img-readme/output15.png" alt="Bild 15" width="200">
    <img src="./img-readme/output16.png" alt="Bild 16" width="200">
    <img src="./img-readme/output17.png" alt="Bild 17" width="200">
</div>

From 2025

<img src="./img-readme/demo4.png" width="1400">
  
## Checklist

Here is the to-do list for the most important tools and tasks in the project:

## Tasks

| **Task** | **Beschreibung**                                                                                                                                                                                                      | **Status** |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Task 1   | Zugriff auf die Datenbank: https://cdas.cancer.gov/nlst/                                                                                                                                                              | ❌         |
| Task 2   | Test Datenbaken: <br> Task09_Spleen(+1.5GB): ```monailabel datasets --download --name Task09_Spleen --output .``` <br> Task09_Spleen(+7GB): ```monailabel datasets --download --name Task01_BrainTumour --output .``` | 🔄         |
| Task 3   | Testen von ```pip install monai-deploy-app-sdk```                                                                                                                                                                     | ❌         |
| Task 4   | Testen von https://monai.io/model-zoo.html                                                                                                                                                                            | 🔄         |
| Task 5   | Problem mit MONAILabel Server, mit neuen Daten und Modellen.                                                                                                                                                          | 🔄         |

Not done ❌ | Done (min. 1 month) ✔️ | Improvements needed 🔧 | In progress 🔄 | Improvements needed ⚠️

> Note: Hey you, you can always add and check off comments or problems here.


## Transformer

### 1. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2018)
**Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova  <br>
**Link:** [arXiv:1810.04805v2](https://arxiv.org/abs/1810.04805v2)  <br>
**Abstract:** We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.
BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).

### 2. Evaluating Large Language Models Trained on Code (2021)
**Authors:** Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such, Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario Amodei, Sam McCandlish, Ilya Sutskever, Wojciech Zaremba<br>
**Link:** [arXiv:2107.03374](https://arxiv.org/abs/2107.03374)  <br>
**Abstract:** We introduce Codex, a GPT language model fine-tuned on publicly available code from GitHub, and study its Python code-writing capabilities. A distinct production version of Codex powers GitHub Copilot. On HumanEval, a new evaluation set we release to measure functional correctness for synthesizing programs from docstrings, our model solves 28.8% of the problems, while GPT-3 solves 0% and GPT-J solves 11.4%. Furthermore, we find that repeated sampling from the model is a surprisingly effective strategy for producing working solutions to difficult prompts. Using this method, we solve 70.2% of our problems with 100 samples per problem. Careful investigation of our model reveals its limitations, including difficulty with docstrings describing long chains of operations and with binding operations to variables. Finally, we discuss the potential broader impacts of deploying powerful code generation technologies, covering safety, security, and economics.

### 3. Training language models to follow instructions with human feedback (2022)
**Authors:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe<br>
**Link:** [arXiv:2203.02155](https://arxiv.org/abs/2203.02155)  <br>
**Abstract:** Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

### 4. Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books (2015)
**Authors:** Yukun Zhu, Ryan Kiros, Richard Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, Sanja Fidler<br>
**Link:** [arXiv:1506.06724](https://arxiv.org/abs/1506.06724)  <br>
**Abstract:** This work presents a Neural Architecture Search (NAS) method using reinforcement learning to automatically generate neural network architectures. NAS demonstrates the ability to discover novel architectures that outperform human-designed models on standard benchmarks.

### 5. Language Models are Few-Shot Learners (2020)
**Authors:** Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, Dario Amodei<br>
**Link:** [arXiv:2005.14165v4](https://arxiv.org/abs/2005.14165v4)  <br>
**Abstract:** Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches. Specifically, we train GPT-3, an autoregressive language model with 175 billion parameters, 10x more than any previous non-sparse language model, and test its performance in the few-shot setting. For all tasks, GPT-3 is applied without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction with the model. GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic. At the same time, we also identify some datasets where GPT-3's few-shot learning still struggles, as well as some datasets where GPT-3 faces methodological issues related to training on large web corpora. Finally, we find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans. We discuss broader societal impacts of this finding and of GPT-3 in general.

### 6. Visual ChatGPT: Talking, Drawing and Editing with Visual Foundation Models (2023)
**Authors:** Chenfei Wu, Shengming Yin, Weizhen Qi, Xiaodong Wang, Zecheng Tang, Nan Duan<br>
**Link:** [arXiv:2303.04671](https://arxiv.org/abs/2303.04671)  <br>
**Abstract:** ChatGPT is attracting a cross-field interest as it provides a language interface with remarkable conversational competency and reasoning capabilities across many domains. However, since ChatGPT is trained with languages, it is currently not capable of processing or generating images from the visual world. At the same time, Visual Foundation Models, such as Visual Transformers or Stable Diffusion, although showing great visual understanding and generation capabilities, they are only experts on specific tasks with one-round fixed inputs and outputs. To this end, We build a system called \textbf{Visual ChatGPT}, incorporating different Visual Foundation Models, to enable the user to interact with ChatGPT by 1) sending and receiving not only languages but also images 2) providing complex visual questions or visual editing instructions that require the collaboration of multiple AI models with multi-steps. 3) providing feedback and asking for corrected results. We design a series of prompts to inject the visual model information into ChatGPT, considering models of multiple inputs/outputs and models that require visual feedback. Experiments show that Visual ChatGPT opens the door to investigating the visual roles of ChatGPT with the help of Visual Foundation Models.

### 7. On the Opportunities and Risks of Foundation Models (2022)
**Authors:** Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S. Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, Erik Brynjolfsson, Shyamal Buch, Dallas Card, Rodrigo Castellon, Niladri Chatterji, Annie Chen, Kathleen Creel, Jared Quincy Davis, Dora Demszky, Chris Donahue, Moussa Doumbouya, Esin Durmus, Stefano Ermon, John Etchemendy, Kawin Ethayarajh, Li Fei-Fei, Chelsea Finn, Trevor Gale, Lauren Gillespie, Karan Goel, Noah Goodman, Shelby Grossman, Neel Guha, Tatsunori Hashimoto, Peter Henderson, John Hewitt, Daniel E. Ho, Jenny Hong, Kyle Hsu, Jing Huang, Thomas Icard, Saahil Jain, Dan Jurafsky, Pratyusha Kalluri, Siddharth Karamcheti, Geoff Keeling, Fereshte Khani, Omar Khattab, Pang Wei Koh, Mark Krass, Ranjay Krishna, Rohith Kuditipudi, Ananya Kumar, Faisal Ladhak, Mina Lee, Tony Lee, Jure Leskovec, Isabelle Levent, Xiang Lisa Li, Xuechen Li, Tengyu Ma, Ali Malik, Christopher D. Manning, Suvir Mirchandani, Eric Mitchell, Zanele Munyikwa, Suraj Nair, Avanika Narayan, Deepak Narayanan, Ben Newman, Allen Nie, Juan Carlos Niebles, Hamed Nilforoshan, Julian Nyarko, Giray Ogut, Laurel Orr, Isabel Papadimitriou, Joon Sung Park, Chris Piech, Eva Portelance, Christopher Potts, Aditi Raghunathan, Rob Reich, Hongyu Ren, Frieda Rong, Yusuf Roohani, Camilo Ruiz, Jack Ryan, Christopher Ré, Dorsa Sadigh, Shiori Sagawa, Keshav Santhanam, Andy Shih, Krishnan Srinivasan, Alex Tamkin, Rohan Taori, Armin W. Thomas, Florian Tramèr, Rose E. Wang, William Wang et al. (14 additional authors not shown)<br>
**Link:** [arXiv:2108.07258](https://arxiv.org/abs/2108.07258)  <br>
**Abstract:** AI is undergoing a paradigm shift with the rise of models (e.g., BERT, DALL-E, GPT-3) that are trained on broad data at scale and are adaptable to a wide range of downstream tasks. We call these models foundation models to underscore their critically central yet incomplete character. This report provides a thorough account of the opportunities and risks of foundation models, ranging from their capabilities (e.g., language, vision, robotics, reasoning, human interaction) and technical principles(e.g., model architectures, training procedures, data, systems, security, evaluation, theory) to their applications (e.g., law, healthcare, education) and societal impact (e.g., inequity, misuse, economic and environmental impact, legal and ethical considerations). Though foundation models are based on standard deep learning and transfer learning, their scale results in new emergent capabilities,and their effectiveness across so many tasks incentivizes homogenization. Homogenization provides powerful leverage but demands caution, as the defects of the foundation model are inherited by all the adapted models downstream. Despite the impending widespread deployment of foundation models, we currently lack a clear understanding of how they work, when they fail, and what they are even capable of due to their emergent properties. To tackle these questions, we believe much of the critical research on foundation models will require deep interdisciplinary collaboration commensurate with their fundamentally sociotechnical nature.

### 8. Training language models to follow instructions with human feedback (2022)
**Authors:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, John Schulman, Jacob Hilton, Fraser Kelton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike, Ryan Lowe<br>
**Link:** [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) <br> 
**Abstract:** Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In other words, these models are not aligned with their users. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback. Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT. In human evaluations on our prompt distribution, outputs from the 1.3B parameter InstructGPT model are preferred to outputs from the 175B GPT-3, despite having 100x fewer parameters. Moreover, InstructGPT models show improvements in truthfulness and reductions in toxic output generation while having minimal performance regressions on public NLP datasets. Even though InstructGPT still makes simple mistakes, our results show that fine-tuning with human feedback is a promising direction for aligning language models with human intent.

### 9. BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining (2022)
**Authors:** Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, Tie-Yan Liu<br>
**Link:** [arXiv:2210.10341](https://arxiv.org/abs/2210.10341)  <br>
**Abstract:** Pre-trained language models have attracted increasing attention in the biomedical domain, inspired by their great success in the general natural language domain. Among the two main branches of pre-trained language models in the general language domain, i.e., BERT (and its variants) and GPT (and its variants), the first one has been extensively studied in the biomedical domain, such as BioBERT and PubMedBERT. While they have achieved great success on a variety of discriminative downstream biomedical tasks, the lack of generation ability constrains their application scope. In this paper, we propose BioGPT, a domain-specific generative Transformer language model pre-trained on large scale biomedical literature. We evaluate BioGPT on six biomedical NLP tasks and demonstrate that our model outperforms previous models on most tasks. Especially, we get 44.98%, 38.42% and 40.76% F1 score on BC5CDR, KD-DTI and DDI end-to-end relation extraction tasks respectively, and 78.2% accuracy on PubMedQA, creating a new record. Our case study on text generation further demonstrates the advantage of BioGPT on biomedical literature to generate fluent descriptions for biomedical terms.

### 10. Release Strategies and the Social Impacts of Language Models (2019)
**Authors:** Irene Solaiman, Miles Brundage, Jack Clark, Amanda Askell, Ariel Herbert-Voss, Jeff Wu, Alec Radford, Gretchen Krueger, Jong Wook Kim, Sarah Kreps, Miles McCain, Alex Newhouse, Jason Blazakis, Kris McGuffie, Jasmine Wang<br>
**Link:** [arXiv:1908.09203](https://arxiv.org/abs/1908.09203)  <br>
**Abstract:** Large language models have a range of beneficial uses: they can assist in prose, poetry, and programming; analyze dataset biases; and more. However, their flexibility and generative capabilities also raise misuse concerns. This report discusses OpenAI's work related to the release of its GPT-2 language model. It discusses staged release, which allows time between model releases to conduct risk and benefit analyses as model sizes increased. It also discusses ongoing partnership-based research and provides recommendations for better coordination and responsible publication in AI.

### 11. WebGPT: Browser-assisted question-answering with human feedback (2022)
**Authors:**Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou, Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, John Schulman<br>
**Link:** [arXiv:2112.09332](https://arxiv.org/abs/2112.09332)  <br>
**Abstract:** We fine-tune GPT-3 to answer long-form questions using a text-based web-browsing environment, which allows the model to search and navigate the web. By setting up the task so that it can be performed by humans, we are able to train models on the task using imitation learning, and then optimize answer quality with human feedback. To make human evaluation of factual accuracy easier, models must collect references while browsing in support of their answers. We train and evaluate our models on ELI5, a dataset of questions asked by Reddit users. Our best model is obtained by fine-tuning GPT-3 using behavior cloning, and then performing rejection sampling against a reward model trained to predict human preferences. This model's answers are preferred by humans 56% of the time to those of our human demonstrators, and 69% of the time to the highest-voted answer from Reddit.

### 12. GPT-4 Technical Report (2023)
**Authors:** OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, Red Avila, Igor Babuschkin, Suchir Balaji, Valerie Balcom, Paul Baltescu, Haiming Bao, Mohammad Bavarian, Jeff Belgum, Irwan Bello, Jake Berdine, Gabriel Bernadett-Shapiro, Christopher Berner, Lenny Bogdonoff, Oleg Boiko, Madelaine Boyd, Anna-Luisa Brakman, Greg Brockman, Tim Brooks, Miles Brundage, Kevin Button, Trevor Cai, Rosie Campbell, Andrew Cann, Brittany Carey, Chelsea Carlson, Rory Carmichael, Brooke Chan, Che Chang, Fotis Chantzis, Derek Chen, Sully Chen, Ruby Chen, Jason Chen, Mark Chen, Ben Chess, Chester Cho, Casey Chu, Hyung Won Chung, Dave Cummings, Jeremiah Currier, Yunxing Dai, Cory Decareaux, Thomas Degry, Noah Deutsch, Damien Deville, Arka Dhar, David Dohan, Steve Dowling, Sheila Dunning, Adrien Ecoffet, Atty Eleti, Tyna Eloundou, David Farhi, Liam Fedus, Niko Felix, Simón Posada Fishman, Juston Forte, Isabella Fulford, Leo Gao, Elie Georges, Christian Gibson, Vik Goel, Tarun Gogineni, Gabriel Goh, Rapha Gontijo-Lopes, Jonathan Gordon, Morgan Grafstein, Scott Gray, Ryan Greene, Joshua Gross, Shixiang Shane Gu, Yufei Guo, Chris Hallacy, Jesse Han, Jeff Harris, Yuchen He, Mike Heaton, Johannes Heidecke, Chris Hesse, Alan Hickey, Wade Hickey, Peter Hoeschele, Brandon Houghton, Kenny Hsu, Shengli Hu, Xin Hu, Joost Huizinga, Shantanu Jain, Shawn Jain , Joanne Jang, Angela Jiang, Roger Jiang, Haozhun Jin, Denny Jin, Shino Jomoto, Billie Jonn, Heewoo Jun, Tomer Kaftan, Łukasz Kaiser, Ali Kamali, Ingmar Kanitscheider, Nitish Shirish Keskar, Tabarak Khan, Logan Kilpatrick, Jong Wook Kim, Christina Kim, Yongjik Kim, Jan Hendrik Kirchner, Jamie Kiros, Matt Knight, Daniel Kokotajlo, Łukasz Kondraciuk, Andrew Kondrich, Aris Konstantinidis, Kyle Kosic, Gretchen Krueger, Vishal Kuo, Michael Lampe, Ikai Lan, Teddy Lee, Jan Leike, Jade Leung, Daniel Levy, Chak Ming Li, Rachel Lim, Molly Lin, Stephanie Lin, Mateusz Litwin, Theresa Lopez, Ryan Lowe, Patricia Lue, Anna Makanju, Kim Malfacini, Sam Manning, Todor Markov, Yaniv Markovski, Bianca Martin, Katie Mayer, Andrew Mayne, Bob McGrew, Scott Mayer McKinney, Christine McLeavey, Paul McMillan, Jake McNeil, David Medina, Aalok Mehta, Jacob Menick, Luke Metz, Andrey Mishchenko, Pamela Mishkin, Vinnie Monaco, Evan Morikawa, Daniel Mossing, Tong Mu, Mira Murati, Oleg Murk, David Mély, Ashvin Nair, Reiichiro Nakano, Rajeev Nayak, Arvind Neelakantan, Richard Ngo, Hyeonwoo Noh, Long Ouyang, Cullen O'Keefe, Jakub Pachocki, Alex Paino, Joe Palermo, Ashley Pantuliano, Giambattista Parascandolo, Joel Parish, Emy Parparita, Alex Passos, Mikhail Pavlov, Andrew Peng, Adam Perelman, Filipe de Avila Belbute Peres, Michael Petrov, Henrique Ponde de Oliveira Pinto, Michael (Rai)Pokorny, Michelle Pokrass, Vitchyr H. Pong, Tolly Powell, Alethea Power, Boris Power, Elizabeth Proehl, Raul Puri, Alec Radford, Jack Rae, Aditya Ramesh, Cameron Raymond, Francis Real, Kendra Rimbach, Carl Ross, Bob Rotsted, Henri Roussez, Nick Ryder, Mario Saltarelli, Ted Sanders, Shibani Santurkar, Girish Sastry, Heather Schmidt, David Schnurr, John Schulman, Daniel Selsam, Kyla Sheppard, Toki Sherbakov, Jessica Shieh, Sarah Shoker, Pranav Shyam, Szymon Sidor, Eric Sigler, Maddie Simens, Jordan Sitkin, Katarina Slama, Ian Sohl, Benjamin Sokolowsky, Yang Song, Natalie Staudacher, Felipe Petroski Such, Natalie Summers, Ilya Sutskever, Jie Tang, Nikolas Tezak, Madeleine B. Thompson, Phil Tillet, Amin Tootoonchian, Elizabeth Tseng, Preston Tuggle, Nick Turley, Jerry Tworek, Juan Felipe Cerón Uribe, Andrea Vallone, Arun Vijayvergiya, Chelsea Voss, Carroll Wainwright, Justin Jay Wang, Alvin Wang, Ben Wang, Jonathan Ward, Jason Wei, CJ Weinmann, Akila Welihinda, Peter Welinder, Jiayi Weng, Lilian Weng, Matt Wiethoff, Dave Willner, Clemens Winter, Samuel Wolrich, Hannah Wong, Lauren Workman, Sherwin Wu, Jeff Wu, Michael Wu, Kai Xiao, Tao Xu, Sarah Yoo, Kevin Yu, Qiming Yuan, Wojciech Zaremba, Rowan Zellers, Chong Zhang, Marvin Zhang, Shengjia Zhao, Tianhao Zheng, Juntang Zhuang, William Zhuk, Barret Zoph<br>
**Link:** [arXiv:2303.08774](https://arxiv.org/abs/2303.08774)  <br>
**Abstract:** We report the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers. GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior. A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed us to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4.

### 13. Sparks of Artificial General Intelligence: Early experiments with GPT-4 (2023)
**Authors:** Sébastien Bubeck, Varun Chandrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg, Harsha Nori, Hamid Palangi, Marco Tulio Ribeiro, Yi Zhang
**Link:** [arXiv:2303.12712](https://arxiv.org/abs/2303.12712)  <br>
**Abstract:** Artificial intelligence (AI) researchers have been developing and refining large language models (LLMs) that exhibit remarkable capabilities across a variety of domains and tasks, challenging our understanding of learning and cognition. The latest model developed by OpenAI, GPT-4, was trained using an unprecedented scale of compute and data. In this paper, we report on our investigation of an early version of GPT-4, when it was still in active development by OpenAI. We contend that (this early version of) GPT-4 is part of a new cohort of LLMs (along with ChatGPT and Google's PaLM for example) that exhibit more general intelligence than previous AI models. We discuss the rising capabilities and implications of these models. We demonstrate that, beyond its mastery of language, GPT-4 can solve novel and difficult tasks that span mathematics, coding, vision, medicine, law, psychology and more, without needing any special prompting. Moreover, in all of these tasks, GPT-4's performance is strikingly close to human-level performance, and often vastly surpasses prior models such as ChatGPT. Given the breadth and depth of GPT-4's capabilities, we believe that it could reasonably be viewed as an early (yet still incomplete) version of an artificial general intelligence (AGI) system. In our exploration of GPT-4, we put special emphasis on discovering its limitations, and we discuss the challenges ahead for advancing towards deeper and more comprehensive versions of AGI, including the possible need for pursuing a new paradigm that moves beyond next-word prediction. We conclude with reflections on societal influences of the recent technological leap and future research directions.<br>

### 14. Swin UNETR: Swin Transformers for Semantic Segmentation of Brain Tumors in MRI Images
**Authors:** Ali Hatamizadeh, Vishwesh Nath, Yucheng Tang, Dong Yang, Holger Roth, Daguang Xu.<br>
**Link:** [arXiv:2201.01266](https://arxiv.org/abs/2201.01266)  <br>
**Abstract:** Semantic segmentation of brain tumors is a fundamental medical image analysis task involving multiple MRI imaging modalities that can assist clinicians in diagnosing the patient and successively studying the progression of the malignant entity. In recent years, Fully Convolutional Neural Networks (FCNNs) approaches have become the de facto standard for 3D medical image segmentation. The popular "U-shaped" network architecture has achieved state-of-the-art performance benchmarks on different 2D and 3D semantic segmentation tasks and across various imaging modalities. However, due to the limited kernel size of convolution layers in FCNNs, their performance of modeling long-range information is sub-optimal, and this can lead to deficiencies in the segmentation of tumors with variable sizes. On the other hand, transformer models have demonstrated excellent capabilities in capturing such long-range information in multiple domains, including natural language processing and computer vision. Inspired by the success of vision transformers and their variants, we propose a novel segmentation model termed Swin UNEt TRansformers (Swin UNETR). Specifically, the task of 3D brain tumor semantic segmentation is reformulated as a sequence to sequence prediction problem wherein multi-modal input data is projected into a 1D sequence of embedding and used as an input to a hierarchical Swin transformer as the encoder. The swin transformer encoder extracts features at five different resolutions by utilizing shifted windows for computing self-attention and is connected to an FCNN-based decoder at each resolution via skip connections. We have participated in BraTS 2021 segmentation challenge, and our proposed model ranks among the top-performing approaches in the validation phase.

### 15. Swin UNETR++: Advancing Transformer-Based Dense Dose Prediction Towards Fully Automated Radiation Oncology Treatments
**Authors:** Kuancheng Wang, Hai Siong Tan, Rafe Mcbeth.<br>
**Link:** [arXiv:2311.06572](https://arxiv.org/abs/2311.06572)  <br>
**Abstract:** The field of Radiation Oncology is uniquely positioned to benefit from the use of artificial intelligence to fully automate the creation of radiation treatment plans for cancer therapy. This time-consuming and specialized task combines patient imaging with organ and tumor segmentation to generate a 3D radiation dose distribution to meet clinical treatment goals, similar to voxel-level dense prediction. In this work, we propose Swin UNETR++, that contains a lightweight 3D Dual Cross-Attention (DCA) module to capture the intra and inter-volume relationships of each patient's unique anatomy, which fully convolutional neural networks lack. Our model was trained, validated, and tested on the Open Knowledge-Based Planning dataset. In addition to metrics of Dose Score SDose and DVH Score SDVH that quantitatively measure the difference between the predicted and ground-truth 3D radiation dose distribution, we propose the qualitative metrics of average volume-wise acceptance rate RVA and average patient-wise clinical acceptance rate RPA to assess the clinical reliability of the predictions. Swin UNETR++ demonstrates near-state-of-the-art performance on validation and test dataset (validation: SDVH=1.492 Gy, SDose=2.649 Gy, RVA=88.58%, RPA=100.0%; test: SDVH=1.634 Gy, SDose=2.757 Gy, RVA=90.50%, RPA=98.0%), establishing a basis for future studies to translate 3D dose predictions into a deliverable treatment plan, facilitating full automation.

### 16. UNETR: Transformers for 3D Medical Image Segmentation
**Authors:** Ali Hatamizadeh, Yucheng Tang, Vishwesh Nath, Dong Yang, Andriy Myronenko, Bennett Landman, Holger Roth, Daguang Xu.<br>
**Link:** [arXiv:2103.10504](https://arxiv.org/abs/2103.10504)  <br>
**Abstract:** Fully Convolutional Neural Networks (FCNNs) with contracting and expanding paths have shown prominence for the majority of medical image segmentation applications since the past decade. In FCNNs, the encoder plays an integral role by learning both global and local features and contextual representations which can be utilized for semantic output prediction by the decoder. Despite their success, the locality of convolutional layers in FCNNs, limits the capability of learning long-range spatial dependencies. Inspired by the recent success of transformers for Natural Language Processing (NLP) in long-range sequence learning, we reformulate the task of volumetric (3D) medical image segmentation as a sequence-to-sequence prediction problem. We introduce a novel architecture, dubbed as UNEt TRansformers (UNETR), that utilizes a transformer as the encoder to learn sequence representations of the input volume and effectively capture the global multi-scale information, while also following the successful "U-shaped" network design for the encoder and decoder. The transformer encoder is directly connected to a decoder via skip connections at different resolutions to compute the final semantic segmentation output. We have validated the performance of our method on the Multi Atlas Labeling Beyond The Cranial Vault (BTCV) dataset for multi-organ segmentation and the Medical Segmentation Decathlon (MSD) dataset for brain tumor and spleen segmentation tasks. Our benchmarks demonstrate new state-of-the-art performance on the BTCV leaderboard.

### 17. UNETR++: Delving into Efficient and Accurate 3D Medical Image Segmentation
**Authors:** Abdelrahman Shaker, Muhammad Maaz, Hanoona Rasheed, Salman Khan, Ming-Hsuan Yang, Fahad Shahbaz Khan.<br>
**Link:** [arXiv:2212.04497](https://arxiv.org/abs/2212.04497)  <br>
**Abstract:** Owing to the success of transformer models, recent works study their applicability in 3D medical segmentation tasks. Within the transformer models, the self-attention mechanism is one of the main building blocks that strives to capture long-range dependencies. However, the self-attention operation has quadratic complexity which proves to be a computational bottleneck, especially in volumetric medical imaging, where the inputs are 3D with numerous slices. In this paper, we propose a 3D medical image segmentation approach, named UNETR++, that offers both high-quality segmentation masks as well as efficiency in terms of parameters, compute cost, and inference speed. The core of our design is the introduction of a novel efficient paired attention (EPA) block that efficiently learns spatial and channel-wise discriminative features using a pair of inter-dependent branches based on spatial and channel attention. Our spatial attention formulation is efficient having linear complexity with respect to the input sequence length. To enable communication between spatial and channel-focused branches, we share the weights of query and key mapping functions that provide a complimentary benefit (paired attention), while also reducing the overall network parameters. Our extensive evaluations on five benchmarks, Synapse, BTCV, ACDC, BRaTs, and Decathlon-Lung, reveal the effectiveness of our contributions in terms of both efficiency and accuracy. On Synapse, our UNETR++ sets a new state-of-the-art with a Dice Score of 87.2%, while being significantly efficient with a reduction of over 71% in terms of both parameters and FLOPs, compared to the best method in the literature.

## Medical information

### Medical imaging procedures

In modern medicine, various imaging procedures are used to provide detailed insights into the human body. These procedures use different technologies and are used depending on the need and the purpose of the examination. The most common imaging procedures are described below.

#### 1. X-ray (classic X-ray)
- **Technology**: X-rays (ionizing radiation)
- **Application**: Often used to show bone fractures, in mammography, for dental examinations or to examine the thorax.
- **Examples**:
- **Digital X-ray**: Modern form of X-ray in which the images are digitally captured and processed.
- **Mammography**: Special X-ray examination for the early detection of breast cancer.

#### 2. CT (computer tomography)
- **Technology**: Use of X-rays to create cross-sectional images of the body.
- **Application**: Provides more detailed images than classic X-rays. Often used to diagnose tumors, bleeding, fractures and internal injuries.
- **Example**: The patient is pushed on a table into a ring-shaped scanner that creates detailed 3D images of the body.

#### 3. MRI (magnetic resonance imaging)
- **Technology**: Use of magnetic fields and radio waves instead of X-rays.
- **Application**: Particularly suitable for examining soft tissues, such as the brain, muscles, tendons and internal organs.

#### 4. PET (positron emission tomography)
- **Technology**: Use of radioactive substances that are injected into the body to make metabolic processes visible.
- **Application**: Often used in combination with CT or MRI to detect tumors or analyze metabolism, for example in cancer diagnosis.

#### 5. DEXA (Dual-Energy X-ray Absorptiometry)
- **Technology**: Special type of X-ray that uses two different energies to measure bone density.
- **Application**: Commonly used to diagnose osteoporosis and measure bone density.

#### 6. Fluoroscopy
- **Technology**: Continuous X-rays allow real-time imaging of movements in the body.
- **Application**: Used for dynamic examinations, such as in angiography or in examinations of the gastrointestinal tract.

#### 7. Fluoroscopy (interventional radiology)
- **Technology**: Use of X-rays to perform minimally invasive procedures under visual control.
- **Application**: Commonly used in procedures such as stent placement or biopsies under X-ray control.

### Overview of Cancers

Cancer is a complex group of diseases characterized by uncontrolled cell growth. The type of cancer depends on the organ or tissue affected. This overview describes the most common types of cancer, their characteristics, risk factors, and symptoms.

#### 1. Lung Cancer
- **Description**: Lung cancer begins in the lungs and is divided into two main types:
- **Small cell lung cancer (SCLC)**: An aggressive cancer that grows quickly and spreads early.
- **Non-small cell lung cancer (NSCLC)**: More common, grows more slowly than SCLC.
- **Risk factors**: Smoking, secondhand smoke, radon exposure, environmental toxins.
- **Symptoms**: Cough, chest pain, shortness of breath, weight loss.

#### 2. Breast cancer (mammary carcinoma)
- **Description**: Usually starts in the milk ducts or glands of the breast. There are different subtypes:
- Hormone receptor positive
- HER2 positive
- Triple negative breast cancer
- **Risk factors**: Genetic predisposition (BRCA1/BRCA2 mutations), hormonal influences, age.
- **Symptoms**: Lumps in the breast, skin changes, discharge from the nipple.

#### 3. Prostate cancer
- **Description**: Affects the prostate, a gland of the male reproductive system. The cancer usually grows slowly but can be aggressive.
- **Risk factors**: Age, genetic predisposition, diet.
- **Symptoms**: Problems urinating, blood in the urine, pain in the pelvic area.

#### 4. Colon cancer (colorectal carcinoma)
- **Description**: Starts in the colon or rectum and often develops from polyps.
- **Risk factors**: Family history, chronic inflammation, unhealthy diet.
- **Symptoms**: Blood in the stool, changes in bowel habits, abdominal pain.

#### 5. Leukemia
- **Description**: Cancer of the blood-forming tissues such as the bone marrow and lymphatic system that causes excessive production of abnormal white blood cells.
- **Types**:
- Acute lymphocytic leukemia (ALL)
- Acute myeloid leukemia (AML)
- Chronic lymphocytic leukemia (CLL)
- Chronic myeloid leukemia (CML)
- **Symptoms**: Fever, fatigue, infections, bleeding.

#### 6. Skin cancer (melanoma and other skin tumors)
- **Description**: Different types of skin cancer:
- **Basal cell carcinoma**: Most common, least aggressive skin cancer.
- **Squamous cell carcinoma**: Can develop from precancerous skin changes.
- **Melanoma**: Most aggressive skin cancer, originates from the melanocytes.
- **Risk factors**: Excessive UV exposure, genetic predisposition.
- **Symptoms**: New or changed skin lesions.

#### 7. Pancreatic cancer (pancreatic carcinoma)
- **Description**: Begins in the cells of the pancreas and is often diagnosed late.
- **Risk factors**: Smoking, diabetes, family history.
- **Symptoms**: Abdominal pain, jaundice, weight loss.

#### 8. Kidney cancer (renal cell carcinoma)
- **Description**: Mostly as renal cell carcinoma, less often as urothelial carcinoma of the kidney.
- **Risk factors**: Smoking, obesity, high blood pressure.
- **Symptoms**: Blood in the urine, back pain, weight loss.

#### 9. Cervical cancer (cervical carcinoma)
- **Description**: Develops in the cervix, usually caused by human papilloma viruses (HPV).
- **Risk factors**: HPV infection, smoking, weakened immune system.
- **Symptoms**: Irregular bleeding, pelvic pain, pain during intercourse.

#### 10. Brain tumor
- **Description**: Benign or malignant tumors in the brain or spinal cord, such as glioblastomas or astrocytomas.
- **Risk factors**: Genetic predisposition, radiation exposure.
- **Symptoms**: Headaches, neurological deficits, seizures.

#### 11. Liver cancer (hepatocellular carcinoma)
- **Description**: Starts in the liver cells, often due to chronic liver disease such as hepatitis or cirrhosis.
- **Risk factors**: Alcohol consumption, liver disease, obesity.
- **Symptoms**: Upper abdominal pain, jaundice, weight loss.

#### 12. Esophageal cancer (esophageal carcinoma)
- **Description**: Starts in the esophagus, usually as squamous cell carcinoma or adenocarcinoma.
- **Risk factors**: Smoking, alcohol consumption, chronic heartburn.
- **Symptoms**: Difficulty swallowing, chest pain, weight loss.

#### 13. Thyroid cancer
- **Description**: Starts in the thyroid gland. Types include papillary, follicular, medullary and anaplastic thyroid cancer.
- **Risk factors**: Genetic predisposition, radiation exposure.
- **Symptoms**: Lumps in the throat, difficulty swallowing, voice changes.

#### 14. Bladder cancer
- **Description**: Usually develops in the cells that line the bladder (urothelial carcinoma).
- **Risk factors**: Smoking, chemicals, chronic bladder infections.
- **Symptoms**: Blood in the urine, frequent or painful urination.

#### 15. Stomach cancer (gastric carcinoma)
- **Description**: Begins in the stomach lining and is often caused by Helicobacter pylori infections or a high-salt diet.
- **Risk factors**: Smoking, family history, unhealthy diet.
- **Symptoms**: Abdominal pain, nausea, loss of appetite, weight loss.

## License

This project is licensed under the MIT license – see the [LICENSE](LICENSE) file for details.