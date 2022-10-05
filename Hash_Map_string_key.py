"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        h=self.calculate_hash_value(string)
        self.table[h]=string

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        h=self.calculate_hash_value(string)
        if self.table[h]==string:
            return h
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        ab = string[0:2]
        count=0
        for i in range(len(ab)):
            # print(ord(ab[i]))
            count+=ord(ab[i])*100**(len(ab)-i-1)
        return count
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
