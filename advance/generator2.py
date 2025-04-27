def rev_str(my_str):
    length = len(my_str)

    for i in range(5, -1, -1):   #doesn't include -1 i.e will work from 5 to 0 
        yield my_str[i]


rev_str("Soumya")