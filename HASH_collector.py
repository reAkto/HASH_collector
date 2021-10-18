### HASH_collector_0.1 ###
# Simple tool for mal_hash list gathering from public depository #
# Intention is just programming and regex practice #
# Some parts are hidden/modified intentionaly #

# Imported libraries
import requests
import sys
import re

# Testing HTTP response from defined URL
result = requests.get("HIDDEN")

# Server responsivity checks
print(result.status_code)
print(result.headers)

# Decode
md5_list = result.content
md5_list_string = md5_list.decode('utf-8')

# Type check
print(type(md5_list_string))

# Header removal via regex
re_header_removal = re.sub(".*\#", "", md5_list_string)

# Print cleansed list of MD5 hashes and terminate program
print(re_header_removal)
sys.exit()
