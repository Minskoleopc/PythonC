# text file
# binary files

# program1
# example -- open a file and close of file
# opening the file and writing the data
# f = open('my.file.txt','w')
# # enter the characters from the command line
# str = input('Enter the text :')
# # write the string into the file
# f.write(str)
# # closing the file
# f.close()


# program 2
# # open the file for reading the data
# f = open('my.file.txt','r')
# # reading all the characters from file
# str = f.read()
# # display them on the screen
# print(str)
# # closing the file
# f.close()


# program 3
# program to write into a file
#
# f = open('my.file2.txt','w')
# print('Entet the text (@ at end)')
# # enter the string from the keyword
# while str != '@':
#     str = input()
#     if str != '@':
#         f.write(str)
# f.close()

# program 4
#
# # opening the file
# f = open('myfile2.txt','a+')
# # if not '@' keep adding into the file
# print('Enter text to append (@ at the end:)')
# while str != '@':
#     str =input()
#     if(str != 'a'):
#         f.write((str))
#
# # put the file pointer to the beginning of file
# f.seek(0,0)
# # read the file
# str = f.read()
# print(str)
# # closing the file
# f.close()

# program 5
# import os , sys
# fname = input('Enter the filename: ')
# if os.path.isfile(fname):
#    f =  open(fname,'r')
# else:
#     print('File does not exist')
#     sys.exit()
# str = f.read()
# print(str)
# f.close()

















