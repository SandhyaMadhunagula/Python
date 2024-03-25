#lex_auth_012693711503400960120
#Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

#It should display the product of the three values except when one of the integer value is 7.
#In that case, 7 should not be included in the product and the values to its left also should not be included.
#If there is only one value to be considered, display that value itself.
#If no values can be included in the product, display -1.


  

def find_product(num1,num2,num3):
    product=0
    if(num3==7):
        product=-1
    elif( num2==7 ):
            product=num3
    elif(num1==7 ):
        product=num2*num3   
   else:
       product=num1*num2*num3
         #write your logic here
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(7,6,2)
print(product)
