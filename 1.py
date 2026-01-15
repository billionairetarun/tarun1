"""
ALGORITHM: ARRANGING CLOTHES IN AN ALMIRAH
1. Initialize an almirah with three main sections: Top, Middle, and Bottom.
2. Create a list of clothes, labeling each by its type (Formal, Casual, or Traditional).
3. Loop through each item in the clothes list.
4. If an item is 'Traditional', place it on the Top Shelf for long-term storage.
5. If an item is 'Formal', place it on the Middle Shelf for easy daily access.
6. For all other items (Casual), place them on the Bottom Shelf.
7. Display the final organization of the almirah.
"""

almirah = {
    "Top_Shelf": [],
    "Middle_Shelf": [],
    "Bottom_Shelf": []
}

clothes_to_store = [
    {"item": "Office Shirt", "type": "Formal"},
    {"item": "Silk Saree", "type": "Traditional"},
    {"item": "Jeans", "type": "Casual"},
    {"item": "T-shirt", "type": "Casual"},
    {"item": "Suit Jacket", "type": "Traditional"}
]

def arrange_almirah(items):
    for item in items:
        if item["type"] == "Traditional":
            almirah["Top_Shelf"].append(item["item"])
        elif item["type"] == "Formal":
            almirah["Middle_Shelf"].append(item["item"])
        else:
            almirah["Bottom_Shelf"].append(item["item"])

arrange_almirah(clothes_to_store)

print("Almirah Organization:")
for shelf, items in almirah.items():
    print(f"{shelf}: {items}")