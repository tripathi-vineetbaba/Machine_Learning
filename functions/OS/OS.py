import os

class OS:

    fileName=''

    def checkDir(self,filename,skip_directory=2):
        parentDir='\\'.join(os.getcwd().split('\\')[0:-skip_directory])
        baseDir=parentDir+'\\'+'model\\'+filename+'\\'

        if os.path.exists(baseDir):
            return True
        else:
            return False


    def createDirectory(self, filename,skip_directory=2):
        parentDir='\\'.join(os.getcwd().split('\\')[0:-skip_directory])
        baseDir=parentDir+'\\'+'model\\'+filename+'\\'
        fileName=''
        if os.path.exists(baseDir):
            self.fileName=baseDir+filename
        else:
            os.mkdir(baseDir)
            self.fileName=baseDir+filename
        return self.fileName


    def get_path(self,filename,skip_dir=2):
        parentDir='\\'.join(os.getcwd().split('\\')[0:-skip_dir])
        baseDir=parentDir+'\\'+'model\\'+filename+'\\'
        self.fileName=baseDir+filename
        return self.fileName


    def get_meta_path(self,filename,skip_dir=2,globalstep=100):
        parentDir='\\'.join(os.getcwd().split('\\')[0:-skip_dir])
        baseDir=parentDir+'\\'+'model\\'+filename+'\\'
        self.filena=baseDir+filename
        file=self.filena+'-'+str(globalstep)+'.meta'
        return file,baseDir

