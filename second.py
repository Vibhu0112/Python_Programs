file1 = open('write.txt', 'w')
L = ["This is python class \n", "Today is practical of python \n", "set-2 is assigned to me for practical \n"]
s = "Hello vibhu \n"
  
# Writing a string to file
file1.write(s)
  
# Writing multiple strings
# at a time
file1.writelines(L)
  
# Closing file
file1.close()
  
# Checking if the data is
# written to file or not
file1 = open('write.txt', 'r')
print(file1.read())
file1.close()