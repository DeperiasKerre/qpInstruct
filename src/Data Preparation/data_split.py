# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 10:56:07 2024

@author: Deperias Kerre
"""
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the csv dataset
file_path="C:/Users/USER/Documents/Projects/Instruction Dataset/instruction_dataset_combined.csv"
data = pd.read_csv(file_path)

# Split the dataset into training and validation sets
train, val = train_test_split(data, test_size=0.2)

# Save the training and validation sets into separate csv files
train_data="C:/Users/USER/Documents/Projects/Instruction Dataset/training_data.csv"
validation_data="C:/Users/USER/Documents/Projects/Instruction Dataset/validation_data.csv"
train.to_csv(train_data, index=False)
val.to_csv(validation_data, index=False)

print("Training and validation datasets have been created successfully.")
