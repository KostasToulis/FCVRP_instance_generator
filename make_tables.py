# I have a csv file named standard_config.csv with 4 columns: instance name, score, %gap, time. The csv is headless (now column line).
# I want to read this file and print its contents in the following way:
# {instance_name} & {score} & {gap} & {time} \\
import pandas as pd
def print_standard_config(file_path):
    # Read the CSV file without a header
    df = pd.read_csv(file_path, header=None, names=['Instance', 'Score', 'Gap', 'Time'])

    # Iterate through each row and print the formatted string
    for i in range(0, len(df), 2):
        row1 = df.iloc[i]
        row2 = df.iloc[i+1] if i+1 < len(df) else None
        line = f"{row1['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row1['Score'])} & {row1['Gap']} & {int(row1['Time']*0.75)}"
        if row2 is not None:
            line += f" & {row2['Instance'].replace('fcvrp_', '').replace('.txt', '').replace('_', '\\_')} & {int(row2['Score'])} & {row2['Gap']} & {int(row2['Time']*0.75)}"
        print(line + " \\\\")

print_standard_config('standard_config.csv')