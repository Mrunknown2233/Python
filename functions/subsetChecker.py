def subSetChecker(set1, set2): 
    return set2.issubset(set1)

set1 = {1,2,3,4,5,6,7,8}
set2 = {6,5,3,1,2}

print(f"set1 {set1} subset of set2 {set2} = {subSetChecker(set1,set2)}")