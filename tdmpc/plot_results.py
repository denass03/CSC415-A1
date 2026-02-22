import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

def find_log_file(exp_name):
    # TD-MPC logs directory structure
    search_pattern = f"logs/cartpole-swingup/**/{exp_name}/**/eval.log"
    matches = glob.glob(search_pattern, recursive=True)
    if not matches:
        print(f"Could not find eval.log for {exp_name}")
        return None
    return matches[0]

def plot_data(ax, exp_name, label, color, linestyle='-'):
    log_file = find_log_file(exp_name)
    if log_file:
        df = pd.read_csv(log_file)
        step_col = 'step' if 'step' in df.columns else df.columns[0]
        reward_col = 'episode_reward' if 'episode_reward' in df.columns else df.columns[-1]
        ax.plot(df[step_col], df[reward_col], label=label, linewidth=2.5, color=color, linestyle=linestyle)

def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Left: Baseline
    ax1.set_title("Reproduction: Baseline (H=5)", fontsize=15, fontweight='bold')
    plot_data(ax1, "baseline_reproduction", "Baseline (H=5)", "blue", "-")
    # The Original Paper's reported score as a reference line
    ax1.axhline(y=875, color='gray', linestyle='--', linewidth=2, label='Original Paper (Reported Max)')
    ax1.set_xlabel("Environment Steps", fontsize=13)
    ax1.set_ylabel("Evaluation Reward", fontsize=13)
    ax1.grid(True, linestyle=':', alpha=0.7)
    ax1.legend(fontsize=12, loc='lower right')
    
    # Right: Ablation
    ax2.set_title("Ablation Study: Planning Horizon", fontsize=15, fontweight='bold')
    plot_data(ax2, "ablation_horizon_1", "H=1", "red", "--")
    plot_data(ax2, "ablation_horizon_3", "H=3", "orange", "-.")
    plot_data(ax2, "baseline_reproduction", "H=5 (Baseline)", "blue", "-")
    plot_data(ax2, "ablation_horizon_7", "H=7", "purple", ":")
    ax2.set_xlabel("Environment Steps", fontsize=13)
    ax2.grid(True, linestyle=':', alpha=0.7)
    ax2.legend(fontsize=12, loc='lower right')
    
    plt.tight_layout()
    plt.savefig("reproduction_plot.png", dpi=300, bbox_inches='tight')
    print("Successfully generated reproduction_plot.png!")

if __name__ == "__main__":
    main()