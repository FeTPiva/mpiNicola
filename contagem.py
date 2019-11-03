import nltk
from nltk.stem import RSLPStemmer


#nltk.download('rslp')
#nltk.download('punkt') 

def Tokenize(sentence):
    sentence = sentence.lower()
    sentence = nltk.word_tokenize(sentence)
    return sentence

def Stemming(sentence):
    stemmer = RSLPStemmer()
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase


def contandoCoisas(texto, arquivo):

    #TTL palavraS
    p = 0
    #TTL STOPWORDS
    s = 0
    result = 0
    
    #palavraS
    palavraTxt = open(arquivo, 'r') #abri a 'base' com as palavras que estou em busca no text a ser analisado
    palavra = palavraTxt.read()
    palavraTxt.close()
    
    #STOP WORDS PERSONALIZADAS
    stoptxt = open('filtro.txt', 'r')
    stop = stoptxt.read()
    stoptxt.close()

    #TOKENIZANDO
    palavra = Tokenize(palavra)    
    stop = Tokenize(stop)
    texto = Tokenize(texto)
    #print(texto)
    
    #Stemmando
    palavra = Stemming(palavra)
    stop = Stemming(stop)
    texto = Stemming(texto)


    #CONTANDO COISAS EFETIVAMENTE
    for i in texto :
        if i in palavra :
            p = p+1 

    for i in texto :
        if i in stop :
            s +=1 
     
    #TOTAL DE PALAVRAS
    ttlwords = len(texto)
   
    #MENOS AS STOP WORDS
    
    if ttlwords == s:
        result = 0
    else:
        ttlwords = ttlwords - s
        result = p/ttlwords
    

    return result

def contandoCoisasPrint(texto, arquivo):
    return print(contandoCoisas(texto, arquivo))


def criaLista(*args):
    lista = []
    i=0
    c = len(args)

    while i < c:
               
        lista.insert(i, args[i])
        i+=1
      
    return lista