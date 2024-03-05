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
    
    def filterGoodFiles(self):
        # We will filter all the files that contain good in there names
        self.filesList = [x for x in self.filesList if x[-10:-6].lower() == 'good']
        #print(100,100)
        #print(self.filesList)
    
    def filterNewFiles(self):
        lastUsedQuestionNumber = ""
        with open("lastUsedFile.txt","r") as lastUsedFile:
            lastUsedQuestionNumber = lastUsedFile.read()
        print(lastUsedQuestionNumber,len(lastUsedQuestionNumber),type(lastUsedQuestionNumber)," <- Last used question Number")
        if lastUsedQuestionNumber != "":
            ctr = 0
            flag = False
            while ctr < len(self.filesList):
                if lastUsedQuestionNumber == self.filesList[ctr][0:len(lastUsedQuestionNumber)] and not flag:
                    flag = not flag
                elif flag and self.filesList[ctr][0:len(lastUsedQuestionNumber)].isnumeric():
                    break
                ctr += 1
            self.filesList = self.filesList[ctr:]   # We will handle only new files 
        else:   # We don't want any changes
            self.filesList = self.filesList
        print("LIST OF FILES")
        print(self.filesList)
                
    def openTheFiles(self):
        for i in range(len(self.filesList)):
            currFileName = self.filesList[i]
            self.filesContent.append("\n")
            self.filesContent.append(currFileName + "\n")
        # We will open the filtered files and will place their content
            with open(self.directories[0] + r'\\' + currFileName,"r") as notebookFile:
                notebookContent = nbformat.read(notebookFile,as_version=4)
            for cell in notebookContent.cells:
                if cell.cell_type == "code":
                    self.filesContent.append(cell.source + "\n")        # the type of cell.content = str
    
    def writeTheContentToFile(self):
        with open("output.txt","w") as outputFile:
            outputFile.write("")
        for i in range(len(self.filesContent)):
            with open("output.txt","a+") as outputFile:
                outputFile.write(self.filesContent[i])
        fileSize = os.path.getsize("output.txt")
        print(f"Output.txt of file size {fileSize} has been written")
    
    def updateTheLastQuestionNumber(self):
        lastFileName = self.filesList[-1]
        lastFileNumber = ""
        for i in lastFileName:
            if i.isnumeric():
                lastFileNumber += i
            else:
                break
        with open("lastUsedFile.txt","w") as outputFile:
            outputFile.write(lastFileNumber)
        
            
    
    def execute(self):
        self.createList()
        self.filterGoodFiles()
        self.filterNewFiles()
        self.openTheFiles()
        self.writeTheContentToFile()
        self.updateTheLastQuestionNumber()

q = QuestionRev()
q.execute()