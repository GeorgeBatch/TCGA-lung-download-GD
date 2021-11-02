import os
import json
import gdown
import pandas as pd


if __name__ == "__main__":
    
    file_batch = "TCGA-lung-WSI-corrupt"
    
    with open(f"../download_status/{file_batch}.json") as json_file:
        download_status = json.load(json_file)
    df = pd.read_csv(f"../names_and_links/{file_batch}.csv")
    
    for url, name in zip(df['URL'], df['Name']):
        save_to = f'../{file_batch}/{name}'
        
        if download_status[name] == 0 or (not os.path.exists(save_to)):
            print(f"Downloading {name} \nFrom: {url} \nInto: '{save_to}'.\n")
            gdown.download_folder(url=url, output=save_to, quiet=False)
            print()
            
            download_status[name] = 1
            with open(f"../download_status/{file_batch}.json", 'w') as json_file:
                json.dump(download_status, json_file)
        else:
            print(f"{name} \n\t has already been successfully downloaded and is present at the expected location.")
            
            
