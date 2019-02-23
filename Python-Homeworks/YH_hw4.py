"""
In this homework, you are expected to write 4 functions for basic bioinformatics operations.
All functions must be RECURSIVE !

Function 1 : It checks whether a given nucleic acid sequence is valid or not.
Function 2 : It checks whether a given nucleic acid sequence is a DNA, RNA or invalid.
	Examples: "ATGC" -> DNA, "AUGC" -> RNA, "UTGC" -> invalid, "ABC" -> invalid
Function 3 : It returns the complementary strand for any given DNA sequence:
	Complementary Base Pairing of DNA: G <-> C , A <-> T
	Example: If the given DNA sequence is "ATTGCC", the function returns "TAACGG"
Function 4 : It finds the number of differences between two nucleic acid sequences.
	Example: If the first sequence is "CATCTCG" and the second sequence is "ACTCAC",
	the difference is 5 since only the "TC and "C" parst overlap (common in the same place):
	CATCTCG --- ACTCAC

Background Informations:
	* Normally, Deoxyribonucleic Acid (DNA) has a double-helix structure, but in this homework
	assume that it is single stranded.
	* Ribonucleic Acid (RNA) is a single helix nucleic acid chain.
	* Allowed nucleotides for DNA are: Cytosine(C), Guanine(G), Adenine(A), Thymine(T)
	* Allowed nucleotides for RNA are: Cytosine(C), Guanine(G), Adenine(A), Uracil(U)
"""

#Yusuf HAYIRLI
count=0 # Counts invalid letters for function_1
def Check_Valid(sequence,count): # Checks if Nucleic acid is valid or invalid
    Nucs=["A","C","G","T","U"]
    if len(sequence) == 0 :
        if count>0:
            return "invalid"
        else:
            return "valid"
    else:
        if "U" in sequence and "T" in sequence:
            count+=1
        elif sequence[0] not in Nucs:
            count+=1
        return Check_Valid(sequence[1:],count)
            
def Check_DNA_RNA(sequence): # Checks if given Nucleic acid is DNA or RNA or invalid.
    if Check_Valid(sequence,count)=="valid":
        
        if len(sequence) == 0:
            return "uncertain"
        
        if sequence[0]=="T":
            return "DNA"
        elif sequence[0]=="U":
            return "RNA"
        else:
            return Check_DNA_RNA(sequence[1:])
    else:
        return "invalid"
    
def Get_Complementary(sequence): # Gives Complementary's of given Nucleic Acid.
    Nucleics=["A","C","G","T"]
    Complementarys=["T","G","C","A"]
    if len(sequence) == 0 :
        return sequence
    else:
        return Complementarys[Nucleics.index(sequence[0])] + Get_Complementary(sequence[1:])

def Get_Difference(first_Nuc,second_Nuc,diff): # Gives 2 different acids' difference.
    if min(len(first_Nuc),len(second_Nuc)) == 0:
        return diff
    else:
        if first_Nuc[0]!=second_Nuc[0]:
            return 1 + Get_Difference(first_Nuc[1:],second_Nuc[1:],diff)
        else:
            return Get_Difference(first_Nuc[1:],second_Nuc[1:],diff)

def main():
    while True:
        sequence=input("Enter your Nucleic Acid Sequence: ")
        if Check_Valid(sequence,count)=="invalid":
            print("Wrong sequence of Nucleic Acid, please enter again!")
            continue
        else:
            break
    print("Sequence is:",Check_Valid(sequence,count))
    print("Also it is:", Check_DNA_RNA(sequence))
    func2=Check_DNA_RNA(sequence)
    if func2=="DNA":
        print("Complementary is:",Get_Complementary(sequence))
    elif func2=="uncertain":
        print("Given Nucleic Acid code is uncertain.")
    else:
        print("It is not a DNA Code!")
    while True:
        first_Nuc=input("Enter your first Nucleic Acid to compare: ")
        if Check_Valid(first_Nuc,count)=="invalid":
            print("Wrong Entry!")
            continue
        second_Nuc=input("Enter your second Nucleic Acid to compare: ")
        if Check_Valid(second_Nuc,count)=="invalid":
            print("Wrong Entry!")
            continue
        break
    diff=(max(len(first_Nuc),len(second_Nuc)) - min(len(first_Nuc),len(second_Nuc)))
    print("Difference is:",Get_Difference(first_Nuc,second_Nuc,diff))
    
    
main()