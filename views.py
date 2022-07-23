
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render
import pymysql


def saludo(request):
    nombre="Juan"
    doc_externo=open("/home/aforero/elnotispin/elnotispinProject/elnotispinProject/Plantillas/miplantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"nombre_persona":nombre})
    documento=plt.render(ctx)
    return HttpResponse(documento)



def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual
    return HttpResponse(documento)

def calculadora(request):
      
    return render(request, "miplantilla.html")

def home(request):
    return render(request, "home.html")

def homes(request):
    p1=Persona("Profesor Juan", "Díaz")
    temasdelcurso=["plantillas", "modelos", "formularios", "vistas", "despliegue"]
    ahora=datetime.datetime.now()
    doc_extertno=loader.get_template('miplantilla.html')
    documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasdelcurso})
    return HttpResponse(documento)

def submitquery(request):
    q = request.GET['query']
    try:
        ans = q
	
        spin = ans+"Hola"
        import spacy
        nlp = spacy.load("es_core_news_sm")
        doc = nlp(ans)
        tokens = [token for token in doc]
	
        
        import PyMultiDictionary
        from PyMultiDictionary import MultiDictionary
        dictionary = MultiDictionary()
        sinonyms = []
        for t in tokens:
                #print(t)
            word = dictionary.synonym('es', str(t))
            if len(word) >=1:
                l = []
                l.append(t)
                l.append(word)
                sinonyms.append(l)
                    #sinonyms.append(word)
            else:
                sinonyms.append(t)
            #print(sinonyms)
            # s = tokens.append(word)
            # print(s)
       # print("sinonimos",sinonyms)
        sentence = str(sinonyms)
        #print(sentence)


        sentence = sentence.replace("['","|").replace("']","").replace("[","{").replace("]", "}").replace(",,", "°°°").replace(",", "").replace(" ?", "?").replace("¿ ", "¿").replace(" !", "!").replace("¡ ", "¡").replace("", "").replace("' '", "|").replace("'", "").replace(" .", ".").replace(" :", ":").replace(" ;", ";").replace("( ", "(").replace(" )", ")")
        sentence = sentence.replace("°°°",",").replace(" ,", ",")
        sentence = sentence[1:]
        sentence = sentence[:-1]
            #print(sentence)

        import re
        import random
        import itertools

        def spintax(text, single=True):
            """Return a list of unique spins of a Spintax text string.

            Args:
                text (string): Spintax text (i.e. I am the {President|King|Ambassador} of Nigeria.)
                single (bool, optional): Optional boolean to return a list or a single spin.

            Returns:
                spins (string, list): Single spin or list of spins depending on single.
            """

            pattern = re.compile('(\{[^\}]+\}|[^\{\}]*)')
            chunks = pattern.split(text)

            def options(s):
                if len(s) > 0 and s[0] == '{':
                    return [opt for opt in s[1:-1].split('|')]
                return [s]

            parts_list = [options(chunk) for chunk in chunks]

            spins = []

            for spin in itertools.product(*parts_list):
                spins.append(''.join(spin))

            if single:
                return spins[random.randint(0, len(spins)-1)]
            else:
                return spins

        #email = '"""'+sentence+'"""'
        spin = spintax(sentence)
        spin1 = spintax(sentence)
        spin = str(spin)
        spin1 = str(spin1)

        mydictionary = {
            "q" : q,
            "ans1" : ans,
            "ans2" : spin,
            "ans3" : spin1,
            "error" : False,
            "result" : True
        }
        return render(request, 'home.html',context=mydictionary)
    except:
        mydictionary = {
            "error" : True,
            "result" : False 
        }
        return render(request, 'home.html',context=mydictionary)
    
    
def submitquery2(request):
    q = request.GET['query']
    try:
        ans = q
        
        import WoobDictionary
        from WoobDictionary import synonym_dictionary

        sentence = '"""'+ans+'"""'
        #print(sentence)
        h = sentence.replace("."," . ").replace(","," , ").replace(":"," : ").replace(";"," ; ").replace("["," [ ").replace("]"," ] ").replace("{"," { ").replace("}"," } ").replace("|"," | ").replace("!"," ! ").replace("¡"," ¡ ").replace("?"," ? ").replace("¿"," ¿ ").replace("","").replace("'"," ' ").replace('"',' " ').replace("("," ( ").replace(")"," ) ")

        tokens = h.split(" ")

        sinonyms = []
        import random
        for t in tokens:        
            word = filter(lambda a: t in a, synonym_dictionary)
            word = list(word)
            
            if len(word) >=1:
                element = word[0]
                l = random.choice(element)        
                sinonyms.append(l)        
            else:
                sinonyms.append(t)

        sentence = str(sinonyms)
        sentence = sentence.replace("'","").replace(", "," ").replace(" .",".").replace(" :",":").replace(" ,",",").replace(" ;",";").replace(" [","[").replace(" ]","]").replace(" {","{").replace(" }","}").replace(" |","|").replace(" !","!").replace(" ¡","¡").replace(" ?","?").replace(" ¿","¿").replace(' "','"').replace(" (","(").replace(" )",")").replace("_"," ").replace(",  ",", ")
        sentence = sentence[1:]
        sentence = sentence[:-1]
        #print(sentence)   
        spines1 = str(sentence)    

        mydictionary1 = {
            "q" : q,
            "ans1" : ans,
            "ans2" : spines1,
            #"ans3" : spines1,
            "error" : False,
            "result" : True
        }
        return render(request, 'home.html',context=mydictionary1)
    except:
        mydictionary = {
            "error" : True,
            "result" : False 
        }
        return render(request, 'home.html',context=mydictionary1)
    
