
import json


def intersect(file1, file2, file_out):
    with open(file1) as input_file_1, open(file2) as input_file_2, open(file_out, "w") as data_file:
        card_ids = []
        for line in input_file_1:
            dict = json.loads(line)
            card_ids.append(dict['id'])
        for line in input_file_2:
            dict = json.loads(line)
            if dict['id'] in card_ids:
                data_file.write(line)


if __name__ == "__main__":
    intersect("card_data.txt", "search_result.txt", "intersection.txt")
