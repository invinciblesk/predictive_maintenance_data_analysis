import pandas as pd
import argparse
import os
from visualization import (
    plot_failure_type_distribution, plot_correlation_matrix, plot_histograms,
    plot_scatterplots, plot_pairplot, plot_boxplots, plot_tool_wear_vs_rotational_speed
)

def main(data_path, output_dir):
    # Load data
    df_raw = pd.read_csv(data_path)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Plot functions
    plot_failure_type_distribution(df_raw, output_dir)
    plot_correlation_matrix(df_raw, output_dir)
    plot_histograms(df_raw, output_dir)
    plot_scatterplots(df_raw, output_dir)
    plot_pairplot(df_raw, output_dir)
    plot_boxplots(df_raw, output_dir)
    plot_tool_wear_vs_rotational_speed(df_raw, output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate and save plots for predictive maintenance data.')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the CSV data file.')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save plot outputs.')
    
    args = parser.parse_args()
    
    main(args.data_path, args.output_dir)
