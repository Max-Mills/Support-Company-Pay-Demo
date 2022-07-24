from enum import Enum
from abc import ABC, abstractmethod
from JobInfo import JobTitle

class JobTaskType(Enum):
	Ticket = 1
	Email = 1
	Call = 2
	GainsightCTA = 3

class IJobTasks(ABC):
	@abstractmethod
	def assignJobItem(self, JobItem):
		pass
	def getJobItems(self):
		pass

class JobTask:
	def __init__(self, id: str, subject: str, taskType: JobTaskType, jobTitle: JobTitle):
		self.__id = id
		self.__subject = subject
		self.__taskType = taskType
		self.__jobTitle = jobTitle
	def getID(self):
		return self.__id
	def getSubject(self):
		return self.__subject
	def getJobTitle(self):
		return self.__jobTitle
	def getTaskType(self):
		return self.__taskType