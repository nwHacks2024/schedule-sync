import requests
import json
import re

# REQUIRES: a string with a first name and last name only, delimited by a space
def find_prof_info(prof_name):
    prof_url_base = "https://www.ratemyprofessors.com/search/professors?q="
    name_list = prof_name.lower().split()
    prof_search_query = prof_url_base + name_list[0] + "%20" + name_list[1]
    page = requests.get(prof_search_query)
    json_data = json.loads(re.search(r'window.__RELAY_STORE__ = ({.*})', page.text).group(1))
    # with open("new_jeff.json", "w") as json_file:
    #     json.dump(json_data, json_file, indent=2)

    prof_json_pattern = re.compile("^V.*$")
    for key, value in json_data.items():
        if prof_json_pattern.match(key):
            school_id = value["school"]["__ref"]
            prof_first = value["firstName"]
            prof_last = value["lastName"]
            school_name = json_data[school_id]["name"]
            num_ratings = value["numRatings"]
            if num_ratings > 0 and school_name == "University of British Columbia" and prof_first.lower() == name_list[0] and prof_last.lower() == name_list[1]:
                avg_rating = value["avgRating"]
                avg_difficulty = value["avgDifficulty"]

    json_file_clean = {
        "firstName": name_list[0],
        "lastName": name_list[1],
        "numRatings": num_ratings,
        "avgRating": avg_rating,
        "avgDifficulty": avg_difficulty
    }

    with open("data/rate_my_prof_data/" + name_list[0] + "_" + name_list[1] + ".json", 'w') as json_file:
        json.dump(json_file_clean, json_file, indent=4)


find_prof_info("Cinda Heeren")
find_prof_info("Lynn Norman")
find_prof_info("William Bowman")
find_prof_info("Mike Feeley")
find_prof_info("Felix Grund")
find_prof_info("Gregor Kiczales")