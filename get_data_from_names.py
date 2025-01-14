import json
import time

import requests


def get_all_card_data(name):
    payload = {"fuzzy": name}
    r = requests.get('https://api.scryfall.com/cards/named', payload)
    card = r.json()
    return card


def get_data_from_names(input_file_name, output_file_name, file_format="Names"):
    with open(input_file_name, "r") as input_file, open(output_file_name, "w") as data_file:
        for line in input_file:
            if file_format == "Decklist":
                name = line[line.find(' '):].strip()
            elif file_format == "Names":
                name = line.strip()
            else:
                break
            card_data = get_all_card_data(name)
            time.sleep(0.05)
            # print(name)
            json.dump(card_data, data_file)
            data_file.write("\n")


if __name__ == "__main__":
    get_data_from_names("deans_cardlist.txt", "deans_card_data.txt")
