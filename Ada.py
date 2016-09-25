nouns=[]
verbs=[]
pronouns=[]

def seperateWords(sentence):
    sentence =' '+sentence+' '
    wordStart=0
    wordEnd=0
    words=[]
    for letter in sentence:
        if(letter==' '):
            if len(sentence[wordStart:wordEnd])>1:
                words.append(sentence[wordStart+1:wordEnd])
            wordStart=wordEnd
        wordEnd+=1    
    return words

#Main Loop
while 1:
    response = input("-> ")
    print(seperateWords(response))
