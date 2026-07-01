file = open("README.md","r")
content = file.read()
print(content,end ="\n\n")
file.close()
print('...................................')

file2 = open("READ.md","r")
for line in file2 :
  print(line.strip())
file2.close()
print('.........................................')
with open('README.md','r') as file :  #Here we are using "with" for reading a file and it will close file automatically
  content = file.read()
  print(content)
