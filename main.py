import time

import requests

import json


def get_all_card_data(name):
    payload = {"fuzzy": name}
    r = requests.get('https://api.scryfall.com/cards/named', payload)
    card = r.json()
    return card


def main():
    file_format = "Names"
    with open("cardslist.txt", "r") as input_file, open("card_data.txt",
                                                        "w") as data_file:
        card_dict = {}
        for line in input_file:
            if file_format == "Decklist":
                name = line[line.find(' '):].strip()
            elif file_format == "Names":
                name = line.strip()
            else:
                break
            card_data = get_all_card_data(name)
            time.sleep(0.05)
            card_dict[name] = card_data
        json.dump(card_dict, data_file)


main()
