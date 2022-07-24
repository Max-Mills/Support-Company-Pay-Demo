from abc import ABC, abstractmethod
from JobTask import JobTask, IJobTasks

class ITeamMember(ABC):
	@abstractmethod
	def getName(self):
		pass
	@abstractmethod
	def getID(self):
		pass
	@abstractmethod
	def getJobTitle(self):
		pass
	@abstractmethod
	def getListJobTasks(self) -> list[JobTask]:
		pass
	@abstractmethod
	def getPay(self) -> int:
		pass