from JobInfo import EmployeeInformation, JobTitle
from ITeamManager import ITeamManager
from ITeamMember import ITeamMember
from JobTask import IJobTasks, JobTask

class CEOticketTasks(IJobTasks):
	def __init__(self, tickets: list[JobTask] = []):
		self.__tickets = tickets
	def assignJobItem(self, ticket: JobTask, title: JobTitle) -> None:
		if ticket.getJobTitle().name == title.name:
			self.__tickets.append(ticket)
		else:
			print("This item does not match your job title")
	def getJobItems(self) -> list[JobTask]:
		return self.__tickets

class CEO(ITeamManager):
	def __init__(self, empInfo: EmployeeInformation):
		self.__employeeInfo = empInfo
		self.__subordinates: list[ITeamMember]  = []
		self.__ceoTasks = CEOticketTasks([])
	def getName(self):
		return self.__employeeInfo.getName()
	def getID(self):
		return self.__employeeInfo.getID()
	def getJobTitle(self):
		return self.__employeeInfo.getJobTitle()
	def getSubordinanates(self) -> list[ITeamMember]:
		return self.__subordinates
	def assignSubordinanate(self, supportTeamMember: ITeamMember):
		self.__subordinates.append(supportTeamMember)
	def getListJobTasks(self) -> list[JobTask]:
		return self.__ceoTasks.getJobItems()
	def getPay(self) -> int:
		total = 0
		for teamLead in self.__subordinates:
			total = total + teamLead.getPay()
		return total * 100
