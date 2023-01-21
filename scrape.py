from config import *

from bs4 import BeautifulSoup
from os.path import exists
import requests
import json
import re

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
            course_dict['name'] = f"{code.upper()} " + i.find('a').attrs['name']
            course_dict['title'] = i.find('b').text
            course_dict['credits'] = int(i.text[i.text.find('(') + 1])
        if i.name == "dd":
            coreqs = []
            prereqs = []
            postreqs = []

            if("Corequisite" in i.text):
                coreqs = i.text.split("Corequisite: ")[1].split('.')[0]
                coreqs = re.findall(r"[A-Z]{3,4} [0-9]{3}", coreqs)
            if("Prerequisite" in i.text):
                prereqs = i.text.split("Prerequisite: ")[1].split('.')[0]
                prereqs = re.findall(r"[A-Z]{3,4} [0-9]{3}", prereqs)

            course_dict['coreqs'] = coreqs
            course_dict['prereqs'] = prereqs
            course_dict['postreqs'] = postreqs
            
            course_descs.append(course_dict)
            course_dict = {}

    # Serializing json
    courses_json = json.dumps(course_descs, indent=4)
    # Writing to sample.json
    with open(filepath, "w") as outfile:
        outfile.write(courses_json)

print("Finished processing!")
