

#Written by Sabina Tjärnlund <satj0011@student.umu.se>. 
#May be used by everyone at Umeå University.
#Usage exept those listed above requires permission by the author.

from Array import Array

class Table(object):
      
      def __init__(self):
            """
                Syfte: Skapar en tom tabell med hjälp av en riktad lista med "a" som undre gräns
                och "b" som övre gräns
                Returvärde: -
                Kommentarer: I boken heter denna funktion Empty.
      
            """
            a=(0,)
            b=(1000,)
            self._table = Array(lo=a,hi=b)
            
            self._firstEmptyPlace = 0
            self._first=0
            
            ##Fundering, kommer self._first alltid vara 0 så den hämtas från __init__?
            ##  Även om den ändras i klassens andra defs?
            ##Om JA: bra för pos, dåligt för self._firstEmptyPlace
            ##Om Nej. dåligt för alla pos, döp om alla pos till 0 i defs och ta bort self._first(värdelös då)          
            ##Fundering nr 2
            ## Det här är ju ett "table", men har gjort den så att det bara är en rad.
            ## ska a=0 eller a=1?
            ## funkar det att indexera som jag gjort eller ska jag använda kordinater ex (a,1) för första pos
            ##(a,2) för andra pos osv eller funkar det med bara nr?
            ##Fundering nr 3
            ## Vet inte riktigt när man ska använda sig av tupler
            ## rad 60 exempelvis i insert. ska det vara if key==NewKey: eller  if(key,)==NewKey
            ## Fundering 4: får error på indentering på defs. vet ej varför
            
      
      def insert(self, key, obj):
            """
                #Syfte: utökar eller omdefinierar tabellen så att nyckeln key kopplas
                       #till värdet obj
                #Returvärde: -
                #Kommentarer: Det krävs att key är en typ som kan jämföras med
                        #likhet. Om det är en egen klass måste man överladda
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
                #Syfte: Testar om tabellen är tom
                #Returvärde: Returnerar sant om tabellen är tom, annars falsk
                #Kommentarer:
            #"""
            
            if self._firstEmptyPlace == 0:
                  return True
            else:
                  return False
      
      def lookup(self, key):
            """
                #Syfte: Ser efter om tabellen innehåller nyckeln key och returnerar
                       #i så fall värdet som är kopplat till nyckeln
                #Returvärde: Returnerar en tuppel (True, obj) där obj är värdet som
                       #är kopplat till nyckeln om nyckeln finns och annars (False, None)
                #Kommentarer: Om kön är tom returneras (False, None)
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
                #Syfte: Tar bort nyckeln key och dess sammankopplade värde.
                #Returvärde: -
                #Kommentarer: Om nyckeln inte finns så händer inget med tabellen
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
                              
                              self._firstEmptyPlace-=1 # sitter den här på rätt rad
                        else:
                              pos+=1


