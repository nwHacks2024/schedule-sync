from urllib import response

import requests
from bs4 import BeautifulSoup
import json
import re

# REQUIRES: valid course code (ex. "CPSC")


def ubc_depts_scrape(dept_name):
    course_list = []
    dept_base_url = "https://courses.students.ubc.ca/cs/courseschedule;jsessionid=Wub6GoUub4NSOfGVkCaxPj0k?pname=subjarea&tname=subj-department&dept="
    dept_url = dept_base_url + dept_name
    dept_class_pattern = re.compile("^section.$")
    response = requests.get(dept_url)

    # with open(dept_name + ".txt", 'w') as text_file:
    #     text_file.write(response.text)

    soup = BeautifulSoup(response.text, "html.parser")
    courses = soup.find_all("tr", {"class": dept_class_pattern})
    for course_title in courses:
        title = course_title.find_all_next("a")[0].text
        course_title_split = title.strip().split(" ")
        course_data = {"courseNum": course_title_split[1], "dept": course_title_split[0]}
        course_list.append(course_data)

    with open("data/ubc_dept_data/" + dept_name + ".json", "w", encoding = "latin-1") as json_file:
        json.dump(course_list, json_file, indent=2)

ubc_depts_scrape("CPSC")
