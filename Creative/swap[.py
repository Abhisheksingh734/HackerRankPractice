def swap_case(s):
    list=[]
    str=""
    for i in s:
        if i.islower()==True:
            list.append(i.upper())
        elif i.isupper()==True:
            list.append(i.lower())
        else:
            list.append(i)
    for i in list:
        str+=i
    return str
    
            
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)