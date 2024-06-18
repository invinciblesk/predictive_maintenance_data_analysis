import matplotlib.pyplot as plt
import seaborn as sns
import math

sns.set(style="whitegrid")

def plot_failure_type_distribution(df, output_dir):
    plt.figure(figsize=(14, 8))
    sns.countplot(x='Failure Type', data=df, hue='Failure Type')
    plt.title('Distribution of Failure Type in the dataset')
    plt.savefig(f'{output_dir}/failure_type_distribution.png')
    plt.close()

def plot_correlation_matrix(df, output_dir):
    corr = df[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']].corr(method='pearson')
    plt.figure(figsize=(20, 16))
    sns.heatmap(corr, annot=True, cmap='viridis')
    plt.title('Correlation matrix')
    plt.savefig(f'{output_dir}/correlation_matrix.png')
    plt.close()

def plot_histograms(df, output_dir):
    cols = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Failure Type']
    plt.figure(figsize=(14, 8))
    for i, column in enumerate(cols, 1):
        plt.subplot(3, 2, i)
        sns.histplot(df[column], kde=True)
        plt.title(column)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        if column == 'Failure Type':
            plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/histograms.png')
    plt.close()

def plot_scatterplots(df, output_dir):
    fig = plt.figure(figsize=(21, 14))
    ax1 = fig.add_subplot(2, 2, 1)
    sns.scatterplot(x='Air temperature [K]', y='Process temperature [K]', data=df, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax1)
    ax1.set_title('Scatterplot of Air temperature [K] vs Process temperature [K]')
    
    ax2 = fig.add_subplot(2, 2, 2)
    sns.scatterplot(x='Rotational speed [rpm]', y='Torque [Nm]', data=df, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax2)
    ax2.set_title('Scatterplot of Rotational speed [rpm] vs Torque [Nm]')
    
    ax3 = fig.add_subplot(2, 2, 3)
    sns.scatterplot(x='Tool wear [min]', y='Torque [Nm]', data=df, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax3)
    ax3.set_title('Scatterplot of Tool wear [min] vs Torque [Nm]')
    
    ax4 = fig.add_subplot(2, 2, 4)
    sns.scatterplot(x='Tool wear [min]', y='Rotational speed [rpm]', data=df, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax4)
    ax4.set_title('Scatterplot of Tool wear [min] vs Rotational speed [rpm]')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/scatterplots.png')
    plt.close()

def plot_pairplot(df, output_dir):
    g = sns.pairplot(df[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Failure Type']], hue='Failure Type', palette='colorblind')
    g.fig.suptitle('Pairplot of Failure Types vs Failure Vector', y=1.02)
    g.savefig(f'{output_dir}/pairplot.png')
    plt.close()

def plot_boxplots(df, output_dir):
    features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    n = len(features)
    ncols = 2
    nrows = math.ceil(n / ncols)
    fig, axs = plt.subplots(nrows, ncols, figsize=(14, 8*nrows))
    for i, feature in enumerate(features):
        row = i // ncols
        col = i % ncols
        boxplot = sns.boxplot(x='Failure Type', y=feature, data=df, hue='Failure Type', palette='colorblind', ax=axs[row, col], legend=False)
        axs[row, col].set_title(f'Boxplot of {feature} vs Failure Type')
        axs[row, col].set_xticklabels(axs[row, col].get_xticks(), rotation=45)
    if n % ncols != 0:
        for col in range(n % ncols, ncols):
            fig.delaxes(axs[nrows-1, col])
    plt.tight_layout()
    plt.savefig(f'{output_dir}/boxplots.png')
    plt.close()

def plot_tool_wear_vs_rotational_speed(df, output_dir):
    sns.relplot(x='Tool wear [min]', y='Rotational speed [rpm]', hue='Failure Type', data=df, palette='colorblind', style='Failure Type', size='Failure Type', sizes=(40, 400))
    plt.title('Relplot of Tool wear [min] vs Rotational speed [rpm]')
    plt.savefig(f'{output_dir}/tool_wear_vs_rotational_speed.png')
    plt.close()
