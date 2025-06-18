name="Pranav"

a=len(name) #Finding Length of the string
print(a)
print(name.upper()) #convert string to upper case 
print(name.lower()) #convert string to lower case
print(name.capitalize()) #convert first char of string to upper case latter
print(name.title()) #convert first char of all string to upper case latter

s=" \nHello word "
print(s.strip()) #remove unwanted space to string
print(s.lstrip()) #remove left side space
print(s.rstrip()) #remove right side space

t="Hyy hii hello"
print(t.find("h")) #finding index
print(t.replace("hii","By")) #replce the string 

a="A,B,C,D"
print(a.split(",")) #slipt a string and convert it into a list 
print(",".join(['A', 'B', 'C', 'D'])) #convert list to string 

txt="Pyton1234567"
print(txt.isalpha()) #retrun true if string conetent only charecters
print(txt.isdigit()) #return true if string has only number
print(txt.isalnum()) #return trun if string has alphanumeric charecters
print(txt.isspace()) #return true if string has only space
