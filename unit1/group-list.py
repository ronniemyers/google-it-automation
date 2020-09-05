def group_list(group, users):
    members = ""
    if len(group)!=0:
        members += group + ":"
    if len(users)!=0:
        members += " " + users[0]
    if len(users)>1:
        for x in users[1:]:
            members += ", " + x
    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
print (group_list("Users",""))