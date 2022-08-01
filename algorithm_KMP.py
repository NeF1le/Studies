s = "lilila"
p = [0] * len(s)
i = 1
j = 0
while i < len(s):
    if s[i] == s[j]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]

a = "lililos lililas"
i = 0
j = 0
while i < len(a):
    if a[i] == s[j]:
        i += 1
        j += 1
        if j == len(s):
            print(True)
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1
if i == len(a):
    print(False)