# Lists - Orderded , mutable , collection of values []
# Dictionaries - Unorderded , mutable, collection of key pair of values {"Key":"Value}
# Tuples - Orderded , immutable , collection of values ()
# Sets - Unorderded , mutable, collection of unique values {"value1" , "value2"}

#Lists stored in a variable
colours = ['Red', 'Blue', 'Pink']

print (colours)

#starts at 0 and from backwards starts at -1
print (colours[1])
print (colours[-2])

#Slicing - range [:]

print (colours[0:2])
print (colours[0:])
print (colours[-3:])

food =['bread', 'cheese' , 'apple', "jam"]
print (food)
#altering list
food[0] ='rice'
del food[1]
print(food)

#checking if item exits 

print ('cheese' in food ) 
print ('jam' in food )

#nested lists

numbers =[1,2,3,4,5]
letters = ['a','b','c','d','e']

combined = [numbers,letters]

print (combined[0][1],combined[1][1])

#multiple data types 
my_list=['a',2,['red','blue'],3.5]
my_list.append('test')
print (my_list)
#print (my_list[0][1])
print (my_list[0])
my_list.remove('test')
print (my_list)

#insert
my_list.insert(0,'mango')
print (my_list)

#extend a list 
my_list.extend('grapes')
print(my_list)

#join
my_list=['test','tester']

x=",".join(my_list)
print(x)