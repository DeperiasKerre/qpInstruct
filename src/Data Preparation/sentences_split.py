# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:00:41 2024

@author: Deperias Kerre
"""
#Splitting generated sentences into separate rows
import csv

# Function to split the sentence and write to a new CSV file
def split_sentences(input_file, output_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        rows = []
        for row in reader:
            sentences = row[0].replace('. ', '.\n').split('\n')  # Split sentences based on full stops
            for sentence in sentences:
                rows.append([sentence])
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Input and output file paths
input_file = "C:/Users/USER/Documents/Projects/generated sentences/original sentences/gen_sentences3.csv"
output_file = "C:/Users/USER/Documents/Projects/generated sentences/splited sentences/gen_split3.csv"

# Call split_sentences function
split_sentences(input_file, output_file)

print('Sentence splitting is done! Check the output file:', output_file)
