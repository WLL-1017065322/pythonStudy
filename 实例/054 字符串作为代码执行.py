# exec
def code_run():
    code = """
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5))
"""
    exec(code)


code_run()
