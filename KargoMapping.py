def isIsomorphic(s, t) -> bool:
    if (len(s) != len(t)):
        return (False)
    return getIso(s,t) and getIso(t,s)
    
def getIso(s, t):
    #print (t)
    len_s = len(s)
    len_t = len(t)
    check = {} #create a dictionary
    for i in range(len_s):
        if s[i] not in check:
            #print (check)
            #print (s[i])
            check[s[i]] = t[i]
            #print(check)
        elif check[s[i]] != t[i]:
            return (False)
    return (True)
print(isIsomorphic("foo", "321"))