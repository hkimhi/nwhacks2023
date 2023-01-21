from config import *

from bs4 import BeautifulSoup
from os.path import exists
import requests
import json

codes_subset = []

for code in CODES:
    if (IGNORE_CACHE or not exists(FILEPATH.format(code.lower()))):
        codes_subset.append(code)
    else:
        print(f"File already exists for code {code}, skipping.")

for code in codes_subset:
    print(f"Processing {code} courses...")

    filepath = FILEPATH.format(code.lower())

    page = requests.get(BASE_LINK.format(code))
    soup = BeautifulSoup(page.text, 'html.parser')

    # print(soup.prettify())
    main_box = soup.find('dl', class_='double')

    course_descs = []

    course_dict = {}
    for i in main_box.children:
        # Title tag
        if i.name == "dt":
            course_dict['name'] = f"{code.upper()} " + \
                i.find('a').attrs['name']
        if i.name == "dd":
            coreq_str = ''
            prereq_str = ''
            postreq_str = ''

            if("Corequisite" in i.text):
                coreq_str = i.text.split("Corequisite: ")[1].split('.')[0]
            if("Prerequisite" in i.text):
                prereq_str = i.text.split("Prerequisite: ")[1].split('.')[0]

            course_dict['coreqs'] = coreq_str
            course_dict['prereqs'] = prereq_str
            course_dict['postreqs'] = postreq_str
            
            course_descs.append(course_dict)
            course_dict = {}

    # Serializing json
    courses_json = json.dumps(course_descs, indent=4)
    # Writing to sample.json
    with open(filepath, "w") as outfile:
        outfile.write(courses_json)

print("Finished processing!")
