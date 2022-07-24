from enum import Enum

class JobTitle(Enum):
	SupportTier1 = 1
	SupportTier2 = 2
	SupportTier3 = 3
	SupportManager = 4
	CEO = 6
	
class EmployeeInformation:
	def __init__(self, name: str, id: str, jobTitle: JobTitle):
		self.__name = name
		self.__id = id
		self.__jobTitle = jobTitle
	def getName(self):
		return self.__name
	def getID(self):
		return self.__id
	def getJobTitle(self):
		return self.__jobTitle