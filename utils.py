import re as regex

def checkEmail(email):

    if (not regex.match(r"[^@]+@[^@]+\.[^@]+", email)):
        return False

    return True

