# cv_automation

Automation project that mixes **UI/functional testing** with **computer-vision workflows**. The repo includes Robot Framework reports, camera/robot modules, Jupyter notebooks, and a Jenkins pipeline.

## Functions
- **UI & functional tests** with HTML/XML reports (`report.html`, `log.html`, `output.xml`).
- **Computer-vision components** (`Camera Driver/`, `models/`, `metrics/`).
- **Notebooks for experiments and training of models** (`jupyter_files/`).

## Repository layout
- cv_automation/
- ├─ Camera Driver/ # Camera capture/driver utilities
- ├─ Robot/ # Image-recognition (static colors)
- ├─ Robot_duo_model/ # Image-recognition (experimental try for dual model)
- ├─ Robot_vid/ # Video-recognition
- ├─ jupyter_files/ # Notebooks for CV/ML experiments
- ├─ metrics/ # Metrics or evaluation artifacts
- ├─ models/ # Model weights/configs (if any)
- ├─ Jenkinsfile # Run within Jenkins for workflow
- ├─ requirements.txt # Python dependencies
- ├─ report.html, log.html, output.xml, interactive_console_output.xml # Test reports
- └─ README.md, LICENSE


## Quick start

### 1) Setup
``bash
python -m venv .venv

pip install --upgrade pip
pip install -r requirements.txt

### 2) Run test suites
Robot/ : for image recognition related to static

Robot_duo_model/ : for video recognition related to Spectrum, Wave, Starlight and Faulty

## Overview

### 3) Working with notebooks
All experimental codes within jupyter_files/

### 4) Storing models and metrics
Configuration
Train and store under models/.
Store evaluation outputs under metrics/.
Add environment-specific settings (e.g., camera index, resolution) as variables in test suites.

## Useful codes
For most up-to-date image recognition model, refer to multiclass_img2_single_model.ipynb under image_recognition in jupyter_files.
Data preprocessing steps and model architecture and training are within this folder.

For most up-to-date video recognition model, refer to 10s_pattern_wdark_faulty.ipynb under video_recognition in jupyter_files.
Data preprocessing steps and model architecture and training are within this folder. The different type of model architectures differ in some layers.
Adjust the values accordingly after each training to see which trained model obtains the best result.
