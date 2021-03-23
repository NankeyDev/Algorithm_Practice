'''
Practice example of hash table using open addressing
Created on Mar 22, 2021

@author: Nankey
Based on example code written by Davide Mastromatteo, github = mastro35
Reference: http://thepythoncorner.com/dev/hash-tables-understanding-dictionaries/

'''

import sys
import pprint

class hashTable:

    def __init__(self, element):
        self.bucketSize = len(element)
        self.buckets = [[] for i in range(self.bucketSize)]
        self.hashInsert(element)
        
    def hashInsert(self, element):
        print('Insert: ', element)
        self.buckets = [None] * self.bucketSize
        
        for key, value in element:
            hashedValue = hash(key)
            index = hashedValue % self.bucketSize
            
            while self.buckets[index] is not None:
                print(f'The key {key} collided with {self.buckets[index]}')
                index = (index + 1) % self.bucketSize

            self.buckets[index] = (key,value)
        
    def hashSearch(self, inputKey):
        print('Search: ', inputKey)
        hashedValue = hash(inputKey)
        index = hashedValue % self.bucketSize
        
        while self.buckets[index] is not None:
            key, value = self.buckets[index]
            if key == inputKey:
                return value
            index = (index + 1) % self.bucketSize
        #return None
        
    def __str__(self):
        return pprint.pformat(self.buckets)

if __name__ == "__main__":
    people = [
        ('Amy', 5),
        ('Jonas', 45),
        ('Ivanka', 64),
        ('Misa', 16)
        ]

print('Python version:', sys.version)
print('            ')

hashTable = hashTable(people)
print('            ')

print(hashTable)
print('            ')

x = 'Misa'
print(x, 'is', hashTable.hashSearch(x), 'years old')



