#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9):
        self.brand = brand
        self.size = size
        self.condition = "Used"

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, value):
        if type(value) == int:
                self._size = value
        else:
            print("size must be an integer")
        
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
