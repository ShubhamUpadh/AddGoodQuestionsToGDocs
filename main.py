# Open file in the given directory and then check if the file has good in its name in last 4 place

import os

class QuestionRev:
    def __init__(self):
        self.directories = [r"G:\Python Exercises\Greg Hoff"]
        self.filesList =[]
    
    def createList(self):
        # We will create the list of all the files in the given directories
        self.filesList = os.listdir(self.directories[0])
        print(self.filesList)
    
    def filterFiles(self):
        # We will filter all the files that contain good in there names
        self.filesList = [x for x in self.filesList if x[-10:-6].lower() == 'good']
        print(100,100)
        print(self.filesList)

q = QuestionRev()
q.createList()
q.filterFiles()