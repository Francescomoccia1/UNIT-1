città = input("Inserisci il nome della tua città di origine: ")
animale = input("Inserisci il nome del tuo animale domestico: ")

if(animale == ""):
    print("Non hai un animale domestico? Usiamo il tuo colore preferito")
    colore = input("Inserisci il tuo colore preferito: ")
    nome_band = città+" "+colore
else:
    nome_band = città +" "+animale

print("Il nome della tua band è: "+nome_band)
