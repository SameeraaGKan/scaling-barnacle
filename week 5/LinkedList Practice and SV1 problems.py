# A Node class might commonly look like the following.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    # Constructor.
    def __init__(self):
        # The first node in the linked list.
        # The head is either a Node object or None if the list is empty.
        self.head = None

    # Method. Adds a new node with the specific data value to the beginning of the linked list.
    def add_first(self, value):
        pass

    # Method. Adds a node with specified value to the end of the list.
    def append(self, value):
        pass

    # Method. Returns the length of the list.
    def length(self):
        pass

    # Method. Returns the value at a given index in the linked list.
    # Index count starts at 0.
    # Returns None if there are fewer nodes in the linked list than the index value.
    def get_at_index(self, index):
        pass


# Linked List Traversal

def traverse(head):
        current = head
        while current:
            # Perform operations on the current node (e.g., print the value)
            current = current.next # Move to the next node








# ********

#Problem 1
''''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

apollo = Villager("Apollo", "Eagle", "pah")

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
#print(apollo.furniture) 

'''


#PROBLEM 2 
"""Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your 
existing code:

Step 2: Create a second instance of Villager in a variable named bones.
The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".

Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! 
How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console."""

'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []


    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20:
            for c in new_catchphrase:
                if not (c.isspace() or c.isalpha()):
                    print("Invalid Catchprase")
                    return
            self.catchphrase = new_catchphrase
            print("Updated Catchphrase")
        else:
            print("Invalid Catchphrase") 

bones = Villager("Bones","Dog", "ruff it up!")

print(bones.greet_player("Samia"))

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
'''
            


# Problems 5

"""
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", or "cacao tree"."""

# PROBLEM 6
"""
Problem 6: Print Inventory
Update the Villager class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a villager’s furniture list.

The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for however many unique 
items exist in the villager's furniture list
If the player has no items, the function should print "Inventory empty".
    
"""
# initialize dictionary
# loop through furniture list
# if in dictionary, then +1
# if not, then = 1
# return "item: quantity"
# if empty, "inventory empty"


'''

class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
	
    # New method
    def add_item(self, item_name):
        valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]

        if item_name in valid:
            self.furniture.append(item_name)


    def print_inventory(self):
        
        if len(self.furniture) == 0:
            print("Inventory empty")
        else:
            item_count = {}
            for item in self.furniture:
                if item in item_count:
                    item_count[item] += 1
                else:
                    item_count[item] = 1
            inventory = " , ".join([f"{item}: {count}" for item, count in item_count.items()])
            print(inventory)

        inventory_list = []
        for item, count in item_count.items():
            inventory_list.append(f"{item}: {count}")   



alice = Villager("Alice", "Koala", "guvnor")
alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()


alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)

Problem 7: Group by Personality
The Villager class has been updated below to include the new string 
attribute personality representing the character's personality type.

Outside of the Villager class, write a function of_personality_type(). 
Given a list of Villager instances townies and a string personality_type as parameters, 
return a list containing the names of all villagers in townies with personality personality_type. 
Return the names in any order.


# input: list -> townies and string -> personality_type
# output: list with names of all villagers with personality type, names in any order

# edge cases: empty list, empty string - return empty list

#planning:
# initialize list, match to personality type
# loop through townies
# if personality = personality_type -> add to list
# return list


#Problem 7
class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
    
def of_personality_type(townies, personality_type):
    match = []
    for person in townies:
        if person.personality == personality_type:
            match.append(person.name)
    return match
            
#time and space: O(N)

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))
'''
"""
Problem 8: Telephone
The Villager constructor has been updated to include an additional attribute neighbor. 
A villager's neighbor is another Villager instance and represents their closest neighbor. 
By default, a Villager's neighbor is set to None.

Given two Villager instances start_villager and target_villager, write a function message_received() 
that returns True if you can pass a message from the start_villager to the 
target_villager through a series of neighbors and False otherwise.

"""

# input: string, start_villager and target_villager
# output: return True - start can pass to target, False - cannot

# 

# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor=None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor
#     # ... methods from previous problems
    
# def message_received(start_villager, target_villager):
#     curr = start_villager
#     while curr:
#         if curr == target_villager:
#             return True
#         curr = curr.neighbor
#     return False

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))


# Problem 9: Nook's Cranny
# A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. 
# The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

# In a normal list, individual elements of the list are stored in adjacent memory locations according to the 
# order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any 
# other element in the list.

# # In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

# Using the provided Node class below, create a linked list Tom Nook -> Tommy where the instance tom_nook
#  has value "Tom Nook" which points to the instance tommy that has value "Tommy".

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy") 
# timmy = Node("Timmy")
# tom_nook.next = timmy 
# timmy.next = tommy

# print(tom_nook.value)
# print(tom_nook.next.value)
# print(timmy.value)
# print(timmy.next.value)
# print(tommy.value)
# print(tommy.next)


# Problem 11

# Problem 11: Saharah
# Using the linked list from Problem 10, remove the tom_nook node and add in a node saharah with value 
# "Saharah" to the end of the list so that the resulting list is timmy -> tommy -> saharah.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy") 
# timmy = Node("Timmy")
# tom_nook.next = timmy
# timmy.next = tommy
# saharah = Node("Saharah")
# tommy.next = saharah

# print(tom_nook.next) 
# print(timmy.value) 
# print(timmy.next.value)  
# print(tommy.value) 
# print(tommy.next.value)
# print(saharah.value)  
# print(saharah.next) 


""" Write your code here
Problem 12: Print List
Write a function print_list() that takes in the head of a linked list and returns a string linking together the values of the list with the separator "->".

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

"""

# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# def print_list(head):
#     curr = head
#     s = []
#     while curr:
#         s.append(curr.value) 
#         curr = curr.next
    
#     return "->".join(s)


# isabelle = Node("Isabelle")
# saharah = Node("Saharah")
# cj = Node("C.J.")

# isabelle.next = saharah
# saharah.next = cj

# print(print_list(isabelle))


