file = open("John Snow" "w")#Here we used "w" for writing the sting to the file.
string = '''John Snow is a character from a fictional story named game of thornes.
He is the lead character in this show.'''
file.write(string)
file.close()

file = open("John Snow","a")#Here we use "a" insted of "w" this is for appending the sting to the above file.
string = '''This is the top triending show now in netflix.'''
file.write(string)
file.close()
