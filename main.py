
from stats import wordcount,charcount,sortchar
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

my_path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at { my_path }...")
print("----------- Word Count ----------")
wordcount(my_path)
    
print("--------- Character Count -------")
mydict = charcount(my_path)
mylist = sortchar(mydict)

for adict in mylist:
    print(f"{ adict['name'] }: { adict['num'] }")

