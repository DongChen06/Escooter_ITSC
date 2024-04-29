import pandas as pd
import os


# Function to convert HH:MM:SS to microseconds
def time_to_microseconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return ((h * 3600) + (m * 60) + s) * 1e6


# Function to check if a time is within a specific range
def is_time_in_range(start_us, end_us, time):
    return start_us <= time <= end_us

scenario = 'passing_pedestrian'  # bike2crosswalk, downhill, intersection, road_fixtures,
                            # road2bikelane, close_proximity, occupied_crosswalk, passing_bus, passing_pedestrian


# filter a DataFrame based on time ranges and save each filtered result as a separate Excel file
def filter_and_save_individual_dfs(df, time_ranges, video_number):
    for index, time_range in enumerate(time_ranges, start=1):
        start_us = time_to_microseconds(time_range[0])
        end_us = time_to_microseconds(time_range[1])
        try:
            filtered_df = df[df['Recording timestamp'].apply(lambda x: is_time_in_range(start_us, end_us, x))]
        except:
            filtered_df = df[df['Recording timestamp [μs]'].apply(lambda x: is_time_in_range(start_us, end_us, x))]

        # Save the filtered DataFrame to a separate Excel file
        filename = os.path.join(folder_name, f'video{video_number}_{index}.xlsx')
        filtered_df.to_excel(filename, index=False, engine='openpyxl')
        print(f'Saved: {filename}')

if scenario == 'road_fixtures':
    folder_name = 'Traffic_scenarios/road_fixtures'
elif scenario == 'bike2crosswalk':
    folder_name = 'Traffic_scenarios/bike2crosswalk'
elif scenario == 'downhill':
    folder_name = 'Traffic_scenarios/downhill'
elif scenario == 'intersection':
    folder_name = 'Traffic_scenarios/intersection'
elif scenario == 'road2bikelane':
    folder_name = 'Traffic_scenarios/road2bikelane'
elif scenario == 'close_proximity':
    folder_name = 'Traffic_scenarios/close_proximity'
elif scenario == 'occupied_crosswalk':
    folder_name = 'Traffic_scenarios/occupied_crosswalk'
elif scenario == 'passing_bus':
    folder_name = 'Traffic_scenarios/passing_bus'
elif scenario == 'passing_pedestrian':
    folder_name = 'Traffic_scenarios/passing_pedestrian'
else:
    raise ValueError(f'Invalid scenario: {scenario}')
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


"""Bike Lane or Road to Crosswalk, bike2crosswalk"""
if scenario == 'bike2crosswalk':
    mar_11_arman = [['0:30:42', '0:30:03'], ['0:46:19', '0:46:23'], ['0:50:31', '0:50:42']]
    mar_13_arman = [['0:44:27', '0:44:33'], ['0:54:00', '0:54:13']]
    mar_16_arman = [['0:53:45', '0:53:51']]
    mar_18_arman = [['0:03:09', '0:03:14'], ['1:04:26', '1:04:30'], ['1:04:54', '1:05:15']]
    mar_19_arman = [['0:06:37', '0:06:42'], ['0:27:05', '0:27:10'], ['0:31:36', '0:31:43'], ['0:41:08', '0:41:13'],
                    ['0:45:35', '0:45:43'], ['0:57:08', '0:57:19'], ['1:00:34',  '1:00:45']]
    mar_25_arman = [['0:03:50', '0:03:57'], ['0:11:30', '0:11:36'], ['0:12:18', '0:12:23'], ['0:21:58', '0:22:06'],
                    ['0:45:22', '0:45:30']]
    mar_27_arman = [['0:04:28', '0:04:34'], ['0:18:03', '0:18:10'], ['0:20:10', '0:20:15'], ['0:27:50', '0:27:57'],
                    ['0:40:08', '0:40:15']]
    mar_30_arman = [['0:06:33', '0:06:37'], ['0:20:07', '0:20:12'], ['0:21:54', '0:22:02'], ['0:36:51', '0:36:58'],
                    ['0:39:44', '0:39:50'], ['0:49:54', '0:50:01']]
    apr_1_arman = [['0:04:37', '0:04:46'], ['0:28:32', '0:28:50'], ['0:28:55', '0:29:02'], ['0:51:34', '0:51:40'],
                   ['0:53:45', '0:53:50']]
    apr_4_arman = [['0:02:10', '0:02:17'], ['0:38:25', '0:38:32'], ['0:49:04', '0:49:11']]

    time_ranges1 = [['0:20:50', '0:21:08'], ['0:21:38', '0:22:14'], ['0:39:27', '0:39:42'], ['0:49:52', '0:50:21'],
                    ['0:52:39', '0:53:01'], ['0:57:20', '0:57:43']]
    time_ranges2 = [['0:37:55', '0:38:20'], ['0:51:04', '0:51:27']]
    time_ranges3 = [['0:11:48', '0:12:08'], ['0:17:12', '0:17:22'], ['0:20:26', '0:20:55'], ['0:22:23', '0:22:41'],
                    ['0:33:05', '0:34:01'], ['0:47:00', '0:47:23'], ['0:51:37', '0:52:18']]
    time_ranges4 = [['0:06:17', '0:06:33'], ['0:07:35', '0:07:47'], ['0:10:44', '0:10:53'], ['0:17:58', '0:18:13'],
                    ['0:46:12', '0:47:20'], ['0:48:38', '0:49:19']]
    time_ranges5 = [['0:16:53', '0:17:23'], ['0:17:36', '0:18:16'], ['0:19:34', '0:21:38'], ['0:25:03', '0:25:25'],
                    ['0:33:05', '0:33:46'], ['0:42:24', '0:42:35']]
    time_ranges6 = [['0:18:04', '0:18:47']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df2, time_ranges2, 12)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df5, time_ranges5, 15)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)

"""High Speed Downhill, downhill"""
if scenario == 'downhill':
    mar_11_arman = [['0:10:46', '0:10:54'], ['0:18:07', '0:18:16'], ['0:24:48', '0:25:00'], ['0:25:26', '0:25:32'],
                    ['0:26:40', '0:26:48'], ['0:36:07', '0:36:14'], ['0:42:17', '0:42:35'], ['0:48:40', '0:49:15']]
    mar_13_arman = [['0:10:36', '0:10:49'], ['0:13:05', '0:13:28'], ['0:16:38', '0:16:50'], ['0:27:47', '0:28:01'],
                    ['0:29:10', '0:29:17'], ['0:37:15', '0:37:30'], ['0:42:47', '0:42:57']]
    mar_16_arman = [['0:05:59', '0:05:37'], ['0:08:19', '0:08:30'], ['0:22:06', '0:22:20'], ['0:22:57', '0:23:12'],
                    ['0:34:41', '0:34:58'], ['0:36:12', '0:36:20'], ['0:42:32', '0:43:09']]
    mar_18_arman = [['0:03:18', '0:03:30'], ['0:21:21', '0:21:32'], ['0:32:15', '0:32:21'], ['0:48:57', '0:49:10'],
                    ['0:59:07','0:59:20'], ['1:01:39', '1:01:48'], ['1:02:56', '1:03:01']]
    mar_19_arman = [['0:06:43', '0:06:53'], ['0:32:05', '0:33:05'], ['0:45:45', '0:45:58'], ['0:50:19', '0:50:31'],
                    ['0:52:48', '0:53:10'], ['0:55:25', '0:55:38'], ['1:00:48', '1:00:52']]
    mar_25_arman = [['0:15:05', '0:15:17'], ['0:47:17', '0:47:30'], ['0:50:09', '0:50:14']]
    mar_27_arman = [['0:04:38', '0:04:47'], ['0:11:06', '0:11:28'], ['0:21:45', '0:21:55'], ['0:28:17', '0:28:33'],
                    ['0:29:24', '0:29:47'], ['0:30:06', '0:30:15'], ['0:31:04', '0:31:17'], ['0:32:22', '0:32:26'],
                    ['0:45:46', '0:46:04']]
    mar_30_arman = [['0:06:39', '0:06:51'], ['0:22:42', '0:23:00'], ['0:27:39', '0:27:51'], ['0:30:20', '0:30:30'],
                    ['0:33:14', '0:33:25']]
    apr_1_arman = [['0:29:57', '0:30:05']]
    apr_4_arman = [['0:02:17', '0:02:45'], ['0:07:55', '0:08:14'], ['0:11:37', '0:11:48'], ['0:13:53', '0:14:07'],
                   ['0:26:41', '0:26:55'], ['0:27:11', '0:28:35'], ['0:38:59', '0:39:07'], ['0:39:34', '0:39:40'],
                   ['0:40:46', '0:40:55'], ['0:43:03', '0:43:16'], ['0:44:11', '0:44:19'], ['0:44:41', '0:44:50']]

    time_ranges1 = [['0:25:30', '0:25:57'], ['0:28:51', '0:29:19'], ['0:45:45', '0:46:09'], ['0:57:35', '0:58:08']]
    time_ranges2 = [['0:16:37', '0:16:56'], ['0:19:17', '0:19:45'], ['0:28:31', '0:28:57'], ['0:32:31', '0:32:51']]
    time_ranges3 = [['0:13:45', '0:14:10'], ['0:24:03', '0:24:15'], ['0:25:32', '0:26:10'], ['0:53:35', '0:54:00']]
    time_ranges4 = [['0:04:04', '0:04:25'], ['0:10:19', '0:10:44'], ['0:22:11', '0:22:27'], ['0:48:00', '0:48:40']]
    time_ranges5 = [['0:24:40', '0:25:06'], ['0:31:12', '0:31:27']]
    time_ranges6 = [['0:19:46', '0:20:27']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df2, time_ranges2, 12)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df5, time_ranges5, 15)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)

"""Intersection, intersection"""
if scenario == 'intersection':
    mar_11_arman = [['0:11:25', '0:11:34'], ['0:12:14', '0:12:46'], ['0:13:38', '0:19:25'], ['0:20:00', '0:20:10'],
                    ['0:20:29', '0:20:35'], ['0:21:50', '0:21:55'], ['0:22:40', '0:23:03'], ['0:23:20', '0:34:35'],
                    ['0:26:35', '0:26:40'], ['0:27:28', '0:27:37'], ['0:29:44', '0:29:52'], ['0:30:40', '0:31:00'],
                    ['0:34:17', '0:34:41'], ['0:35:26', '0:35:29'], ['0:36:35', '0:36:29'], ['0:38:17', '0:38:22'],
                    ['0:39:04', '0:39:09'], ['0:40:56', '0:41:53'], ['0:43:05', '0:43:25'], ['0:43:50', '0:43:59']]
    mar_13_arman = [['0:04:55', '0:06:20'], ['0:09:23', '0:09:30'], ['0:10:46', '0:11:25'], ['0:12:45', '0:12:58'],
                    ['0:13:28', '0:14:25'], ['0:14:54', '0:14:59'], ['0:15:27', '0:15:52'], ['0:16:55', '0:17:12'],
                    ['0:26:55', '0:27:25'], ['0:29:55', '0:30:05'], ['0:34:30', '0:34:40'], ['0:37:32', '0:38:05'],
                    ['0:39:10', '0:40:12'], ['0:45:19', '0:45:30'], ['0:50:45', '0:52:11']]
    mar_16_arman = [['0:06:25', '0:07:15'], ['0:08:43', '0:08:47'], ['0:17:34', '0:18:15'], ['0:18:32', '0:18:36'],
                    ['0:23:12', '0:24:29'], ['0:43:21', '0:43:37'], ['0:44:15', '0:45:22'], ['0:47:10', '0:47:48'],
                    ['0:48:42', '0:48:49'], ['0:49:15', '0:50:04'], ['0:52:31', '0:52:50']]
    mar_18_arman = [['0:03:56', '0:04:12'], ['0:04:55', '0:05:04'], ['0:07:17', '0:07:25'], ['0:08:55', '0:09:04'],
                    ['0:10:26', '0:10:31'], ['0:10:55', '0:12:02'], ['0:12:40', '0:12:50'], ['0:13:10', '0:13:21'],
                    ['0:14:45', '0:14:53'], ['0:15:33', '0:15:36'], ['0:16:03', '0:16:34'], ['0:31:42', '0:31:45'],
                    ['1:00:35', '1:00:50'], ['1:01:51', '1:02:20'], ['1:04:53', '1:04:58']]
    mar_19_arman = [['0:07:20', '0:07:31'], ['0:08:07', '0:08:55'], ['0:12:25', '0:12:37'], ['0:13:52', '0:14:26'],
                    ['0:14:48', '0:15:41'], ['0:16:15', '0:17:03'], ['0:17:20', '0:18:33'], ['0:20:40', '0:20:53'],
                    ['0:21:10', '0:21:15'], ['0:21:40', '0:22:00'], ['0:23:03', '0:24:02'], ['0:29:57', '0:30:03'],
                    ['0:35:16', '0:35:25'], ['0:42:53', '0:42:57'], ['0:46:01', '0:46:27'], ['0:47:12', '0:47:38']]
    mar_25_arman = [['0:04:38', '0:04:50'], ['0:05:40', '0:06:52'], ['0:16:14', '0:17:13'], ['0:18:27', '0:18:32'],
                    ['0:21:33', '0:21:55'], ['0:22:54', '0:23:04'], ['0:23:35', '0:24:05'], ['0:25:28', '0:25:35'],
                    ['0:26:12', '0:26:17'], ['0:26:34', '0:26:43'], ['0:27:13', '0:27:27'], ['0:28:33', '0:28:41'],
                    ['0:31:49', '0:31:53'], ['0:32:47', '0:32:58'], ['0:46:24', '0:46:30']]
    mar_27_arman = [['0:05:14', '0:05:28'], ['0:06:08', '0:06:24'], ['0:08:19', '0:08:24'], ['0:09:08', '0:10:25'],
                    ['0:11:43', '0:12:09'], ['0:12:27', '0:13:32'], ['0:14:00', '0:14:06'], ['0:14:28', '0:15:14'],
                    ['0:16:30', '0:16:40'], ['0:18:30', '0:18:44'], ['0:19:12', '0:20:20'], ['0:20:52', '0:21:33'],
                    ['0:30:30', '0:30:40'], ['0:32:45', '0:32:56'], ['0:36:15', '0:36:25'], ['0:36:52', '0:37:00'],
                    ['0:37:30', '0:38:10'], ['0:41:28', '0:41:40'], ['0:44:05', '0:45:19'], ['0:46:46', '0:49:08']]
    mar_30_arman = [['0:07:15', '0:07:23'], ['0:07:55', '0:08:03'], ['0:10:50', '0:11:04'], ['0:12:28', '0:12:37'],
                    ['0:12:58', '0:13:30'], ['0:13:59', '0:14:30'], ['0:14:50', '0:15:00'], ['0:16:33', '0:16:43'],
                    ['0:17:35', '0:17:42'], ['0:18:02', '0:18:10'], ['0:18:41', '0:19:05'], ['0:25:52', '0:26:06'],
                    ['0:33:33', '0:34:00'], ['0:37:53', '0:38:00'], ['0:38:21', '0:38:31'], ['0:38:55', '0:39:00'],
                    ['0:41:14', '0:42:08']]
    apr_1_arman = [['0:05:28', '0:05:33'], ['0:06:22', '0:06:30'], ['0:08:30', '0:08:36'], ['0:09:44', '0:11:00'],
                   ['0:12:20', '0:12:36'], ['0:14:10', '0:14:23'], ['0:15:10', '0:15:15'], ['0:15:38', '0:15:51'],
                   ['0:17:26', '0:17:36'], ['0:18:31', '0:18:42'], ['0:19:03', '0:19:12'], ['0:19:43', '0:19:47'],
                   ['0:37:43', '0:37:50'], ['0:41:27', '0:41:34'], ['0:41:56', '0:42:25'], ['0:42:49', '0:42:54'],
                   ['0:45:10', '0:45:41'], ['0:47:14', '0:47:48']]
    apr_4_arman = [['0:03:45', '0:03:55'], ['0:05:13', '0:05:25'], ['0:06:22', '0:06:32'], ['0:09:05', '0:09:26'],
                   ['0:10:35', '0:11:10'], ['0:11:58', '0:12:05'], ['0:13:23', '0:13:34'], ['0:14:19', '0:14:23'],
                   ['0:14:42', '0:14:46'], ['0:15:09', '0:15:32'], ['0:15:58', '0:16:03'], ['0:16:32', '0:17:32'],
                   ['0:17:45', '0:18:58'], ['0:20:07', '0:20:18'], ['0:22:05', '0:22:10'], ['0:32:14', '0:32:23'],
                   ['0:40:22', '0:40:30'], ['0:42:10', '0:42:42'], ['0:44:51', '0:44:58'], ['0:45:36', '0:45:55'],
                   ['0:46:15', '0:47:02']]

    time_ranges1 = [['0:20:18', '0:20:34'], ['0:20:50', '0:21:08'], ['0:21:23', '0:21:33'], ['0:21:38', '0:22:14'],
                    ['0:23:56', '0:24:27'], ['0:24:28', '0:25:12'], ['0:27:09', '0:27:23'], ['0:38:38', '0:39:10'],
                    ['0:49:05', '0:49:15'], ['0:49:52', '0:50:31'], ['0:52:39', '0:53:01'], ['0:54:10', '0:55:03'],
                    ['0:57:20', '0:57:43']]
    time_ranges2 = [['0:14:38', '0:14:48'], ['0:26:25', '0:26:38'], ['0:31:02', '0:31:22'], ['0:37:55', '0:38:20'],
                    ['0:46:08', '0:46:18'], ['0:51:04', '0:51:27']]
    time_ranges3 = [['0:10:16', '0:10:27'], ['0:11:26', '0:11:33'], ['0:11:48', '0:12:08'], ['0:12:22', '0:12:30'],
                    ['0:14:02', '0:14:12'], ['0:14:40', '0:14:47'], ['0:14:57', '0:16:41'], ['0:19:18', '0:19:26'],
                    ['0:20:26', '0:20:55'], ['0:22:23', '0:22:58'], ['0:24:11', '0:24:33'], ['0:28:48', '0:28:57'],
                    ['0:30:37', '0:30:56'], ['0:32:25', '0:32:37'], ['0:33:05', '0:34:01'], ['0:44:01', '0:44:53'],
                    ['0:45:04', '0:45:09'], ['0:47:00', '0:47:23'], ['0:47:37', '0:47:46'], ['0:48:06', '0:48:16'],
                    ['0:51:37', '0:52:18']]
    time_ranges4 = [['0:04:40', '0:05:19'], ['0:06:17', '0:06:33'], ['0:06:48', '0:07:15'], ['0:07:22', '0:07:28'],
                    ['0:07:35', '0:07:47'], ['0:08:28', '0:08:40'], ['0:08:58', '0:09:07'], ['0:09:16', '0:09:24'],
                    ['0:10:44', '0:10:53'], ['0:11:46', '0:11:59'], ['0:12:39', '0:12:55'], ['0:14:21', '0:15:54'],
                    ['0:16:03', '0:16:11'], ['0:17:58', '0:18:13'], ['0:18:46', '0:18:54'], ['0:20:35', '0:20:53'],
                    ['0:25:38', '0:26:05'], ['0:26:37', '0:26:43'], ['0:27:03', '0:27:21'], ['0:39:13', '0:40:22'],
                    ['0:46:12', '0:47:20'], ['0:47:38', '0:47:58']]
    time_ranges5 = [['0:05:49', '0:06:11'], ['0:10:17', '0:10:26'], ['0:16:19', '0:10:26'], ['0:16:53', '0:17:23'],
                    ['0:17:36', '0:18:16'], ['0:18:51', '0:19:06'], ['0:19:21', '0:19:28'], ['0:19:34', '0:21:38'],
                    ['0:21:49', '0:22:00'], ['0:22:23', '0:22:34'], ['0:23:02', '0:23:21'], ['0:24:11', '0:24:40'],
                    ['0:25:03', '0:25:25'], ['0:27:57', '0:28:13'], ['0:28:53', '0:29:08'], ['0:33:05', '0:33:46'],
                    ['0:38:11', '0:38:21'], ['0:38:40', '0:38:55'], ['0:39:22', '0:39:39'], ['0:41:55', '0:42:04']]
    time_ranges6 = [['0:04:29', '0:05:24'], ['0:08:47', '0:09:59'], ['0:13:57', '0:14:25'], ['0:16:02', '0:16:11'],
                    ['0:18:04', '0:18:47'], ['0:26:41', '0:26:53'], ['0:28:33', '0:28:59'], ['0:29:16', '0:29:37'],
                    ['0:29:58', '0:30:25'], ['0:37:21', '0:38:35'], ['0:38:48', '0:38:58'], ['0:39:14', '0:39:21'],
                    ['0:39:46', '0:39:52'], ['0:40:55', '0:41:10'], ['0:42:41', '0:42:50'], ['0:42:35', '0:43:31']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df2, time_ranges2, 12)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df5, time_ranges5, 15)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)

"""Road_fixtures, road_fixtures"""
if scenario == 'road_fixtures':
    mar_11_arman = [['0:13:18', '0:13:23'], ['0:14:44', '0:14:49'], ['0:21:20', '0:21:23'], ['0:24:57', '0:25:02'],
                    ['0:29:27', '0:29:33'], ['0:30:20', '0:30:25'], ['0:35:50', '0:35:53']]
    mar_13_arman = [['0:06:56', '0:07:00'], ['0:08:19', '0:08:23'], ['0:08:58', '0:09:02'], ['0:21:45', '0:21:50'],
                    ['0:25:58', '0:26:24'], ['0:26:42', '0:26:45']]
    mar_16_arman = [['0:07:24', '0:07:27'], ['0:07:52', '0:07:57'], ['0:09:19', '0:09:25'], ['0:10:06', '0:10:11']]
    mar_18_arman = [['0:05:10', '0:05:14'], ['0:05:40', '0:05:47'], ['0:07:12', '0:07:18'], ['0:08:32', '0:08:38'],
                    ['0:14:09', '0:14:12']]
    mar_19_arman = [['0:09:04', '0:09:07'], ['0:09:27', '0:09:31'], ['0:11:02', '0:11:09'], ['0:11:45', '0:11:51'],
                    ['0:19:14', '0:19:16'], ['0:19:24', '0:19:26'], ['0:43:24', '0:43:26'], ['0:43:35', '0:43:37'],
                    ['0:56:22', '0:56:27']]
    mar_25_arman = [['0:07:02', '0:07:05'], ['0:07:29', '0:07:34'], ['0:15:15', '0:15:20'], ['0:15:51', '0:15:56'],
                    ['0:24:44', '0:24:48'], ['0:25:01', '0:25:04']]
    mar_27_arman = [['0:06:32', '0:06:35'], ['0:06:58', '0:07:03'], ['0:08:14', '0:08:19'], ['0:08:49', '0:08:55'],
                    ['0:15:51', '0:15:54'], ['0:16:01', '0:16:04']]
    mar_30_arman = [['0:08:12', '0:08:15'], ['0:08:35', '0:08:42'], ['0:10:28', '0:10:33'], ['0:15:42', '0:15:45'],
                    ['0:15:53', '0:15:56']]
    apr_1_arman = [['0:06:40', '0:06:43'], ['0:07:06', '0:07:10'], ['0:08:26', '0:08:32'],  ['0:09:13', '0:09:19'],
                   ['0:16:39', '0:16:42'], ['0:16:53', '0:16:57']]
    apr_4_arman = [['0:19:31', '0:19:33'], ['0:19:39', '0:19:41']]

    time_ranges1 = [['0:15:12', '0:15:22'], ['0:28:10', '0:28:20']]
    time_ranges2 = [['0:31:34', '0:31:44']]
    time_ranges3 = [['0:04:57', '0:05:02'], ['0:52:37', '0:52:43']]
    time_ranges4 = [['0:21:16', '0:21:22'], ['0:21:50', '0:21:56'], ['0:23:02', '0:23:07'], ['0:23:23', '0:23:27'],
                    ['0:35:43', '0:35:48'], ['0:36:05', '0:36:13']]
    time_ranges6 = [['0:05:27', '0:05:32'], ['0:05:54', '0:06:01'], ['0:32:25', '0:32:28'], ['0:32:36', '0:32:39'],
                    ['0:32:54', '0:32:57'], ['0:33:47', '0:33:51'], ['0:33:53', '0:33:56']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df2, time_ranges2, 12)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)

"""Road_to_Bikelane, road2bikelane"""
if scenario == 'road2bikelane':
    mar_11_arman = [['0:13:04', '0:13:10'], ['0:17:58', '0:18:08'], ['0:18:10', '0:18:15'], ['0:19:27', '0:19:33'],
                    ['0:21:20', '0:21:28'], ['0:23:15', '0:23:22'], ['0:28:40', '0:28:45'], ['0:33:52', '0:33:57'],
                    ['0:35:00', '0:35:07'], ['0:35:47', '0:35:54'], ['0:37:45', '0:37:50'], ['0:38:15', '0:38:24'],
                    ['0:40:50', '0:40:55'], ['0:42:13', '0:42:18'], ['0:46:58', '0:47:02'], ['0:47:04', '0:47:08']]
    mar_13_arman = [['0:06:39', '0:06:48'], ['0:10:34', '0:10:42'], ['0:14:23', '0:14:28'], ['0:14:44', '0:14:51'],
                    ['0:16:32', '0:16:38'], ['0:19:30', '0:19:35'], ['0:28:00', '0:28:05'], ['0:40:10', '0:40:15'],
                    ['0:41:28', '0:41:33'], ['0:41:55', '0:42:02'], ['0:42:48', '0:42:53']]
    mar_16_arman = [['0:07:37', '0:07:42'], ['0:12:14', '0:12:19'], ['0:14:00', '0:14:05'], ['0:47:48', '0:47:53'],
                    ['0:50:57', '0:51:03'], ['0:51:22', '0:51:28'], ['0:52:15', '0:52:20'], ['0:52:27', '0:52:34'],
                    ['0:53:55', '0:54:00']]
    mar_18_arman = [['0:10:12', '0:10:32'], ['0:12:02', '0:12:08'], ['0:12:18', '0:12:23'], ['0:12:30', '0:12:36'],
                    ['0:14:10', '0:14:20'], ['1:02:55', '1:03:00'], ['1:03:28', '1:03:33']]
    mar_19_arman = [['0:13:42', '0:13:48'], ['0:14:23', '0:14:28'], ['0:15:43', '0:15:48'], ['0:19:23', '0:19:30'],
                    ['0:22:37', '0:22:45'], ['0:42:17', '0:42:27'], ['0:42:30', '0:42:35'], ['0:58:13', '0:58:18']]
    mar_25_arman = [['0:07:14', '0:07:24'], ['0:18:10', '0:18:39'], ['0:25:01', '0:25:11'], ['0:25:57', '0:26:07'],
                    ['0:26:14', '0:26:23'], ['0:28:04', '0:28:10'], ['0:42:58', '0:43:08'], ['0:47:25', '0:47:33'],
                    ['0:50:07', '0:50:12']]
    mar_27_arman = [['0:11:32', '0:11:40'], ['0:12:06', '0:12:12'], ['0:13:33', '0:13:40'], ['0:20:25', '0:20:37'],
                    ['0:36:57', '0:37:13'], ['0:44:00', '0:44:10'], ['0:45:37', '0:45:44'], ['0:49:47', '0:49:55'],
                    ['0:50:27', '0:50:33'], ['0:50:42', '0:50:46']]
    mar_30_arman = [['0:08:23', '0:08:30'], ['0:12:17', '0:12:37'], ['0:13:30', '0:13:37'], ['0:17:49', '0:17:58'],
                    ['0:26:16', '0:26:22'], ['0:29:00', '0:29:05'], ['0:35:15', '0:35:20'], ['0:37:45', '0:37:50'],
                    ['0:38:35', '0:38:41']]
    apr_1_arman = [['0:12:08', '0:12:17'], ['0:12:31', '0:12:40'], ['0:14:28', '0:14:35'], ['0:28:52', '0:19:02'],
                   ['0:29:07', '0:29:12'], ['0:32:28', '0:32:33'], ['0:34:35', '0:34:40'], ['0:41:20', '0:41:25'],
                   ['0:42:28', '0:42:36'], ['0:47:05', '0:47:15'], ['0:48:07', '0:48:14']]
    apr_4_arman = [['0:09:34', '0:09:40'], ['0:09:57', '0:10:05'], ['0:11:10', '0:11:20'], ['0:12:58', '0:13:05'],
                   ['0:14:13', '0:14:19'], ['0:14:36', '0:14:58'], ['0:32:07', '0:32:12'], ['0:33:56', '0:34:02'],
                   ['0:43:15', '0:43:21'], ['0:43:36', '0:43:41']]

    time_ranges1 = [['0:20:08', '0:20:18'], ['0:22:53', '0:23:03'], ['0:23:21', '0:23:38'], ['0:33:55', '0:34:12'],
                    ['0:58:02', '0:58:19']]
    time_ranges3 = [['0:11:21', '0:11:27'], ['0:46:54', '0:47:02']]
    time_ranges4 = [['0:11:06', '0:11:12'], ['0:28:26', '0:28:47'], ['0:29:26', '0:29:41'], ['0:41:43', '0:41:46']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)


"""Close_Proximity, close_proximity"""
if scenario == 'close_proximity':
    mar_11_arman = [['0:19:51', '0:20:27'], ['0:23:21', '0:23:26'], ['0:30:20', '0:30:28'], ['0:34:14', '0:34:20'],
                    ['0:39:05', '0:39:15'], ['0:40:49', '0:41:00'], ['0:43:01', '0:43:10']]
    mar_13_arman = [['0:15:58', '0:16:05'], ['0:32:17', '0:33:20']]
    mar_16_arman = [['0:21:37', '0:21:40']]
    mar_18_arman = [['0:12:55', '0:13:13']]
    mar_19_arman = [['0:13:52', '0:13:58'], ['0:16:06', '0:16:20'], ['0:35:12', '0:35:20'], ['0:45:07', '0:47:15']]
    mar_25_arman = [['0:18:20', '0:18:29'], ['0:22:19', '0:23:29']]
    mar_27_arman = [['0:13:56', '0:13:59'], ['0:14:02', '0:14:04'], ['0:14:16', '0:14:28'], ['0:16:26', '0:16:37'],
                    ['0:20:50', '0:21:00'], ['0:43:55', '0:44:12']]
    mar_30_arman = [['0:13:53', '0:14:06'], ['0:14:45', '0:15:52'], ['0:22:38', '0:22:41'], ['0:27:52', '0:27:54']]
    apr_1_arman = [['0:12:20', '0:12:23'], ['0:14:31', '0:16:06'], ['0:17:38', '0:17:51'], ['0:28:00', '0:28:14'],
                   ['0:28:26', '0:28:35'], ['0:37:53', '0:37:56'], ['0:34:12', '0:34:15'], ['0:38:38', '0:38:40'],
                   ['0:38:59', '0:39:02']]
    apr_4_arman = [['0:11:54', '0:12:14'], ['0:16:11', '0:16:36'], ['0:19:43', '0:19:51'], ['0:20:10', '0:20:24'],
                   ['0:27:50', '0:27:53'], ['0:29:00', '0:29:02'], ['0:39:49', '0:39:52'], ['0:47:55', '0:48:10']]

    time_ranges1 = [['0:10:31', '0:10:41']]
    time_ranges2 = [['0:24:12', '0:24:22'], ['0:26:25', '0:26:39'], ['0:46:27', '0:46:43']]
    time_ranges3 = [['0:14:10', '0:14:17'], ['0:16:50', '0:16:55'], ['0:19:32', '0:19:38'], ['0:19:40', '0:19:46'],
                    ['0:28:30', '0:28:38'],
                    ['0:38:03', '0:38:10'], ['0:38:21', '0:38:25'], ['0:38:56', '0:39:06'], ['0:45:17', '0:45:23'],
                    ['0:45:43', '0:45:52'], ['0:49:05', '0:49:14']]
    time_ranges4 = [['0:16:08', '0:16:13'], ['0:17:38', '0:17:43'], ['0:18:58', '0:19:16'], ['0:27:21', '0:27:48'],
                    ['0:30:57', '0:31:10'], ['0:49:45', '0:49:54']]
    time_ranges5 = [['0:25:33', '0:25:44'], ['0:29:16', '0:29:17'], ['0:30:36', '0:30:40'], ['0:36:53', '0:37:11']]
    time_ranges6 = [['0:10:31', '0:10:39'], ['0:27:56', '0:28:00'], ['0:44:20', '0:44:24']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df2, time_ranges2, 12)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df5, time_ranges5, 15)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)

"""Occupied_Crosswalk, occupied_crosswalk"""
if scenario == 'occupied_crosswalk':
    mar_11_arman = [['0:14:03', '0:14:07'], ['0:30:54', '0:30:59'], ['0:40:34', '0:40:39']]
    mar_13_arman = [['0:05:23', '0:05:48'], ['0:09:41', '0:09:43'], ['0:36:41', '0:37:08'], ['0:50:49', '0:51:00']]
    mar_16_arman = [['0:09:51', '0:09:54'], ['0:45:06', '0:45:19']]
    mar_18_arman = [['0:05:21', '0:05:26'], ['0:05:39', '0:05:45'], ['0:06:22', '0:06:25'], ['0:08:31', '0:08:35']]
    mar_19_arman = [['0:11:02', '0:11:05'], ['0:11:44', '0:11:49'], ['1:01:28', '1:01:33']]
    mar_25_arman = [['0:15:49', '0:15:53'], ['0:24:28', '0:24:31']]
    mar_27_arman = [['0:44:20', '0:44:25'], ['0:50:56', '0:51:02']]
    mar_30_arman = [['0:07:13', '0:07:17'], ['0:07:56', '0:07:59'], ['0:43:27', '0:43:35']]
    apr_1_arman = [['0:07:50', '0:07:53'], ['0:09:05', '0:09:11'], ['0:11:48', '0:11:52'], ['0:48:32', '0:48:38']]

    time_ranges1 = [['0:17:00', '0:17:10'], ['0:17:21', '0:17:31']]
    time_ranges3 = [['0:17:12', '0:17:22'], ['0:22:23', '0:22:41'], ['0:24:24', '0:24:32'], ['0:52:37', '0:52:43']]
    time_ranges4 = [['0:12:32', '0:12:37'], ['0:22:31', '0:22:36'], ['0:33:46', '0:33:50'], ['0:36:36', '0:36:44'],
                    ['0:41:30', '0:41:35'], ['0:42:01', '0:42:06']]
    time_ranges5 = [['0:07:49', '0:08:00'], ['0:12:07', '0:12:14']]
    time_ranges6 = [['0:03:27', '0:03:31'], ['0:04:03', '0:04:11'], ['0:07:46', '0:07:51'], ['0:08:25', '0:08:33'],
                    ['0:17:21', '0:18:12'], ['0:42:35', '0:43:31'], ['0:44:20', '0:44:24'], ['0:44:54', '0:44:58']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df5, time_ranges5, 15)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)


"""Passing Bus, passing_bus"""
if scenario == 'passing_bus':
    mar_11_arman = [['0:30:18', '0:30:23']]
    mar_13_arman = [['0:08:58', '0:09:09']]
    mar_16_arman = [['0:40:50', '0:40:55']]
    mar_18_arman = [['0:12:25', '0:12:33'], ['0:51:38', '0:51:42'], ['1:03:56', '1:03:59']]
    mar_25_arman = [['0:36:19', '0:36:23'], ['0:48:55', '0:48:59']]
    mar_27_arman = [['0:04:45', '0:04:48']]
    mar_30_arman = [['0:51:25', '0:51:28']]
    apr_1_arman = [['0:05:38', '0:05:41'], ['0:05:55', '0:05:57'], ['0:14:16', '0:14:19'], ['0:20:29', '0:20:32']]
    apr_4_arman = [['0:39:48', '0:39:53'], ['0:42:46', '0:42:49'], ['0:44:15', '0:44:18']]

    time_ranges1 = [['0:14:01', '0:14:11'], ['0:18:14', '0:18:21'], ['0:58:02', '0:58:19']]
    time_ranges2 = [['0:31:41', '0:31:51']]
    time_ranges3 = [['0:28:00', '0:28:20'], ['0:29:08', '0:29:47'], ['0:53:44', '0:52:52']]
    time_ranges4 = [['0:06:34', '0:06:38'], ['0:09:44', '0:10:10'], ['0:11:23', '0:11:35'], ['0:48:26', '0:48:35']]
    time_ranges5 = [['0:05:13', '0:05:32'], ['0:16:30', '0:16:42'], ['0:40:06', '0:40:17']]
    time_ranges6 = [['0:08:25', '0:08:37']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df2, time_ranges2, 12)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df5, time_ranges5, 15)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)


"""Passing_Pedestrian, passing_pedestrian"""
if scenario == 'passing_pedestrian':
    mar_11_arman = [['0:10:11', '0:10:42'], ['0:15:38', '0:17:05'], ['0:50:39', '0:51:58']]
    mar_13_arman = [['0:02:44', '0:02:53'], ['0:21:50', '0:21:54'], ['0:22:54', '0:23:08'], ['0:23:16', '0:24:00'],
                    ['0:54:16', '0:54:20'], ['0:54:37', '0:54:40']]
    mar_16_arman = [['0:04:28', '0:04:32'], ['0:04:43', '0:04:49'], ['0:10:24', '0:10:36'], ['0:11:05', '0:11:13'],
                    ['0:12:10', '0:12:16'], ['0:13:46', '0:13:51'], ['0:48:16', '0:48:21']]
    mar_18_arman = [['0:02:44', '0:03:08'], ['0:07:59', '0:08:16'], ['0:26:18', '0:26:20'], ['0:27:15', '0:27:19'],
                    ['0:28:50', '0:28:53'], ['0:45:12', '0:45:18'], ['1:05:31', '1:05:35'],
                    ['1:05:52', '1:05:59'], ['1:06:10', '1:06:18'], ['1:06:38', '1:07:00'], ['1:07:28', '1:07:43']]
    mar_19_arman = [['0:06:16', '0:06:21'], ['0:06:28', '0:06:32'], ['0:39:05', '0:39:19'], ['0:45:34', '0:45:42'],
                    ['0:59:16', '0:59:20'], ['0:59:27', '0:59:30'], ['0:59:52', '0:59:58'], ['1:00:20', '1:00:24'],
                    ['1:01:48', '1:01:51']]
    mar_25_arman = [['0:03:32', '0:03:52'], ['0:08:03', '0:08:11'], ['0:08:17', '0:08:20'], ['0:10:44', '0:11:10'],
                    ['0:11:54', '0:11:58'], ['0:12:25', '0:12:34'], ['0:13:22', '0:13:25'], ['0:13:37', '0:13:40'],
                    ['0:14:29', '0:14:32'], ['0:14:38', '0:14:45'], ['0:49:18', '0:49:35'], ['0:50:32', '0:50:34'],
                    ['0:51:09', '0:51:20'], ['0:51:22', '0:51:28']]
    mar_27_arman = [['0:04:05', '0:04:30'], ['0:38:41', '0:38:51'], ['0:40:06', '0:40:11'], ['0:51:18', '0:53:18']]
    mar_30_arman = [['0:06:16', '0:06:19'], ['0:40:14', '0:40:20'], ['0:45:57', '0:46:02'], ['0:52:17', '0:52:20'],
                    ['0:52:27', '0:52:29']]
    apr_1_arman = [['0:04:03', '0:04:38'], ['0:24:49', '0:24:53'], ['0:43:27', '0:43:45'], ['0:49:12', '0:49:32'],
                    ['0:54:02', '0:54:16'], ['0:54:29', '0:54:34'], ['0:54:44', '0:55:04']]
    apr_4_arman = [['0:01:24', '0:01:27'], ['0:01:30', '0:01:32'], ['0:01:38', '0:01:40'], ['0:01:53', '0:01:55'],
                    ['0:36:17', '0:36:20'], ['0:49:28', '0:50:03'], ['0:50:12', '0:50:24']]

    time_ranges1 = [['0:10:48', '0:10:49']]
    time_ranges2 = [['0:39:29', '0:39:36'], ['0:52:35', '0:52:42']]
    time_ranges3 = [['0:42:50', '0:43:21'], ['0:54:14', '0:54:22']]
    time_ranges4 = [['0:03:18', '0:03:23'], ['0:37:18', '0:37:27'], ['0:37:30', '0:37:39'], ['0:37:48', '0:37:51'],
                    ['0:37:56', '0:37:58'], ['0:53:23', '0:53:54']]
    time_ranges5 = [['0:29:43', '0:29:56'], ['0:31:59', '0:32:19'], ['0:43:37', '0:44:21']]
    time_ranges6 = [['0:02:19', '0:02:53'], ['0:45:18', '0:45:25']]

    # Load dataframes
    df1_arman = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2_arman = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3_arman = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4_arman = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5_arman = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6_arman = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7_arman = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8_arman = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9_arman = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10_arman = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    df1 = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df1_arman, mar_11_arman, 1)
    filter_and_save_individual_dfs(df2_arman, mar_13_arman, 2)
    filter_and_save_individual_dfs(df3_arman, mar_16_arman, 3)
    filter_and_save_individual_dfs(df4_arman, mar_18_arman, 4)
    filter_and_save_individual_dfs(df5_arman, mar_19_arman, 5)
    filter_and_save_individual_dfs(df6_arman, mar_25_arman, 6)
    filter_and_save_individual_dfs(df7_arman, mar_27_arman, 7)
    filter_and_save_individual_dfs(df8_arman, mar_30_arman, 8)
    filter_and_save_individual_dfs(df9_arman, apr_1_arman, 9)
    filter_and_save_individual_dfs(df10_arman, apr_4_arman, 10)

    filter_and_save_individual_dfs(df1, time_ranges1, 11)
    filter_and_save_individual_dfs(df2, time_ranges2, 12)
    filter_and_save_individual_dfs(df3, time_ranges3, 13)
    filter_and_save_individual_dfs(df4, time_ranges4, 14)
    filter_and_save_individual_dfs(df5, time_ranges5, 15)
    filter_and_save_individual_dfs(df6, time_ranges6, 16)


