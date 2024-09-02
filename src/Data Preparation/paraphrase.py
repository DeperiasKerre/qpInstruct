# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:04:16 2024

@author: Deperias Kerre
"""
#open ai key intitialization
import openai
#openai.api_key = "REPLACE_WITH_YOUR_OPEN_AI_KEY"
#function to paraphrase with GPT 3
import csv
def paraphrase_sentences(sentences,output_file_path):
    paraphrased_sentences = []
    for sentence in sentences:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Including 5 examples for each sentence and without changing the meaning, please paraphrase the following sentence: '{sentence}'",
            max_tokens=400
        )
        paraphrased_sentence = response.choices[0].text.strip()
        paraphrased_sentences.append(paraphrased_sentence)
    
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Paraphrased Sentence'])
        for original, paraphrased in zip(sentences, paraphrased_sentences):
            writer.writerow([paraphrased])
    
    print(f"Paraphrased sentences saved to {output_file_path}")
#function extract sentences in batches of 4 from csv file. Important so as not parse huge tokens to GPT at once.
import pandas as pd

def extract_column_data(csv_file_path, column_name, start_row=None, end_row=None):
    # Read the CSV file using pandas
    data = pd.read_csv(csv_file_path)
    
    # Extract the specified column data
    column_data = data[column_name].tolist()
    
    # Remove header if start_row is not specified
    if start_row is None:
        column_data = column_data[1:]
    
    # Slice the column data based on the specified row ranges
    if start_row is not None:
        if end_row is not None:
            column_data = column_data[start_row:end_row]
        else:
            column_data = column_data[start_row:]
    
    return column_data
#extracting the sentences and parsing to a list. Sentences extracted in batches of 3 lines to avoid parsing excess tokens to GPT
f_path="C:/Users/USER/Documents/Projects/sentences_original.csv"
column_name = 'sentence'
start_row = 0
end_row = 3
column_data = extract_column_data(f_path, column_name, start_row, end_row)
#print(column_data)
#parsing the extracted sentences to GPT for paraphrasing
sentences=column_data
csv_output_file = "C:/Users/USER/Documents/Projects/paraphrased sentences/para_sentences1.csv"
paraphrase_sentences(sentences,csv_output_file)
