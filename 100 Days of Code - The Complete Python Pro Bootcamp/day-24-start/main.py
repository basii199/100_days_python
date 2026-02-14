file = open('file.txt')
# when using open, always remember to close the file with .close()
content = file.read()
# other useful methods -> readline, readlines
print(content)
file.close()

# or use the with syntax that closes it at the end of scope
# with open('file.txt', mode='a') as file_2:
    # modes -> r: read, w: write, a: append
    # file_2.write('\nThis is me. Hehe')
    # cont = file_2.read()
    # print(cont)

