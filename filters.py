import json


def main():
    with open("card_data.txt", "r") as input_file, open("filtered_card_data.txt", "w") as data_file:
        for line in input_file:
            card = json.loads(line)
            color_id = card["color_identity"]
            if "G" not in color_id and "U" not in color_id and "B" not in color_id:
                json.dump(card, data_file)
                data_file.write("\n")


if __name__ == "__main__":
    main()
