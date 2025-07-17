
# import pandas as pd
# def print_standard_config(file_path):
#     df = pd.read_csv(file_path, header=None, names=['Instance', 'Score', 'Previous', 'Gap', 'Time'])
#
#     for i in range(0, len(df), 2):
#         row1 = df.iloc[i]
#         row2 = df.iloc[i+1] if i+1 < len(df) else None
#         line = f"{row1['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row1['Score'])} & {int(row1['Previous'])} & {row1['Gap']} & {int(row1['Time']*0.75)}"
#         if row2 is not None:
#             line += f" & {row2['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row2['Score'])} & {int(row2['Previous'])} & {row2['Gap']} & {int(row2['Time']*0.75)}"
#         print(line + " \\\\")
#
# print_standard_config('standard_config.csv')

import pandas as pd

def print_grouped_and_sorted(file_path):
    # Read the CSV file without a header
    df = pd.read_csv(file_path, header=None, names=['Instance', 'Score', 'Previous', 'Gap', 'Time'])

    # Extract the grouping key and the sorting key
    df['GroupKey'] = df['Instance'].str.extract(r'fcvrp_([A-Za-z0-9-]+_\d+)_\d+_\d+')
    df['SortKey'] = df['Instance'].str[-5]

    # Group by the key and sort within each group
    grouped = df.groupby('GroupKey', sort=False)
    for group_key, group in grouped:
        sorted_group = group.sort_values(by='SortKey')
        for i in range(0, len(sorted_group), 2):
            row1 = sorted_group.iloc[i]
            row2 = sorted_group.iloc[i+1]
            line = f"& {row1['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row1['Score'])} & {int(row1['Previous'])} & {float(row1['Gap']):.1f} & {int(row1['Time'])}"
            # if row2 is not None:
            line += f" & {row2['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row2['Score'])} & {int(row1['Previous'])} & {float(row2['Gap']):.1f} & {int(row2['Time'])}"
            print(line + " \\\\")

print_grouped_and_sorted('standard_config.csv')