import requests
from bs4 import BeautifulSoup
import json
import re


# helper function for has_prof() and get_prof_name(); retrieves tables
def get_tables(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", {"class", "table"})
    return tables

# helper function for scrape_ubc_courses; checks if instructor is listed
def has_prof(url):
    tables = get_tables(url)
    has_prof = any("Instructor:" in table.text for table in tables)
    return has_prof

# helper function for scrape_ubc_courses to get prof of section
def get_prof_name(url):
    tables = get_tables(url)
    prof_name = tables[2].find_all("a")[0].text.strip().split(" ")
    # prof_text = tables[2].text.strip()
    # prof_text_split = re.sub("^Instructor:\s*", "", prof_text).split(" ")
    first_name = prof_name[1]
    last_name = prof_name[0].replace(",", "")
    return first_name + " " + last_name
    # with open(dept_name + course_name + ".txt", 'w') as text_file:
    #     text_file.write(response.text)


# REQUIRES: valid dept name and valid course code
def scrape_ubc_courses(json_course_path):
    prof_list = []
    section_list = []
    with open(json_course_path, 'r') as json_file:
        list_of_dept_courses = json.load(json_file)

    for dept_course in list_of_dept_courses:
        course_name = dept_course["dept"] + " " + dept_course["courseNum"]
        course_base_url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept="

        course_name_split = course_name.split(" ")
        dept_name = course_name_split[0].upper()
        course_name = course_name_split[1]
        course_url = course_base_url + dept_name + "&course=" + course_name
        course_class_pattern = re.compile("^section.$")
        response = requests.get(course_url)

        soup = BeautifulSoup(response.text, "html.parser")
        course_sections = soup.find_all("tr", {"class": course_class_pattern})
        for course_section in course_sections:
            section_info = course_section.find_all("td")

            name = section_info[1].text.strip().split(" ")
            if len(name) <= 1:
                continue
            dept = name[0]
            course_num = name[1]
            section_num = name[2]
            term = section_info[3].text.strip()
            year = "2023/2024"
            days = section_info[6].text.strip()
            time = section_info[7].text.strip() + "-" + section_info[8].text.strip()

            section_page = course_section.find_all("a")[0]["href"]
            ubc_base_url = "https://courses.students.ubc.ca"
            section_url = ubc_base_url + section_page
            if has_prof(section_url):
                prof_name = get_prof_name(section_url)
                teaching_data = {"dept": dept, "course_num": course_num,
                                 "section_num": section_num, "year": year,
                                 "name": prof_name}
                prof_list.append(teaching_data)

            section_data = {"dept": dept, "course_num": course_num,
                            "section_num": section_num,
                            "term": term, "year": year,
                            "days": days, "time": time}
            section_list.append(section_data)

    with open("data/ubc_courses_data/" + dept_name + "_section_list.json", "w", encoding="latin-1") as json_file:
        json.dump(section_list, json_file, indent=2)
    with open("data/ubc_courses_data/" + dept_name + "_teaching_list.json", "w", encoding="latin-1") as json_file:
        json.dump(prof_list, json_file, indent=2)


scrape_ubc_courses("data/ubc_dept_data/CPSC.json")