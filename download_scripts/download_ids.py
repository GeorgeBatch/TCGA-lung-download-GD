import os
import json
import gdown
import pandas as pd

def change_format(url):
    l = url.split('/')
    url_for_download = "https://drive.google.com/uc?id=" + l[5]
    return url_for_download

if __name__ == "__main__":
    
    file_batch = "TCGA-lung-IDs"
    
    with open(f"../download_status/{file_batch}.json") as json_file:
        download_status = json.load(json_file)
    df_ids = pd.read_csv(f"../names_and_links/{file_batch}.csv")
    df_ids['URL_for_download'] = df_ids['URL'].apply(change_format)
    

    for url, name in zip(df_ids['URL_for_download'], df_ids['Name']):
        save_to = f'../{name}'
        
        if download_status[name] == 0 or (not os.path.exists(save_to)):
            print(f"Downloading {name} from {url} into '{save_to}'.")
            gdown.download(url=url, output=save_to, quiet=False)
            
            download_status[name] = 1
            with open(f"../download_status/{file_batch}.json", 'w') as json_file:
                json.dump(download_status, json_file)
        else:
            print(f"{name} \n\t has already been successfully downloaded and is present at the expected location.")
            
            
