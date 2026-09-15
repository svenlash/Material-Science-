#модуль chem - чтение молекул и работа со связями 
#chem.molsurf - расчет молекулярных свойства 
#TPSA (Topological Polar Surface Area) — площадь полярных атомов (O, N + связанные H)
#ASA (Accessible Surface Area) — площадь поверхности молекулы, доступная для растворителя (все атомы)
from rdkit import Chem 
from rdkit.Chem import MolSurf
ciguatoxin = "ciguatoxin.mol"
mol = Chem.MolFromMolFile(ciguatoxin)

if mol is None: 
    print('ошибка')
else:
    TPSA = MolSurf.TPSA(mol)
    ASA = MolSurf.LabuteASA(mol)
    print(f"Polar Surface Area (TPSA):{TPSA:.2f}Å²")
    print(f"Labute ASA: {ASA:.2f}Å²")
