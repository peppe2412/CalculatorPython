"""
Calcolatrice in python 
"""
"""
Iniziare con dichiare delle funzioni,
che andranno ad eseguire le operazioni (+, -, *, /)
"""

#Funzione per sommare
def sum(x, y):
    return x + y

#Funzione per sotrarre
def substraction(x, y):
    return x - y

#Funzione per moltiplicare
def multiplication(x, y):
    return x * y

#Funzione per dividere
def division(x, y):
    return x / y


"""
Dare la possibilità di scegliere l'operazione,
che si vuole eseguire
"""
print("Segli l'operazione!")
print("1.Somma")
print("2.Sotrazione")
print("3.Moltiplicazione")
print("4.Divisione")

"""
Eseguire il loop, in base all'operazione scelta
"""
while True:
    #Dare possibilità di scegliere
    choice = input("Selziona(1/2/3/4)")
    if choice in ('1', '2', '3', '4'):
        try:
            #Far inserire i numeri
            number1 = float(input("Inserisci primo numero: "))
            number2 = float(input("Inserisci secondo numero: "))
        except ValueError:
            print("Inserire dato valido!")
            continue
        
        """
        Eseguire i risultati, in base all'operazione scelta
        """
        # Somma
        if (choice == '1'):
            print(f"L'operazione fra {number1} + {number2} fa: {sum(number1, number2)}")
            
        # Sottrazione 
        elif (choice == '2'):
            print(f"L'operazione {number1} - {number2} fa: {substraction(number1, number2)}")
            
        # Moltiplicazione
        elif (choice == '3'):
            print(f"L'operazione {number1} x {number2} fa: {multiplication(number1, number2)}")
            
        # Divisione
        elif (choice == '4'):
            
            # In caso di denominatore uguale a zero eseguire l'errore specifico
            if (number2 == 0): raise ZeroDivisionError("Non si può dividere per zero")
            
            print(f"L'operazione {number1} / {number2} fa: {division(number1, number2)}")
        else:
            print("Inserire un numero valido")    
        
            
            