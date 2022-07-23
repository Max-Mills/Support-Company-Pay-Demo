from enum import Enum
from abc import ABC, abstractmethod

class EmployeeInformation:
	def __init__(self, name: str, id: str):
		self.name = name
		self.id = id
	def getName(self):
		return self.name
	def getID(self):
		self.id

class CalculatePay(ABC):
	@abstractmethod
	def getPay(self) -> int:
		pass

class Tiers(Enum):
	Tier1 = 1
	Tier2 = 2
	Tier3 = 3

class Ticket():
	def __init__(self, id: str, subject: str, tier: Tiers):
		self.id = id
		self.subject = subject
		self.tier = tier

class SupportInfo():
	def __init__(self, tier: Tiers, tickets: list[Ticket] = []):
		self.tier = tier
		self.tickets = tickets
	def assignTicket(self, ticket: Ticket):
		if ticket.tier.value == self.tier.value:
			self.tickets.append(ticket)
		else:
			print("Not the same Tier")
	def getTickets(self):
		return self.tickets

class SupportTeamMember(CalculatePay):
	def __init__(self, empInfo: EmployeeInformation, supInfo: SupportInfo):
		self.empInfo = empInfo
		self.supInfo = supInfo
	def getPay(self) -> int:
		return self.supInfo.tier.value * len(self.supInfo.tickets)

class IManages(ABC):
	@abstractmethod
	def getSubordinanates(self) -> list[str]:
		pass
	@abstractmethod
	def assignSubordinanate(self, supportTeamMember: SupportTeamMember) -> list[str]:
		pass

class SupportTeamLead(SupportTeamMember, IManages):
	def __init__(self, empInfo: EmployeeInformation, supInfo: SupportInfo, subordinates: list[SupportTeamMember] = []) -> None:
		super().__init__(empInfo, supInfo)
		self.subordinates = subordinates
	def getSubordinanates(self) -> list[SupportTeamMember]:
		return self.subordinates
	def assignSubordinanate(self, supportTeamMember: SupportTeamMember):
		self.subordinates.append(supportTeamMember)
	def getPay(self) -> int:
		totalTickets = 0
		for supMember in self.getSubordinanates():
			totalTickets = totalTickets + len(supMember.supInfo.getTickets())
		return totalTickets * 2 
		

class CEO(CalculatePay, IManages):
	def __init__(self, empInfo: EmployeeInformation, subordinates: list[SupportTeamMember] = []):
		self.empInfo = empInfo
		self.subordinates = subordinates
	def getSubordinanates(self) -> list[SupportTeamMember]:
		return self.subordinates
	def assignSubordinanate(self, supportTeamLead: SupportTeamLead) -> None:
		return self.subordinates.append(supportTeamLead)
	def getPay(self) -> int:
		total = 0
		for supLead in self.subordinates:
			total = total + supLead.getPay()
		return total * 10
		

def buildEmployees():
	samaraEmpInfo = EmployeeInformation("Samara", "4321")
	iggyEmpInfo = EmployeeInformation("Iggy", "111")
	gcEmpInfo = EmployeeInformation("GC", "1111")
	maxEmpInfo = EmployeeInformation("Max", "1234")
	jasonEmpInfo = EmployeeInformation("Jason", "1")
	beatriceEmpInfo = EmployeeInformation("Beatrice", "2222")

	samaraSupInfo = SupportInfo(Tiers.Tier1, [])
	maxSupInfo = SupportInfo(Tiers.Tier2, [])
	beatriceSupInfo = SupportInfo(Tiers.Tier2, [])
	iggySupInfo = SupportInfo(Tiers.Tier3, [])
	gcSupInfo = SupportInfo(Tiers.Tier3, [])

	max = SupportTeamLead(maxEmpInfo, maxSupInfo, [])
	beatrice = SupportTeamMember(beatriceEmpInfo, beatriceSupInfo)
	samara = SupportTeamMember(samaraEmpInfo, samaraSupInfo)
	iggy = SupportTeamMember(iggyEmpInfo, iggySupInfo)
	gc = SupportTeamLead(gcEmpInfo, gcSupInfo, [])
	jason = CEO(jasonEmpInfo,[])

	max.assignSubordinanate(samara)
	max.assignSubordinanate(beatrice)
	gc.assignSubordinanate(max)
	gc.assignSubordinanate(iggy)
	jason.assignSubordinanate(gc)
	
	Ticket1 = Ticket("1", "Help!", Tiers.Tier2)
	Ticket2 = Ticket("2", "Everything is on fire!", Tiers.Tier3)
	Ticket3 = Ticket("3", "Quick question", Tiers.Tier1)
	Ticket4 = Ticket("4", "Feature Request", Tiers.Tier1)

	beatrice.supInfo.assignTicket(Ticket1)
	samara.supInfo.assignTicket(Ticket3)
	samara.supInfo.assignTicket(Ticket4)
	iggy.supInfo.assignTicket(Ticket2)


	printEmpSalery(jason)

def printEmpSalery(ceo: CEO):
	employees: list = []
	employees.append(ceo)
	employees = getSubordinatesFromManager(employees, ceo)

	for emp in employees:
		print(f"{emp.empInfo.getName()} is getting paid {emp.getPay()}")

def getSubordinatesFromManager(employees: list, manager: IManages):
	for emp in manager.getSubordinanates():
		employees.append(emp)
		if isinstance(emp, IManages):
			employees = getSubordinatesFromManager(employees, emp)
	return employees
		
		
buildEmployees()








