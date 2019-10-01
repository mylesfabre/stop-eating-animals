# Myles Fabre
# CS5 Black hw2pr2
# Due: 09/24/2019

def compose(function):
    '''composes a functions in order, and thus executes the last function first and in backwards or'''
    if function == []:
        print("List is empty, no function to return ")
        return 0
    elif len(function) == 1:
        return function[0]
    else:
        return lambda x: function[0](compose(function[1:])(x))

def makePoly(coefficients):
    '''creates a polynomial function of power len(coefficients) - 1 using a list of coefficients'''
    if coefficients == []:
        print("No coefficients entered")
        return 0
    else:
        #power = len(coefficients) - 1 
        #return lambda   (coefficients[0]**power, coefficients[0:])
        rest = makePoly(coefficients[1:])
        return lambda x : (coefficients[0]*x) + rest