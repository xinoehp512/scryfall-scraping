import json


def convert_to_json(file_input, file_output):
    with open(file_input, "r") as input_file, open(file_output, "w") as data_file:
        card_dict = {}
        for line in input_file:
            dict = json.loads(line)
            # print(dict['name'])
            card_dict[dict['name']] = dict
        json.dump(card_dict, data_file)


if __name__ == "__main__":
    convert_to_json("intersection.txt", "json.txt")
