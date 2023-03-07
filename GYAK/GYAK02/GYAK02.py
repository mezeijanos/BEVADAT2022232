# %%
import numpy as np

# %%
#FONTOS!!!

# CSAK OTT LEHET HASZNÁLNI FOR LOOP-OT AHOL A FELADAT KÜLÖN KÉRI!
# [1,2,3,4] --> ezek az értékek np.array-ek. Ahol listát kérek paraméterként ott külön ki fogom emelni!
# Ha végeztél a feladatokkal, akkor notebook-ot alakítsd át .py.
# A FÁJLBAN CSAK A FÜGGVÉNYEK LEGYENEK! (KOMMENTEK MARADHATNAK)

# %%


# %%
#Készíts egy függvényt ami létre hoz egy nullákkal teli numpy array-t.
#Paraméterei: mérete (tuple-ként), default mérete pedig legyen egy (2,2)
#Be: (2,2)
#Ki: [[0,0],[0,0]]
#create_array()

# %%
def create_array(size = (2,2)) -> np.array:
    return np.zeros(size)



# %%
#Készíts egy függvényt ami a paraméterként kapott array-t főátlóját feltölti egyesekkel
#Be: [[1,2],[3,4]]
#Ki: [[1,2],[3,1]]
#set_one()

# %%
def set_one(array: np.array) -> np.array:   #fill_diagonal view, nincs visszatérési értéke, eredetit módosítja
    np.fill_diagonal(array,1)
    return array

#a = np.array([[1,2],[3,4]])
#print(set_one(a))

# %%
# Készíts egy függvényt ami transzponálja a paraméterül kapott mártix-ot:
# Be: [[1, 2], [3, 4]]
# Ki: [[1, 3], [2, 4]]
# do_transpose()

# %%
def do_transpose(matrix: np.array) -> np.array:
    mx = np.transpose(matrix)
    return mx

#a = np.array([[1,2],[3,4]])
#print(do_transpose(a))

# %%
# Készíts egy olyan függvényt ami az array-ben lévő értékeket N tizenedjegyik kerekíti, ha nincs megadva ez a paraméter, akkor legyen az alapértelmezett a kettő 
# Be: [0.1223, 0.1675], 2
# Ki: [0.12, 0.17]
# round_array()

# %%
def round_array(array: np.array, decimals: int = 2) -> np.array:
    arr = np.around(array, decimals)
    return arr

#a = np.array([0.1223, 0.1675])
#print(round_array(a, 3))


# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 0 - False-ra, az 1 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ True False False], [ True  True  True], [False False False]]
# bool_array()

# %%
def bool_array(arr: np.array) -> np.array:
    return np.array(arr, dtype=bool)

#a = [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
#print(bool_array(a))

# %%
# Készíts egy olyan függvényt, ami a bementként kapott 0 és 1 ből álló tömben a 1 - False-ra az 0 True-ra cserélni
# Be: [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
# Ki: [[ False True True], [ False  False  False], [True True True]]
# invert_bool_array()

# %%
def invert_bool_array(arr: np.array) -> np.array:
    return np.logical_not(arr)

#a = [[1, 0, 0], [1, 1, 1],[0, 0, 0]]
#print(invert_bool_array(a))

# %%
# Készíts egy olyan függvényt ami a paraméterként kapott array-t kilapítja
# Be: [[1,2], [3,4]]
# Ki: [1,2,3,4]
# flatten()


# %%
def flatten(arr: np.array) -> np.array:
  #return arr.flatten()
  #flattened = arr.flatten()
  flattened = np.ravel(arr)
  return flattened

#a = np.array([[1, 0, 0], [1, 1, 1],[0, 0, 0]])
#a = [[1, 0, 0], [1, 1, 1], [0, 0, 0]]
#print(flatten(a))


