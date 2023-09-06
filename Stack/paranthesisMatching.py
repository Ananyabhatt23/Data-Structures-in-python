def paranmatch(filepath):
    with open(filepath,"r") as file:
        content = file.read()
    list1 = "{(["
    list2 = "})]"
    stk = []

    for i in content:
        if i in list1:
            stk.append(i)
        elif i in list2:
            if len(stk) == 0:
                print("Matching Not Done")
                return
            indexoflist2 = list2.index(i)
            val = list1[indexoflist2]
            if val in stk:
                ind1 = stk.index(val)
                if stk.index(val) == len(stk)-1:
                    stk.pop(ind1)
            else:
                print("Matching not Done here: "+i)
    if len(stk) != 0:
        print("Error")
        
paranmatch("E:\\ADS LAB PRACTICE\\Stack Programs\\ParanthesisMatching\\testfile.txt")