print("Hello")

school work

#EXERCISE 2

x_ = int(input('Enter number A: '))
y_ = int(input('Enter number B: '))
 
if x_ < y_ :
    print(f"{x_} is smaller than {y_}")
elif x_ == y_ :
    print(f'{x_} is equal to {y_}')

else:
    print(f'{y_} is smaller than {x_}')

#EXERCISE 3
x_ = int(input('Enter number A: '))
y_ = int(input('Enter number B: '))
z_ = int(input('Enter number C: '))

#function to get the greatest number from input
 def greatest_number(a,b,c):
    maximum_ = max(a,b,c)
    return maximum_
if x_ == y_ == z_:
    print('The numbers you entered are EQUAL')
else:
    func_ = greatest_number(x_,y_,z_)
    print(func_, "is the greatest")
    
 #EXERCISE 4

 x_ = int(input('Enter number A: '))
y_ = int(input('Enter number B: '))
z_ = int(input('Enter number C: '))
 
list_ = [x_,y_,z_]
unique_list = []
#create list of unique elements
for i in list_:
    if i not in unique_list:
        unique_list.append(i)
print(f'There are {len(unique_list)} unique numbers in {(x_,y_,z_)} = {unique_list}' )
