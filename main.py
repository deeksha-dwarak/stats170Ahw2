import csv
import pandas as pd
from splink import block_on

def main():
    # Read cs rankings
    df = pd.read_csv("cs_rankings_cleanNames")

    # Standardization
    try:
        df['clean_name'] = df['clean_name'].astype(str).str.lower()
        df['full_name'] = df['full_name'].astype(str).str.lower()
        pattern = r"[.]"
        df['clean_name'] = df['clean_name'].str.replace(pattern, '', regex=True)
        df['full_name'] = df['full_name'].str.replace(pattern, '', regex=True)
        df_replaced = df.fillna(value=None)
        print("clean names standardized")
    except:
        print("something went wrong")
    
    # Blocking
    
