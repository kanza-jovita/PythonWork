def tests(test1, test2):
    #.This is a conditional statement checking if test1 is equal to test2
    if test1 == test2:
        # If test1 is equal to test2, it returns the value of test1.
        return test1
    else:
        #If test1 is not equal to test2, it returns the value of test2.
        return test2
#This prompts the user to enter the marks for the second test and stores it in the variable test2.

test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))


'''
 The code below defines a function called courseWrk that calculates and prints the final coursework marks based on input coursework marks and marks for two tests. It prompts the user to input their coursework marks, calculates the final marks, and prints them.

'''
def courseWrk(cswork,):
    #  This  calls a function named tests with arguments 
    testsMark = tests(test1,test2)
    #This line calculates the average of cswork and testsMark and assigns it to avgtestsCswork
    avgtestsCswork = (cswork + testsMark)/2
    #This line calculates the final Cswork marks by taking 40% of the average test and Cswork marks and assigns it to fnltestsCswork.
    fnltestsCswork = avgtestsCswork * (40/100)
    #This line prints a  line that separetes the output.
    print('..............................')
    #This line prints the final coursework marks calculated in the previous step.
    print('your final coursework marks is: ', fnltestsCswork)
    print('..............................')
# This prompts the user to input their coursework marks and converts the input to an integer before assigning it to the variable cswork.
cswork = int(input('Please enter your course work Marks: '))
 
#This calls the csWrk function with cswork as the argument, initiating the calculation and printing of the final coursework marks.
courseWrk(cswork)