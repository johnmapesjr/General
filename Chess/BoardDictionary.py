# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 10:20:50 2014

@author: owner
"""
from pickle import *
import sys


def loadfile():

    global BoardDictionary
    try:
       with open('chess.dat', "rb") as file:
           unpickler = Unpickler(file);
           BoardDictionary = unpickler.load();
           if not isinstance(BoardDictionary, dict):
              BoardDictionary = {};
    except EOFError:
       return {}
       

#load only once
BoardDictionary = {}  #data file dictionary
loadfile()
#start loop
while True:
           
    print("Chess Dictionary: Enter command(p-rint,l-ength,d-elete,e-xit)")
    command = input()
    
    if command == "p":
        # Loop over items and unpack each item.
        print("fen, values")
        for k, v in sorted(BoardDictionary.items()):
            # Display key and value.
            print(k, v)
           
    if command == "d":
        # delete the board from the dictionary.
        print("Enter fen of board to delete:")
        fen = input()
        # Remove key-value at windows
        del BoardDictionary[fen]
        
    
    if command == "l":
        # Display length
        print("Length:", len(BoardDictionary))
    
    if command == "e":
        # exit
        print("exit")
        sys.exit()
        
        
    
    
       
       