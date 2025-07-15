
#* Q1. read a file poem.txt and print wheather it contains a work 'twinkle'
# with open('poem.txt') as file:
#     if('twinkle' in file.read()):
#          print('WORD present')
#     else:
#         print("WORD NOT present")    
   

#* Q2. generate 2 to 20 table for a 13 year old and save each table in tables folderxw
# def generateTable(num):
#     with open(f'tables/table_{num}.txt', 'a') as file:
#         for i in range(1,11):
#             content = f"{num} X {i} = {num * i}\n"
#             file.write(content)


# for i in range(2,21):
#     generateTable(i)


#* Read a file subtitle.txt and replace all the sensor words in the list ['ganda', 'donkey', 'kutta']
list =  ['ganda', 'donkey', 'kutta']
with open('subtitle.txt', 'r') as file:
    content  = file.read()
    for word in list:
        if(word in content):
            content = content.replace(word, '#' * len(word))
with open('subtitle.txt', 'w') as file:
    file.write(content)