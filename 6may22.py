
'''
1209. Remove All Adjacent Duplicates in String II

'''

s = "deeedbbcccbdaa"

k = 3
s1 = []
s2 = []
for i in s:
    s2.append(i)
    if len(s2)>1 and s2[-1] == s2[-2]:
        s1.append(s1[-1]+1)
    else:
        s1.append(1)
    if s1[-1] == k:
        del s2[-k:]
        del s1[-k:]


print(''.join(s2))

