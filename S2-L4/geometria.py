import math

scelta = input("Scegli tra queste la figura della quale vuoi calcolare il perimetro o circonferenza (Quadrato, Cerchio, Rettangolo):\n")

if scelta == "Quadrato":
    lato = float(input("Qual'è la lunghezza del lato del quadrato?: "))
    perimetro = lato*4
    print(f"Il perimetro del quadrato è: {perimetro}")
elif scelta == "Cerchio":
    raggio = float(input("Qual'è il raggio del cerchio?:"))
    circonferenza = 2*math.pi*raggio
    print(f"La circonferenza del cerchio è: {circonferenza}")
elif scelta == "Rettangolo":
    base = float(input("Qual'è la base del rettangolo?: "))
    altezza = float(input("Qual'è l'altezza del rettangolo?: "))
    perimetro = 2*(base+altezza)
    print(f"Ilperimetro del rettangolo è: {perimetro}")
else:print("Non hai scelto correttamente la forma geometrica!")


