import time

import requests

import json

import get_data_from_names
import list_operations
import search
import search_file


def main():
    file_format = "Names"
    with open("cardslist.txt", "r") as input_file, open("card_data.txt",
                                                        "w") as data_file:
        for line in input_file:
            if file_format == "Decklist":
                name = line[line.find(' '):].strip()
            elif file_format == "Names":
                name = line.strip()
            else:
                break
            card_data = get_data_from_names.get_all_card_data(name)
            time.sleep(0.05)
            json.dump(card_data, data_file)
            data_file.write("\n")


# with open("card_data.txt", "r") as input_file:
#     for i in range(10):
#         line = input_file.readline()
#         card = json.loads(line)
#         print(card['name'])

# with open("temp.txt", "w") as data_file:
#     card_data = get_all_card_data("Vicious Clown")
#     json.dump(card_data, data_file)


if __name__ == "__main__":
    result_folder = "files/search_results/"
    search.search("game:paper sort:edhrec", result_folder+"edhrec_sort.txt")
    # search_file.search_with_cached(result_folder+"is_black_search_result.txt", "files/deans_card_data.txt", "json.txt")
