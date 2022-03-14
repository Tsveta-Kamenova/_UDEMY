def middle(s):
    if len(s)%2==0:
        i = int(len(s)/2)-1
        return s[i]+s[i+1]
    else:
        return s[int(len(s)/2)]


print(middle(input()))