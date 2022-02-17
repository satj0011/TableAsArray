# -*- coding: latin-1 -*-

#Written by Lena Kallin Westin <kallin@cs.umu.se>.
#May be used in the course Datastrukturer och Algoritmer (Python) at Ume� University.
#Usage exept those listed above requires permission by the author.

class IndexOutOFBoundaryError(Exception):
    pass
class IndexesDoNotMatchError(Exception):
    pass

"""
Datatypen Array enligt definitionen p� sidan 91 i Lars-Erik Janlert,
Torbj�rn Wiberg Datatyper och algoritmer 2., [rev.] uppl.,Lund,
Studentlitteratur, 2000, x, 387 s. ISBN 91-44-01364-7

Variabler och funktioner som inleds med ett enkelt underscore "_" �r privata
f�r klassen och ska inte anv�ndas av de som anv�nder denna klass.

"""
class Array(object):
    
    def __init__(self, lo = (0, ), hi = (0, )):
        """
            Syfte: Skapar ett tomt f�lt med elementen i lo and hi som undre och
            �vre gr�nser p� index.
            Parametrar: lo en n-tippel med undre gr�nser p� index
                        hi en n-tippel med �vre gr�nser p� index
            Returv�rde: -
            Kommentarer: I boken heter denna funktion Create.
                         Om man ska skapa en vector (dvs bara ett v�rde p�
                         hi and lo s� kom ih�g att skriva (lo_val, ) resp.
                         (hi_val, ) f�r att det ska bli tupler...
        """
        self._numDimensions = len(lo)
        if self._numDimensions != len(hi):
            raise IndexesDoNotMatchError
        self._low = lo
        self._high = hi
        self._numOfData = 1
        for i in range(self._numDimensions):
            self._numOfData = self._numOfData * ( hi[i] - lo[i] + 1)        
        # Skapa den interna vektorn
        self._array=[None]*self._numOfData
        # Bygg basen
        self._base = [0 for _ in range(self._numDimensions)]
        self._base[0] = 1    
        for i in range(1, self._numDimensions):
            self._base[i] = self._base[i-1]*(self._high[i-1] - self._low[i-1]+1)        

    def setValue(self, index, value):
        """
            Syfte: S�tter v�rdet p� plats index till v�rdet value.
            Parametrar: index tuppel som anger platsen i arrayen
                        value v�rdet som ska in i arrayen
            Returv�rde: -
            Kommentarer: Det �r odefinierat vad som h�nder om index ligger
                        utanf�r till�tet intervall
        """
        ii = self._getInternalIndex(index)
        self._array[ii] = value

    def _getInternalIndex(self, index):
        """
            Syfte: Omvandlar indexet som ges som en tupel till ett internt index
            Parametrar: index tuppel som anger platsen i arrayen
            Returv�rde: index i den interna arrayen
            Kommentarer: Detta �r en intern funktion som ej ska anv�ndas utanf�r klassen
        """


        # Skapa index
        internalIndex = 0
        for i in range(self._numDimensions):
            if (index[i] < self._low[i]) or (index[i] > self._high[i]):
                        raise IndexOutOFBoundaryError             
            internalIndex = internalIndex + (index[i]-self._low[i])*self._base[i]            
        return internalIndex 
    
    

    def low(self):
        """
            Syfte: Ger de l�gre indexgr�nserna f�r arrayen
            Parametrar: 
            Returv�rde: En tupel med mingr�nserna f�r arrayen
            Kommentarer: 
        """
        return self._low
    
    def high(self):
        """
            Syfte: Ger de h�gre indexgr�nserna f�r arrayen
            Parametrar: 
            Returv�rde: En tupel med maxgr�nserna f�r arrayen
            Kommentarer: 
        """
        return self._high

    def hasValue(self, index):
        """
            Syfte: Returnerar sant om v�rdet p� plats index i arrayen �r satt (med setValue)
            Parametrar: index tuppel som anger platsen i arrayen
            Returv�rde: -
            Kommentarer: Det �r odefinierat vad som h�nder om index ligger
                        utanf�r till�tet intervall
        """
        return self._array[self._getInternalIndex(index)] != None

    def inspectValue(self, index):
        """
            Syfte: Ger v�rdet p� plats index i arrayen
            Parametrar: index tuppel som anger platsen i arrayen
            Returv�rde: v�rdet p� angiven plats
            Kommentarer: Det �r odefinierat vad som h�nder om index ligger
                        utanf�r till�tet intervall
        """
        return self._array[self._getInternalIndex(index)]
