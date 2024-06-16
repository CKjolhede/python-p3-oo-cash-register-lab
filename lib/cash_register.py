#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []

  def add_item(self, name, price = 0, quantity = 1):
    self.total = self.total + (price * quantity) 
    for _ in range(quantity):
        self.items.append(name)
    return

  def apply_discount(self):
    self.total = self.total * ((100 - self.discount)/100)
    if self.discount > 0:
      print(f'After the discount, the total comes to ${int(self.total)}.') 
    else: 
      print("There is no discount to apply.")