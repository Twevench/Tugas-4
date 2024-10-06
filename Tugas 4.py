# masukkan dua matriks
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Cek apakah matriks dapat di kalikan
if len(A[0]) != len(B):
    print("Matriks tidak bisa dikalikan karena ukuran tidak sesuai.")
else:
    # Inisialisasi matriks hasil dengan nol
    hasil = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Melakukan perkalian matriks
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                hasil[i][j] += A[i][k] * B[k][j]

    # Tampilkan hasil matriks
    print("Hasil perkalian matriks:")
    for row in hasil:
        print(row)
