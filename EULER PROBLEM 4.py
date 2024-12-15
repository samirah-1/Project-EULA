#SAMIRAH ALAM, Project EULER, Problem 4 in Python
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99 .Find the largest palindrome made from the product of two 3-digit numbers.
# -------------------------------------------------------------------
#Import Libraries
# -------------------------------------------------------------------
# -------------------------------------------------------------------
#Global Variables
# -------------------------------------------------------------------
largestPalindrome = 0
multiplier1=100
multiplier2=100
productList =[]

# -------------------------------------------------------------------
#Subprograms
# -------------------------------------------------------------------
def buildProduct(pmultiplier1,pmultiplier2):          #This FUnction creates the product of multiplier 1 and 2
    product = pmultiplier1 * pmultiplier2
    return product
    
def isPalindrome(pproductList):  #This function checks if the number is a palindrome
    index = 0          #this will count how many postions we will check of pproductList
    largestPalindrome=0   #This will store the most recent palindrome
    listLength = len(pproductList)
    while index != listLength:  #This loop will check each value of the list and not leave the range
        analyseItem = str(pproductList[index]) #This converts the item we are analysing into a string
        if analyseItem == (analyseItem[::-1]): #So we can check if it is a palindrome, reading forward will equal to reading backward
            largestPalindrome = int(analyseItem)  #this stores the most recent largest palindrome in the variable
            index = index + 1  #move to next item in list
        else:
            index = index + 1  #Move to next item in list
    return (largestPalindrome)  #Will return largest in range of list, to main program
    
        
    
    
# -------------------------------------------------------------------
#Main Program
# -------------------------------------------------------------------
while multiplier1 != 1000:          #This will loop till multiplier 1 is no longer 3 digits
    while multiplier2 != 1000:     #This will loop till multiplier 2 is no longer 3 digits
        addToList =buildProduct(multiplier1,multiplier2)   #Here, we are calling the product maker function
        productList.append(addToList) #We add the product to a list
        multiplier2 = multiplier2+1   #Multiplier 2 increases by one to create a new product
    multiplier1= multiplier1+1  #This increases by one so we can go again
    multiplier2=100 #So the multiplier2 while loop loops again

largestPalindrome = isPalindrome(productList)  #This is calling the function we defined and storing the largest palindrome
print("The largest palindrome which is the product of 2 three digit numbers is "largestPalindrome)

