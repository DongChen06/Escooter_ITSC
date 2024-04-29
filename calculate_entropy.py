import pandas as pd
import numpy as np
import scipy.stats
import os
from tqdm import tqdm
import math

data_folder = 'Traffic_scenarios/road_fixtures'
output_file = 'Outputs/road_fixtures.csv'
excel_files = [file for file in os.listdir(data_folder) if file.endswith('.xlsx')]
width, height = 1920, 1080
# gaze parameters
pixel_bins = 100  # TODO: Check
pixel_bin_width = math.ceil(width / pixel_bins)
pixel_bin_height = math.ceil(height / pixel_bins)
road_center_radius = np.tan(12 / 180 * np.pi) * 1920 / 2 / np.tan(55 / 180 * np.pi)  # TODO: Check


# stationary gaze entropy
def stationary_gaze_entropy(gaze_array):
    p_data = pd.Series(gaze_array).value_counts()  # counts occurrence of each value
    entropy = scipy.stats.entropy(p_data, base=2)  # get entropy from counts
    return entropy


# gaze transition entropy
def gaze_transition_entropy(gaze_array):   # TODO: Check
    # Creating transition matrix from the gaze array
    n = len(np.unique(gaze_array))
    trans_mat = np.zeros((n, n))
    gaze_indices = {val: idx for idx, val in enumerate(np.unique(gaze_array))}
    for (i, j) in zip(gaze_array, gaze_array[1:]):
        trans_mat[gaze_indices[i], gaze_indices[j]] += 1
    # Normalizing transition matrix to get probabilities
    trans_mat = trans_mat / trans_mat.sum(axis=1, keepdims=True)
    # Calculating entropy
    entropy = -np.nansum(trans_mat * np.log2(trans_mat))
    return entropy


# fixation information
def calculate_fixation_length(df, gaze_area_column, timestamp_column):   # TODO: Check
    # Convert timestamps from microseconds to seconds for easier interpretation
    df['AdjustedTime'] = df[timestamp_column] / 1e6

    # Identify fixations as sequences of consecutive identical gaze areas
    df['fixation_id'] = (df[gaze_area_column].shift() != df[gaze_area_column]).cumsum()

    fixation_group = df.groupby('fixation_id')
    number_of_fixations = 0
    fixation_length = []

    # Iterate through each group to calculate fixation lengths
    for fixation_id, group in fixation_group:
        # We assume a fixation is when there are at least two consecutive gaze points in the same area
        if len(group) >= 2:
            number_of_fixations += 1
            fixation_length.append(group['AdjustedTime'].max() - group['AdjustedTime'].min())

    # Calculate mean fixation length and fixation rate per second
    mean_fixation_length = np.mean(fixation_length) if fixation_length else 0
    number_fixation_per_second = number_of_fixations / (df['AdjustedTime'].max() - df['AdjustedTime'].min())

    return mean_fixation_length, number_fixation_per_second


def floatrange(start, stop, steps):
    return [start + float(i) * (stop - start) / (float(steps) - 1) for i in range(steps)]


def findRC(x):  # TODO: Check
    bins = floatrange(min(x), max(x), int(x.max() - x.min()))
    n = np.zeros((len(bins), 2))
    x = np.array(x)
    for i in range(len(bins) - 1):
        n[i, 0] = (bins[i] + bins[i + 1]) / 2
        a = x[(x > bins[i]) & (x < bins[i + 1])]
        n[i, 1] = len(a)
    return n[:, 0][n[:, 1] == n[:, 1].max()].mean()


results = []
for file in tqdm(excel_files):
    print(file)

    try:
        file_path = os.path.join(data_folder, file)
        try:
            df = pd.read_excel(file_path, engine='openpyxl',
                               usecols=['Recording timestamp', 'Gaze point X', 'Gaze point Y',
                                        'Fixation point X', 'Fixation point Y']).dropna()
        except:
            df = pd.read_excel(file_path, engine='openpyxl',
                               usecols=['Recording timestamp [μs]', 'Gaze point X [MCS px]', 'Gaze point Y [MCS px]',
                                        'Fixation point X [MCS px]', 'Fixation point Y [MCS px]']).dropna()

        if len(df) != 0:
            try:
                df['Gaze point X'] = df['Gaze point X'].astype(int)
                df['Gaze point Y'] = df['Gaze point Y'].astype(int)
                df['gaze_points'] = list(zip(df['Gaze point X'], df['Gaze point Y']))
                df['fixation_gaze_points'] = list(zip(df['Fixation point X'], df['Fixation point Y']))
            except:
                df['Gaze point X'] = df['Gaze point X [MCS px]'].astype(int)
                df['Gaze point Y'] = df['Gaze point Y [MCS px]'].astype(int)
                df['gaze_points'] = list(zip(df['Gaze point X [MCS px]'], df['Gaze point Y [MCS px]']))
                df['fixation_gaze_points'] = list(zip(df['Fixation point X [MCS px]'], df['Fixation point Y [MCS px]']))

            df['gaze_area'] = df['gaze_points'].apply(
                lambda x: x[0] // pixel_bin_width + x[1] // pixel_bin_height * pixel_bins)
            df['fixation_gaze_area'] = df['fixation_gaze_points'].apply(
                lambda x: x[0] // pixel_bin_width + x[1] // pixel_bin_height * pixel_bins)

            # Compute stationary gaze entropy
            s_entropy = stationary_gaze_entropy(df['fixation_gaze_area'])

            # Compute gaze transition entropy
            t_entropy = gaze_transition_entropy(df['fixation_gaze_area'])

            # Compute fixation information
            try:
                mean_fixation_length, num_fixation_per_sec = calculate_fixation_length(df, 'fixation_gaze_area',
                                                                                       'Recording timestamp [μs]')
            except:
                mean_fixation_length, num_fixation_per_sec = calculate_fixation_length(df, 'fixation_gaze_area',
                                                                                   'Recording timestamp')
            try:
                road_center_x = findRC(df['Fixation point X'])
                road_center_y = findRC(df['Fixation point Y'])

                df['RC'] = np.nan
                df['RC'][
                    (((df['Fixation point X'] - road_center_x) ** 2 + (
                            df['Fixation point Y'] - road_center_y) ** 2) ** 0.5) < road_center_radius] = 1
                df['RC'][
                    (((df['Fixation point X'] - road_center_x) ** 2 + (
                            df['Fixation point Y'] - road_center_y) ** 2) ** 0.5) >= road_center_radius] = 0
                PRC = sum(df['RC']) / len(df)

                gaze_variablity_x = np.std(df['Gaze point X'])
                gaze_variablity_y = np.std(df['Gaze point Y'])
            except:
                road_center_x = findRC(df['Fixation point X [MCS px]'])
                road_center_y = findRC(df['Fixation point Y [MCS px]'])

                df['RC'] = np.nan
                df['RC'][
                    (((df['Fixation point X [MCS px]'] - road_center_x) ** 2 + (
                            df['Fixation point Y [MCS px]'] - road_center_y) ** 2) ** 0.5) < road_center_radius] = 1
                df['RC'][
                    (((df['Fixation point X [MCS px]'] - road_center_x) ** 2 + (
                            df['Fixation point Y [MCS px]'] - road_center_y) ** 2) ** 0.5) >= road_center_radius] = 0
                PRC = sum(df['RC']) / len(df)

                gaze_variablity_x = np.std(df['Gaze point X [MCS px]'])
                gaze_variablity_y = np.std(df['Gaze point Y [MCS px]'])

            results.append({
                'file': file,
                'stationary_gaze_entropy': s_entropy,
                'gaze_transition_entropy': t_entropy,
                'mean_fixation_length': mean_fixation_length,
                'number_fixation_per_second': num_fixation_per_sec,
                'gaze_variablity_x': gaze_variablity_x,
                'gaze_variablity_y': gaze_variablity_y,
                'PRC': PRC
            })
    except:
        continue

results_df = pd.DataFrame(results)
results_df.to_csv(output_file, index=False)
