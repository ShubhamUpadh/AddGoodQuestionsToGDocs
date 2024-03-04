# Open file in the given directory and then check if the file has good in its name in last 4 place

import os
import codecs
import nbformat

class QuestionRev:
    def __init__(self):
        self.directories = [r"G:\Python Exercises\Greg Hoff"]
        self.filesList =[]
        self.filesContent = []
    
    def createList(self):
        # We will create the list of all the files in the given directories
        self.filesList = os.listdir(self.directories[0])
        #print(self.filesList)
    
    def filterFiles(self):
        # We will filter all the files that contain good in there names
        self.filesList = [x for x in self.filesList if x[-10:-6].lower() == 'good']
        #print(100,100)
        #print(self.filesList)
        
    def openTheFiles(self):
        for i in range(len(self.filesList)):
            currFileName = self.filesList[i]
            self.filesContent.append(currFileName)
        # We will open the filtered files and will place their content
            with open(self.directories[0] + r'\\' + currFileName,"r") as notebookFile:
                notebookContent = nbformat.read(notebookFile,as_version=4)
            for cell in notebookContent.cells:
                if cell.cell_type == "code":
                    self.filesContent.append(cell.source)        # the type of cell.content = str
    '''
    def addExtraSpaces(self):
        temp = self.filesContent
        for i in range(len(temp)):
            if temp[0:2].isnumeric():
     '''           
    
    def writeTheContentToFile(self):
        with open("output.txt","w") as outputFile:
            outputFile.write("")
        for i in range(len(self.filesContent)):
            with open("output.txt","a+") as outputFile:
                outputFile.write(self.filesContent[i])
        fileSize = os.path.getsize("output.txt")
        print(f"Output.txt of file size {fileSize} has been written")
            
    
    def execute(self):
        self.createList()
        self.filterFiles()

q = QuestionRev()
q.createList()
q.filterFiles()
q.openTheFiles()
#print(q.filesContent)
q.writeTheContentToFile()