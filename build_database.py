from config import *
import json
import re

# 1. Load all courses into memory so we can see their preqs
# 2. For each course, add self as a post-req for each of its prereqs
# 3. Compile and save into one large dataset file which will contain every course with:
#       1) name
#       2) description
#       3) prereqs
#       4) coreqs
#       5) postreqs

if(BUILD_DATABASE):
    with open("courses.json", "w") as outfile:
        outfile.write('[\n')

        for code in CODES:
            filepath = FILEPATH.format(code.lower())
            with open(filepath) as infile:
                text = infile.read()
                # drop the square brackets at the start and end
                text = text[2:len(text)-2] + ',\n'

                outfile.write(text)
        
        outfile.write(']')

with open("courses.json") as infile:
    all_courses = json.load(infile)

    for course in all_courses:
        prereqs = course['prereqs'].split('.')[0]
        matches = re.findall(r"[A-Z]{3,4} [0-9]{3}", prereqs)
        
        for curr_course in all_courses:
            if(curr_course['name'] in matches):
                if(curr_course['postreqs'] == ''):
                    curr_course['postreqs'] = course['name']
                else:
                    curr_course['postreqs'] += f", {course['name']}"

    # postreqs should be added back, update courses.json file
    
    # Serializing and writing json
    courses_json = json.dumps(all_courses, indent=4)
    with open("courses.json", "w") as outfile:
        outfile.write(courses_json)
