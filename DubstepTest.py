s = input()

def s1(s):
    s = s.split('WUB')
    list = []
    for i in s:
        if i != '':
            list =list+ [i]
    return ' '.join(list)



print(s1(s))
