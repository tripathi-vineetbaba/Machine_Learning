import sqlite3, os

class DatabaseConnection:

     filename=''

     def createRequiredPath(self,filename):
         parentDir='\\'.join(os.getcwd().split('\\')[0:-1])
         baseDir=parentDir+'\\'+'database-file\\'
         fileName=baseDir+filename+'.db'
         if checkDir(baseDir):
            return fileName
         else:
            return None


     def __init__(self,file):
         self.filename=createRequiredPath(file)
         if filename is not None:
                  self.connect=sqlite3.connect(filename)
         else :
                  return 'Connection Refused'


     def __enter__(self):
         return self.connect


     def __exit__(self, exc_type, exc_val, exc_tb):
         self.connect.close()


     def checkDir(imagePath):
         if os.path.exists(imagePath):
             return True
         else:
             os.mkdir(imagePath)
             checkDir(imagePath)

     def getDatafilePath(self):
         return self.filename
