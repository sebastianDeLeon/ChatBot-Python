import random
import re



def getResponse(entrada):
    splitM = re.split(r'\s|[,;:.?!-_]\s*',entrada.lower())
    checkResponse = check_all_responses(splitM)
    return checkResponse

def messageProbability(userMesage,recognizeWords,singleResponse=False,requiredWord=[]):
    messageCertainly=0
    hasRequiredWords=True

    for word in userMesage:
        if word in recognizeWords:
            messageCertainly+=1
    percentage = float(messageCertainly)/float(len(recognizeWords))
    for word in requiredWord:
        if word not in userMesage:
            hasRequiredWords=False
            break
    if hasRequiredWords or singleResponse:
        return int(percentage*100)
    else:
        return 0

def check_all_responses(message):
        highestProb= {}

        def response(botResponse,listOfWords,singleResponse=False, requiredWord=[]):
            nonlocal highestProb
            highestProb[botResponse] = messageProbability(message, listOfWords, singleResponse, requiredWord)
        response("Hola",["hola","klk","saludos","buenas","hey"],singleResponse=True)

        response("Yo bien y tu?", ["como", "estas", "va", "vas", "sientes"], singleResponse=True)

        response(["Me algro", "Es bueno escucharlo","Eso es fantastico"]
                 [random.randrange(3)], ["bien", "fantastico", "excelenta"], singleResponse=True)

        response("Que mal... Espero que mejores...", ["mal", "horrible"], singleResponse=True)

        response("No hay de que",["gracias","estoy muy agradecido","te lo agradezco", "thanks","thx"],singleResponse=True)

        response("El itla esta ubicado en las américas , km. 27, la caleta, calle 27, 11606",
                 ["donde", "ubicacion", "ubicados", "direccion", "encuentra"], singleResponse=True)

        # Cuando se fundo el itla
        response("El ITLA fue fundado el 15 de agosto de 2000",
                 ["Cuando", "año", "fecha", "fundo", "creo"], singleResponse=True)

        # Quien fundo el itla
        response("Fue fundado por Leonel Fernandez",
                 [ "fundador", "creador"], singleResponse=True)

        # nombrar alguna carrera
        response((["Tecnologo en software", "redes de informacion", "Inteligencia artificial", "informatica forense"][
                     random.randrange(4)]),
                 ["dime", "carrera", "nombrame", "tecnologo"], singleResponse=True)

        # QUien es el rector
        response("Omar Méndez Lluberes es actualmente el rector del itla",
                 [ "rige","director","dirige", "rector", "director", "como", "llama","rectoria"], singleResponse=True)

        # materias que dan en sofwares
        response("el itla esta ubicado en las américas , km. 27, la caleta, calle 27, 11606",
                 ["donde", "ubicacion", "ubicados", "direccion"], singleResponse=True)

        # decreto
        response("Se fundo mediantel el Decreto No. 422-00",
                 ["mediante", "decreto"], singleResponse=["decreto"])

        # certificado ISO
        response("El ITLA obtuvo el certificado ISO en 2000",
                 ["certificado", "año", "iso", "fundo", "creo","certificacion"], singleResponse=True)

        # transporte
        response(
            "El ITLA tiene 3 rutas de trasnporte la 27 de febrero, la Charles De Gaulle y la ave. Francisco Alberto Caamaño Deño",
            ["transporte", "ruta", "lleva", "llevar", "llegar","llego", "wawa","como", "voy"], singleResponse=True)

        # precio del transporte
        response("El del boleto del transporte cuesta 25 la ida y 25 la vuelta",
                 ["ticket", "boleto", "viaje","precio"], singleResponse=True)

        response("En el sitio web del itla",
                 ["informacion", "mas", "info", "acceder"], singleResponse=True)

    #Pregunas del itla


        bestMatch = max(highestProb,key= highestProb.get)

        return unknown() if highestProb[bestMatch] < 1 else bestMatch

def unknown():
    response = ["Podrias repetirlo?", "No entendi muy bien","Podrias ser mas claro"][random.randrange(3)]

while True:
    print("bot: "+getResponse(input("You: ")))