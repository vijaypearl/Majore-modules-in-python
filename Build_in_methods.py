# 1)replace
a = "hello world"
a.replace(" ","_")
print(a)   #hello_world


# 2)split 

#Example 1 with respect to white space
a = "hello world"
a.split()  #by default with respect to white space splitting    
#ans would be ['hello', 'world']

#Example 2 with respect to comma:
b = "vijay,ramesh,prem"
b.split(",")
#ans would be ['vijay', 'ramesh', 'prem']


# 3)strip - To remove whitespace in string
#scenario 1
a = "  hello"
a.strip()   #ans - "hello"

#scenario2
a = "  hello"
a.strip(" h")  #ans - "ello"


#4)join
c = [a,b,c,d]
c.join()      #ans - "abcd"


#5)min
a = "abc"
min(a) #ans - a


#6)max
a = "abc"
min(a) #ans - c


#7)lower
a = "abA"
a.lower()      #ans - aba


#9)upper
a = "abA"
a.upper()      #ans -ABA 


#10)title
a = "welcome hello world"
a.title()    #ans - Welcome Hello World - first letter of every word change into upper case 







