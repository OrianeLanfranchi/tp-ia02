from typing import List, Tuple
import pprint
import os
import itertools
import subprocess

#model
model = [-1, -2, -3, -4, 5, -6, -7, -8, -9, -10, -11, 12, -13, -14, -15, -16, -17, -18, -19, -20, -21, 22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, 33, -34, -35, -36, -37, -38, -39, -40, -41, -42, 43, -44, -45, -46, -47, -48, -49, -50, -51, -52, 53, -54, -55, -56, -57, -58, -59, -60, -61, -62, 63, 64, -65, -66, -67, -68, -69, -70, -71, -72, -73, 74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, 87, -88, -89, -90, -91, -92, -93, -94, -95, -96, 97, -98, -99, -100, 101, -102, -103, -104, -105, -106, -107, -108, 109, -110, -111, -112, -113, -114, -115, -116, -117, -118, -119, -120, -121, -122, -123, -124, -125, 126, -127, -128, -129, -130, 131, -132, -133, -134, -135, -136, -137, 138, -139, -140, -141, -142, -143, -144, -145, -146, -147, 148, -149, -150, -151, -152, -153, -154, -155, -156, -157, -158, -159, -160, 161, -162, 163, -164, -165, -166, -167, -168, -169, -170, -171, -172, -173, -174, -175, -176, -177, -178, -179, 180, -181, -182, -183, -184, -185, -186, -187, 188, -189, -190, -191, 192, -193, -194, -195, -196, -197, -198, -199, -200, -201, 202, -203, -204, -205, -206, -207, -208, 209, -210, -211, -212, -213, -214, -215, -216, -217, -218, -219, -220, 221, -222, -223, -224, -225, -226, -227, -228, -229, -230, 231, -232, -233, -234, -235, -236, -237, -238, -239, -240, 241, -242, -243, -244, -245, -246, -247, -248, -249, -250, 251, -252, -253, -254, -255, -256, 257, -258, -259, -260, -261, -262, -263, -264, -265, -266, -267, -268, -269, 270, -271, -272, -273, -274, -275, -276, 277, -278, -279, -280, -281, -282, -283, -284, 285, -286, -287, -288, 289, -290, -291, -292, -293, -294, -295, -296, -297, -298, -299, -300, 301, -302, -303, -304, -305, -306, -307, 308, -309, -310, -311, -312, -313, -314, -315, -316, -317, 318, -319, -320, -321, -322, -323, -324, -325, -326, -327, 328, -329, -330, -331, -332, -333, -334, 335, -336, -337, -338, -339, -340, -341, -342, -343, -344, -345, -346, -347, 348, -349, -350, -351, -352, -353, -354, -355, -356, -357, -358, 359, -360, -361, -362, -363, -364, 365, -366, -367, -368, -369, -370, -371, 372, -373, -374, -375, -376, -377, -378, -379, -380, -381, -382, -383, -384, 385, -386, -387, -388, -389, -390, -391, -392, -393, -394, -395, 396, 397, -398, -399, -400, -401, -402, -403, -404, -405, -406, -407, -408, -409, -410, -411, 412, -413, -414, 415, -416, -417, -418, -419, -420, -421, -422, -423, -424, -425, 426, -427, -428, -429, -430, -431, -432, -433, -434, -435, -436, -437, -438, -439, -440, 441, -442, 443, -444, -445, -446, -447, -448, -449, -450, -451, -452, -453, 454, -455, -456, -457, -458, -459, -460, -461, -462, -463, -464, -465, -466, 467, -468, -469, -470, -471, -472, 473, -474, -475, -476, -477, -478, -479, -480, -481, -482, 483, -484, -485, -486, -487, -488, -489, -490, -491, -492, -493, -494, 495, -496, -497, -498, -499, -500, 501, -502, -503, -504, 505, -506, -507, -508, -509, -510, -511, -512, -513, -514, -515, -516, -517, 518, -519, -520, -521, -522, -523, -524, 525, -526, -527, -528, -529, -530, -531, -532, -533, -534, -535, -536, -537, 538, -539, -540, -541, 542, -543, -544, -545, -546, -547, -548, -549, -550, -551, -552, -553, -554, -555, -556, 557, -558, -559, -560, -561, 562, -563, -564, -565, -566, -567, -568, 569, -570, -571, -572, -573, -574, -575, -576, -577, -578, -579, -580, -581, -582, -583, 584, -585, -586, -587, -588, -589, -590, -591, 592, -593, -594, -595, -596, -597, 598, -599, -600, -601, -602, -603, 604, -605, -606, -607, -608, -609, -610, -611, -612, -613, -614, -615, -616, -617, -618, -619, -620, 621, -622, -623, -624, -625, -626, 627, -628, -629, -630, -631, -632, 633, -634, -635, -636, -637, -638, -639, -640, -641, -642, -643, 644, -645, -646, -647, -648, -649, -650, 651, -652, -653, -654, -655, -656, -657, -658, -659, -660, 661, -662, -663, -664, -665, -666, -667, -668, -669, -670, 671, -672, -673, -674, -675, -676, 677, -678, -679, -680, -681, -682, -683, -684, -685, -686, -687, -688, -689, -690, -691, 692, -693, -694, -695, -696, -697, -698, 699, -700, -701, -702, 703, -704, -705, -706, -707, -708, -709, -710, -711, -712, -713, -714, -715, -716, -717, 718, -719, -720, -721, -722, -723, -724, -725, -726, -727, -728, 729]

# alias de types
Grid = List[List[int]]
PropositionnalVariable = int
Literal = int
Clause = List[Literal]
ClauseBase = List[Clause]
Model = List[Literal]

example: Grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


example2: Grid = [
    [0, 0, 0, 0, 2, 7, 5, 8, 0],
    [1, 0, 0, 0, 0, 0, 0, 4, 6],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 0, 8, 1, 0, 0, 0, 0],
    [4, 0, 6, 3, 0, 1, 0, 0, 9],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 2, 0, 0, 0, 0, 3, 1, 0],
]


empty_grid: Grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

#### fonctions fournies


def write_dimacs_file(dimacs: str, filename: str):
    with open(filename, "w", newline="") as cnf:
        cnf.write(dimacs)


def exec_gophersat(
    filename: str, cmd: str = "gophersat", encoding: str = "utf8"
) -> Tuple[bool, List[int]]:
    result = subprocess.run(
        [cmd, filename], capture_output=True, check=True, encoding=encoding
    )
    string = str(result.stdout)
    lines = string.splitlines()

    if lines[1] != "s SATISFIABLE":
        return False, []

    model = lines[2][2:-2].split(" ")

    return True, [int(x) for x in model]


### fonctions utilitaires


def cell_to_variable(i: int, j: int, val: int) -> PropositionnalVariable:
    # cell to variable
    return i * 9 * 9 + j * 9 + val + 1


def variable_to_cell(var: PropositionnalVariable) -> Tuple[int, int, int]:
    # variable to cell
    var = var - 1
    i = var // (9 * 9)
    j = var % (9 * 9) // 9
    val = var % 9
    return i, j, val


def model_to_grid(model: Model, nb_vals: int = 9) -> Grid:
    # model to grid
    sudoku = []
    for i in range(nb_vals):
        ligne = []
        for j in range(nb_vals):
            for k in range(nb_vals):
                if model[cell_to_variable(i, j, k - 1)] > 0:
                    ligne.append(
                        (model[cell_to_variable(i, j, k - 1)] - 1) % nb_vals + 1
                    )
        sudoku.append(ligne)
    return sudoku


### fonctions contraintes génériques


def at_least_one(variables: List[PropositionnalVariable]) -> Clause:
    # at least one
    clause = []
    for var in variables:
        clause.append(var)
    return clause


def unique(variables: List[PropositionnalVariable]) -> ClauseBase:
    # unique
    reverse = []
    clause = []
    for var in variables:
        reverse.append(-var)
    combinations = [list(x) for x in itertools.combinations(reverse, 2)]
    clause.append(at_least_one(variables))
    for combination in combinations:
        clause.append(combination)
    return clause


### contraintes sudoku
def create_cell_constraints() -> ClauseBase:
    # cell constraints
    clause = []
    for i in range(0, 729, 9):
        clause += unique(
            [1 + i, 2 + i, 3 + i, 4 + i, 5 + i, 6 + i, 7 + i, 8 + i, 9 + i]
        )
    return clause

def create_line_constraints() -> ClauseBase :
    # line constraints
    clauses = []
    for i in range(9):
        for var in range(9):
            liste = []
            for j in range(9):
                liste.append(cell_to_variable(i, j, var))
            clauses.append(at_least_one(liste))
    return clauses

def create_column_constraints() -> ClauseBase :
    # column constraints
    clauses = []
    for i in range(9):
        for var in range(9):
            liste = []
            for j in range(9):
                liste.append(cell_to_variable(j, i, var))
            clauses.append(at_least_one(liste))
    return clauses

def create_box_constraints() -> ClauseBase :
    # box constraints
    clause = []
    for i in range(3) :
        for j in range(3) :
            for z in range(9) :
                liste = []
                for x in range(3) :
                    for y in range(3) :
                        liste.append((3 * j + y) * 9 + (3 * i + x) * 81 + z + 1)
                clause.append(at_least_one(liste))
    return clause

def create_value_constraints(grid: Grid) -> ClauseBase :
    #rconstraints values
    clause = []
    for i in range(9) :
        for j in range(9) :
            if grid[i][j] != 0 :
                clause.append(
                    [cell_to_variable(i, j, grid[i][j] - 1)]
                )
    return clause

def generate_problem(grid: Grid) -> ClauseBase  :
    clause = []
    clause += create_cell_constraints()
    clause += create_line_constraints()
    clause += create_column_constraints()
    clause += create_box_constraints()
    clause += create_value_constraints(grid)
    return clause

### appel au solver
def clauses_to_dimacs(clauses: ClauseBase, nb_vars: int) -> str :
    dimacs =  f"p cnf {nb_vars} {len(clauses)}\n"
    for clause in clauses :
        for var in clause :
            dimacs += f"{var} "
        dimacs += "0\n"
    return dimacs
    
#### fonction principale


def main():
    path = "../../Gophersat/sudoku.cnf"
    write_dimacs_file(clauses_to_dimacs(generate_problem(example2), 729), path)
    result = exec_gophersat(path)
    pprint.pp(model_to_grid(result[1]))




if __name__ == "__main__":
    main()
