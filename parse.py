from bs4 import BeautifulSoup
from os.path import exists
import requests
import json

IGNORE_CACHE = False

codes = ["ELEC", "CPEN", "ENPH", "CHBE", "BMEG", "ENVE", "CIVL", "ENVE", "IGEN", "MANU", "MECH", "MINE", "MTRL"]
base_link = "https://www.calendar.ubc.ca/vancouver/courses.cfm?code={}"

for i in range(len(codes)):
    code = codes[i]
    filepath = f"courses/{code.lower()}.json"
    if(not IGNORE_CACHE and exists(filepath)):
        print(f"File already exists for code {code}, skipping.")
        continue
    else:
        print(f"Processing {code} courses...")

    page = requests.get(base_link.format(code))
    soup = BeautifulSoup(page.text, 'html.parser')

    # print(soup.prettify())
    main_box = soup.find('dl', class_='double')

    course_descs = []

    course_dict = {}
    for i in main_box.children:
        # Title tag
        if i.name == "dt":
            course_dict['name'] = f"{code.upper()} " + i.find('a').attrs['name']
        if i.name == "dd":
            course_description_str_arr = i.text.split("Prerequisite: ")
            course_dict['desc'] = course_description_str_arr[0]
            if (len(course_description_str_arr) > 1):
                prereq_str = course_description_str_arr[1][:-1] # dropping newline at the end
                coreq_str = ""

                if "Corequisite" in prereq_str:
                    index = prereq_str.find("Corequisite")
                    coreq_str = prereq_str[index+13:]
                    prereq_str = prereq_str[0:index-1]

                course_dict['prereqs'] = prereq_str
                course_dict['coreqs'] = coreq_str
            # print(course_dict)
            course_descs.append(course_dict)
            course_dict = {}


    # Serializing json
    courses_json = json.dumps(course_descs, indent=4)
    # Writing to sample.json
    with open(filepath, "w") as outfile:
        outfile.write(courses_json)

print("Finished processing!")