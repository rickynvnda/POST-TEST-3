print("===========SELAMAT DATANG DI PROGRAM TAKOYAKI============")
variable={"toko":"Takoyaki","varian1":2000,"varian2":2500} 
ulang = "y" 
while ulang == "y" : 
    print("Silahkan pilih varian Takoyaki")     
    print("[1] Beli Varian 1  Rp 2000, Ready 45 pcs ")     
    print("[2] Beli Varian 2  Rp 2500, Ready 40 pcs ")

    pilihan= input("Masukan Pilihan anda : ")     
    if pilihan  == "1" : 
        print (" Varian 1 Rp 2000/pcs")         
        harga =2000         
        jumlah=int( input("Jumlah Takoyaki yang anda inginkan? : "))         
        total=harga*jumlah         
        print("Total harga=","Rp.",total)

        if  jumlah>= 10: 
            print("Selamat anda mendapatkan diskon sebesar 10%!")             
            diskon = total*10/100             
            hasil = total -int(diskon)             
            b=int (variable["varian1"]-int(hasil))             
            print ("diskon menjadi {}".format(hasil))             
            ulang = input ("Apakah anda ingin mengulang (y/t)? : ").lower()             
            print("===================================================================")
            print("                           TERIMA KASIH                            ")
            print("===================================================================")
        else : 
            if  (jumlah)<= 10: 
                print (" Varian 1 Rp 2000/pcs") 
                print("Tidak dapat diskon, bayar dengan harga normal")                 
                total=harga*jumlah                 
                print("Total harga = ","Rp.",total)                 
                ulang == "t"                 
                ulang = input ("Apakah anda ingin mengulang (y/t)? : ").lower() 
                print("===================================================================")
                print("                           TERIMA KASIH                            ")
                print("===================================================================") 
    
    elif pilihan  == "2" : 
        print (" Varian 2 Rp 2500/pcs")         
        harga =2500         
        jumlah=int( input("Masukan jumlah Takoyaki yg anda inginkan?"))         
        total=harga*jumlah         
        print("Total harga=","Rp.",total)

        if  jumlah>= 8: 
            print("Selamat anda mendapatkan diskon sebesar 8%!")             
            diskon = total*8/100             
            hasil = total -int(diskon)             
            print ("diskon menjadi {}".format(hasil))             
            ulang = input ("Apakah anda ingin mengulang (y/t) ?: ").lower()             
            print("===================================================================")
            print("                           TERIMA KASIH                            ")
            print("===================================================================") 
    else :
        if  (jumlah)<= 8: 
            print (" Varian 1 Rp 2500 /pcs")                 
            print("Tidak dapat diskon, bayar dengan harga normal")                 
            total=harga*jumlah                 
            print("Total harga=","Rp.",total) 
                                          
            ulang = input ("Apakah anda ingin mengulang (y/t) ?: ").lower()
            ulang == "t"                 
            print("===================================================================")
            print("                           TERIMA KASIH                            ")
            print("===================================================================")    
 
            print(" Mohon Maaf, Pilihan anda tidak tersedia")
            ulang = input (" Apakah Anda Ingin Mengulang (y/t) ?:").lower()     
            ulang == "t"    
            print("===================================================================")
            print("                           TERIMA KASIH                            ")
            print("===================================================================")