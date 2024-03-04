# Open file in the given directory and then check if the file has good in its name in last 4 place

import os
import codecs
import nbformat

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
    
    def openTheFiles(self):
        # We will open the filtered files and will place their content
        #for file in self.filesList:
        f = codecs.open(self.directories[0] + r'\\' + self.filesList[0])
        print(f.read())
        f.close()
    
    def openTheFiles2(self):
        print(self.filesList[0])
        # We will open the filtered files and will place their content
        with open(self.directories[0] + r'\\' + self.filesList[0],"r") as notebookFile:
            notebookContent = nbformat.read(notebookFile,as_version=4)
        for cell in notebookContent.cells:
            if cell.cell_type == "code":
                print("Code :")
                print(cell.source)
            elif cell.cell_type == "markdown":
                print("MarkDown")
                print(cell.source)
        
    
    def execute(self):
        self.createList()
        self.filterFiles()

q = QuestionRev()
q.createList()
q.filterFiles()
q.openTheFiles2()