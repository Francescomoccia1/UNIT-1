def quiz():
    # Lista di domande e risposte corretteD
    domande_e_risposte = [
        {"domanda": "Quando è stata scoperta l'America?: ", "risposta": "1492"},
        {"domanda": "Qual è la capitale dell'Italia?: ", "risposta": "Roma"},
        {"domanda": "Chi ha scritto 'La Divina Commedia'?: ", "risposta": "Dante Alighieri"},
        {"domanda": "Qual è la formula chimica dell'acqua?: ", "risposta": "H2O"},
        {"domanda": "In quale anno è caduto il Muro di Berlino?: ", "risposta": "1989"},
        {"domanda": "Qual è il pianeta più vicino al Sole?: ", "risposta": "Mercurio"},
        {"domanda": "Qual è la montagna più alta del mondo?: ", "risposta": "Everest"},
        {"domanda": "Chi ha dipinto la Gioconda?: ", "risposta": "Leonardo da Vinci"},
        {"domanda": "Qual è il numero atomico del carbonio?: ", "risposta": "6"},
        {"domanda": "Chi ha teorizzato la relatività?: ", "risposta": "Albert Einstein"}
    ]
    
    punteggio = 0

    for item in domande_e_risposte:
        risposta = input(item["domanda"])
        if risposta.lower() == item["risposta"].lower():
            print("Corretto!")
            punteggio += 1
        else:
            print(f"Sbagliato. La risposta corretta è: {item['risposta']}")

    print(f"Il tuo punteggio finale è: {punteggio} su {len(domande_e_risposte)}")

# Esegui il quiz
quiz()


