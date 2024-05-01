import csv

def sum_csv_part(filename, start_row, end_row, start_col, end_col):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        
        # Ensure start_row and end_row are within the range of rows
        start_row = max(0, min(start_row, len(data)-1))
        end_row = max(start_row, min(end_row, len(data)-1))
        
        # Ensure start_col and end_col are within the range of columns
        start_col = max(0, min(start_col, len(data[0])-1))
        end_col = max(start_col, min(end_col, len(data[0])-1))
        
        for i in range(start_row, end_row + 1):
            row_sum = 0  # Initialize sum variable for each row
            for j in range(start_col, end_col + 1):
                try:
                    row_sum += float(data[i][j])  # Accumulate values for each row
                except ValueError:
                    print("ValueError: Invalid literal for float():", data[i][j])
            print("Sum of values in row", i+1, ":", row_sum)

def multiply_csv_part(filename, start_row, end_row, start_col, end_col):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        
        # Ensure start_row and end_row are within the range of rows
        start_row = max(0, min(start_row, len(data)-1))
        end_row = max(start_row, min(end_row, len(data)-1))
        
        # Ensure start_col and end_col are within the range of columns
        start_col = max(0, min(start_col, len(data[0])-1))
        end_col = max(start_col, min(end_col, len(data[0])-1))
        
        for i in range(start_row, end_row + 1):
            row_product = 1  # Initialize product variable for each row as 1
            for j in range(start_col, end_col + 1):
                try:
                    row_product *= float(data[i][j])  # Accumulate values for each row
                except ValueError:
                    print("ValueError: Invalid literal for float():", data[i][j])
            print("Product of values in row", i+1, ":", row_product)

sum_csv_part('data.csv', 1, 3, 6, 7)
multiply_csv_part('data.csv', 1, 3, 3, 4)