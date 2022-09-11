def merge_the_tools(string, k):
    s=[i for i in string]
    for i in range(len(string)//k):
        t=''
        for j in range(k):
            t+=s[0]
            s.pop(0)
        u=''
        for h in t:
            if h not in u:
                u+=h
        print(u) 

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)