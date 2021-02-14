name=input("enter the name")
def most_frequent(name):
    dict={}
    for n in name[::-1]:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1

    return dict 
print(most_frequent(name))





