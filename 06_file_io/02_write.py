file = open('newFile.txt', 'w') # if file not exits, then it will create one on that name 

file.write('this is new file content')
file.close()


#* append in file
file = open('newFile.txt', 'a')
file.write('this is appended text')
file.close()