String1=input("enter a string: ")

def upperandlower(String1): 
    Upper=[]
    Lower=[]
    for i in String1:
        if i.isupper():
            Upper.append(i)
        elif i.islower():
            Lower.append(i)
    return "No. of Upper case characters : ",len(Upper), "No. of Lower case Characters : ", len(Lower)

print(upperandlower(String1))