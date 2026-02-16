#Dictionary
info={"name":"raso",
      "age":28,
      "place":"hyderabad"}
print(info)

#Access values
print(info.keys())
print(info.values())
print(info.get("name"))

#add an item
info["course"]="AI&ML"
print(info.items())

#update a value
info["age"]="25"
print(info.items())

#loop through dictionary
for keys,values in info.items():
    print(keys, ":", values)
