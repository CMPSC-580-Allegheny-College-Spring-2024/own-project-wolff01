import csv
import streamlit as st
import pandas as pd

def sum_csv(filename, start_row, end_row, start_col, end_col):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        
        start_row = max(0, min(start_row, len(data)-1))
        end_row = max(start_row, min(end_row, len(data)-1))
        
        start_col = max(0, min(start_col, len(data[0])-1))
        end_col = max(start_col, min(end_col, len(data[0])-1))
        
        sums = []
        for i in range(start_row, end_row + 1):
            row_sum = sum(float(data[i][j]) for j in range(start_col, end_col + 1))
            sums.append(row_sum)
        return sums

def multiply_csv(filename, start_row, end_row, start_col, end_col):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        
        start_row = max(0, min(start_row, len(data)-1))
        end_row = max(start_row, min(end_row, len(data)-1))
        
        start_col = max(0, min(start_col, len(data[0])-1))
        end_col = max(start_col, min(end_col, len(data[0])-1))
        
        products = []
        for i in range(start_row, end_row + 1):
                row_product = float(data[i][start_col]) * float(data[i][end_col])
                products.append(row_product)
        return products

def divide_csv(filename, start_row, end_row, start_col, end_col):
    sums = sum_csv(filename, start_row, end_row, start_col, end_col)
    products_1 = multiply_csv(filename, start_row, end_row, 3, 4)
    products_2 = multiply_csv(filename, start_row, end_row, 3, 5)
    
    division_results_1 = []
    division_results_2 = []
    for sum_val, prod_val in zip(sums, products_1):
        if sum_val != 0:
            division_results_2.append(prod_val / sum_val)
        else:
            division_results_2.append(float('NaN'))

    for sum_val, prod_val in zip(sums, products_2):
        if sum_val != 0:
            division_results_1.append(prod_val / sum_val)
        else:
            division_results_1.append(float('NaN'))

    column_names = [((res_1 * res_2)* 100)for res_1, res_2 in zip(division_results_1, division_results_2)]


    st.title("Perfect Timing")

    a = {'Names': csv_row_range(filename, 1, 135),'Swing Efficiency %': column_names}
    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()

    sort_column = st.selectbox('Select column to sort by:', df.columns)
    df_sorted = df.sort_values(by=sort_column, ascending=False)

    st.table(df_sorted)

def csv_row_range(filename, start_row_index, end_row_index):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        result = []
        for row_index in range(start_row_index, min(end_row_index + 1, len(rows))):
            result.append(rows[row_index][0])
        return result


divide_csv('data.csv', 1, 135, 6, 7)
