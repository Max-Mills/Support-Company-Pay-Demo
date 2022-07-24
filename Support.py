from JobTask import JobTask, IJobTasks
from JobInfo import JobTitle, EmployeeInformation
from ITeamManager import ITeamManager
from ITeamMember import ITeamMember

class SupportTicketTasks(IJobTasks):
	def __init__(self, tickets: list[JobTask] = []):
		self.__tickets = tickets
	def assignJobItem(self, ticket: JobTask, title: JobTitle) -> None:
		if ticket.getJobTitle().name == title.name:
			self.__tickets.append(ticket)
		else:
			print("This item does not match your job title")
	def getJobItems(self) -> list[JobTask]:
		return self.__tickets

class SupportTeamMember(ITeamMember):
	def __init__(self, employeeInfo: EmployeeInformation) -> None:
		self.__employeeInfo = employeeInfo
		self.__supportTicketTasks = SupportTicketTasks([])
	def getName(self):
		return self.__employeeInfo.getName()
	def getID(self):
		return self.__employeeInfo.getID()
	def getJobTitle(self):
		return self.__employeeInfo.getJobTitle()
	def getListJobTasks(self) -> list[JobTask]:
		return self.__supportTicketTasks.getJobItems()
	def getPay(self) -> int:
		return len(self.getListJobTasks()) * 2 
	def assignTicketToSelf(self, ticket: JobTask):
		self.__supportTicketTasks.assignJobItem(ticket, self.getJobTitle())

class SupportTeamLead(ITeamManager):
	def __init__(self, employeeInfo: EmployeeInformation) -> None:
		self.__employeeInfo = employeeInfo
		self.__supportTicketTasks = SupportTicketTasks([])
		self.__subordinates: list[ITeamMember] = []
	def getName(self):
		return self.__employeeInfo.getName()
	def getID(self):
		return self.__employeeInfo.getID()
	def getJobTitle(self):
		return self.__employeeInfo.getJobTitle()
	def getEmployeeInformation(self):
		return self.__employeeInfo
	def getListJobTasks(self) -> list[JobTask]:
		return self.__supportTicketTasks.getJobItems()
	def getSubordinanates(self) -> list[ITeamMember]:
		return self.__subordinates
	def assignSubordinanate(self, supportTeamMember: ITeamMember):
		self.__subordinates.append(supportTeamMember)
	def getPay(self) -> int:
		totalTickets = 0
		for supMember in self.getSubordinanates():
			totalTickets = totalTickets + len(supMember.getListJobTasks())
		return totalTickets * 2 



