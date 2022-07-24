from abc import abstractmethod
from ITeamMember import ITeamMember

class ITeamManager(ITeamMember):
	@abstractmethod
	def getSubordinanates(self) -> list[ITeamMember]:
		pass
	@abstractmethod
	def assignSubordinanate(self, supportTeamMember: ITeamMember):
		pass