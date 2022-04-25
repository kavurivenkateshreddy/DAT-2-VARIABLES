"""
Date: 19th April 2022 Tuesday
Name: kavuri venkatesh reddy
File Desc: variable rules,way to assign variables,isidentifier()
"""
'''alphabits > start : middle : end
   numerical >         middle : end
 under scrol > start : middle ; end
 we should not enter any space in between the variable 
 we can reuse the variables there is no limites for the naming of variables.'''
a=1;b=2
print(a) #1
print(b) #2
print(a);print(b) #1
                  #2
print(a,b) # 1 2
c,d,e=3,4,5
print(c) #
print(d) #4
print(e) #5
print(c,d,e) #3 4 5
print(c);print(d);print(e) #3
                           #4
                           #5
f=g=h=6;i=7;j=8
print(f) #6
print(g) #6
print(h) #6
print(f,g,h) #6 6 6
print(f,i,j) #6 7 8
# print(k) #Name Error: name 'k' is not defined
print('a'.isidentifier()) #True
print('_'.isidentifier()) #True
print('_a'.isidentifier()) #True
print('a_'.isidentifier()) #True
print('1'.isidentifier())  #False
print('s_1'.isidentifier()) #True
print('n.1'.isidentifier()) #False
print('a 1_'.isidentifier()) #False