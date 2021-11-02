import json
import pandas as pd

file_batches = ["TCGA-lung-IDs", "TCGA-lung-WSI-corrupt", "TCGA-lung-WSI"]

if __name__ == "__main__":

    for file_batch in file_batches:
        df = pd.read_csv(f"../names_and_links/{file_batch}.csv")
        
        initial_status = dict.fromkeys(df["Name"], 0)
        file_name = f"../download_status/{file_batch}.json"
        
        with open(file_name, 'w') as outfile:
            json.dump(initial_status, outfile)
        print(f"Created a record file '{file_name}'.")