import sets
import SloppyCell.ExprManip as ExprManip
from SloppyCell.ReactionNetworks.Reactions import Reaction

class FluxReaction(Reaction):
	def __init__(self, id, **kwargs):
		self.kineticLaw = 'flux'
		self.stoichiometry = {'reactant': +1}
		self.doKwargsSubstitution(kwargs)
		Reaction.__init__(self, id, self.stoichiometry, self.kineticLaw)

class MichaelisCompetitiveInhibition(Reaction):
	def __init__(self, id, **kwargs):
		self.kineticLaw = 'k*E*S/(Km + (KI/Km)*I + S)'
		self.stoichiometry = {'E': 0,
							  'S': -1,
							  'P': +1,
							  'I': 0}
		self.doKwargsSubstitution(kwargs)
		Reaction.__init__(self, id, self.stoichiometry, self.kineticLaw)

class MichaelisActivation(Reaction):
	def __init__(self, id, **kwargs):
		self.kineticLaw = 'k*E*(ST - S)/(Km + ST - S)'
		self.stoichiometry = {'E': 0,
							  'S': +1}
		self.doKwargsSubstitution(kwargs)
		Reaction.__init__(self, id, self.stoichiometry, self.kineticLaw)

class MichaelisDeactivation(Reaction):
	def __init__(self, id, **kwargs):
		self.kineticLaw = 'k*E*S/(S + Km)'
		self.stoichiometry = {'E':0,
							  'S':-1}
		self.doKwargsSubstitution(kwargs)
		Reaction.__init__(self, id, self.stoichiometry, self.kineticLaw)
