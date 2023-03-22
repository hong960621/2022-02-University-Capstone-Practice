from pymatgen.core import Lattice, Structure, Molecule
import json
    
coords = [[0, 0, 0], [0.75,0.5,0.75]]
lattice = Lattice.from_parameters(a=3.84, b=3.84, c=3.84, alpha=120,
                                      beta=90, gamma=60)
struct = Structure(lattice, ["Si", "Si"], coords)
    
coords = [[0.000000, 0.000000, 0.000000],
         [0.000000, 0.000000, 1.089000],
         [1.026719, 0.000000, -0.363000],
         [-0.513360, -0.889165, -0.363000],
         [-0.513360, 0.889165, -0.363000]]
methane = Molecule(["C", "H", "H", "H", "H"], coords)
    
print(struct)
print(methane)
    
with open('structure.json','w') as f:
    json.dump(struct.as_dict(), f)