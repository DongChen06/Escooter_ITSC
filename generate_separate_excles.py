import pandas as pd
import os


# Function to convert HH:MM:SS to microseconds
def time_to_microseconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return ((h * 3600) + (m * 60) + s) * 1e6


# Function to check if a time is within a specific range
def is_time_in_range(start_us, end_us, time):
    return start_us <= time <= end_us


senario = 'roadwobikelane'  # 'walkways', 'sidewalk', 'roadwbikelane', 'roadwobikelane'

if senario == 'roadwobikelane':
    folder_name = 'Separate_excels/roadwobikelane'
elif senario == 'sidewalk':
    folder_name = 'Separate_excels/sidewalk'
elif senario == 'walkways':
    folder_name = 'Separate_excels/walkways'
elif senario == 'roadwbikelane':
    folder_name = 'Separate_excels/roadwbikelane'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


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


"""Road w. Bike Lane, roadwbikelane"""
if senario == 'roadwbikelane':
    dec_11_arik = [['0:20:12', '0:20:20'], ['0:21:07', '0:21:44'], ['0:22:08', '0:24:03'], ['0:27:47', '0:28:39'],
                   ['0:29:31', '0:29:41'], ['0:31:45', '0:34:41'], ['0:34:00', '0:34:41'], ['0:37:59', '0:38:30'],
                   ['0:39:41', '0:40:00'], ['0:49:14', '0:49:55'], ['0:50:18', '0:50:43'], ['0:52:09', '0:52:41'],
                   ['0:52:58', '0:55:13'], ['0:55:31', '0:55:42'], ['0:56:40', '0:57:22'], ['0:58:05', '0:58:31'],
                   ['1:01:02', '1:01:33']]
    dec_14_arik = [['0:10:34', '0:11:24'], ['0:12:00', '0:13:40'], ['0:14:34', '0:14:42'], ['0:15:26', '0:17:45'],
                   ['0:19:00', '0:19:18'], ['0:20:00', '0:20:07'], ['0:23:11', '0:24:56'], ['0:28:36', '0:28:56'],
                   ['0:30:21', '0:31:06'], ['0:34:28', '0:34:55'], ['0:38:21', '0:39:14'], ['0:49:13', '0:49:58'],
                   ['0:50:22', '0:50:27']]
    dec_20_arik = [['0:06:11', '0:06:20'], ['0:08:46', '0:10:27'], ['0:12:06', '0:11:34'], ['0:13:08', '0:14:50'],
                   ['0:14:54', '0:15:04'], ['0:18:59', '0:20:00'], ['0:21:58', '0:22:12'], ['0:26:14', '0:26:23'],
                   ['0:27:27', '0:28:19'], ['0:28:41', '0:29:07'], ['0:35:47', '0:35:58'], ['0:37:00', '0:38:47'],
                   ['0:44:52', '0:46:55'], ['0:47:30', '0:48:07']]
    feb_13_arik = [['0:05:32', '0:06:00'], ['0:08:48', '0:10:22'], ['0:14:20', '0:14:55'], ['0:15:41', '0:16:17'],
                   ['0:16:40', '0:16:55'], ['0:17:21', '0:17:25'], ['0:19:03', '0:19:43'], ['0:21:39', '0:22:26'],
                   ['0:28:55', '0:29:26'], ['0:32:44', '0:33:10'], ['0:33:37', '0:34:00'], ['0:35:17', '0:35:36'],
                   ['0:36:18', '0:36:57'], ['0:37:21', '0:37:28'], ['0:38:01', '0:38:26'], ['0:41:52', '0:42:23']]
    feb_16_arik = [['0:10:01', '0:10:45'], ['0:38:45', '0:39:02'], ['0:42:41', '0:42:46']]
    jan_25_arik = [['0:05:37', '0:06:17'], ['0:06:39', '0:06:51'], ['0:07:12', '0:07:20'], ['0:08:40', '0:09:50'],
                   ['0:10:12', '0:11:53'], ['0:13:18', '0:13:30'], ['0:15:53', '0:18:05'], ['0:18:13', '0:18:49'],
                   ['0:24:04', '0:24:28'], ['0:26:50', '0:27:06'], ['0:27:18', '0:28:34'], ['0:28:46', '0:29:35'],
                   ['0:29:44', '0:31:10'], ['0:39:26', '0:39:22'], ['0:40:15', '0:40:20'], ['0:41:19', '0:42:15'],
                   ['0:48:26', '0:48:45'], ['0:51:08', '0:51:39']]

    time_ranges1 = [['0:18:00', '0:18:12'], ['0:19:32', '0:21:30'], ['0:29:54', '0:30:45'], ['0:33:58', '0:34:20'],
                    ['0:34:46', '0:35:05'], ['0:35:50', '0:36:41'], ['0:37:34', '0:38:15'], ['0:42:16', '0:43:13'],
                    ['0:43:25', '0:44:50'], ['0:47:00', '0:47:07'], ['0:50:07', '0:50:20']]
    time_ranges2 = [['0:10:36', '0:10:49'], ['0:14:25', '0:14:40'], ['0:16:38', '0:18:45'], ['0:19:35', '0:21:00'],
                    ['0:28:03', '0:28:26'], ['0:40:12', '0:41:30'], ['0:42:00', '0:42:50']]
    time_ranges3 = [['0:12:16', '0:14:02'], ['0:47:50', '0:52:18'], ['0:53:50', '0:53:57']]
    time_ranges4 = [['0:10:20', '0:10:28'], ['0:12:08', '0:14:18'], ['0:20:15', '0:22:46'], ['1:02:55', '1:03:30']]
    time_ranges5 = [['0:13:45', '0:14:00'], ['0:15:46', '0:19:30'], ['0:22:41', '0:24:21'], ['0:25:20', '0:27:00'],
                    ['0:29:03', '0:30:22'], ['0:31:42', '0:35:41'], ['0:41:12', '0:42:20'], ['0:42:37', '0:44:18'],
                    ['0:45:42', '0:47:37'], ['0:57:15', '0:58:15'], ['1:00:41', '1:00:48']]
    time_ranges6 = [['0:12:12', '0:12:26'], ['0:14:34', '0:18:55'], ['0:27:10', '0:28:26'], ['0:29:10', '0:31:16'],
                    ['0:31:38', '0:32:31'], ['0:34:40', '0:36:40'], ['0:36:46', '0:39:02'], ['0:40:35', '0:41:24'],
                    ['0:47:13', '0:47:19'], ['0:48:10', '0:48:51'], ['0:51:39', '0:51:48'], ['0:53:13', '0:53:35']]
    time_ranges7 = [['0:18:19', '0:18:30'], ['0:22:07', '0:23:30'], ['0:24:06', '0:25:03'], ['0:26:04', '0:26:18'],
                    ['0:28:11', '0:33:10'], ['0:33:45', '0:34:06'], ['0:38:35', '0:40:49'], ['0:43:05', '0:44:46'],
                    ['0:45:30', '0:47:30'], ['0:50:05', '0:50:11']]
    time_ranges8 = [['0:11:36', '0:11:47'], ['0:12:37', '0:14:27'], ['0:18:10', '0:18:19'], ['0:33:00', '0:34:25'],
                    ['0:35:27', '0:36:12'], ['0:36:33', '0:36:56'], ['0:44:06', '0:44:15'], ['0:45:40', '0:46:28'],
                    ['0:49:11', '0:49:53'], ['0:50:30', '0:50:44']]
    time_ranges9 = [['0:13:36', '0:14:08'], ['0:12:24', '0:12:33'], ['0:14:33', '0:14:54'], ['0:15:02', '0:17:52'],
                    ['0:17:27', '0:17:53'], ['0:22:03', '0:25:56'], ['0:26:50', '0:29:02'], ['0:31:01', '0:33:38'],
                    ['0:34:00', '0:35:17'], ['0:36:56', '0:37:48'], ['0:38:07', '0:38:40'], ['0:49:50', '0:51:46']]
    time_ranges10 = [['0:09:35', '0:09:59'], ['0:11:14', '0:12:59'], ['0:13:34', '0:14:16'], ['0:14:28', '0:14:33'],
                     ['0:14:51', '0:14:55'], ['0:16:06', '0:16:36'], ['0:17:33', '0:17:50'], ['0:19:01', '0:20:30'],
                     ['0:27:03', '0:29:27'], ['0:29:52', '0:32:09'], ['0:34:01', '0:35:17'], ['0:43:18', '0:43:39'],
                     ['0:44:59', '0:45:38'], ['0:45:51', '0:46:08'], ['0:47:04', '0:48:04'], ['0:48:32', '0:48:54']]

    # Load dataframes
    df_dec_11_arik = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df_dec_14_arik = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df_dec_20_arik = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df_feb_13_arik = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df_feb_16_arik = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')
    df_jan_25_arik = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df1 = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7 = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8 = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9 = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10 = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df_dec_11_arik, dec_11_arik, 11)
    filter_and_save_individual_dfs(df_dec_14_arik, dec_14_arik, 12)
    filter_and_save_individual_dfs(df_dec_20_arik, dec_20_arik, 13)
    filter_and_save_individual_dfs(df_feb_13_arik, feb_13_arik, 14)
    filter_and_save_individual_dfs(df_feb_16_arik, feb_16_arik, 15)
    filter_and_save_individual_dfs(df_jan_25_arik, jan_25_arik, 16)

    filter_and_save_individual_dfs(df1, time_ranges1, 1)
    filter_and_save_individual_dfs(df2, time_ranges2, 2)
    filter_and_save_individual_dfs(df3, time_ranges3, 3)
    filter_and_save_individual_dfs(df4, time_ranges4, 4)
    filter_and_save_individual_dfs(df5, time_ranges5, 5)
    filter_and_save_individual_dfs(df6, time_ranges6, 6)
    filter_and_save_individual_dfs(df7, time_ranges7, 7)
    filter_and_save_individual_dfs(df8, time_ranges8, 8)
    filter_and_save_individual_dfs(df9, time_ranges9, 9)
    filter_and_save_individual_dfs(df10, time_ranges10, 10)

"""Sidewalk, sidewalk"""
if senario == 'sidewalk':
    dec_11_arik = [['0:10:44', '0:11:00'], ['1:01:39', '1:01:44'], ['1:02:08', '1:02:34'], ['1:02:52', '1:03:15']]
    dec_14_arik = [['0:09:15', '0:09:32'], ['0:09:54', '0:10:03'], ['0:39:15', '0:39:38'], ['0:44:45', '0:45:04']]
    dec_20_arik = [['0:11:38', '0:12:51'], ['0:50:57', '0:51:04']]
    feb_13_arik = [['0:03:25', '0:03:44'], ['0:15:20', '0:15:38'], ['0:22:45', '0:22:56'], ['0:29:44', '0:29:56'],
                   ['0:35:57', '0:36:15'], ['0:42:33', '0:42:41'], ['0:43:08', '0:43:53']]
    feb_16_arik = [['0:18:45', '0:19:00']]
    jan_25_arik = [['0:03:38', '0:03:54'], ['0:06:53', '0:06:59'], ['0:07:47', '0:07:58'], ['0:12:51', '0:13:04']]

    time_ranges1 = [['0:15:20', '0:15:30'], ['0:44:50', '0:45:06'], ['0:50:50', '0:51:03']]
    time_ranges2 = [['0:26:07', '0:26:27']]
    time_ranges3 = [['0:10:10', '0:11:15'], ['0:38:03', '0:39:12'], ['0:39:33', '0:40:23'], ['0:41:01', '0:41:46'],
                    ['0:53:08', '0:53:25'], ['0:53:31', '0:53:46']]
    time_ranges4 = [['0:02:33', '0:03:10'], ['0:07:57', '0:08:18'], ['0:16:55', '0:17:25'], ['0:17:33', '0:17:57'],
                    ['0:20:07', '0:20:15'], ['0:24:15', '0:24:41'], ['0:24:42', '0:24:48'], ['0:24:50', '0:25:15'],
                    ['0:25:49', '0:26:05'], ['0:29:55', '0:30:21'], ['0:30:26', '0:30:40'], ['0:41:16', '0:41:53'],
                    ['0:42:31', '0:42:54'], ['0:43:00', '0:46:23'], ['0:51:05', '0:52:30'], ['0:52:54', '0:53:55'],
                    ['0:55:34', '0:56:12'], ['0:58:27', '0:59:00'], ['1:03:53', '1:04:25'], ['1:05:20', '1:05:55'],
                    ['1:06:09', '1:08:00']]
    time_ranges5 = [['0:06:06', '0:06:39'], ['0:24:21', '0:25:20'], ['0:30:22', '0:30:58'], ['0:35:47', '0:38:12'],
                    ['0:38:20', '0:39:25'], ['0:44:18', '0:44:44'], ['0:49:22', '0:49:40'], ['0:51:26', '0:52:35'],
                    ['0:54:28', '0:55:02'], ['0:59:21', '1:00:41'], ['1:01:36', '1:02:05']]
    time_ranges6 = [['0:20:11', '0:20:33'], ['0:20:39', '0:21:42'], ['0:22:40', '0:25:13'], ['0:25:19', '0:27:05'],
                    ['0:39:25', '0:39:48'], ['0:43:11', '0:43:44'], ['0:44:29', '0:44:42'], ['0:54:05', '0:54:16']]
    time_ranges7 = [['0:11:12', '0:11:27'], ['0:12:28', '0:12:51'], ['0:14:26', '0:14:38'], ['0:33:15', '0:33:36'],
                    ['0:35:28', '0:36:04'], ['0:36:14', '0:37:25'], ['0:37:48', '0:38:21'], ['0:47:51', '0:48:02'],
                    ['0:49:08', '0:49:39']]
    time_ranges8 = [['0:17:09', '0:17:26'], ['0:17:31', '0:18:02'], ['0:19:22', '0:20:10'], ['0:25:40', '0:25:55'],
                    ['0:27:06', '0:27:52'], ['0:34:55', '0:35:20'], ['0:38:40', '0:38:54'], ['0:51:26', '0:51:42']]
    time_ranges9 = [['0:19:08', '0:19:23'], ['0:20:15', '0:21:25'], ['0:39:18', '0:39:42'], ['0:40:04', '0:40:20'],
                    ['0:44:04', '0:44:25'], ['0:45:36', '0:46:10'], ['0:46:27', '0:47:47'], ['0:52:19', '0:52:25']]
    time_ranges10 = [['0:01:46', '0:02:02'], ['0:20:33', '0:21:44'], ['0:22:17', '0:23:49'], ['0:23:53', '0:25:03'],
                     ['0:25:31', '0:27:00'], ['0:35:20', '0:37:26'], ['0:49:33', '0:49:40']]

    # Load dataframes
    df_dec_11_arik = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df_dec_14_arik = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df_dec_20_arik = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df_feb_13_arik = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df_feb_16_arik = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')
    df_jan_25_arik = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df1 = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7 = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8 = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9 = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10 = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df_dec_11_arik, dec_11_arik, 11)
    filter_and_save_individual_dfs(df_dec_14_arik, dec_14_arik, 12)
    filter_and_save_individual_dfs(df_dec_20_arik, dec_20_arik, 13)
    filter_and_save_individual_dfs(df_feb_13_arik, feb_13_arik, 14)
    filter_and_save_individual_dfs(df_feb_16_arik, feb_16_arik, 15)
    filter_and_save_individual_dfs(df_jan_25_arik, jan_25_arik, 16)

    filter_and_save_individual_dfs(df1, time_ranges1, 1)
    filter_and_save_individual_dfs(df2, time_ranges2, 2)
    filter_and_save_individual_dfs(df3, time_ranges3, 3)
    filter_and_save_individual_dfs(df4, time_ranges4, 4)
    filter_and_save_individual_dfs(df5, time_ranges5, 5)
    filter_and_save_individual_dfs(df6, time_ranges6, 6)
    filter_and_save_individual_dfs(df7, time_ranges7, 7)
    filter_and_save_individual_dfs(df8, time_ranges8, 8)
    filter_and_save_individual_dfs(df9, time_ranges9, 9)
    filter_and_save_individual_dfs(df10, time_ranges10, 10)

"""No bike lane, roadwobikelane"""
if senario == 'roadwobikelane':
    dec_11_arik = [['0:11:13', '0:12:55'], ['0:13:10', '0:20:10'], ['0:20:28', '0:20:57'], ['0:24:58', '0:27:47'], ['0:28:51', '0:29:30'],
                   ['0:29:45', '0:30:06'], ['0:31:07', '0:31:22'], ['0:34:42', '0:33:58'], ['0:34:43', '0:36:49'], ['0:37:40', '0:37:58'],
                   ['0:38:31', '0:38:40'], ['0:40:01', '0:45:21'], ['0:45:48', '0:47:16'], ['0:47:38', '0:49:07'], ['0:49:56', '0:50:10'],
                   ['0:50:45', '0:52:08'], ['0:57:24', '0:58:04'], ['1:00:16', '1:01:01'], ['1:01:53', '1:02:07'], ['1:02:35', '1:02:50']]
    dec_14_arik = [['0:09:36', '0:09:50'], ['0:11:26', '0:11:59'], ['0:13:41', '0:14:32'], ['0:14:42', '0:15:10'], ['0:17:47', '0:18:59'],
                   ['0:19:21', '0:20:00'], ['0:20:09', '0:21:35'], ['0:22:16', '0:22:24'], ['0:24:56', '0:25:06'], ['0:25:14', '0:26:05'],
                   ['0:26:21', '0:28:36'], ['0:28:59', '0:30:20'], ['0:31:17', '0:34:28'], ['0:34:56', '0:36:16'], ['0:36:51', '0:38:01'],
                   ['0:39:40', '0:44:40'], ['0:45:12', '0:47:22'], ['0:48:11', '0:49:12'], ['0:50:50', '0:50:20'], ['0:50:28', '0:51:09'],
                   ['0:51:26', '0:52:15']]
    dec_20_arik = [['0:04:37', '0:05:29'], ['0:05:40', '0:06:10'], ['0:06:23', '0:07:49'], ['0:08:25', '0:08:45'], ['0:010:28', '0:11:24'],
                   ['0:11:32', '0:11:54'], ['0:16:34', '0:18:50'], ['0:20:01', '0:20:34'], ['0:21:48', '0:21:55'], ['0:22:15', '0:22:25'],
                   ['0:22:59', '0:24:14'], ['0:24:34', '0:26:12'], ['0:26:26', '0:26:52'], ['0:27:37', '0:27:52'], ['0:28:22', '0:28:29'],
                   ['0:27:38', '0:29:55'], ['0:30:22', '0:30:41'], ['0:32:05', '0:33:14'], ['0:34:03', '0:34:55'], ['0:35:10', '0:35:45'],
                   ['0:38:49', '0:41:43'], ['0:42:15', '0:42:38'], ['0:43:55', '0:44:07'], ['0:48:50', '0:49:50'], ['0:50:40', '0:50:54'],
                   ['0:51:08', '0:51:43'], ['0:52:19', '0:54:07']]
    feb_13_arik = [['0:03:53', '0:05:17'], ['0:06:08', '0:08:47'], ['0:10:24', '0:13:44'], ['0:14:56', '0:15:19'], ['0:16:18', '0:16:38'],
                   ['0:17:25', '0:17:47'], ['0:18:12', '0:19:01'], ['0:22:57', '0:23:17'], ['0:23:53', '0:25:14'], ['0:27:20', '0:28:52'],
                   ['0:30:22', '0:31:00'], ['0:31:18', '0:32:42'], ['0:34:03', '0:35:16'], ['0:35:36', '0:35:57'], ['0:36:57', '0:37:10'],
                   ['0:38:27', '0:39:29'], ['0:39:41', '0:40:05'], ['0:40:30', '0:41:50'], ['0:42:52', '0:43:05']]
    feb_16_arik = [['0:02:55', '0:04:34'], ['0:05:17', '0:08:50'], ['0:09:50', '0:10:00'], ['0:11:06', '0:18:06'], ['0:19:01', '0:28:36'],
                   ['0:28:59', '0:33:13'], ['0:33:45', '0:38:37'], ['0:39:03', '0:42:41'], ['0:42:47', '0:44:53']]
    jan_25_arik = [['0:04:08', '0:04:42'], ['0:07:22', '0:07:39'], ['0:08:10', '0:08:35'], ['0:11:55', '0:12:50'], ['0:13:09', '0:13:17'],
                   ['0:13:32', '0:14:27'], ['0:18:50', '0:20:33'], ['0:20:53', '0:24:03'], ['0:24:29', '0:25:50'], ['0:28:35', '0:28:45'],
                   ['0:29:36', '0:29:42'], ['0:31:14', '0:32:57'], ['0:33:26', '0:37:34'], ['0:37:46', '0:38:23'], ['0:42:16', '0:46:13'],
                   ['0:47:19', '0:48:25'], ['0:50:23', '0:51:07'], ['0:50:21', '0:53:17']]

    time_ranges1 = [['0:10:43', '0:15:20'], ['0:17:20', '0:18:00'], ['0:18:14', '0:18:39'], ['0:19:20', '0:19:32'],
                    ['0:21:30', '0:23:20'], ['0:24:35', '0:28:40'], ['0:35:05', '0:35:50'], ['0:38:31', '0:42:16'],
                    ['0:46:22', '0:46:58'], ['0:47:20', '0:49:25'], ['0:50:20', '0:50:33']]
    time_ranges2 = [['0:03:08', '0:10:36'], ['0:11:25', '0:14:22'], ['0:14:52', '0:16:38'], ['0:18:45', '0:19:35'],
                    ['0:21:15', '0:21:49'], ['0:24:41', '0:26:05'], ['0:26:32', '0:26:58'], ['0:27:24', '0:28:03'],
                    ['0:28:30', '0:40:12'], ['0:41:31', '0:41:58'], ['0:42:50', '0:47:17'], ['0:48:00', '0:50:48'],
                    ['0:52:12', '0:54:05']]
    time_ranges3 = [['0:04:52', '0:10:10'], ['0:14:02', '0:25:40'], ['0:29:12', '0:36:25'], ['0:42:10', '0:47:50'],
                    ['0:53:57', '0:54:48']]
    time_ranges4 = [['0:03:12', '0:07:41'], ['0:08:19', '0:10:20'], ['0:10:29', '0:12:08'], ['0:14:19', '0:16:55'],
                    ['0:31:30', '0:32:27'], ['0:59:00', '1:02:55'], ['1:03:30', '1:03:50'], ['1:04:30', '1:04:57']]
    time_ranges5 = [['0:06:40', '0:13:45'], ['0:14:00', '0:15:43'], ['0:19:30', '0:22:41'], ['0:27:00', '0:27:11'],
                    ['0:42:22', '0:42:37'], ['0:49:40', '0:50:44'], ['0:52:35', '0:53:30'], ['0:54:00', '0:54:28'],
                    ['0:55:02', '0:56:55'], ['0:58:22', '0:58:44'], ['1:00:48', '1:01:36']]
    time_ranges6 = [['0:04:40', '0:09:40'], ['0:10:52', '0:12:11'], ['0:12:42', '0:13:24'], ['0:14:13', '0:14:32'],
                    ['0:19:00', '0:20:00'], ['0:29:00', '0:29:10'], ['0:32:32', '0:34:40'], ['0:36:40', '0:36:45'],
                    ['0:39:03', '0:39:23'], ['0:41:25', '0:42:01'], ['0:42:34', '0:43:10'], ['0:44:15', '0:44:26'],
                    ['0:44:58', '0:45:10'], ['0:45:41', '0:47:12'], ['0:47:47', '0:48:08'], ['0:52:54', '0:53:12'],
                    ['0:53:36', '0:53:45']]
    time_ranges7 = [['0:03:53', '0:07:55'], ['0:11:36', '0:12:21'], ['0:14:45', '0:18:18'], ['0:18:37', '0:18:52'],
                    ['0:20:04', '0:20:30'], ['0:21:40', '0:22:04'], ['0:25:10', '0:26:01'], ['0:26:26', '0:28:10'],
                    ['0:40:58', '0:43:04'], ['0:47:32', '0:47:50'], ['0:50:12', '0:50:56']]
    time_ranges8 = [['0:04:33', '0:09:12'], ['0:10:22', '0:11:35'], ['0:12:10', '0:12:30'], ['0:15:16', '0:17:08'],
                    ['0:18:20', '0:19:21'], ['0:20:15', '0:20:34'], ['0:21:37', '0:23:05'], ['0:27:57', '0:32:35'],
                    ['0:32:48', '0:32:57'], ['0:34:25', '0:34:48'], ['0:36:13', '0:36:32'], ['0:37:11', '0:37:30'],
                    ['0:38:05', '0:38:39'], ['0:40:14', '0:40:42'], ['0:40:47', '0:41:09'], ['0:41:32', '0:44:05'],
                    ['0:45:16', '0:45:39'], ['0:49:54', '0:50:28'], ['0:50:45', '0:50:56']]
    time_ranges9 = [['0:06:36', '0:12:22'], ['0:12:37', '0:13:01'], ['0:13:26', '0:13:35'], ['0:17:57', '0:18:44'],
                    ['0:19:45', '0:20:10'], ['0:26:12', '0:26:19'], ['0:29:03', '0:31:00'], ['0:35:18', '0:35:47'],
                    ['0:37:50', '0:38:06'], ['0:38:41', '0:39:17'], ['0:39:50', '0:40:00'], ['0:42:05', '0:44:00'],
                    ['0:51:54', '0:52:00']]
    time_ranges10 = [['0:02:15', '0:09:34'], ['0:10:00', '0:10:39'], ['0:13:00', '0:13:25'], ['0:14:16', '0:14:28'],
                     ['0:14:58', '0:15:13'], ['0:15:32', '0:16:04'], ['0:21:54', '0:22:09'], ['0:29:30', '0:29:51'],
                     ['0:32:10', '0:34:00'], ['0:38:31', '0:39:12'], ['0:39:26', '0:42:12'], ['0:42:44', '0:43:16'],
                     ['0:43:40', '0:44:58'], ['0:48:10', '0:48:31'], ['0:48:55', '0:49:06']]

    # Load dataframes
    df_dec_11_arik = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df_dec_14_arik = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df_dec_20_arik = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df_feb_13_arik = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df_feb_16_arik = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')
    df_jan_25_arik = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df1 = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df3 = pd.read_excel('Data/data_arman/16_Mar.xlsx', engine='openpyxl')
    df4 = pd.read_excel('Data/data_arman/18_Mar.xlsx', engine='openpyxl')
    df5 = pd.read_excel('Data/data_arman/19_Mar.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7 = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8 = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9 = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10 = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df_dec_11_arik, dec_11_arik, 11)
    filter_and_save_individual_dfs(df_dec_14_arik, dec_14_arik, 12)
    filter_and_save_individual_dfs(df_dec_20_arik, dec_20_arik, 13)
    filter_and_save_individual_dfs(df_feb_13_arik, feb_13_arik, 14)
    filter_and_save_individual_dfs(df_feb_16_arik, feb_16_arik, 15)
    filter_and_save_individual_dfs(df_jan_25_arik, jan_25_arik, 16)

    filter_and_save_individual_dfs(df1, time_ranges1, 1)
    filter_and_save_individual_dfs(df2, time_ranges2, 2)
    filter_and_save_individual_dfs(df3, time_ranges3, 3)
    filter_and_save_individual_dfs(df4, time_ranges4, 4)
    filter_and_save_individual_dfs(df5, time_ranges5, 5)
    filter_and_save_individual_dfs(df6, time_ranges6, 6)
    filter_and_save_individual_dfs(df7, time_ranges7, 7)
    filter_and_save_individual_dfs(df8, time_ranges8, 8)
    filter_and_save_individual_dfs(df9, time_ranges9, 9)
    filter_and_save_individual_dfs(df10, time_ranges10, 10)

"""Walkways, walkways"""
if senario == 'walkways':
    dec_11_arik = [['0:10:20', '0:10:43'], ['0:30:07', '0:30:41']]
    dec_14_arik = [['0:08:45', '0:09:14'], ['0:52:26', '0:52:50']]
    dec_20_arik = [['0:26:53', '0:27:37'], ['0:42:48', '0:43:45'], ['0:54:10', '0:54:57']]
    feb_13_arik = [['0:03:00', '0:03:24'], ['0:43:54', '0:44:22']]
    feb_16_arik = [['0:02:15', '0:02:53'], ['0:45:00', '0:45:35']]
    jan_25_arik = [['0:03:06', '0:03:37'], ['0:37:35', '0:37:45'], ['0:53:19', '0:53:53']]

    time_ranges1 = [['0:10:13', '0:10:40'], ['0:15:32', '0:17:15'], ['0:51:04', '0:52:06']]
    time_ranges2 = [['0:21:53', '0:24:35'], ['0:54:19', '0:54:50']]
    time_ranges6 = [['0:03:56', '0:04:36'], ['0:54:17', '0:55:18']]
    time_ranges7 = [['0:03:22', '0:03:52'], ['0:07:56', '0:08:42'], ['0:10:30', '0:11:12'], ['0:51:00', '0:51:36']]
    time_ranges8 = [['0:04:07', '0:04:31'], ['0:51:43', '0:53:20']]
    time_ranges9 = [['0:06:06', '0:06:33'], ['0:52:27', '0:53:06']]
    time_ranges10 = [['0:01:18', '0:01:41'], ['0:49:40', '0:50:30']]

    # Load dataframes
    df_dec_11_arik = pd.read_excel('Data/data_arik/time_ranges1.xlsx', engine='openpyxl')
    df_dec_14_arik = pd.read_excel('Data/data_arik/time_ranges2.xlsx', engine='openpyxl')
    df_dec_20_arik = pd.read_excel('Data/data_arik/time_ranges3.xlsx', engine='openpyxl')
    df_feb_13_arik = pd.read_excel('Data/data_arik/time_ranges5.xlsx', engine='openpyxl')
    df_feb_16_arik = pd.read_excel('Data/data_arik/time_ranges6.xlsx', engine='openpyxl')
    df_jan_25_arik = pd.read_excel('Data/data_arik/time_ranges4.xlsx', engine='openpyxl')
    df1 = pd.read_excel('Data/data_arman/11_Mar.xlsx', engine='openpyxl')
    df2 = pd.read_excel('Data/data_arman/15_Mar.xlsx', engine='openpyxl')
    df6 = pd.read_excel('Data/data_arman/1_Apr.xlsx', engine='openpyxl')
    df7 = pd.read_excel('Data/data_arman/25_Mar.xlsx', engine='openpyxl')
    df8 = pd.read_excel('Data/data_arman/27_Mar.xlsx', engine='openpyxl')
    df9 = pd.read_excel('Data/data_arman/30_Mar.xlsx', engine='openpyxl')
    df10 = pd.read_excel('Data/data_arman/4_Apr.xlsx', engine='openpyxl')

    # function for each DataFrame and its respective time ranges
    filter_and_save_individual_dfs(df_dec_11_arik, dec_11_arik, 11)
    filter_and_save_individual_dfs(df_dec_14_arik, dec_14_arik, 12)
    filter_and_save_individual_dfs(df_dec_20_arik, dec_20_arik, 13)
    filter_and_save_individual_dfs(df_feb_13_arik, feb_13_arik, 14)
    filter_and_save_individual_dfs(df_feb_16_arik, feb_16_arik, 15)
    filter_and_save_individual_dfs(df_jan_25_arik, jan_25_arik, 16)

    filter_and_save_individual_dfs(df1, time_ranges1, 1)
    filter_and_save_individual_dfs(df2, time_ranges2, 2)
    filter_and_save_individual_dfs(df6, time_ranges6, 6)
    filter_and_save_individual_dfs(df7, time_ranges7, 7)
    filter_and_save_individual_dfs(df8, time_ranges8, 8)
    filter_and_save_individual_dfs(df9, time_ranges9, 9)
    filter_and_save_individual_dfs(df10, time_ranges10, 10)
