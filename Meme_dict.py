meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado"
}

while True:

    word = input("Escribe una palabra moderna que no entiendes (¡Escribe en mayusculas!)")
    
    if word in meme_dict:
        print(meme_dict[word])
    elif word not in meme_dict and word != "FIN":
        print("Aun no tenemos esa palabra... ¡Pero la agregaremos pronto!")

    if word == "FIN":
        break
