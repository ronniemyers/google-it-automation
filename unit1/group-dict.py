def groups_per_user(group_dictionary):
  user_groups = {}
  for key in group_dictionary.keys():
    for val in group_dictionary[key]:
      if val in user_groups.keys():
        user_groups[val].append(key)
      else:
        user_groups[val]=[key]
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"]}))