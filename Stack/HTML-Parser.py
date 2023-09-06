def match_tages(filepath):
    with open(filepath,'r') as file:
        content = file.read()
    stack = []
    i = 0

    while i < len(content):
        if content[i] == '<':
            if content[i] == '</':
                i = i+2
                entag = content.find('>',i)
                if entag == -1:
                    return False
                closingtag = content[i:entag].strip()
                i = entag + 1

                if not stack or stack.pop() != closingtag:
                    return False
                
            else:
                i = i+1
                entag = content.find('>',i)
                if entag == -1:
                    return False
                openingtag = content[i:entag].strip()
                i = entag + 1
                stack.append(openingtag)

        else:
            i = i+1
    return len(stack) == 0
    
if match_tages('E:\ADS LAB PRACTICE\Stack Programs\Stack\HtmlDummyFile.html'):
    print("Tags are properly matched.")
else:
    print("Tags are not properly matched.")



