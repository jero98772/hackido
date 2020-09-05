from random import randrange
class feelings():
	def __init__(self,feelsFile):
		self.feelsFile = str(feelsFile)
	def feelsIntxt(self):
		self.feelsList = []
		with open(self.feelsFile, 'r') as self.feels:
			for self.feel in self.feels.readlines():
				self.feelsList.append(str(self.feel).replace("\n",""))
		return self.feelsList
	def rndChouseFeel(self):
		self.rnd = randrange(len(self.feelsList))
		self.rndFeel = self.feelsList[self.rnd]
		return self.rndFeel
	def rndChouseFeels(self,times):
		self.times = times
		self.i = 0
		self.rndFeelsList = []
		while self.i < self.times:
			self.rnd = randrange(len(self.feelsList))
			self.rndFeel = self.feelsList[self.rnd]
			if not (self.rndFeel in self.rndFeelsList) :
				self.rndFeelsList.append(self.rndFeel)
				self.i += 1
		else:
			return self.rndFeelsList
	def opcionFeels(self):
		self.feelOpcions =["escoje un sentimiento"]
		for self.feel in self.feelsList:
			self.feelOpcions.append(self.feel)
		return self.feelOpcions