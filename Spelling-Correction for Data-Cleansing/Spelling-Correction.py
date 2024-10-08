import pandas as pd
import re

def remove_repeated_characters(text):
    return re.sub(r'(.)\1{2,}', r'\1\1', text)

def spelling_correction(text):
    return text

df = pd.read_excel('EXCEL Clean-Result Data FF.xlsx')

df['review'] = df['review'].apply(lambda x: remove_repeated_characters(str(x)) if pd.notnull(x) else '')
df['review'] = df['review'].apply(spelling_correction)

df.to_csv('CSV Result-Cleansing {apps}.csv', index=False)
df.to_excel('EXCEL Result-Cleansing {apps}.xlsx', index=False)

print("Data cleansing selesai dan disimpan di 'Result-Cleansing'.")
