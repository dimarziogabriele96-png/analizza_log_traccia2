# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 19:08:43 2025

@author: gdira

Questo codice prende una lista di liste da un file json e fa uscire in un file json 
per ogni utente la lista degli eventi diversi a cui partecipa
per ogni evento diverso quanti utenti sono associati a lui

"""
import argparse

from Sottoprog import lettura
from Sottoprog import scrittura
from Sottoprog import log
from Sottoprog import conta_ev

# Parser per ottenere path di ingresso e uscita  
parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', type=str, required=True, help='Inserire path file di ingresso')
parser.add_argument('-o', '--output', type=str, required=True, help='Inserire primo path file di uscita')
parser.add_argument('-a', '--avvisi', type=int, choices=[1], help='Inserire 1 se si vogliono gli aggiornamenti, 0 se non si vogliono')


pars = parser.parse_args()

Pin = pars.input
Pout = pars.output
avv =  pars.avvisi

# Se avvisi = 1 da ulteriori informazioni
if avv == 1:
    print(f'Il path del file di input è {Pin}')
    print(f'Il path del primo file di output è {Pout}')

# Lettura del file json di ingresso (con sottoprogramma)
dati = lettura(Pin)
    
diz = log(dati)

dc = conta_ev(diz)
    
# Creazione del file json di uscita (con sottoprogramma)
b = scrittura(dc,Pout)
if avv == 1:
    if not b:
        print('Errore nella scittura del file')
    else:
        print('Scrittura file completata')
    
