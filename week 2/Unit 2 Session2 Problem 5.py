# Problem 5: Best Set
# As part of the festival, attendees cast votes for their favorite set.
#  Given a dictionary votes that maps attendees id numbers to the 
# artist they voted for, return the artist that had the most number of votes.
#  If there is a tie, return any artist with the top number of votes.

# Understand:
# input: a dictionary
# output: the artist that had the most number of votes

#Plan:
# 1. Initialize an empty dictionary to store the count of votes for each artist.
# 2. Iterate through the values in the votes dictionary.
# 3. If the artist is already in the dictionary, increment the count.
# 4. Otherwise, add the artist to the dictionary with a count of 1.
# 5. Return the artist with the maximum count.

def best_set(votes):
    artist_votes = {}
    for artist in votes.values():
        if artist in artist_votes:
            artist_votes[artist] += 1
        else:
            artist_votes[artist] = 1
    return max(artist_votes, key=artist_votes.get)


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))