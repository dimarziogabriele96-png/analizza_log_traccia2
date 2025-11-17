# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 11:25:12 2025

@author: gdira
"""
import json
from collections import Counter

def scrittura(dati: dict | list | list[list], path: str) -> bool:
    """
    Scrive un dizionario in un file json con indent = 3
    """
    try:
        fo = open(path,'w',encoding='utf-8')
        json.dump(dati, fo, indent=3)
        fo.close()
        return True
    except json.decoder.JSONDecodeError():
        print('Formato json non valido')
        return False



def lettura(path: str) -> list[list] | dict | None:
    """
    Legge e restituisce i dati contenuti in un file json
    """
    try:     
        fi = open(path,'r', encoding='utf-8')
        dati = json.load(fi)
        fi.close()
        return dati
    except OSError:
        print(f"File all'indirizzo {path} non trovato")
        return None
    except json.decoder.JSONDecodeError():
        print('Formato json non valido')
        return None
    



def log(dati: list[list]) -> dict:
    """
    Prende una lista di log e la trasforma in un dizionario che ha come
    chiave l'ID dell'utente e come valori gli eventi ad esso associati

    """
    dizionario = {}
    for e in dati:
         if e[1] not in dizionario:
              dizionario.update({e[1]:[e[4]]})
         else:
              dizionario[e[1]].append(e[4])
    return dizionario


def conta_ev(dizionario: dict) -> dict:
    """
    Condensa le informazioni sulle azioni in un unico dizionario nidificato.
    """

    # Trasforma il dizionario di partenza in conteggi nidificati
    dati_condensati = {}
    for user_id, actions_list in dizionario.items():
        # Utilizza Counter per contare le occorrenze di ogni azione
        dati_condensati[user_id] = dict(Counter(actions_list))
    return dati_condensati