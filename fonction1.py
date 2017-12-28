import os,time
import random
import sys
from textblob import TextBlob







#data
##########################################

complementIn=['ma7lek',':*','n7ebek']
regime_etudeIn=['na9raw','le9raya','l9raya','el9raya','9raya','chna9raw','t9ari','t9arri','etude',"d'etude"]
supcom_descriptionIn = ['a7kili','chnya','a7kilna','parle','talk']
greetIn = ['ahla','salut','hello','hi']
nameIn = ['chesmek','chesmik','esmek','chesmek?','chesmik?','esmek?']
supcom =['supcom',"sup'com",'supcom?',"sup'com?",'supcom.',"sup'com.",'supcom!',"sup'com!",'supco',"sup'co","subcom","sub'com"]
first_greetin_message='first greeting message : welcome hope you enjoy '
clubIn=['clubs','clubet','club','clubs?','clubet?','club?']
bourseIn=['bourse?','flous?','bource?','bours?','bourse','flous','bource','bours']
foyerIn=['sokna','foyer','sokna?','foyer?']
foyerEtatIn=['behi','etat','a7kili']
transportIn=['transport','transprt','9riba','transport?','transprt?','9riba?']
voyage_etudeIn=['voyage']
double_dipIn=['diplome','diplom','diplome?','diplom?','diplomation']
restoIn=['resto','mekla','restaurant','resto?','mekla?','restaurant?']
cooperationIn=['cooperations','cooperation']
supcom_reasonsIn=['why','pourquoi','3leh','behia','nemchi','chrayek','na5ter','choose']
sportsIn=['sport','sports','sport?','sports?','sportives','sportifs','sportive','sportif','sportives?','sportifs?','sportive?','sportif?']
absIn=["l'abcsence",'abscence''4iyabet','n4ib','abscences','7dhour','4iyabet?','n4ib?','abscences?','7dhour?','presence','presence?',"l'abscence"]
helpIn=['help','3aweni','t3aweni','t3awenni','help?','3aweni?','t3aweni?','t3awenni?']
thankIn=['thanks','thank','3aychek','merci']
internetIn=['internet','connexion']
profIn=['prof','profs','profet','prof?','profs?','profet?']
emplacementIn=['wen','weni','wini','mawjouda','maoujouda','where',"win"]
certifIn=['certif','certificat','certifs','certifcats','certif?','certificat?','certifs?','certifcats?']
moocIn=['mooc','mooc?']
rangsIn=['rangs','rang']
interaction1In=['nal7a9','nal7a9?','nousel']
doubdipnbreIn=['9addeh','9addech','nombre','combien']




complement_response=['thanks']
supcom_descriptionOut = 'supcom hya ecole dingenieurs de telecom bla bla bla '
nameOut = ["my name is sup'bot "]
greetOut = ['hello ','hi there ','whats up ']
regime_etudeOut='na9raw barcha 7ajet fe supcom...'
clubOut=['clubs description......']
bourseOut=['bourse description....']
foyerOut=["jma3et l 1ere lkol 3and'hom l7a9 fi 3am foyer"]
foyerEtatOut=['hayel l foyer..']
transportOut=['transport description..']
voyage_etudeOut="voyage d'etude description..."
double_dipOut='double diplome description..'
restOut=['resto description...']
cooperationOut=['cooperation description...']
supcom_reasonsOut=['supcom is the best school in tunisia']
sportsOut=['fama les sports lkol fe supcom foot, voley, ping pong..']
absOut=['3andek l7a9 fi 25% 4iyabet..']
helpOut=["i'm here to help you just ask what you want"]
thankOut=["no problem, that's what i do"]
internetOut=['7ala l connexion']
profOut=['men a7san ma fama fi tounes']
emplacementOut=['supcom mawjouda fi technopole el ghazela..']
certifOut=['fel 1ere fama mooc w fe 2eme fama..']
moocOut=['mooc description..']
rangsOut=['a5er wa7ed d5al fel mp 3awnawel .. w fel pc .. ..']
interaction1Out='9addeh rang mta3ek?'
interaction1_1Out='chnya l filiere?'
doubdipnbreOut='barcha yo5rjou double dip..'








#INITIALISATION
############################################
respond_already=False




#FONCTIONS
############################################

def word_in_sentence(words,liste):
        spcm= False
        for word in words :
                if word in liste :
                        spcm=True
        return spcm

def response_genrator (words,messageIn,messageOut):
        fck=""
        for word in words:
                if word.lower() in messageIn :
                        fck= fck +(random.choice(messageOut))
                        break
        return fck

def test (resp):
        if resp=='' or resp==first_greetin_message :
                return False
        else:
                return True

                        





def fonc(sentence):

        resp=''
        d=''
        f=''
     
        words=sentence.split()                        





        if not test(resp):
                resp=response_genrator(words,rangsIn,rangsOut)

        if not test(resp):
                resp=response_genrator(words,helpIn,helpOut)

        if not test(resp):
                resp=response_genrator(words,profIn,profOut)

        if not test(resp):
                resp=response_genrator(words,absIn,absOut)

        if not test(resp):
                        resp=response_genrator(words,sportsIn,sportsOut)

        if not test(resp):
                resp=response_genrator(words,clubIn,clubOut)

        if not test(resp):
                resp=response_genrator(words,bourseIn,bourseOut)

        if not test(resp):
                resp=response_genrator(words,transportIn,transportOut)

        if not test(resp):
                resp=response_genrator(words,cooperationIn,cooperationOut)

        if not test(resp):
                resp=response_genrator(words,certifIn,certifOut)

        if not test(resp):
                resp=response_genrator(words,moocIn,moocOut)
                
        if not test(resp):
                        if word_in_sentence(words,supcom):
                                for word in words:
                                        if word.lower() in regime_etudeIn :
                                                resp= resp +regime_etudeOut
                                                d='done'
                                                break

                                if d!='done':
                                        for word in words:
                                                        if word.lower() in supcom_descriptionIn:
                                                                resp = resp + supcom_descriptionOut
                                                                f='done'
                                                                break
                                        if f!='done':
                                                resp = response_genrator(words,supcom_reasonsIn,supcom_reasonsOut)

                                        if not test(resp):
                                                resp = response_genrator(words,emplacementIn, emplacementOut)

                                        if not test(resp):
                                                resp=resp+ "chet7eb ta3raf 3al sup'com?"

        if not test(resp):
                resp=response_genrator(words,helpIn,helpOut)

        if not test(resp):
                resp=response_genrator(words,complementIn,complement_response)


        if not test(resp):
                resp=response_genrator(words,thankIn,thankOut)





        
                        

        if resp=='' or resp==first_greetin_message:
                return("i didn't understand you")
        else :
                return (resp)



###############################################
















        
