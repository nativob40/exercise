def contain(words, letters):
    
    l_words = []
    
    for l in letters:
        for i in words:
            pos = i.find(l)
            if pos != -1:
                l_words.append(i)
    
    return print(set(l_words))

words = ['casa','aereo','pesce']



contain(words,'pr')