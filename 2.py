"""
ALGORITHM: ARRANGING CLOTHES IN A LUGGAGE BAG
1. Define a suitcase with three layers: Base, Middle, and Top.
2. List the items to be packed, noting their weight and if they are delicate.
3. Check each item one by one to decide its placement:
    a. If the item is 'Heavy' (like boots), place it in the Base Layer for stability.
    b. If the item is 'Delicate', place it in the Top Layer to prevent damage.
    c. For all other clothes, roll them to save space and place them in the Middle Layer.
4. Execute the packing process.
5. Print the final packing order from bottom to top.
"""

suitcase = {
    "Base_Layer": [],
    "Middle_Layer": [],
    "Top_Layer": []
}

packing_list = [
    {"name": "Hiking Boots", "weight": "Heavy", "delicate": False},
    {"name": "Cotton T-shirts", "weight": "Light", "delicate": False},
    {"name": "Evening Silk Dress", "weight": "Light", "delicate": True},
    {"name": "Denim Pants", "weight": "Heavy", "delicate": False},
    {"name": "Toiletries", "weight": "Medium", "delicate": False}
]

def pack_suitcase(items):
    for item in items:
        if item["weight"] == "Heavy":
            suitcase["Base_Layer"].append(item["name"])
        elif item["delicate"] == True:
            suitcase["Top_Layer"].append(item["name"])
        else:
            suitcase["Middle_Layer"].append("Rolled " + item["name"])

pack_suitcase(packing_list)

print("Luggage Packing Order:")
print("Bottom Layer:", suitcase["Base_Layer"])
print("Middle Layer:", suitcase["Middle_Layer"])
print("Top Layer:", suitcase["Top_Layer"])