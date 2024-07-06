
# Importing the os module in Python provides a way to interact with the operating system. Here are some key uses:

import os



# __name__ is the string '__main__' 
# os.path.abspath(__name__) tries to convert this name to an absolute path.
BASE_DIR = os.path.abspath(__name__)




class config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATION = False