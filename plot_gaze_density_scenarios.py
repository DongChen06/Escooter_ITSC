import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"

df_bike2crosswalk = pd.read_excel(
    'Whole_excels/bike2crosswalk.xlsx', engine='openpyxl',
    usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_downhill = pd.read_excel('Whole_excels/downhill.xlsx', engine='openpyxl',
                            usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_intersection = pd.read_excel('Whole_excels/intersection.xlsx', engine='openpyxl',
                                usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_road_fixtures = pd.read_excel('Whole_excels/road_fixtures.xlsx', engine='openpyxl',
                                 usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_road2bikelane = pd.read_excel('Whole_excels/road2bikelane.xlsx', engine='openpyxl',
                                 usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_close_proximity = pd.read_excel('Whole_excels/close_proximity.xlsx', engine='openpyxl',
    usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_occupied_crosswalk = pd.read_excel('Whole_excels/occupied_crosswalk.xlsx', engine='openpyxl',
    usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_passing_bus = pd.read_excel('Whole_excels/passing_bus.xlsx', engine='openpyxl',
                               usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

df_passing_pedestrian = pd.read_excel('Whole_excels/passing_pedestrian.xlsx', engine='openpyxl',
    usecols=['Gaze point X [MCS px]', 'Gaze point Y [MCS px]'])

dfs = [df_bike2crosswalk.dropna(), df_intersection.dropna(), df_occupied_crosswalk.dropna(),
       df_downhill.dropna(), df_close_proximity.dropna(),
       df_road_fixtures.dropna(), df_road2bikelane.dropna(),
       df_passing_bus.dropna(), df_passing_pedestrian.dropna()]

names = ['Bike lane to crosswalk', 'Intersection', 'Occupied crosswalk',
         'Downhill', 'Close proximity',
         'Road fixtures', 'Road to bike lane',
         'Passing bus', 'Passing pedestrian']

title_fontsize = 20
common_title_fontsize = 20
label_fontsize = 16
cbar_fontsize = 16

# Create a 3x3 grid of subplots
fig, axes = plt.subplots(3, 3, figsize=(15, 15))

# Plotting each DataFrame's data in the grid
for ax, df, name in zip(axes.flatten(), dfs, names):
    h = ax.hist2d(df['Gaze point X [MCS px]'], df['Gaze point Y [MCS px]'],
                  bins=35, cmap='jet', range=[[800, 1200], [250, 750]])  # , range=[[600, 1200], [400, 700]]
    ax.set_title(name, fontsize=title_fontsize)
    fig.colorbar(h[3], ax=ax).ax.tick_params(labelsize=cbar_fontsize)

fig.text(0.5, 0.01, 'Horizontal gaze position (px)', ha='center', va='center', fontsize=common_title_fontsize)
fig.text(0.01, 0.5, 'Vertical gaze position (px)', ha='center', va='center', rotation='vertical',
         fontsize=common_title_fontsize)

# Adjust the layout to make room for titles, labels, and colorbars
plt.tight_layout(pad=3.0)
# Further adjust subplots to prevent overlap
fig.subplots_adjust(left=0.1, bottom=0.1)

# set a larger font size for the ticks as well
for ax in axes.flatten():
    ax.tick_params(axis='both', which='major', labelsize=label_fontsize)

# Adjust the layout to make room for titles, labels, and colorbars
plt.tight_layout(pad=3.0)

plt.savefig('gaze_density_grid.png', dpi=600)
plt.savefig('gaze_density_grid.pdf')
plt.show()
