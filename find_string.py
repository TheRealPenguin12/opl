import sys, os, re
from colorama import Style
str_to_find = f".+/{re.escape(sys.argv[1])}"
str_to_find_in = open("report.txt", "r").read()
print("Please wait...")
search = re.search(f'{str_to_find}', str_to_find_in)
if search:
    print(f"Found: {search.group(0).replace(str_to_find, f'{Style.BRIGHT}sys.argv[1]{Style.RESET_ALL}')}.")
else:
    print("Could not find.")
