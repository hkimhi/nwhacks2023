# IGNORE_CACHE
# Default: False
# Only used for scraping
# If set to True, re-scrapes data for coures and OVERWRITES currently existing files (if they exist)
# If set to False, does not re-scrape data if a file is already found with the correct course code
IGNORE_CACHE = False

# BUILD_DATABASE
# Default: False
# Only usedd for building the database file
# If set to True, rebuilds the database file with all courses
# If set to False, processing will happen on the current database file (if it exists)
BUILD_DATABASE = False

# FILEPATH
# The location where files are saved
FILEPATH = "courses/{}.json"

# COLS
COLS = ["name", "desc", "prereqs", "coreqs"]

# CODES
# The course codes of the subjects we are interested in scraping from the UBC website
# Case-insensitive
CODES = ["ELEC", "CPEN", "ENPH", "CHBE", "BMEG", "ENVE", "CIVL", "ENVE", "IGEN",
         "MANU", "MECH", "MINE", "MTRL", "MATH", "CPSC", "PHYS", "APSC", "EECE", "EOSC"]

# BASE_LINK
# The url from which we can scrape data after formatting the string with the correct code
BASE_LINK = "https://www.calendar.ubc.ca/vancouver/courses.cfm?code={}"