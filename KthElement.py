# Name: Isac Polasak
# OSU Email: Polasais@oregonstate.edu
# Course: CS325
# Description: We check if an element at an index is smaller in arr1 or arr2,
# depending on that, we add it to the new array and up the index on whichever
# element was smaller. Then, when that while loop is done, we check if there’s
# anything left in arr1 or arr2, whichever has something left gets added at the
# end of the new array. Finally, we print whatever is in the kth position.


def kthElement(Arr1, Arr2, k):
    i = 0            #We will set i as Arr1’s starting index
    j = 0            #We will set j as Arr1’s starting index
    new_array = []
    while len(Arr1) > i and len(Arr2) > j:
    #While there are more items left in arr1 or arr2, continue the adding to the new array.
        if Arr1[i] > Arr2[j]:   #If element in arr1 is > element in arr2, append element 1
            new_array.append(Arr2[j])
            j += 1
        else:
            new_array.append(Arr1[i])
            i += 1
    if i >= len(Arr1):          #If there are still items left in arr2, append arr2 to end of new arr.
        while j < len(Arr2):
            new_array.append(Arr2[j])
            j += 1
    else:
        while i < len(Arr1):
            new_array.append(Arr1[i])
            i += 1
    return new_array[k-1] #return k-1 to get the kth element.
