'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def evaluate_expression(expression):
    result = 0
    current_number = None
    current_operator = '+'
    for char in expression:
        if char.isdigit():
            if current_number is None:
                current_number = int(char)
            else:
                current_number = current_number * 10 + int(char)
        elif char in ('+', '-','/','*'):
            if current_operator == '+':
                result += current_number
            elif current_operator == '-':
                result -= current_number
            elif current_operator =='*':
                result *=current_number
            elif current_operator =='/':
                result /=current_number
            current_operator = char
            current_number = None 

            
    if current_operator == '+':
        result += current_number
    elif current_operator == '-':
        result -= current_number
    elif current_operator =='*':
        result *=current_number
    elif current_operator =='/':
        result /=current_number
    return result


expression = input("enter expression :")
result = evaluate_expression(expression)
print(result)
