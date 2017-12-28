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

def response_genrator (messageIn,messageOut):
        fck=resp
        for word in words:
                if word.lower() in messageIn :
                        fck= fck +(random.choice(messageOut))
                        break
        return fck

def test (resp):
        if resp=='' or resp==first_greetin_message or variable_for_test==True:
                return False
        else:
                return True

                        




#PROGRAMME PRINCIPALE
############################################
def fonc(sentence):
        filiere=False
        rang=False
        while True:
                resp=''
                sentence = input()
                d=''
                f=''
                c=''

                variable_for_test=False
                
                sentence_with_blob=TextBlob(sentence)
                words=sentence.split()

        '''check if the user is asking about supcom or something else and generate a response based on that'''
                
        

                if sentence == '':
                        print ('=> Nice meeting you')
                        time.sleep(4)
                        os.system("sudo shutdowwn -h now")
                else:
                        
       
                        if not respond_already:
                                resp= first_greetin_message
                                respond_already=True


                        for word in words:
                                if word.lower() in greetIn  :
                                        variable_for_test=True
                                        if  resp == first_greetin_message :
                                                resp= resp+ '.'
                                        else:
                                                resp= resp +(random.choice(greetOut))
                                        
                                        break

                        if not test(resp):
                                resp=response_genrator(nameIn,nameOut)

                        if not test(resp):
                                for word in words:
                                        if word.lower() in interaction1In:
                                                resp = resp + interaction1_1Out
                                                filiere=True
                                                break



                        if not test(resp) and (filiere == True):
                                resp=resp+interaction1Out
                                filiere=False
                                actual_fil=sentence
                                rang=True



                        if not test(resp) and (rang==True):
                                rang=False
                                if actual_fil.lower()=='mp':
                                        if int(sentence)<180 :
                                                resp=resp+'yes tal7a9'
                                        else:
                                        resp=resp+'non mtal7a9ch'

                                if actual_fil.lower()=='pc':
                                        if int(sentence)<100 :
                                                resp=resp+'yes tal7a9'
                                        else:
                                                resp=resp+'non mtal7a9ch'

                                if actual_fil.lower()=='pt' or actual_fil.lower()=='techno' :
                                        if int(sentence)<25 :
                                                resp=resp+'yes tal7a9'
                                        else:
                                                resp=resp+'non mtal7a9ch'



                        if not test(resp):
                                resp=response_genrator(rangsIn,rangsOut)

                        if not test(resp):
                                resp=response_genrator(helpIn,helpOut)

                        if not test(resp):
                                resp=response_genrator(profIn,profOut)

                        if not test(resp):
                                resp=response_genrator(absIn,absOut)

                        if not test(resp):
                                resp=response_genrator(sportsIn,sportsOut)

                        if not test(resp):
                                resp=response_genrator(clubIn,clubOut)

                        if not test(resp):
                                resp=response_genrator(bourseIn,bourseOut)

                        if not test(resp):
                                resp=response_genrator(transportIn,transportOut)

                        if not test(resp):
                                resp=response_genrator(cooperationIn,cooperationOut)

                        if not test(resp):
                                resp=response_genrator(certifIn,certifOut)

                        if not test(resp):
                                resp=response_genrator(moocIn,moocOut)

                        if not test(resp):
                                if word_in_sentence(words,voyage_etudeIn)and word_in_sentence(words,['etude',"d'etude",'etude?',"d'etude?"]) :
                                        resp=resp+voyage_etudeOut

                        if not test(resp):
                                if word_in_sentence(words,['double','doble','double'])and word_in_sentence(words,double_dipIn) :
                                        for word in words :
                                                if word in doubdipnbreIn :
                                                        resp = resp+doubdipnbreOut
                                                        break
                                        if not test(resp):
                                                resp=resp+double_dipOut

                        if not test(resp):
                                resp=response_genrator(restoIn,restOut)



                        if not test(resp):
                                if word_in_sentence(words, foyerIn):
                                        for word in words:
                                                if word.lower() in foyerEtatIn:
                                                        resp= resp+(random.choice(foyerEtatOut))
                                                        c='done'
                                                        break
                                        if c!='done':
                                                resp=resp+(random.choice(foyerOut))
                        

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
                                                        resp = response_genrator(supcom_reasonsIn,supcom_reasonsOut)

                                                if not test(resp):
                                                        resp = response_genrator(emplacementIn, emplacementOut)

                                                if not test(resp):
                                                        resp=resp+ "chet7eb ta3raf 3al sup'com?"


                        if not test(resp):
                                resp=response_genrator(helpIn,helpOut)

                        if not test(resp):
                                resp=response_genrator(complementIn,complement_response)


                        if not test(resp):
                                resp=response_genrator(thankIn,thankOut)





        
                        

                        if resp=='' or resp==first_greetin_message:
                                print("i didn't understand you")
                        else :
                                print (resp)



###############################################
















        
