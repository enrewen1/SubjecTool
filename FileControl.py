from tkinter import filedialog
import codecs
import os
class inputMode:
    def __init__(self, fileName=""):
        self.setFile(fileName)
    def setFile(self, fileName=""):
        
        self.fileInputStream = None
        
        try:
            self.fileInputStream = codecs.open(fileName, mode='r', encoding='utf-8')
        except:
            fileNameFromDialog = filedialog.askopenfilename()
            self.fileInputStream = codecs.open(fileNameFromDialog, mode='r', encoding='utf-8')
    
        self.str = self.fileInputStream
        return self.fileInputStream
    
    def getData(self, dataType=0):
        try:
            if dataType == 0:
                return (self.fileInputStream).read()
            return (self.fileInputStream).readlines()
        except:
            print("File Read Error")
    def closeMode(self):
        (self.fileInputStream).close()
