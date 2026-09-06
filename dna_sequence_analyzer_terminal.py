DNA=input("Enter the DNA sequence: ")
hi=DNA.upper()
A=hi.count("A")
T=hi.count("T")
C=hi.count("C")
G=hi.count("G")
print("Number of A's:", A)
print("Number of T's:", T)
print("Number of C's:", C)
print("Number of G's:", G)
GC_content= (G + C) / len(DNA) * 100
print("GC content percentage:", GC_content, "%")
bases=hi.count("A") + hi.count("T") + hi.count("C") + hi.count("G")
if bases != len(DNA):
    print("Warning: The DNA sequence contains invalid characters.")
else:
    print("The DNA sequence is valid.")
    