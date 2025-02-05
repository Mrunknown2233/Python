def wordFreq(s): #here s is a string offcourse
    s = s.lower(); #This is done to count 2 occurrence of a given word with different cases(lower or upper) as 1
    words = s.split();
    # print(type(words))
    freq = {} #creating a empty dictionary

    for word in words: 
        if word in freq :
            freq[word] += 1 ;  #here word works as a key for dict freq which is taken from a list words
        else : 
            freq[word] = 1;  #here word works as a key for dict freq which is taken from a list words
    return freq

s = '''This is the sample string which is very beautiful.
    But reading this will make you dumb. No worries you are born dumb!'''

wordCounts = wordFreq(s)

print(wordCounts)