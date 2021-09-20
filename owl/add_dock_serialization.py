from owlready2 import *

onto = get_ontology("new_onthology.owl")
onto.load()

with onto:

    def to_json(self):
        return {
            'VelocityWind': self.VelocityWind,
            'VelocityCurrent': self.VelocityCurrent,
        }

    onto.Dock.to_json = to_json

onto.save('navy_docking.owl')