class converter:
    def __init__(self):
        self.filename = "conversions.txt"
        self.dict = {}
        
    def add_currency(self):
        action = input("Hi, type in a country and the country that you would like to convert into to.")
        print("structure it in the format of,  your country - other country: conversion rate")
        for i in open(self.filename, "r+"):
            segments = i.strip(":", 1)
            self.map[segments[0] = segments[1].rstrip("\n")
            
            
    
c1 = converter()
