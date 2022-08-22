#Read the file line by line
# for line in open('nameslist.txt'):
#     print(line) 

#Read only the 5th line of the file
# f = open('nameslist.txt')
# secret_data = f.read(5)
# print(secret_data)
# f.close()

#Read only the 5th first characters of the file
# i =0
# for i in range (1, 6):
#     f = open('nameslist.txt')
#     secret_data = f.read(i)
# print(secret_data)
# f.close() 

#Read all the file and return it as a list of strings. Then split each word
# f = open('nameslist.txt')
# secret_data = f.readlines() 
# print(secret_data)
# f.close()

#Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the 
# count_d=0
# count_lea=0
# count_luke = 0

# f = open("nameslist.txt")
# while True:
#     line = f.readline()
#     line = line.strip()
#     if (line == "Darth"):
#        count_d = count_d + 1
#     elif (line == "Lea"):
#         count_lea += 1
#     elif (line =="Luke"):
#         count_luke +=1   
#     elif (not line):
#         break
# print(f"Number of Darth is: {count_d}\nNumber of Lea is: {count_lea}\nNumber of Luke is: {count_luke} ")


#Append your first name at the end of the file
# f=open("nameslist.txt","a")
# f.write("\nAvishek")
# f.close()

#Append "SkyWalker" next to each first name "Luke"
f = open("nameslist.txt","a+")
while True:
    line = f.readline()
    line = line.strip()
    if (line == "Luke"):
      f.write (line + " SkyWalker")
    if (not line):
       break
f.close()

