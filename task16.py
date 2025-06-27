ticket = 100000
sale = 0
age = int(input("yoshni kiriting:"))

if age >=0  and age >= 8:
    sale = 50
if age >= 8 and age >=15:
    sale = 30

ticket = ticket - ticket * sale / 100 

print("chiqish:"f"Chipta narxi {ticket} so'm va {sale}% chegirma qo'llanildi")
