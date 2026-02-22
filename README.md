# TD-MPC Planning Horizon Sensitivity Study

This repository contains a reproduction and architectural sensitivity analysis of the paper **"Temporal Difference Learning for Model Predictive Control" (Hansen et al., 2022)**. This project was completed as part of the CSC415: Introduction to Reinforcement Learning course.

## Project Overview
The core of this project investigates the trade-off between model-based planning and model-free value estimation. We specifically analyze the impact of the planning horizon ($H$) on the agent's ability to solve the `cartpole-swingup` task in the DeepMind Control Suite.

## Lab Machine Setup (From Scratch)

These instructions are optimized for university lab machines (Ubuntu/Debian) where `sudo` and `conda` are unavailable.


Running the following lines is recommented:

```Bash
# Downgrade build tools for compatibility
pip3 install --user "pip<24.1" setuptools==65.5.0 wheel==0.38.4

# Install PyTorch with CUDA support (for GPU acceleration)
pip3 install --user torch torchvision torchaudio

# Install RL environment and logging dependencies
pip3 install --user gym==0.21.0 hydra-core termcolor dm_control pandas matplotlib

export MUJOCO_GL="egl"

# cd into the root directory
cd tdmpc

# run the experiment
python3 run_experiments.py

# generate the graphs (after running experiment)
python3 plot_results.py
```
