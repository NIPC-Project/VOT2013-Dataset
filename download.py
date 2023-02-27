import urllib.request
import os
import json

data_folder = "data/"
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

description_url = "https://data.votchallenge.net/vot2013/dataset/description.json"
description_path = data_folder + os.path.basename(description_url)
urllib.request.urlretrieve(description_url, description_path)


annotations_base_url = "https://data.votchallenge.net/vot2013/dataset/"
channels_base_url = "https://data.votchallenge.net/sequences/"

with open(description_path, "r") as f:
    description_dict = json.load(f)
    for sequence in description_dict["sequences"]:
        name = sequence["name"]
        print(f"downloading {name}...")

        annotations_url = annotations_base_url + sequence["annotations"]["url"]
        annotations_path = data_folder + name + ".zip"
        urllib.request.urlretrieve(annotations_url, annotations_path)

        channels_url = channels_base_url + sequence["channels"]["color"]["uid"] + ".zip"
        channels_path = data_folder + name + "_frames.zip"
        urllib.request.urlretrieve(channels_url, channels_path)
    print("DONE!")
