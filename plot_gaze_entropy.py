import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

# Load the data from each Excel file
data_roadwbikelane = pd.read_csv('Outputs/roadwbikelane.csv')
data_roadwobikelane = pd.read_csv('Outputs/roadwobikelane.csv')
data_sidewalk = pd.read_csv('Outputs/sidewalk.csv')
data_walkways = pd.read_csv('Outputs/walkways.csv')


data_roadwbikelane['event'] = 'Road w. bike lane'
data_roadwobikelane['event'] = 'Road w.o. bike lane'
data_sidewalk['event'] = 'Sidewalks'
data_walkways['event'] = 'Walkways'


# Combine the data from all events into one DataFrame
data_combined = pd.concat([data_sidewalk, data_walkways, data_roadwbikelane, data_roadwobikelane])


def save_and_show_figure(fig, filename):
    fig.tight_layout()  # Adjust the layout
    fig.savefig(f'{filename}.png', dpi=600)
    fig.savefig(f'{filename}.pdf', dpi=600)
    plt.show()

font_size = 16
tick_size = 10
degree = 0

labels = ['Sidewalks', 'Walkways', 'Bike lane', 'No bike lane']

# Stationary Gaze Entropy and Gaze Transition Entropy
fig1, axs1 = plt.subplots(2, 1, figsize=(8, 6))  # 2 rows, 1 column
sns.boxplot(x='event', y='stationary_gaze_entropy', data=data_combined, palette="Set3", ax=axs1[0])
sns.swarmplot(x='event', y='stationary_gaze_entropy', data=data_combined, color=".25", dodge=True, ax=axs1[0])
axs1[0].set_ylabel('Stationary gaze entropy', fontsize=font_size)
axs1[0].set_xlabel('')
axs1[0].tick_params(labelbottom=False)
sns.boxplot(x='event', y='gaze_transition_entropy', data=data_combined, palette="Set3", ax=axs1[1])
sns.swarmplot(x='event', y='gaze_transition_entropy', data=data_combined, color=".25", dodge=True, ax=axs1[1])
axs1[1].set_ylabel('Gaze transition entropy', fontsize=font_size)
axs1[1].set_xticklabels(labels, rotation=degree, ha="center", fontsize=font_size)
axs1[1].set_xticks(range(len(labels)))
axs1[1].set_xlabel('')
save_and_show_figure(fig1, 'gaze_entropy_metrics_arman')

# Gaze Variability X and Gaze Variability Y
fig2, axs2 = plt.subplots(2, 1, figsize=(8, 6))  # 2 rows, 1 column
sns.boxplot(x='event', y='gaze_variablity_x', data=data_combined, palette="Set3", ax=axs2[0])
sns.swarmplot(x='event', y='gaze_variablity_x', data=data_combined, color=".25", dodge=True, ax=axs2[0])
axs2[0].set_ylabel('Gaze variability X', fontsize=font_size)
axs2[0].set_xlabel('')
axs2[0].tick_params(labelbottom=False)
sns.boxplot(x='event', y='gaze_variablity_y', data=data_combined, palette="Set3", ax=axs2[1])
sns.swarmplot(x='event', y='gaze_variablity_y', data=data_combined, color=".25", dodge=True, ax=axs2[1])
axs2[1].set_ylabel('Gaze variability Y', fontsize=font_size)
axs2[1].set_xticklabels(labels, rotation=degree, ha="center", fontsize=font_size)
axs2[1].set_xticks(range(len(labels)))
axs2[1].set_xlabel('')
save_and_show_figure(fig2, 'gaze_variability_metrics_arman')

# Third Figure: PRC
fig3, ax3 = plt.subplots(figsize=(8, 3))
sns.boxplot(x='event', y='PRC', data=data_combined, palette="Set3", ax=ax3)
sns.swarmplot(x='event', y='PRC', data=data_combined, color=".25", dodge=True, ax=ax3)
ax3.set_ylabel('Percentage of road center', fontsize=font_size)
ax3.set_xticklabels(labels, rotation=degree, ha="center", fontsize=font_size)
ax3.set_xticks(range(len(labels)))
ax3.set_xlabel('')
save_and_show_figure(fig3, 'prc_metric_arman')

# Fixation length and frequency
fig4, axs4 = plt.subplots(2, 1, figsize=(8, 6))
sns.boxplot(x='event', y='mean_fixation_length', data=data_combined, palette="Set3", ax=axs4[0])
sns.swarmplot(x='event', y='mean_fixation_length', data=data_combined, color=".25", dodge=True, ax=axs4[0])
axs4[0].set_ylabel('Mean fixation length (s)', fontsize=font_size)
axs4[0].set_xlabel('')
axs4[0].tick_params(labelbottom=False)
sns.boxplot(x='event', y='number_fixation_per_second', data=data_combined, palette="Set3", ax=axs4[1])
sns.swarmplot(x='event', y='number_fixation_per_second', data=data_combined, color=".25", dodge=True, ax=axs4[1])
axs4[1].set_ylabel('Fixations per second', fontsize=font_size)
axs4[1].set_xticklabels(labels, rotation=degree, ha="center", fontsize=font_size)
axs4[1].set_xticks(range(len(labels)))
axs4[1].set_xlabel('')
save_and_show_figure(fig4, 'fixation_metrics_arman')
