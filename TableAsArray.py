

#Written by Sabina Tj�rnlund <satj0011@student.umu.se>. 
#May be used by everyone at Ume� University.
#Usage exept those listed above requires permission by the author.

from Array import Array

class Table(object):
      
      def __init__(self):
            """
                Syfte: Skapar en tom tabell med hj�lp av en riktad lista med "a" som undre gr�ns
                och "b" som �vre gr�ns
                Returv�rde: -
                Kommentarer: I boken heter denna funktion Empty.
      
            """
            a=(0,)
            b=(1000,)
            self._table = Array(lo=a,hi=b)
            
            self._firstEmptyPlace = 0
            self._first=0
            
            ##Fundering, kommer self._first alltid vara 0 s� den h�mtas fr�n __init__?
            ##  �ven om den �ndras i klassens andra defs?
            ##Om JA: bra f�r pos, d�ligt f�r self._firstEmptyPlace
            ##Om Nej. d�ligt f�r alla pos, d�p om alla pos till 0 i defs och ta bort self._first(v�rdel�s d�)          
            ##Fundering nr 2
            ## Det h�r �r ju ett "table", men har gjort den s� att det bara �r en rad.
            ## ska a=0 eller a=1?
            ## funkar det att indexera som jag gjort eller ska jag anv�nda kordinater ex (a,1) f�r f�rsta pos
            ##(a,2) f�r andra pos osv eller funkar det med bara nr?
            ##Fundering nr 3
            ## Vet inte riktigt n�r man ska anv�nda sig av tupler
            ## rad 60 exempelvis i insert. ska det vara if key==NewKey: eller  if(key,)==NewKey
            ## Fundering 4: f�r error p� indentering p� defs. vet ej varf�r
            
      
      def insert(self, key, obj):
            """
                #Syfte: ut�kar eller omdefinierar tabellen s� att nyckeln key kopplas
                       #till v�rdet obj
                #Returv�rde: -
                #Kommentarer: Det kr�vs att key �r en typ som kan j�mf�ras med
                        #likhet. Om det �r en egen klass m�ste man �verladda
                        #funktionen __eq__
            #"""
            
            if self._firstEmptyPlace==0:
                  self._firstEmptyPlace += 1
                  self._table.setValue(pos, value=(key,obj))
            else:
                  found=False
                  pos=self._first
                  while (not found) and (pos!= seld._firstEmptyPlace):
                        (NewKey,NewObj)=self._table.inspectValue(pos)
                        if key==NewKey: # kanske (key,)
                              found=True
                              self._table.setValue(pos, value=(key,obj))
                              self._firstEmptyPlace += 1
                        else:
                              pos+=1
                  if not found:
                        self._table.setValue(self._firstEmptyPlace, value=(key,obj))
                   
                        self._firstEmptyPlace += 1
            
                  
      def isempty(self):
            """
                #Syfte: Testar om tabellen �r tom
                #Returv�rde: Returnerar sant om tabellen �r tom, annars falsk
                #Kommentarer:
            #"""
            
            if self._firstEmptyPlace == 0:
                  return True
            else:
                  return False
      
      def lookup(self, key):
            """
                #Syfte: Ser efter om tabellen inneh�ller nyckeln key och returnerar
                       #i s� fall v�rdet som �r kopplat till nyckeln
                #Returv�rde: Returnerar en tuppel (True, obj) d�r obj �r v�rdet som
                       #�r kopplat till nyckeln om nyckeln finns och annars (False, None)
                #Kommentarer: Om k�n �r tom returneras (False, None)
            """

            pos=self._first ##### pos=0?
            while pos!= self._firstEmptyPlace:
                  (NewKey,NewObj)=self._table.inspectValue(pos)
                  if NewKey==key:
                        return (True, NewObj)
                  pos+=1
            return (False,None)
                  
            
            
      
      def remove(self, key):
            """
                #Syfte: Tar bort nyckeln key och dess sammankopplade v�rde.
                #Returv�rde: -
                #Kommentarer: Om nyckeln inte finns s� h�nder inget med tabellen
            """ 
            if self._firstEmptyPlace!=0:
                  found=False
                  pos=self._first
                  nextpos=pos+1
                  while (not found) and (pos!=self._firstEmptyPlace):
                        (NewKey,NewValue)=self._table.inspectValue(pos)
                        if NewKey==key:
                              found=True
                              
                              while nextpos!=self._firstEmptyPlace:
                                    (Key1,Value1)=self._table.inspectValue(pos)
                                    self._table.setValue(pos, value=(Key1,Value1))
                                    pos+=1
                                    nextpos+=1
                              
                              self._firstEmptyPlace-=1 # sitter den h�r p� r�tt rad
                        else:
                              pos+=1


