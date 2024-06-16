#!/usr/bin/env python3
import ipdb

class CashRegister:
  
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.previous_transactions = {}

  def add_item(self, name, price = 0, quantity = 1):
    self.total = self.total + (price * quantity) 
    for _ in range(quantity):
        self.items.append(name)
    self.previous_transactions = ({"item":name, "price":price, "quantity":quantity})

  def apply_discount(self):
    self.total = self.total * ((100 - self.discount)/100)
    if self.discount > 0:
      print(f'After the discount, the total comes to ${int(self.total)}.') 
    else: 
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    if not self.previous_transactions:
        return "There are no transactions"
    self.total -= (
        self.previous_transactions[-1]["price"] 
        * self.previous_transactions[-1]["quantity"])
    for _ in range(self.previous_transactions[-1]["quantity"]):
        self.items.pop()
    self.previous_transactions.pop()
  
new_register = CashRegister(10)
cash_register = CashRegister()
cash_register_with_discount = CashRegister(20)
new_register.add_item("eggs", 1.99)
new_register.add_item("tomato", 1.76)
cash_register.add_item("Lucky Charms", 4.5)
cash_register.add_item("Ritz Crackers", 5.0)
cash_register.add_item("Justin's Peanut Butter Cups", 2.50, 2)
#ipdb.set_trace()