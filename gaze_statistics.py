import pandas as pd

# Load the data from each CSV file
data_paths = {
    'Bike to Crosswalk': 'Outputs/bike2crosswalk.csv',
    'Downhill': 'Outputs/downhill.csv',
    'Intersection': 'Outputs/intersection.csv',
    'Road Fixtures': 'Outputs/road_fixtures.csv',
    'Road to Bike Lane': 'Outputs/road2bikelane.csv',
    'Close Proximity': 'Outputs/close_proximity.csv',
    'Occupied Crosswalk': 'Outputs/occupied_crosswalk.csv',
    'Passing Bus': 'Outputs/passing_bus.csv',
    'Passing Pedestrian': 'Outputs/passing_pedestrian.csv'
}

# Load and label data
data_list = []
for event, path in data_paths.items():
    temp_df = pd.read_csv(path)
    temp_df['event'] = event
    data_list.append(temp_df)

# Combine the data from all events into one DataFrame
data_combined = pd.concat(data_list)

# Metrics to calculate mean and variance for
metrics = [
    'stationary_gaze_entropy', 'gaze_transition_entropy',
    'gaze_variablity_x', 'gaze_variablity_y',
    'PRC', 'mean_fixation_length', 'number_fixation_per_second'
]

# Prepare text to save
results_text = ""

# Calculate mean and variance for each metric by event, append to results_text
for metric in metrics:
    grouped_data = data_combined.groupby('event')[metric]
    stats_df = pd.DataFrame({
        'Mean': grouped_data.mean(),
        'Variance': grouped_data.var()
    })
    results_text += f"\nStatistics for {metric}:\n"
    results_text += stats_df.to_string() + "\n"

# Write results_text to a text file
with open('gaze_statistics_summary.txt', 'w') as file:
    file.write(results_text)
