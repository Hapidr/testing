matriks1 = [
    [4,5],
    [9,10]
]

matriks2 = [
    [1, 2],
    [3, 4]
]
print("Matriks 1")
for baris in range(len(matriks1)):
    for kolom in range(len(matriks1[0])):
        print(matriks1[baris][kolom], end=' ')
    print()

print("\nMatriks 2")
for baris in range(len(matriks2)):
    for kolom in range(len(matriks2[0])):
        print(matriks2[baris][kolom], end=' ')
    print()


matriks3 = []
for baris in range(len(matriks1)):
    row = []
    for kolom in range(len(matriks1[0])):
        total = 0
        for baris2 in range(len(matriks2)):
            total = total + (matriks1[baris][baris2] * matriks2[baris2][kolom])
        row.append(total)
    matriks3.append(row)

print('='*20, "\nPerkalian")
for baris in range(len(matriks3)):
    for kolom in range(len(matriks3[0])):
        print(matriks3[baris][kolom], end=' ')
    print()
