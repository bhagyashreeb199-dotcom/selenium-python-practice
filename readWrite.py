#file = open("text.txt")

#Reading all component
#print(file.read(2))

#read first line
#print(file.readline())
#read 2nd line
#print(file.readline())

#print content line by line using readline
'''line = file.readline()
while line != "":
    print(line)
    line = file.readline()

print("that's it")'''

#print content using readlines
'''for line in file.readlines():
    print(line)

file.close()'''


with open('test.txt', 'r') as file:
    read = file.readlines()  #a,b,c,d,e
    reversed(read)  #e,d,c,b,a

    with open('test.txt', 'w') as file1:
        for line in reversed(read):
            file1.write(line)

