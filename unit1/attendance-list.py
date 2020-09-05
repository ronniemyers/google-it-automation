# Generate a new list containing the elements of list2
# Followed by the elements of list1 in reverse order

def combine_lists(list1, list2):
    combine = list2

    for i in reversed(range(len(list1))):
        combine.append(list1[i])
    return combine


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
