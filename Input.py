import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="Admin",passwd="Zochova2244",database="covid")
mycursor = mydb.cursor()


if (mydb):
     print("Connection successful")
else:
    print("Connection successful")

meno = input("Zadajte krstne meno požuvatela:")

priezvisko = input("Zadajte priezvisko použivatela:")

datumpoztest = input("Zadajte datum kedy ste boli pozitive testovany: (YYYY-MM-DD).Alebo ak ste neboli tak napište 'nie:'") 
  

covidpass = input("Máte platný Covid Pass?:")

ockovanie = input("Ste očkovaný?")

email = input("Zadajte svoj email:")
if "@" not in email:
    print("Neplatný email")
    email = input("Zadajte svoj email:")

"Ano" or "ano" or "ANO" == True
"Nie" or "nie" or "NIE" == False


Udaje = (meno,priezvisko,datumpoztest,covidpass,ockovanie,email)
Insertion = ("INSERT INTO users" "(meno, priezvisko, datumpoztest, covidpass, ockovanie, email)" "VALUES (%s,%s,%s,%s,%s,%s)")
data_data = (meno, priezvisko, datumpoztest, covidpass, ockovanie, email)

mycursor.execute(Insertion,data_data)
mydb.commit()
mycursor.close()
mydb.close()


