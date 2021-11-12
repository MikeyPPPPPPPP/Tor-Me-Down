#this code will get the  installation date of tor and grab the path and name of all images/videos downloaded after that (Windows)

import os
import time
import string

class torMeDown:
	'''this code will get the  installation date of tor and grab the path and name of all images/videos downloaded after that (Windows)'''
	def __init__(self):
		self.desktop = os.path.extendsuser('~')
		self.appdata = os.path.extendsuser('AppData')
		self.drives = [x for x in list(string.ascii_uppercase) if os.path.exists(x+':\\') == True]

		self.susExtentions = ('png','jpeg','jpg', 'mov', 'mp4')
		self.torLoaction = ''#
		self.torInstallationDate = ''#
		self.pathOfImagesAndVideosFound = {}#   {name:[time, path]}
		self.textFilePathsAndUrl = {}
		self.possibleOnionUrlsInTextFiles = {}			#{ path:[ urls ] }

	def makeFull(self, file):
		return os.path.abspath(file)

	def afterTor(self, file):
		return self.torInstallationDate < makeFull(file)

	def getTorData(self):
		if os.path.exists(os.path.extendsuser('~')+'\\AppData\\Roaming\\tor\\tor.exe'):
			self.torLoaction = os.path.extendsuser('~')+'\\AppData\\Roaming\\tor\\tor.exe'
			self.torInstallationDate = time.ctime(os.path.getctime(os.path.extendsuser('~')+'\\AppData\\Roaming\\tor\\tor.exe'))

	def getData(self, file):
		return time.ctime(os.path.getctime(makeFull(file)))

	def pealLayers(self, file):
		'''this function searches a give file for .onion in it'''
		self.onionUrls = []
		with open(makeFull(file), 'r') as peal:
			for line in peal.readlines():
				if '.onion' in line:
					self.onionUrls.append(line)
		self.textFilePathsAndUrl[file]=self.onionUrls


	def findYourSoul(self):
		'''this function searches the computer for files made AFTER the instilation of tor'''
		self.base = [os.path.extendsuser('~')+'\\Desktop']

		#this will do a base search (desktop) befor the full search
		for root, dirs, files in os.walk(self.base):
		    path = root.split(os.sep)
		    for file in files:
		    	if afterTor(file):
			    	if file.split('.')[-1] == 'txt':
			        	self.pealLayers(self.makeFull(file))
			        elif file.split('.')[-1] in self.susExtentions:
			        	self.pathOfImagesAndVideosFound[file] = [time.ctime(os.path.getctime(file)), os.path.abspath(file)]
			        else:
			        	pass

		for x in self.drives:
			for root, dirs, files in os.walk(x+':\\'):
			    path = root.split(os.sep)
			    for file in files:
			    	if afterTor(file):
				    	if file.split('.')[-1] == 'txt':
				        	self.pealLayers(self.makeFull(file))
				        elif file.split('.')[-1] in self.susExtentions:
				        	self.pathOfImagesAndVideosFound[file] = [time.ctime(os.path.getctime(file)), os.path.abspath(file)]
				        else:
				        	pass


