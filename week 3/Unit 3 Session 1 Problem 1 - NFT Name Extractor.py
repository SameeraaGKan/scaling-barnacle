"""

You're curating a large collection of NFTs for a digital art gallery,
 and your first task is to extract the names of these NFTs from a given list of dictionaries. 
 Each dictionary in the list represents an NFT, and contains information such as the name,
   creator, and current value.

Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and
 provide a rationale for why you believe your solution has the stated time and space complexity.

"""

def extract_nft_names(nft_collection):
    """
    Extracts the names of NFTs from a list of dictionaries.

    Parameters:
    nft_collection (list): A list of dictionaries, each representing an NFT.

    Returns:
    list: A list of NFT names.
    """
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft['name'])
    return nft_names

# def extract_nft_names(nft_collection):
#     nft_names = []
#     for nft in nft_collection:
#         nft_names += nft["name"]
#     return nft_names


"""
You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.

Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
def identify_popular_creators(nft_collection):
    creator_count = {}
    for nft in nft_collection:
        creator = nft["creator"]
        creator_count[creator] = creator_count.get(creator, 0) + 1
    return [creator for creator, count in creator_count.items() if count > 1]

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]
# print(extract_nft_names(nft_collection))

print(identify_popular_creators(nft_collection))


