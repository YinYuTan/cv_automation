# cv_automation

Automation project that mixes **UI/functional testing** with **computer-vision workflows**. The repo includes Robot Framework reports, camera/robot modules, Jupyter notebooks, and a Jenkins pipeline.

## Highlights
- **UI & functional tests** with HTML/XML reports (`report.html`, `log.html`, `output.xml`).
- **Computer-vision components** (`Camera Driver/`, `models/`, `metrics/`).
- **Notebooks for experiments** (`jupyter_files/`).
- **CI-ready** via `Jenkinsfile`.
- Licensed under **MIT**.

## Repository layout
cv_automation/
├─ Camera Driver/ # Camera capture/driver utilities
├─ Robot/ # Image-recognition (static colors)
├─ Robot_duo_model/ # Image-recognition (try for dual model)
├─ Robot_vid/ # Video-recognition
├─ jupyter_files/ # Notebooks for CV/ML experiments
├─ metrics/ # Metrics or evaluation artifacts
├─ models/ # Model weights/configs (if any)
├─ Jenkinsfile # CI pipeline
├─ requirements.txt # Python dependencies
├─ report.html, log.html, output.xml, interactive_console_output.xml # Test reports
└─ README.md, LICENSE


## Quick start

### 1) Setup
``bash
python -m venv .venv

pip install --upgrade pip
pip install -r requirements.txt

### 2) Run the test suite
# Run all tests (example)
robot Robot/
# Or target a specific suite
robot Robot_duo_model/

## Overview

### 3) Work with notebooks
jupyter notebook jupyter_files/

### 4) Storing models and metrics
Configuration
Train and store under models/.
Store evaluation outputs under metrics/.
Add environment-specific settings (e.g., camera index, resolution) as variables in test suites.

## Useful codes

