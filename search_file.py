import search
import list_intersection
import convert_to_json


def search_file(query, source, json_dest):
    search.search(query, "search_result.txt")
    list_intersection.intersect(source, "search_result.txt", "intersection.txt")
    convert_to_json.convert_to_json("intersection.txt", json_dest)


if __name__ == "__main__":
    search_file("id:rw otag:draw sort:edhrec", "card_data.txt", "json.txt")
