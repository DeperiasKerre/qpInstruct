# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:27:35 2024

@author: Deperias Kerre
"""
#import pandas
import pandas as pd
# Read the input CSV file
input_file = "C:/Users/USER/Documents/Projects/Instruction Dataset/merged_data.csv"
data = pd.read_csv(input_file)

# Shuffle the rows
shuffled_data = data.sample(frac=1).reset_index(drop=True)

# Save the shuffled data to another CSV file
output_file = "C:/Users/USER/Documents/Projects/Instruction Dataset/instruction_dataset.csv"
shuffled_data.to_csv(output_file, index=False)
