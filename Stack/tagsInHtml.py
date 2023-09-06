def match_tags(html):
    stack = []
    i = 0  

    while i < len(html):
        if html[i] == '<':
            if html[i:i + 2] == '</':
                i += 2
                tag_end = html.find('>',i)
                if tag_end == -1:
                    return False  
                closing_tag = html[i:tag_end].strip()
                i = tag_end + 1

                if not stack or stack.pop() != closing_tag:
                    return False
            else:
                i += 1
                tag_end = html.find('>', i)
                if tag_end == -1:
                    return False  
                opening_tag = html[i:tag_end].strip()
                i = tag_end + 1
                stack.append(opening_tag)

        else:
            i += 1
    return len(stack) == 0


html_string = "<html><head><title>Sample Page</title></head><body><p>Hello, world!</p></body></html>"
if match_tags(html_string):
    print("Tags are properly matched.")
else:
    print("Tags are not properly matched.")

    

