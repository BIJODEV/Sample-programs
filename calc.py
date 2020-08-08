#-------Calc using Closures---------
def calc(a,b):
    a = int(input("enter a number : "))
    b = int(input("enter another number : "))
    def add():
        result = a+b
        print('Addition of {0} + {1} = {2}'.format(a,b,result))

        def sub():
            result = a-b
            print('Subtraction of {0} - {1} = {2}'.format(a,b,result))

            def mul():
                result = a*b
                print('Multiplication of {0} * {1} = {2}'.format(a,b,result))
            return mul()

        return sub()

    return add()

print(calc('a','b'))
