import SloppyCell.ReactionNetworks
import SloppyCell.ReactionNetworks.Reactions as Reactions
from bcreactions import *
#commit test
network = SloppyCell.ReactionNetworks.Network('bc')

network.addCompartment('cell')

# Estrogen Receptor Activation (1)
network.addSpecies('Atase','cell',0.0,typicalValue=10000)
network.addSpecies('Andro','cell',10000,typicalValue=10000)
network.addSpecies('Estr','cell',0.0,typicalValue=10000)
network.addSpecies('Let','cell',0.0,typicalValue=10000)
network.addSpecies('ESR1i','cell',10000,typicalValue=10000)
network.addSpecies('ESR1a','cell',10000,typicalValue=10000)
network.addSpecies('Tam','cell',0.0,typicalValue=10000)

network.addParameter('K1',10.0)
network.addParameter('kpAndro',0.1)
network.addParameter('kpEstr',0.1)
network.addParameter('vEstr',1.0)
network.addParameter('KmAndro',50000)
network.addParameter('KILet',50000)
network.addParameter('kbESR1',0.1)
network.addParameter('kuESR1',1.0)
network.addParameter('vESR1a',1.0)
network.addParameter('KmEstr',50000)
network.addParameter('KITam',50000)

network.addReaction(FluxReaction,
    'AndroProduction',
    reactant='Andro',
    flux='K1')

network.addReaction(Reactions.ExponentialDecayReaction,
    'AndroDestruction',
    species='Andro',
    rate='kpAndro')

network.addReaction(MichaelisCompetitiveInhibition,
    'EstrogenProduction',
    E='Atase',S='Andro',I='Let',P='Estr',
    k='vEstr',Km='KmAndro',KI='KILet')

network.addReaction(Reactions.HeterodimerizationReaction,
    'EstrogenBinding',
    A='Estr',B='ESR1i',dimer='ESR1a',
    rate='kbESR1')

network.addReaction(Reactions.HeterodimerDissociationReaction,
    'EstrogenUnbinding',
    dimer='ESR1a',A='ESR1i',B='Estr',
    rate='kuESR1')

network.addReaction(Reactions.ExponentialDecayReaction,
    'EstrDestruction',
    species='Estr',
    rate='kpEstr')

network.addReaction(MichaelisCompetitiveInhibition,
    'TAMinhibitESTR',
    E='Estr',S='ESR1i',I='Tam',P='ESR1a',
    k='vESR1a',Km='KmEstr',KI='KITam')

# EGF signaling to Erk (2)
network.addSpecies('EGF',10000,typicalValue=10000)
network.addSpecies('ErbB2',10000,typicalValue=10000)
network.addSpecies('ErbB2i',0.0,typicalValue=10000)
network.addSpecies('ErbB2a',0.0,typicalValue=10000)
network.addSpecies('Raf1a',0.0,typicalValue=10000)
network.addSpecies('Erka',0.0,typicalValue=10000)
network.addSpecies('PPTase',5000,typicalValue=5000)
network.addSpecies('DUSP4',0.0,typicalValue=5000)
network.addSpecies('mDUSP4',0.0,typicalValue=100)

network.addParameter('kbEGF',0.1)
network.addParameter('kuEGF',1.0)
network.addParameter('kErbB2Auto',1.0)
network.addParameter('KmErbB2Auto',50000)
network.addParameter('vErbB2Raf1i',2.0,)
network.addParameter('KmErbB2Raf1i',50000)
network.addParameter('Raf1T',50000)
network.addParameter('vESR1Raf1i',2.0)
network.addParameter('KmESR1Raf1i',50000)
network.addParameter('vPPTaseRaf1a',2.0)
network.addParameter('KmPPTaseRaf1a',50000)
network.addParameter('ErkT',50000)
network.addParameter('vRaf1aErka',2.0)
network.addParameter('KmRaf1aErka',50000)
network.addParameter('vErkErbB2a',2.0)
network.addParameter('KmErkErbB2a',50000)
network.addParameter('vDUSP4Erka',2.0)
network.addParameter('KmDUSP4Erka',50000)
network.addParameter('ktlDUSP4',1.0)
network.addParameter('kpmDUSP4',0.1)

network.addReaction(Reactions.HeterodimerizationReaction,
    'EGFBinding',
    A='EGF',B='ErbB2',dimer='ErbB2i',
    rate='kbEGF')

network.addReaction(Reactions.HeterodimerDissociationReaction,
    'EGFUnbinding',
    dimer='ErbB2i',A='EGF',B='ErbB2',
    rate='kuEGF')

network.addReaction(Reactions.SelfCatalyticMichaelisMentenReaction,
    'ErbB2Autophosphorylation',
    S='ErbB2i',P='ErbB2a',
    k='kErbB2Auto',Km='KmErbB2Auto')

network.addReaction(MichaelisActivation,
    'Raf1ActivationByErbB2',
    E='ErbB2a',S='Raf1a',
    ST='Raf1T',k='vErbB2Raf1i',Km='KmErbB2Raf1i')

network.addReaction(MichaelisActivation,
    'Raf1ActivationByESR1',
    E='ESR1a',S='Raf1a',
    ST='Raf1T',k='vESR1Raf1i',Km='KmESR1Raf1i')

network.addReaction(MichaelisDeactivation,
    'Raf1Inactivation',
    E='PPTase',S='Raf1a',
    k='vPPTaseRaf1a',Km='KmPPTaseRaf1a')

network.addReaction(MichaelisActivation,
    'ErkActivationByRaf1',
    E='Raf1a',S='Erka',
    ST='ErkT',k='vRaf1aErka',Km='KmRaf1aErka')

network.addReaction(Reactions.MichaelisMentenReaction,
    'ErbB2DeactivationByErk',
    E='Erka',S='ErbB2a',P='ErbB2i',
    k='vErkErbB2a',Km='KmErkErbB2a')

network.addReaction(MichaelisDeactivation,
    'ErkDeactivation',
    E='DUSP4',S='Erka',
    k='vDUSP4Erka',Km='KmDUSP4Erka')

network.addReaction(Reactions.ConstructionReaction,
    'DUSP4Translation',
    template='mDUSP4',product='DUSP4',
    rate='ktlDUSP4')

network.addReaction(Reactions.ExponentialDecayReaction,
    'mDUSP4Degradation',
    species='mDUSP4',
    rate='kpmDUSP4')

# EGF signaling to p38 (3)
network.addSpecies('RalGTP',10000,typicalValue=10000)
network.addSpecies('p38a',10000,typicalValue=10000)
network.addSpecies('RalGAP',10000,typicalValue=10000)

network.addParameter('RalT',10000)
network.addParameter('vErbB2Ral',2.0)
network.addParameter('KmErbB2Ral',50000)
network.addParameter('vRalGAP',2.0)
network.addParameter('KmRalGAP',50000)
network.addParameter('vDUSP4p38',2.0)
network.addParameter('KmDUSP4p38',50000)
network.addParameter('p38T',10000)
network.addParameter('vRalp38',2.0)
network.addParameter('KmRalp38',50000)

network.addReaction(MichaelisActivation,
    'RalActivation',
    E='ErbB2a',S='RalGTP',
    ST='RalT',k='vErbB2Ral',Km='KmErbB2Ral')

network.addReaction(MichaelisDeactivation,
    'RalDeactivation',
    E='RalGAP',S='RalGTP',
    k='vRalGAP',Km='KmRalGAP')

network.addReaction(MichaelisActivation,
    'p38Activation',
    E='RalGTP',S='p38a',
    ST='p38T',k='vRalp38',Km='KmRalp38')

network.addReaction(MichaelisDeactivation,
    'p38Deactivation',
    E='DUSP4',S='p38a',
    k='vDUSP4p38',Km='KmDUSP4p38')

# Estrogen signaling to Akt (4)
network.addSpecies('PIK3CAa',10000,typicalValue=10000)
network.addSpecies('mAURKA',0.0,typicalValue=100)
network.addSpecies('AURKA',0.0,typicalValue=10000)
network.addSpecies('mAKT',0.0,typicalValue=100)
network.addSpecies('Akti',10000,typicalValue=10000)
network.addSpecies('Akta',0.0,typicalValue=10000)

network.addParameter('PIK3CAT',10000)
network.addParameter('vESR1PIK3CA',2.0)
network.addParameter('KmESR1PIK3CA',50000)
network.addParameter('vPPTasePIK3CA',2.0)
network.addParameter('KmPPTasePIK3CA',50000)
network.addParameter('ktlAKT',1.0)
network.addParameter('kpmAKT',1.0)
network.addParameter('vPIK3CAAkt',2.0)
network.addParameter('KmPIK3CAAkt',50000)
network.addParameter('ktlAURKA',1.0)
network.addParameter('kpmAURKA',1.0)
network.addParameter('vAURKAAkt',2.0)
network.addParameter('KmAURKAAkt',50000)
network.addParameter('vPPTaseAkt',2.0)
network.addParameter('KmPPTaseAkt',50000)

network.addReaction(MichaelisActivation,
    'PIK3CAActivation',
    E='ESR1a',S='PIK3CAa',
    ST='PIK3CAT',k='vESR1PIK3CA',Km='KmESR1PIK3CA')

network.addReaction(MichaelisDeactivation,
    'PIK3CADeactivation',
    E='PPTase',S='PIK3CAa',
    k='vPPTasePIK3CA',Km='KmPPTasePIK3CA')

network.addReaction(Reactions.ConstructionReaction,
    'AURKATranslation',
    template='mAURKA',product='AURKA',
    rate='ktlAURKA')

network.addReaction(Reactions.ExponentialDecayReaction,
    'mAURKADegradation',
    species='mAURKA',
    rate='kpmAURKA')

network.addReaction(Reactions.ConstructionReaction,
    'AktTranslation',
    template='mAKT',product='Akti',
    rate='ktlAKT')

network.addReaction(Reactions.ExponentialDecayReaction,
    'mAKTDegradation',
    species='mAKT',
    rate='kpmAKT')

network.addReaction(Reactions.MichaelisMentenReaction,
    'AktActivationByPIK3CA',
    E='PIK3CAa',S='Akti',P='Akta',
    k='vPIK3CAAkt',Km='KmPIK3CAAkt')

network.addReaction(Reactions.MichaelisMentenReaction,
    'AktActivationByAURKA',
    E='AURKA',S='Akti',P='Akta',
    k='vAURKAAkt',Km='KmAURKAAkt')

network.addReaction(Reactions.MichaelisMentenReaction,
    'AktDeactivation',
    E='PPTase',S='Akta',P='Akti',
    k='vPPTaseAkt',Km='KmPPTaseAkt')




network.compile()
