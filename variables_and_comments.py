# what is comment 
#..comments are used to understand the code
#there are two types of comment
#1) single line comment
#2) multiline comment : directly is not there in python so we used docstrings
 # let see the single line comment..this is single line comment#
'''this is multiline comment 
   this is multiline comment 
    it is used for for long statements '''

# now understand variables with the example
x=2 # x is variable : so what is variable ..the answer is .. variable is a container to stored the data

# now we can understand the meaning the dynamic and static programming language
# int x = 2 , int x=3, int x=4 , is static type programming language like java , c , c++
# now talk about the dynamic programming language 
        # age = 22  in the dynamic programming we should not the write like int x or etc ..in the world of python

# now understand the refrence count
x=22
print(x)# so the refrence count will be 1
y=22
print(y)# so the refrence count will be 2 
z=22
print(z)# so the refrence count will be 3

#..................python main rules..............................
#1) the characters is use a/A to Z/z ,  and the special characters are allowed is the only underscore __
#2) start of the variabls will be start with the alphabet not with the number but can add the number on the last
#3) Case sensitve in python lets see example
name="rajat"
Name="swastik"
print(name)
print(Name)
#4) the fourth rule will be : Avoid using keywords
#5) variable name should be logical let see example 
x=2 # not logical
age =20 # logical

# now lets see the input output method
# basically in the world of python the handy menthod is used the print function
print("hello python learners !")

# lets see the supported formatted string in the python
your="swastik shukla"
age=20
print(f"my name is {your} and my age is {age}") # this is called the formatted string and thr output

# let see one more interesting thing in the output function
a=2
b=3
c=4
print(x,y,z,sep="@") # any special character for sep like _, #,%, etc

#2)now lets see the input function
name=input("what is your name ") # input method is a formated of the string we see further about the string
print(name)