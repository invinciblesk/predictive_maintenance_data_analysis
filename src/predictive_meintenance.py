#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import math

#load data
df_raw = pd.read_csv('../data/predictive_maintenance.csv')



#Data visualization

#Plot failure type distribution
plt.figure(figsize=(14,8))

sns.countplot(x='Failure Type', data=df_raw, hue='Failure Type')
plt.title('Distribution of Failure Type in the dataset')

plt.show()





#correlation matrix of using pearson correlation
corr = df_raw[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']].corr(method='pearson')
corr

#plot correlation matrix of 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', using pearson correlation
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='viridis')
plt.title('Correlation matrix')
plt.show()





# Define the columns to plot
cols = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Failure Type']

# Create a figure
plt.figure(figsize=(14,8))

# Loop over the columns and create subplots
for i, column in enumerate(cols, 1):
    plt.subplot(3, 2, i)
    sns.histplot(df_raw[column], kde=True)
    plt.title(column)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    
    # If the column is 'Failure Type', rotate the x-axis labels
    if column == 'Failure Type':
        plt.xticks(rotation=45)

# Adjust the layout and show the plot
plt.tight_layout()
plt.show();




#Relplot of failure type distribution


# Define the figure
fig = plt.figure(figsize=(21, 14))

# First subplot
ax1 = fig.add_subplot(2, 2, 1)
sns.scatterplot(x='Air temperature [K]', y='Process temperature [K]', data=df_raw, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax1)
ax1.set_title('Scatterplot of Air temperature [K] vs Process temperature [K]')

# Second subplot
ax2 = fig.add_subplot(2, 2, 2)
sns.scatterplot(x='Rotational speed [rpm]', y='Torque [Nm]', data=df_raw, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax2)
ax2.set_title('Scatterplot of Rotational speed [rpm] vs Torque [Nm]')

# Third subplot
ax3 = fig.add_subplot(2, 2, 3)
sns.scatterplot(x='Tool wear [min]', y='Torque [Nm]', data=df_raw, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax3)
ax3.set_title('Scatterplot of Tool wear [min] vs Torque [Nm]')

# Fourth subplot
ax4 = fig.add_subplot(2, 2, 4)
sns.scatterplot(x='Tool wear [min]', y='Rotational speed [rpm]', data=df_raw, hue='Failure Type', style='Failure Type', palette='viridis', size='Failure Type', sizes=(40, 400), ax=ax4)
ax4.set_title('Scatterplot of Tool wear [min] vs Rotational speed [rpm]')

# Adjust the layout
plt.tight_layout()
plt.show()




# Pairplot of 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Failure Type'
g = sns.pairplot(df_raw[['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Failure Type']], hue='Failure Type', palette='colorblind')

# Set the title for the figure
g.fig.suptitle('Pairplot of Failure Types vs Failure Vector', y=1.02)

plt.show();





features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
n = len(features)
ncols = 2
nrows = math.ceil(n / ncols)

fig, axs = plt.subplots(nrows, ncols, figsize=(14, 8*nrows))

for i, feature in enumerate(features):
    row = i // ncols
    col = i % ncols
    boxplot = sns.boxplot(x='Failure Type', y=feature, data=df_raw, palette='colorblind', ax=axs[row, col])
    axs[row, col].set_title(f'Boxplot of {feature} vs Failure Type')
    boxplot.set_xticklabels(boxplot.get_xticklabels(), rotation=45)

# Remove empty subplots
if n % ncols != 0:
    for col in range(n % ncols, ncols):
        fig.delaxes(axs[nrows-1, col])

plt.tight_layout()
plt.show()





#Relplot x='Tool wear [min]', y='Rotational speed [rpm]', hue='Failure Type'
sns.relplot(x='Tool wear [min]', y='Rotational speed [rpm]', hue='Failure Type', data=df_raw, palette='colorblind', style='Failure Type', size='Failure Type', sizes=(40, 400))
plt.title('Relplot of Tool wear [min] vs Rotational speed [rpm]')
plt.show()





