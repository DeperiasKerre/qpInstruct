# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:51:57 2024

@author: Deperias Kerre
"""
##data preprocessing for llama 2 finetuning
import csv

def process_csv(input_file, output_file, start_string, end_string):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    # Add start and end strings to the first column
    for row in data[1:]:
        row[0] = start_string + row[0] + end_string
        
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print(f"CSV file processed and saved to {output_file}")

# Specify the input and output file names, start and end strings
input_file = "C:/Users/USER/Documents/Projects/Instruction Dataset/preprocessed_data/qcl_dataset.csv"
output_file = 'qcl_dataset.csv'
start_string = '### Instruction: '
end_string = '### Response:'

process_csv(input_file, output_file, start_string, end_string)
