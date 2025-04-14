import tkinter as tk
from tkinter import filedialog, simpledialog
import pandas as pd

# Import pandas & openpyxl

def select_file(prompt):
    return filedialog.askopenfilename(title=prompt, filetypes=[("Excel files", "*.xlsx;*.xls")])

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

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    source_file = select_file("Select Source Excel File")
    target_file = select_file("Select Target Excel File")

    if not source_file or not target_file:
        print("File selection canceled.")
        return

    row_indices_str = simpledialog.askstring("Row Indices", "Enter row indices (comma-separated):")
    row_indices = list(map(int, row_indices_str.split(',')))

    source_sheet = simpledialog.askstring("Source Sheet", "Enter source sheet name (or leave blank for first sheet):")
    target_sheet = simpledialog.askstring("Target Sheet", "Enter target sheet name:")
    column_name = simpledialog.askstring("Column Name", "Enter column name for the new data:")

    move_rows_to_new_table(
        source_file=source_file,
        target_file=target_file,
        row_indices=row_indices,
        source_sheet=source_sheet if source_sheet else 0,
        target_sheet=target_sheet,
        column_name=column_name
    )

if __name__ == "__main__":
    main()
