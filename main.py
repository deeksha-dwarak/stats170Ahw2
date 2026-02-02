import csv
import pandas as pd

def main():
    df = pd.read_csv("cs_rankings_cleanNames")
    try:
        df['clean_name'] = df['clean_name'].astype(str).str.lower()
        pattern = r"[.]"
        df['clean_name'] = df['clean_name'].str.replace(pattern, '', regex=True)
        print("clean names standardized")
    except:
        print("something went wrong")