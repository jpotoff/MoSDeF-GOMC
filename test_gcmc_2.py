import sys
from unyt import unyt_quantity

sys.path.insert(0, "/home/ai8111/mosdef/MoSDeF-GOMC")
from mosdef_gomc.formats.gmso_gomc_conf_writer import GOMCControl
from mosdef_gomc.formats.gmso_charmm_writer import Charmm

class MockCharmm(Charmm):
    def __init__(self):
        self.filename_box_1 = "box1"
        self.filename_box_0 = "box0"
        self.electrostatic_1_4 = 1.0
        self.residues = ["RES"]
        self.all_res_unique_atom_name_dict = {"RES": ["O"]}
        self.box_0_vectors = [[10.0, 0.0, 0.0], [0.0, 10.0, 0.0], [0.0, 0.0, 10.0]]
        self.box_1_vectors = [[10.0, 0.0, 0.0], [0.0, 10.0, 0.0], [0.0, 0.0, 10.0]]
        self.combining_rule = "lorentz"
        self.utilized_NB_expression = "LJ"
        self.ff_filename = "ff.inp"

charmm_obj = MockCharmm()

inputs = {
    "RestartFreq": [True, 50000],
    "CheckpointFreq": [True, 50000],
    "ChemPot": {"RES": unyt_quantity(1.0, "kJ/mol")},
    "VDWGeometricSigma": False
}

try:
    gomc_control = GOMCControl(
        charmm_obj, 
        "GCMC", 
        1000000, 
        unyt_quantity(298.0, 'K'), 
        check_input_files_exist=False,
        input_variables_dict=inputs
    )
    print("RestartFreq in object:", gomc_control.RestartFreq)
    print("CheckpointFreq in object:", gomc_control.CheckpointFreq)
except Exception as e:
    import traceback
    traceback.print_exc()
