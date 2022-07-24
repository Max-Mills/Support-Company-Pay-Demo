
from ITeamManager import ITeamManager
from CEO import CEO
from ITeamMember import ITeamMember
from JobInfo import EmployeeInformation, JobTitle
from JobTask import JobTask, JobTaskType
from Support import SupportTeamLead, SupportTeamMember, SupportTicketTasks

def buildEmployees():
	samaraEmpInfo = EmployeeInformation("Samara", "4321", JobTitle.SupportTier1)
	iggyEmpInfo = EmployeeInformation("Iggy", "111", JobTitle.SupportTier3)
	gcEmpInfo = EmployeeInformation("GC", "1111", JobTitle.SupportManager)
	maxEmpInfo = EmployeeInformation("Max", "1234", JobTitle.SupportTier2)
	jasonEmpInfo = EmployeeInformation("Jason", "1", JobTitle.CEO)
	beatriceEmpInfo = EmployeeInformation("Beatrice", "2222", JobTitle.SupportTier2)

	max = SupportTeamLead(maxEmpInfo, SupportTicketTasks([]), [])
	beatrice = SupportTeamMember(beatriceEmpInfo, SupportTicketTasks([]))
	samara = SupportTeamMember(samaraEmpInfo, SupportTicketTasks([]))
	iggy = SupportTeamMember(iggyEmpInfo, SupportTicketTasks([]))
	gc = SupportTeamLead(gcEmpInfo,SupportTicketTasks([]), [])
	jason = CEO(jasonEmpInfo,[])

	max.assignSubordinanate(samara)
	max.assignSubordinanate(beatrice)
	gc.assignSubordinanate(max)
	gc.assignSubordinanate(iggy)
	jason.assignSubordinanate(gc)

	Ticket1 = JobTask("1", "Help!", JobTaskType.Ticket, JobTitle.SupportTier2)
	Ticket2 = JobTask("1", "Help!", JobTaskType.Ticket, JobTitle.SupportTier3)
	Ticket3 = JobTask("3", "Quick question", JobTaskType.Ticket, JobTitle.SupportTier1)
	Ticket4 = JobTask("4", "Feature Request", JobTaskType.Ticket, JobTitle.SupportTier1)

	beatrice.assignTicketToSelf(Ticket1)
	samara.assignTicketToSelf(Ticket3)
	samara.assignTicketToSelf(Ticket4)
	iggy.assignTicketToSelf(Ticket2)

	printEmpSalary(jason)

def printEmpSalary(ceo: CEO):
	employees: list[ITeamMember] = []
	employees.append(ceo)
	employees = getSubordinatesFromManager(employees, ceo.getSubordinanates())

	for emp in employees:
		print(f"{emp.getName()} is getting paid {emp.getPay()}")

def getSubordinatesFromManager(employees: list, managerSubordinates: list[ITeamManager]):
	for emp in managerSubordinates:
		employees.append(emp)
		if isinstance(emp, ITeamManager):
			employees = getSubordinatesFromManager(employees, emp.getSubordinanates())
	return employees
		
buildEmployees()








