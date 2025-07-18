import pandas as pd
import os
import re

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
            line += f" & {row2['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row2['Score'])} & {int(row2['Previous'])} & {float(row2['Gap']):.1f} & {int(row2['Time'])}"
            print(line + " \\\\")

def print_light_config(file_path):
    # Read CSV without header and assign column names
    df = pd.read_csv(file_path, header=None, names=['Instance', 'BKS', 'Obj', '%Gap', 'T', 'ObjB', '%GapB', 'TB'])

    # Extract group key as before
    df['GroupKey'] = df['Instance'].str.extract(r'fcvrp_([A-Za-z0-9-]+_\d+)_\d+_\d+')
    df['SortKey'] = df['Instance'].str[-5]

    # Group by GroupKey
    grouped = df.groupby('GroupKey', sort=False)

    for group_key, group in grouped:
        sorted_group = group.sort_values(by='SortKey')
        for _, row in sorted_group.iterrows():
            line = (
                f"& {row['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} "
                f"& {int(row['BKS'])} & {int(row['Obj'])} & {float(row['%Gap']):.1f} & {int(row['T'])} "
                f"& {int(row['ObjB'])} & {float(row['%GapB']):.1f} & {int(row['TB'])} \\\\"
            )
            print(line)


def print_new_instances_best(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as f:
                first_line = f.readline().strip()
                score_match = re.search(r'Cost:\s*([0-9.]+)', first_line)
                score = float(score_match.group(1)) if score_match else None
                data.append({'Instance': filename, 'Score': score})

    df = pd.DataFrame(data)
    df['GroupKey'] = df['Instance'].str.extract(r'fcvrp_([A-Za-z0-9-]+_\d+)_\d+_\d+')
    df['SortKey'] = df['Instance'].str[-5]

    grouped = df.groupby('GroupKey', sort=False)
    for group_key, group in grouped:
        sorted_group = group.sort_values(by='SortKey')
        for i in range(0, len(sorted_group), 4):
            rows = sorted_group.iloc[i:i+4]
            line = ''
            for _, row in rows.iterrows():
                line += f"& {row['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row['Score'])} & "
            print(line.rstrip(' & ') + " \\\\")

print_new_instances_best('newInstances-best')

# print_grouped_and_sorted('standard_config.csv')
# print_light_config('light_configuration.csv')