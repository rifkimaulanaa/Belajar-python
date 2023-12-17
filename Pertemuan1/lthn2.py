print(' Python Kalkulator Sederhana  ')
print()
 
print('1. Penjumlahan')
print('2. Pengurangan')
print('3. Perkalian')
print('4. Pembagian')
print('5. Modulus')
print()
 
pilihan = int(input("Input pilihan operasi: "))
num1 = int(input('Angka pertama: '))
num2 = int(input('Angka kedua: '))
print()
 
if pilihan == 1:
  print('Hasil dari',num1,'+',num2,'=',round(num1+num2,2))
elif pilihan == 2:
  print('Hasil dari',num1,'-',num2,'=',round(num1-num2,2))
elif pilihan == 3:
  print('Hasil dari',num1,'*',num2,'=',round(num1*num2,2))
elif pilihan == 4:
  print('Hasil dari',num1,'/',num2,'=',round(num1/num2,2))
elif pilihan == 5:
  print('Hasil dari',num1,'%',num2,'=',round(num1%num2,2))
else:
  print('Maaf, pilihan menu tidak tersedia')