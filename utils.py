import re as regex
from PIL import ImageTk, Image

def checkEmail(email):

    if (not regex.match(r"[^@]+@[^@]+\.[^@]+", email)):
        return False

    return True
