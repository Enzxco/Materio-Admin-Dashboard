import sys
import os

# Add the project directory to the Python path
project_home = '/home/materioadmin/Materio'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

from app import app as application

if __name__ == '__main__':
    application.run()
