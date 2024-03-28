def subsetsGenerations(planeta):
    subsets = []
    def funcBacktrack(start, path): # Função backtrack
        subsets.append(path[:])
        for i in range(start, len(planeta)):
            path.append(planeta[i])
            funcBacktrack(i + 1, path)
            path.pop()
    funcBacktrack(0, [])
    return subsets

def main():
    planeta = input().strip()  # Removendo espaços em branco 
    if (planeta == ":") or (planeta == ": "):  # Verificando se a entrada é apenas ":"
        print("[[]]")
    elif planeta == "":
        print(f"O número de subsets de visitação é 1")
        print("São eles: [[]]")
    else:
        planeta = planeta.split(", ")
        planeta = [item.strip() for item in planeta]  # Removendo espaços em branco em cada planeta
        planeta.sort()
        subsets = subsetsGenerations(planeta)
        print(f"O número de subsets de visitação é {len(subsets)}")
        print(f"São eles: {subsets}") 

if __name__ == "__main__":
    main()
