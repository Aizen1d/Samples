myDictionary = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(dictionary):
    online = 0
    for key, value in dictionary.items():
        if value == "online":
            online = online + 1

    return online

print(online_count(myDictionary))
