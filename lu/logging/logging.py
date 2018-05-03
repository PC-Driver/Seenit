f = open('logging.txt', 'w')

def writing(content):
    print (content)
    f.write(content)

def closing():
    f.close()