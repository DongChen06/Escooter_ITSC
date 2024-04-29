import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

df_roadwbikelane = pd.read_csv(
    'whole_excel_arman/roadwbikelane.csv',
    usecols=['Gaze point X', 'Gaze point Y'])

df_sidewalk = pd.read_excel('whole_excel_arman/sidewalk.xlsx',
                            engine='openpyxl', usecols=['Gaze point X', 'Gaze point Y'])

df_roadwobikelane = pd.read_csv(
    'whole_excel_arman/roadwobikelane.csv',
    usecols=['Gaze point X', 'Gaze point Y'])

df_walkways = pd.read_excel('whole_excel_arman/walkways.xlsx',
                            engine='openpyxl', usecols=['Gaze point X', 'Gaze point Y'])

dfs = [df_sidewalk.dropna(), df_walkways.dropna(), df_roadwbikelane.dropna(), df_roadwobikelane.dropna()]

names = ['Sidewalks', 'Walkways', 'Road w. bike lane', 'Road w.o. bike lane']

title_fontsize = 12
common_title_fontsize = 12
label_fontsize = 10
cbar_fontsize = 10

# Create a 1x4 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

# Plotting each DataFrame's data in the grid
for ax, df, name in zip(axes.flatten(), dfs, names):
    h = ax.hist2d(df['Gaze point X'], df['Gaze point Y'],
                  bins=35, cmap='jet', range=[[700, 1200], [250, 750]])  # , range=[[600, 1200], [400, 700]]
    ax.set_title(name, fontsize=title_fontsize)
    fig.colorbar(h[3], ax=ax).ax.tick_params(labelsize=cbar_fontsize)

fig.text(0.5, 0.01, 'Horizontal gaze position (px)', ha='center', va='center', fontsize=common_title_fontsize)
fig.text(0.01, 0.5, 'Vertical gaze position (px)', ha='center', va='center', rotation='vertical',
         fontsize=common_title_fontsize)

# Further adjust subplots to prevent overlap
# fig.subplots_adjust(left=0.1, bottom=0.1)
# fig.subplots_adjust(wspace=0.3, hspace=0.3)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, hspace=0.3, wspace=0.3)

for ax in axes.flatten():
    ax.tick_params(axis='both', which='major', labelsize=label_fontsize)

plt.tight_layout()
plt.savefig('gaze_density_arman.png', dpi=600)
plt.savefig('gaze_density_arman.pdf')
plt.show()
