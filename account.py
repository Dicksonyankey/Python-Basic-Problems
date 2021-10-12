balance = 0

def user_A(x):
    global balance
    balance = balance + x
    
def user_B(x):
    global balance
    balance = balance + x

user_A(500)
user_B(600)
print(balance)