import subprocess
import time

def run_experiment(task, horizon, seed, run_name, extra_args=None):
    if extra_args is None:
        extra_args = []
        
    print(f"--- Starting {run_name} (Horizon: {horizon}) ---")
    start_time = time.time()
    
    command = [
        "python3", "src/train.py",
        f"task={task}",
        f"horizon={horizon}",
        f"seed={seed}",
        f"exp_name={run_name}"
    ] + extra_args
    
    subprocess.run(command)
    
    elapsed = (time.time() - start_time) / 60
    print(f"--- Finished {run_name} in {elapsed:.2f} minutes ---\n")

if __name__ == "__main__":
    task_name = "cartpole-swingup" 
    # 1. Planning Horizon Ablation
    run_experiment(task=task_name, horizon=1, seed=42, run_name="ablation_horizon_1")

    run_experiment(task=task_name, horizon=3, seed=42, run_name="ablation_horizon_3")

    run_experiment(task=task_name, horizon=5, seed=42, run_name="ablation_horizon_5")

    run_experiment(task=task_name, horizon=7, seed=42, run_name="ablation_horizon_7")


