
def get_book_text(filename):
    with open(filename) as f:
        return f.read()

def wordcount(filepath):
    myraw = get_book_text(filepath)
    lines = myraw.split("\n")
    count = 0
    for line in lines:
        words = line.split()
        count += len(words)
    print(f"Found { count } total words")

def charcount(filepath):
    myraw = get_book_text(filepath).lower()

    mydict = {}
    for i in range(0,len(myraw)):
        try:
            mydict[myraw[i:i+1]] += 1
        except:
            mydict[myraw[i:i+1]] = 1

    return mydict

def sort_on(items):
    return items["num"]

def sortchar(adict):
    mylist = []
    for akey in adict:
        sd = {
                "name": akey,
                "num": adict[akey],
            }
        mylist.append(sd)

    mylist.sort(reverse=True, key=sort_on)
    return mylist


