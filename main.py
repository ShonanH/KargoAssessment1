import sys

first_arg = sys.argv[1]
second_arg = sys.argv[2]

def isIsomorphic(s=first_arg, t=second_arg):
    if (len(s) != len(t)):
        return (False)
    return getIso(s,t) and getIso(t,s)
    
def getIso(s=first_arg, t=second_arg):
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
if __name__ == "__main__":
    print(isIsomorphic())
