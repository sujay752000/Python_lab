lst = ["sujay", "prasad", "ashik", "sreeraj"]

name_dict = {}

for i in lst:
    name_dict.update({i: i.count("a")})

print(name_dict)

for key, val in name_dict.items():
    print(f"a in {key} = {val}")
