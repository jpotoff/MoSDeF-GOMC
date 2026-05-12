import sys
from unyt import unyt_quantity
from mosdef_gomc.formats.gmso_gomc_conf_writer import GOMCControl

class DummyCharmm:
    def __init__(self):
        self.filename_box_1 = "box1"
        self.filename_box_0 = "box0"
        self.electrostatic_1_4 = 1.0
        self.residues = ["RES"]
        self.all_res_unique_atom_name_dict = {"RES": ["O"]}
        self.box_0_vectors = [10.0, 10.0, 10.0]
        self.box_1_vectors = [10.0, 10.0, 10.0]
        self.combining_rule = "lorentz"
        self.utilized_NB_expression = "LJ"

charmm_obj = DummyCharmm()

inputs = {
    "RunSteps": 100000,
    "RestartFreq": [True, 50000],
    "ChemPot": {"RES": 1.0},
    "VDWGeometricSigma": False
}

try:
    gomc_control = GOMCControl(
        "GCMC", 
        unyt_quantity(298.0, 'K'), 
        100000, 
        "ff.inp", 
        "box0.pdb", 
        "box0.psf", 
        charmm_obj, 
        inputs
    )
    print("RestartFreq in object:", gomc_control.RestartFreq)
except Exception as e:
    import traceback
    traceback.print_exc()
