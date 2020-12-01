#validate phone number
def phonevalidator(number):
    """This function takes a string and checks that it is a valid US number: 10 digits or 11 starting with 1"""
    cleaned = ""
    num = filter(lambda x: x.isdigit(), number)
    for e in num:
        cleaned += e
    if len(cleaned) == 10:
        return True
    if len(cleaned) == 11:
        if cleaned[0] == "1":
            return True
    return False

print(phonevalidator("1-800-800-8000"))

def isFreds(name):
    """This function checks for Fred, to ensure no one whose name is Fred can get through. Sorry, Freds. Freddie is ok, though. Freddo too."""
    start = name.find("Fred")
    if start == -1:
        return False
    end = start + 4
    if len(name) == 4:
        return True
    try:
        if name[start - 1] == " " and name[end + 1] == " ":
            return True
    except:
        pass
    try:
        if name[start - 1] == " ":
            return True
    except:
        pass
    try:
        if name[end + 1] == " ":
            return True
    except:
        pass
    return False
