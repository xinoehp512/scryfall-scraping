import time

import requests

import json


def search(query, file_output):
    with open(file_output, "w") as data_file:
        payload = {"q": query}
        r = requests.get('https://api.scryfall.com/cards/search', payload)
        while True:
            list = r.json()
            for card in list["data"]:
                json.dump(card, data_file)
                data_file.write("\n")
            if list["has_more"]:
                time.sleep(0.05)
                r = requests.get(list["next_page"])
            else:
                break


if __name__ == "__main__":
    search("id:rw o:'+1/+1 counter'", "search_result.txt")
