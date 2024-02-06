l = [2,4,6,4,8,7,2,8,8,9,4,6,6,10,7,5]

unique = []

duplicate = []


for i in l:
    if(i in unique):
        unique.remove(i)
        duplicate.append(i)
    else:
        if(i not in duplicate):
            unique.append(i)                                                                                                                                                                                                                                                                                                                

print(unique)
print(duplicate)