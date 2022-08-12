import sys, os, re
from colorama import Style
print("Receiving data...")
str_to_find = f".+/{re.escape(sys.argv[1])}"
str_to_find_in = open("report.txt", "r").read()
print("Data recieved.")
print("Searching...\n")
search = re.findall(f"{str_to_find}", str_to_find_in)
already_found = []
counter = 0
if search:
    for result in search:
        if not result in already_found:
            counter += 1
            print(f"{counter}. Found: " + {result.replace(sys.argv[1], f"{Style.BRIGHT}{sys.argv[1]}{Style.RESET_ALL}")} + ".")
            already_found.append(result)
        sys.stdout.flush()
else:
    print("Could not find.")