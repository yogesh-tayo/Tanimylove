def sortBoxes(boxList):
    value1=[]
    value2=[]
    for i in boxList:
        if i.split()[1].isdigit():
            value2.append(i)
        else:
            value1.append(i)    
    value1=sorted(value1,key=lambda x:x.split()[0])
    value1=sorted(value1,key=lambda x:x.split()[1:])
    return value1+value2