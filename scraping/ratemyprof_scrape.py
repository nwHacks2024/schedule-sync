import requests
import json
from bs4 import BeautifulSoup
import re

# REQUIRES: file path to JSON with names of profs
def find_prof_info(json_section_path):
    prof_list = []
    searched_profs = []
    with open(json_section_path, 'r') as json_file:
        list_of_dept_sections = json.load(json_file)

    prof_url_base = "https://www.ratemyprofessors.com/search/professors?q="
    for section in list_of_dept_sections:
        prof_name = section['name']
        if prof_name in searched_profs:
            continue
        else:
            searched_profs.append(prof_name)
        name_list = prof_name.lower().split()
        prof_search_query = prof_url_base + name_list[0] + "%20" + name_list[1]
        page = requests.get(prof_search_query)

        json_data = json.loads(re.search(r'window.__RELAY_STORE__ = ({.*})', page.text).group(1))

        prof_json_pattern = re.compile("^V.*$")
        avg_rating = "NA"
        avg_difficulty = "NA"
        num_ratings = "0"
        for key, value in json_data.items():
            if prof_json_pattern.match(key):
                school_id = value["school"]["__ref"]
                prof_first = value["firstName"]
                prof_last = value["lastName"]
                school_name = json_data[school_id]["name"]
                if school_name == "University of British Columbia" or prof_first.lower() == name_list[0] or prof_last.lower() == name_list[1]:
                    prof_id = value["legacyId"]
                    prof_url = "https://www.ratemyprofessors.com/professor/" + str(prof_id)
                    prof_page = requests.get(prof_url)
                    soup = BeautifulSoup(prof_page.text, "html.parser")
                    num_ratings_raw = soup.find_all("div", {"class", "RatingValue__NumRatings-qw8sqy-0 jMkisx"})
                    num_ratings_clean = num_ratings_raw[0].find_all("a")[0].text
                    num_ratings = re.search("[0-9]*", num_ratings_clean).group()
                    if num_ratings != "":
                        difficulty = soup.find_all("div", {"class", "FeedbackItem__FeedbackNumber-uof32n-1 kkESWs"})
                        avg_difficulty = difficulty[1].text
                        rating = soup.find_all("div", {"class": "RatingValue__Numerator-qw8sqy-2 liyUjw"})
                        avg_rating = rating[0].text
                    else:
                        num_ratings = "0"
                    break

                # num_ratings = value["numRatings"]
                # avg_rating = "NA"
                # avg_difficulty = "NA"
                # if num_ratings < 1 or school_name != "University of British Columbia" or prof_first.lower() != name_list[0] or prof_last.lower() != name_list[1]:
                #     continue
                # else:
                #     avg_rating = value["avgRating"]
                #     avg_difficulty = value["avgDifficulty"]

        prof_data = {
            "name": prof_name,
            "numRatings": num_ratings,
            "avgRating": avg_rating,
            "avgDifficulty": avg_difficulty
        }
        prof_list.append(prof_data)

    with open("data/rate_my_prof_data/all_prof_list.json", "w", encoding="latin-1") as json_file:
        json.dump(prof_list, json_file, indent=2)


find_prof_info("data/ubc_courses_data/CPSC_teaching_list.json")
