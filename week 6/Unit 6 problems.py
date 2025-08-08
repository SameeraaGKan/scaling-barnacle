# We will approach problems using the six steps in the UMPIRE approach.
# UMPIRE: Understand, Match, Plan, Implement, Review, Evaluate.

# We’ll apply these six steps to the problems we’ll see in the first half of the course.

# We will learn to:

# Understand the problem
# Match identifies common approaches you've seen/used before
# Plan a solution step-by-step, and
# Implement the solution
# Review your solution
# Evaluate your solution's time and space complexity and think critically about the advantages and disadvantages of your chosen approach.


# Q1
# Problem 1: Building a Playlist
# The assignment statement to the top_hits_2010s variable below creates the linked list
#  Uptown Funk -> Party Rock Anthem -> Bad Romance. Break apart the assignment statement 
#  into multiple lines with one call to the Node constructor per line to recreate the list.

class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
		
# top_hits_2010s = SongNode("Uptown Funk", Node2)

# Node2 = SongNode("Party Rock Anthem", Node3)
# Node3 = SongNode("Bad Romance")

top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

print_linked_list(top_hits_2010s)


# Q2

# Problem 2: Top Artists
# Given the head of a linked list playlist, return a dictionary that 
# maps each artist 
# in the list to its frequency.

# Evaluate the time complexity of your solution. Define your variables and provide a 
# rationale for why you believe your solution has the stated time and space complexity.

# input: head, playlist
# output: return dictionary, artist: frequency
# class SongNode:
# 	def __init__(self, song, artist, next=None):
# 		self.song = song
#         self.artist = artist
# 		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
	pass

