class converter:
    def __init__(self):
        self.filename = "conversions.txt"
        self.diction = {}
        file = self.filename
        
        
    def add_currency(self):
        print()
        print("Hi, type in a country and the country that you would like to convert into to.")
        action = input("structure it in the format of,  your country - other country: conversion rate")
        for i in open(self.filename, "r+"):
            segments = i.rstrip(":", 1)
            self.diction[segments[0]] = segments[0].rstrip("\n")
            
            
            
    
c1 = converter()