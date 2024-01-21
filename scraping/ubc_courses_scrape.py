import requests
from bs4 import BeautifulSoup
import json
import re

# REQUIRES: valid dept name and valid course code
def scrape_ubc_courses(course_name):
    course_base_url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept="
    course_name_split = course_name.split(" ")
    dept_name = course_name_split[0].upper()
    course_name = course_name_split[1]
    course_url = course_base_url + dept_name + "&course=" + course_name
    course_class_pattern = re.compile("^section.$")
    response = requests.get(course_url)
    # with open(dept_name + course_name + ".txt", 'w') as text_file:
    #     text_file.write(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    course_sections = soup.find_all("tr", {"class": course_class_pattern})
    course_info = course_sections[0].find_all("td")
    section_info = course_sections[0].find_all("a")[0]["href"]
    ubc_base_url = "https://courses.students.ubc.ca"
    section_url = ubc_base_url + section_info

    # print(section_info[0].text)
    # name = course_info[1].text.strip()
    # type = course_info[2].text.strip()
    # term = course_info[3].text.strip()
    # delivery = course_info[4].text.strip()
    # days = course_info[6].text.strip().split(" ")
    # start = course_info[7].text.strip()
    # end = course_info[8].text.strip()
    # ubc_base_url = "https://courses.students.ubc.ca"
    # for info in course_info:
    #     print(info.text)
    # for section in course_sections:
    #     print(section.text + "\n")
    # print(type(course_sections))

scrape_ubc_courses("CPSC 110")