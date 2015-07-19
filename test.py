import os
import sys

sys.path += ["D:/server/apps/standalone/ftrack-python"]

os.environ['FTRACK_SERVER'] = 'https://fabiano-petroni.ftrackapp.com'
os.environ['FTRACK_APIKEY'] = 'c7181086-18da-11e5-ad63-f23c91df2148'
os.environ['LOGNAME'] = 'fabianopetroni@gmail.com'

import ftrack

for project in ftrack.getProjects():
    print project.getFullName()

