import pandas as pd

def move_rows_to_new_table(source_file, target_file, row_indices, source_sheet=0, target_sheet='NewTable', column_name='MovedData'):
    # Load the source Excel file
    source_df = pd.read_excel(source_file, sheet_name=source_sheet)

    # Select specific rows
    selected_rows = source_df.iloc[row_indices]

    # Extract data for the new column
    new_column_data = selected_rows.apply(lambda row: ' | '.join(map(str, row.values)), axis=1)

    # Create a new DataFrame for the target column
    target_df = pd.DataFrame({column_name: new_column_data})

    # Write the new DataFrame to a new sheet in the target Excel file
    with pd.ExcelWriter(target_file, engine='openpyxl', mode='a') as writer:
        target_df.to_excel(writer, sheet_name=target_sheet, index=False)

    print(f"Moved {len(row_indices)} rows to '{target_sheet}' in '{target_file}'.")

# Example usage
move_rows_to_new_table(
    source_file='source.xlsx',
    target_file='target.xlsx',
    row_indices=[0, 2, 5],  # Specify the rows to move
    source_sheet='Sheet1',
    target_sheet='ProcessedData',
    column_name='ExtractedInfo'
)