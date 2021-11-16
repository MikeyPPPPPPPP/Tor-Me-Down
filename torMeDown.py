import os
import time
import string
import os.path

class torMeDown:
    '''this code will get the  installation date of tor and grab the path and name of all images/videos downloaded after that (Windows)'''
    def __init__(self):
        self.desktop = os.path.expanduser('~')
        self.appdata = os.path.expanduser('AppData')
        self.drives = [x+':\\' for x in list(string.ascii_uppercase) if os.path.exists(x+':\\') == True]

        self.susExtentions = ('png','jpeg','jpg', 'mov', 'mp4')
        self.torLoaction = ''#
        self.torInstallationDate = ''#
        self.pathOfImagesAndVideosFound = {}#   {name:[time, path]}
        self.textFilePathsAndUrl = {}
        self.possibleOnionUrlsInTextFiles = {}          #{ path:[ urls ] }

    def makeFull(self, file):
        return os.path.abspath(file)

    def afterTor(self, file):
        return self.torInstallationDate < time.ctime(os.path.getctime(file))

    def getTorData(self):
        if os.path.exists(os.path.expanduser('~')+'\\AppData\\Roaming\\tor\\tor.exe'):
            self.torLoaction = os.path.expanduser('~')+'\\AppData\\Roaming\\tor\\tor.exe'
            self.torInstallationDate = time.ctime(os.path.getctime(os.path.expanduser('~')+'\\AppData\\Roaming\\tor\\tor.exe'))

        elif os.path.exists('D:\\tor\\Tor Browser\\Browser\\firefox.exe'):
            self.torLoaction = 'D:\\tor\\Tor Browser\\Browser\\firefox.exe'
            self.torInstallationDate = time.ctime(os.path.getctime('D:\\tor\\Tor Browser\\Browser\\firefox.exe'))

    def getData(self, file):
        return time.ctime(os.path.getctime(makeFull(file)))

    def pealLayers(self, file):
        '''this function searches a give file for .onion in it'''
        self.onionUrls = []
        try:
            with open(file, '+r') as peal:
                for line in peal.readlines():
                    if '.onion' in line:
                        self.onionUrls.append(line)
                        self.textFilePathsAndUrl[file]=self.onionUrls
        except FileNotFoundError:
            pass

    def findYourSoul(self, path):
        '''this function searches the computer for files made AFTER the instilation of tor'''
        
        
        
        #this will do a base search (desktop) befor the full search
        for x in os.listdir(path):
            try:
                if os.path.isdir(path+'\\'+x):
                    
                    self.findYourSoul(path+'\\'+x+'\\')
                
                if os.path.isfile(path+'\\'+x):
                    
                    if self.afterTor(path+'\\'+x) == True:
                        if x.split('.')[-1] == 'txt':
                            
                            self.pealLayers(path+'\\'+x)#self.makeFull(file))
                    
                        elif file.split('.')[-1] in self.susExtentions:
                            self.pathOfImagesAndVideosFound[file] = [time.ctime(os.path.getctime(file)), os.path.abspath(file)]
                        else:
                            pass
                    
                
            except:
                pass
        for drive in self.drives:
            for x in os.listdir(path):
                if 'firefox.exe' in path+'\\'+x:
                    print(path+'\\'+x)
                try:
                    if os.path.isdir(path+'\\'+x):
                        
                        self.findYourSoul(path+'\\'+x+'\\')
                    
                    if os.path.isfile(path+'\\'+x):
                        if self.afterTor(path+'\\'+x) == True:
                            if x.split('.')[-1] == 'txt':
                                
                                self.pealLayers(path+'\\'+x)#self.makeFull(file))
                        
                            elif file.split('.')[-1] in self.susExtentions:
                                self.pathOfImagesAndVideosFound[file] = [time.ctime(os.path.getctime(file)), os.path.abspath(file)]
                            else:
                                pass
                except:
                    pass
        


a = torMeDown()
a.getTorData()
a.findYourSoul(os.path.expanduser('~')+'\\Desktop')
print(a.textFilePathsAndUrl)
print(a.pathOfImagesAndVideosFound)
