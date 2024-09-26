from typing import List, Dict, Generator

def decomp(n: int, nb_bits: int) -> List[bool] :
    liste = []
    for i in range(nb_bits) :
        bit = n%2
        n = int(n/2)
        if bit :
            liste.append(True)
        else :
            liste.append(False)
    # for i in liste :
    #     print(i)
    return liste

def interpretation(voc: List[str], vals: List[bool]) -> Dict[str, bool] :
    dictionnary = {}
    for i in range(len(voc)) :
        dictionnary[voc[i]] = vals[i]
    #print(dictionnary)
    return dictionnary

def genInterpretations(voc: List[str]) -> Generator[Dict[str, bool], None, None] : 
    for i in range(2**len(voc)) :
        yield(interpretation(voc, decomp(i, len(voc))))

def valuate(formula: str, interpretation: Dict[str, bool]) -> bool:
    for key, value in interpretation.items() :
        formula = formula.replace(key, str(value))
    return bool(eval(formula))

def tableVerite(formula: str, variables: List[str]) :
    print(formula)
    for variable in variables :
        print(variable, end = "")
        print(" ------- ", end = "")
    print("eval.")
    gen = genInterpretations(variables)
    for dic in gen :
        for variable in variables :
            print(dic[variable], end = "")
            print("  |  ", end = "")
        print(valuate(formula, dic))

def isValide(formula: str, variables: List[str]) :
    gen = genInterpretations(variables)
    for dic in gen :
        if valuate(formula, dic) == False :
            return False
    return True

def isContradictoire(formula: str, variables: List[str]) :
    gen = genInterpretations(variables)
    for dic in gen :
        if valuate(formula, dic) == True :
            return False
    return True

def isContingente(formula: str, variables: List[str]) :
    if not isValide() and not isContradictoire() :
        return True
    return False

def isCons(f1: str, f2: str, variables: List[str]) -> bool :
    gen = genInterpretations(variables)
    for dic in gen :
        if (valuate(f1, dic) == True and valuate(f2, dic) == False) or (valuate(f1, dic) == False and valuate(f2, dic) == True) :
            return False
    return True

def main() :
    # decomp(3,4)
    # interpretation(["A", "B", "C"], [True, False, True])
    genInterpretations(["A", "B", "C"])
    boolean = valuate("(A or B) and not C", {"A" : True, "B" : True, "C" : False})
    tableVerite("(A or B) and not C", ["A", "B", "C", "D"])

if __name__ == "__main__" :
    main()