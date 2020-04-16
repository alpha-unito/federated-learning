def a():
    print('a')

obj = {'callback': a}

obj['callback']()