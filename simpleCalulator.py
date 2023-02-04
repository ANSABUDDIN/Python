FirstValue = int(input("Enter First Value : -  "))
SecondValue = int(input("Enter Second Value10: -  "))
Operator = input("Enter Operator : -  ")


if Operator == "+":
    print(FirstValue + SecondValue)
elif Operator == "-":
    print(FirstValue - SecondValue)
elif Operator == "*":
    print(FirstValue * SecondValue)
elif Operator == "/":
    print(FirstValue / SecondValue)    
else:
    print(""" 
    Only Use This Operators + , - , * , / 
    """)