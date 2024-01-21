import requests
from bs4 import BeautifulSoup
import json
import re

# REQUIRES: a string with a first name and last name only, delimited by a space
def find_prof_info(prof_name):
    prof_url_base = "https://www.ratemyprofessors.com/search/professors?q="
    name_list = prof_name.lower().split()
    prof_search_query = prof_url_base + name_list[0] + "%20" + name_list[1]
    page = requests.get(prof_search_query)
    # soup = BeautifulSoup(page.text, "html.parser")
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
            print(school_name == "University of British Columbia" and prof_first.lower() == name_list[0] and prof_last.lower() == name_list[1])
            if school_name == "University of British Columbia" and prof_first == name_list[0] and prof_last == name_list[1]:
                avg_rating = value["avgRating"]
                num_ratings = value["numRatings"]
                avg_difficulty = value["avgDifficulty"]
                print(avg_rating + ", " + num_ratings + ", " + avg_difficulty)


    # prof_ids = []
    # for key, value in json_data.items():
    #     for inner_key, inner_value in value.items():
    #         if inner_value == "name" and inner_value == "University of British Columbia":
    #             prof_ids.append(key)
    # for id in prof_ids:
    #     if json_data[id]["firstName"] == name_list[0] and json_data[id]["lastName"] == name_list[1]:
    #         school_id = json_data[id]["school"]["ref"]
    #         if json_data[school_id][""]
    # print(type(json_data))

    # pretty_json = json.dumps(json_data)
    # print(type(pretty_json))
    # script = soup.findAll('script')
    # print(script)
    # data = script.split("bootstrapData['menuMonthWeeks'] = ", 1)[-1].rsplit(';', 1)[0]
    # data = json.loads(data)


find_prof_info("Cinda Heeren")
