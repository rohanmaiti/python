# file = open('file.txt') # when opening a file the function open takes 2 arguments 
                        # 1. path of file 2. mode (read[r], write[w], append[a], updating[+], [rt]open for read in text mode) 
                        # 2. By default it's in read mode
# content = file.read()
# file.close() 
# print(content)


# file1 = open("newFile.txt")
# filelines = file1.readlines() # this returns a list of lines 
# file1.close()
# print(filelines)
# file1.close()

#* what if the file that you want to read does not exists?
# file2 = open('xyz.txt') # this  will give error 
# content = file2.read()
# print(content) 
# file2.close()



#* have another similar function ---> readline
# file = open('newFile.txt')
# line = file.readline()
# while( line != ""):
#     print(line)
#     line = file.readline()
# else:
#     print("\n---complete reading lines---")
# file.close()


#* with 
# to remove the burden of closing file 
with open('newFile.txt') as f:
    print(f.read())

# after exting the with block, file automaticaly closes 