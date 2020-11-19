print("============== Program By : @rickynvnda ==============")
print("======================================================")

n = int (input("Masukan Nilai : "))
x = 0
while (x < n) :
    if (10 ** x > n) :
        break
    else:
         print("Hasil hitung dari yang terkecil 10^x : ", 10 ** x)
    x += 1

print("Nilai terkecil dari 10^x lebih dari n adalah : ", 10 ** x)

print("======================================================")
print("==================== Terima Kasih ====================")