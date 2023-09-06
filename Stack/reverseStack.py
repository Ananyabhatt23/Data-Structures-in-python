import os

def reverseStackContent():
    stacklist = []
    with open('E:\\ADS LAB PRACTICE\\Stack Programs\\ReverseContent\\ReverseContent.txt','r') as file:
        content = file.read()
        content = content.split()
        stacklist = content
        stacklist.reverse()
        file.close()
    with open('E:\\ADS LAB PRACTICE\\Stack Programs\\ReverseContent\\ReverseContent.txt','w') as rfile:
        for i in stacklist:
            rfile.write(i+' ')
        rfile.close()

        
reverseStackContent()