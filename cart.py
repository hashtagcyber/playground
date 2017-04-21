#!/usr/bin/env python
#Create a new class, called items. Used to define the UPC,name,and price of items in the store
class item(object):
#List to store the item names that currently exist.
	inventory = {}

	def __init__(self,name,price):
		self.name = name
		self.price = price
		self.itemno = len(item.inventory) + 1
		item.inventory[self.itemno] = self

	def __str__(self):
		strName = "Item:\t\t%s\n" % self.name
		strPrice = "Price:\t\t$%.2f\n" % self.price
		strItemNo = "ItemNum:\t%04d" % self.itemno
		return strName + strPrice + strItemNo
#Class to store on hand
class mystore(object):
	localstock = {}
	def restock(self,OHitem,qty):
		mystore.localstock[OHitem] = qty
	def __str__(self):
		results = ""
		for x in mystore.localstock:
			results += "Item: %s\tQty: %s\n" % (x.name,mystore.localstock[x])
		return results
