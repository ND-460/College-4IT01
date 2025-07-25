print("By 22IT460")
dict1 = {'a':10,'b':20}
dict2 = {'a':5,'c':20}
combine = dict1.copy()
for key in dict2:
    if key in combine:
        combine[key] = combine[key] + dict2[key]
    else:
        combine[key] = dict2[key]
print(f"Combined dictionary of {dict1} and {dict2} is {combine}")