import os
from app import db
from app import app
import views  # Ensure this is placed after `from app import app`

if __name__ == '__main__':
    app.run()
