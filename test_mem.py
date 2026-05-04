import mbuild as mb
import gmso
from mosdef_gomc.formats.gmso_charmm_writer import Charmm

class Water(mb.Compound):
    def __init__(self):
        super(Water, self).__init__()
        self.add(mb.Particle(name='O', pos=[0, 0, 0]), label='O')
        self.add(mb.Particle(name='H', pos=[0.1, 0, 0]), label='H1')
        self.add(mb.Particle(name='H', pos=[0, 0.1, 0]), label='H2')
        self.add_bond((self[0], self[1]))
        self.add_bond((self[0], self[2]))

box = mb.Box(lengths=[100, 100, 100])
waters = mb.fill_box(Water(), n_compounds=5000, box=box)
waters.name = 'H2O'
print("Waters built")

# Just call Charmm with fake inputs, maybe we can mock it or just pass it in?
# We might need to give it a forcefield...
# Let's just create a mock topology and call unique_atom_naming directly!
from mosdef_gomc.formats.gmso_charmm_writer import unique_atom_naming
top = waters.to_gmso()
print("Converted to GMSO")

residue_id_list = [1 for _ in range(top.n_sites)]
residue_names_list = ['H2O' for _ in range(top.n_sites)]

import time
start = time.time()
unique_atom_naming(top, residue_id_list, residue_names_list)
end = time.time()
print(f"unique_atom_naming took {end - start} seconds")

