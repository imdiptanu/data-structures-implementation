"""
hashmap.py
Hashmap implementation in python.
@author: diptanu sarkar, ds9297@cs.rit.edu
"""
from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''
class _delobj: pass
DELETED = Entry(_delobj(),None)

class Hashmap:

	__slots__ = 'table','numkeys','cap','maxload'

	def __init__(self,initsz=100,maxload=0.7):
		'''
		Creates an open-addressed hash map of given size and maximum load factor
		:param initsz: Initial size (default 100)
		:param maxload: Max load factor (default 0.7)
		'''
		self.cap = initsz
		self.table = [None for _ in range(self.cap)]
		self.numkeys = 0
		self.maxload = maxload

	def put(self,key,value):
		'''
		Adds the given (key,value) to the map, replacing entry with same key if present.
		:param key: Key of new entry
		:param value: Value of new entry
		'''
		firstDeleted = None # we have to search through the whole line to to make sure we aren't adding duplicates
		index = self.hash_func(key) % self.cap
		while self.table[index] is not None and \
						self.table[index].key != key:
			if self.table[index] == DELETED and firstDeleted == None:
				firstDeleted = index
			index += 1
			if index == len(self.table):
				index = 0
		#if we encountered a deleted and we didn't find the key change the key index to the first deleted index
		if firstDeleted != None and (self.table[index] == None or self.table[index].key != key):
			index = 	firstDeleted	
		#otherwise if we haven't found the index then increase the size of the occupied cells
		elif self.table[index] is None:
			self.numkeys += 1
			
		self.table[index] = Entry(key,value)
		if self.numkeys/self.cap > self.maxload:

			# rehashing
			oldtable = self.table
			# refresh the table
			self.cap *= 2
			self.table = [None for _ in range(self.cap)]
			self.numkeys = 0
			# put items in new table
			for entry in oldtable:
				if entry is not None:
					self.put(entry[0],entry[1])


	def remove(self,key):
		'''
		Remove an item from the table
		:param key: Key of item to remove
		:return: Value of given key
		'''
		index = self.hash_func(key) % self.cap
		while self.table[index] is not None and self.table[index].key != key:
			index += 1
			if index == len(self.table):
				index = 0
		if self.table[index] is not None:
			self.table[index] = DELETED


	def get(self,key):
		'''
		Return the value associated with the given key
		:param key: Key to look up
		:return: Value (or KeyError if key not present)
		'''
		index = self.hash_func(key) % self.cap
		while self.table[index] is not None and self.table[index].key != key:
			index += 1
			if index == self.cap:
				index = 0
		if self.table[index] is not None:
			return self.table[index].value
		else:
			raise KeyError('Key ' + str(key) + ' not present')

	def contains(self,key):
		'''
		Returns True/False whether key is present in map
		:param key: Key to look up
		:return: Whether key is present (boolean)
		'''
		index = self.hash_func(key) % self.cap
		while self.table[index] is not None and self.table[index].key != key:
			index += 1
			if index == self.cap:
				index = 0
		return self.table[index] is not None

	def hash_func(self,key):
		'''
		Not using Python's built in hash function here since we want to
		have repeatable testing...
		However it is terrible.
		Assumes keys have a len() though...
		:param key: Key to store
		:return: Hash value for that key
		'''
		# if we want to switch to Python's hash function, uncomment this:
		#return hash(key)
		return len(key)

def printMap(map):
	for i in range(map.cap):
		print(str(i)+": " + str(map.table[i]))

def testMap():
	map = Hashmap(initsz=5)
	map.put('apple',1)
	map.put('banana',2)
	map.put('orange',15)
	printMap(map)
	print(map.contains('apple'))
	print(map.contains('grape'))
	print(map.get('orange'))

	print('--------- adding one more to force table resize ')
	map.put('grape',7)
	printMap(map)

	print('--------- testing remove')
	map.remove('apple')
	map.remove('orange')
	printMap(map)

	print('--------- testing add to a DELETED location')
	map.put('peach',16)
	map.put('grape',19)
	printMap(map)
	print(map.get('grape'))


if __name__ == '__main__':
	testMap()
