


from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QFileDialog
import os
from datetime import datetime
import PIL.ImageGrab

class snapshot:
    
    
    def getfilename(self):
             fileFilter='Data file (*.png)'
             QFileDialog.getOpenFileName(parent =self, caption ='select a file', directory=os.getcwd(), filter=fileFilter )
             snapshot.getfilename(self)
    def currenttime(self):
            current_datetime = datetime.now()
            print(current_datetime)
    def openfile(self):
            newpath = r'C:\Users\samar\Desktop' 
            if not os.path.exists(newpath):
                 os.makedirs(newpath)
    # getting the path
    def getfilename(self):
            fileFilter='Data file (*.png)'
            options=QFileDialog.getOpenFileName(parent =self, caption ='select a file', directory=os.getcwd(), filter=fileFilter )
            snapshot.getfilename(self)
            if options:
                self.whateever.text(str(options))

    def getdirectory(self):
             response = QtWidgets.QFileDialog.getExistingDirectory(caption= 'Select folder')
             print (response)
             return response

    def getsavefilename(self):
            fileFilter='Data file (*.png)'
            response=QtWidgets.QFileDialog.getSaveFileName( caption ='select a file', directory='snapshot.png', filter= fileFilter, initialFilter='image file (*.png) '
            )
            return response

    def screenshoting(self):
            im = PIL.ImageGrab.grab()
           # im.save(snapshot.getfilename())
            im.show()
            fileFilter='Data file (*.png)'
            QFileDialog.getSaveFileName(caption ='select a file', directory='snapshot.png', filter= fileFilter, initialFilter='image file (*.png) '
            )
    
            name = QtGui.QFileDialog.getSaveFileName(self,'Save File')
            file = open(name,'w')
    
 
            file.close()
   
            
            

            

# put on file just in case
#path=r'C:\Users\samar\Desktop'
#or i in range(1,11):
   # os.chdir(path)
    #newfolder='Tutorial'+str(i)
    #try:
      # if not os.path.exists(newfolder):
               # os.makedirs(newfolder)
            #TO MAKE FOLDER INSITE THE OTHER FOLDER
       #path2=path+'//'+newfolder
       #os.chdir(path2)
       #for j in range (1,3):
                #newfolder_2='Test'+str(j)
                #os.makedirs(newfolder_2)
    #except: OSError
    #print('Error:alrady exists')
                



#ile1 = open(completeName, "w")
#file1.write("file information")
#file1.close()

#save_path =snapshot.getdirectory()
#file_name = 'text.txt'

#completeName = os.path.join(save_path, file_name)
#print(completeName)
#if __name__ == '__main__':
  
