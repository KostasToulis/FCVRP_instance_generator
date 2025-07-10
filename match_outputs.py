# I have two csv files, the new_instance_results.csv and the output.csv. I want to open them both in dataframes with two columns; the first column is the instance name and the second is the score. I want to match the instances of output to the first file and save its scores into a new column in the new_instance_results file.
import pandas as pd

def match_outputs(new_instance_file, output_file, output_column_name='Score'):
    # Load the dataframes
    new_instance_df = pd.read_csv(new_instance_file, header=None, names=['Instance', 'Score'])
    new_instance_df.reset_index(drop=True, inplace=True)
    output_df = pd.read_csv(output_file, header=None, names=['Instance', 'Score'])

    # Ensure both dataframes have the correct columns
    if 'Instance' not in new_instance_df.columns or 'Score' not in output_df.columns:
        raise ValueError("DataFrames must contain 'Instance' and 'Score' columns.")

    print(new_instance_df.head())
    print(output_df.head())

    # Merge the dataframes on the 'Instance' column
    merged_df = pd.merge(new_instance_df, output_df, on='Instance', how='left')

    # Rename the score column from output_df to the specified name
    merged_df.rename(columns={'Score_y': output_column_name}, inplace=True)

    # Drop the original score column from new_instance_df if it exists
    if 'Score_x' in merged_df.columns:
        merged_df.drop(columns=['Score_x'], inplace=True)

    return merged_df

merged_df = match_outputs('new_instance_results.csv', 'output.csv')
merged_df.to_csv('matched_results.csv', index=False)