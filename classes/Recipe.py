from database import Database

class Recipe:

    # attributes
    TAG = ""
    creator = ""
    title = ""
    prepMode = ""
    estimatedTime = ""
    image = ""
    views = 0  


    # constructor
    def __init__(self, TAG, creator, title, prepMode, estimatedTime, image, views):
        self.TAG = TAG
        self.creator = creator
        self.title = title
        self.prepMode = prepMode
        self.estimatedTime = estimatedTime
        self.image = image
        self.views = views

    # methods
    