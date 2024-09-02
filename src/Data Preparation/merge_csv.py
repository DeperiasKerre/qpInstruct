# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:26:14 2024

@author: Deperias Kerre
"""
#import libraries
import os
import csv

directory = "C:/Users/USER/Documents/Projects/csv files"

# Get list of all CSV files in the directory
files = [file for file in os.listdir(directory) if file.endswith('.csv')]

# Create a new CSV file to store merged data
with open('C:/Users/USER/Documents/Projects/csv files/merged_data.csv', 'w', newline='') as merged_file:
    writer = csv.writer(merged_file)
    
    # Loop through each CSV file
    for file in files:
        with open(os.path.join(directory, file), 'r') as csv_file:
            reader = csv.reader(csv_file)
            
            # Skip header rows
            next(reader, None)
            
            # Write data from each file to the merged file
            for row in reader:
                writer.writerow([row[0]])

print('Data has been successfully merged into merged_data.csv')
