import tkinter as tk


root = tk.Tk()
root.title("DNA Sequence Analyzer")
root.geometry("450x550")
root.config(bg="#F4F1EA")

DNA=tk.Label(root, text="Enter the DNA sequence:",font=("Segoe UI",16, "bold"),bg="#F4F1EA", fg="#2C3E50", wraplength=300)
DNA.pack(pady=15)

DNA_entry=tk.Entry(root, width=30)
DNA_entry.pack(pady=10)

DNA_length_label=tk.Label(root, text="Length of DNA sequence: ", font=("Segoe UI",11), relief="solid", borderwidth=1, bg="#EAE6DC", fg="#2C3E50")
DNA_length_label.pack(pady=5)


validity_label=tk.Label(root, text="", font=("Segoe UI",11,"bold"))
validity_label.pack(pady=5)

counts_frame=tk.Frame(root, bg="#F4F1EA")
counts_frame.pack(pady=10)

A_count=tk.Label(counts_frame, text="Number of A's: ", font=("Segoe UI",11), bg="#F4F1EA", fg= "#4A7A3D" )
A_count.grid(row=0, column=0, padx=10)
T_count=tk.Label(counts_frame, text="Number of T's: ", font=("Segoe UI",11), bg="#F4F1EA", fg= "#A8402A" )
T_count.grid(row=0,column=1, padx=10)
C_count=tk.Label(counts_frame, text="Number of C's: ", font=("Segoe UI",11), bg="#F4F1EA", fg="#2C5F6F")
C_count.grid(row=1, column=0, padx=10, pady=5)
G_count=tk.Label(counts_frame, text="Number of G's: ", font=("Segoe UI",11), bg="#F4F1EA", fg= "#B37D1A")
G_count.grid(row=1, column=1, padx=10, pady=5)


GC_content_label=tk.Label(root, text="", font=("Segoe UI",11))
GC_content_label.pack(pady=5)

def check_DNA():

    DNA_final=DNA_entry.get().upper().strip().replace("\n", "")
    
    DNA_length=len(DNA_final)
    A=DNA_final.count("A")
    T=DNA_final.count("T")
    C=DNA_final.count("C")
    G=DNA_final.count("G")

    no_of_bases=A+T+C+G

    DNA_length_label.config(text="Length of DNA sequence: " + str(DNA_length))

    if no_of_bases != DNA_length:
        validity_label.config(text="Warning: The DNA sequence contains invalid characters.", fg="red")
    else:
        validity_label.config(text="The DNA sequence is valid!", fg="green")

    A_count.config(text="Number of A's: " + str(A)) 
    T_count.config(text="Number of T's: " + str(T))
    C_count.config(text="Number of C's: " + str(C))
    G_count.config(text="Number of G's: " + str(G))

    if DNA_length > 0:
        GC_content= (G + C) / DNA_length * 100
        GC_content_label.config(text="GC content percentage: " + str(round(GC_content, 2)) + "%")
    else:
        GC_content_label.config(text="GC content percentage: N/A")

check_button=tk.Button(root, text="Count Bases", bg="#4A6670", fg="white", activebackground="#3A5460",font=("Segoe UI",12,"bold"), command=check_DNA)
check_button.pack(pady=10)
        
root.mainloop()
