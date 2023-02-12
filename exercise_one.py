def repeated(num):
    
    for i in str(num):
        if str(num).count(i) > 1:
            return print('y')

    return print('n')


repeated(13265) # 'n'
repeated(33265) # 'y'