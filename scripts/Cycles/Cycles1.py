# ---------------------------Пароль--------------------------
def password_checking(password):
    true_password = "0000"
    while password != true_password:
        password = input("please input your password: ")
    print("Password is: true")

password_checking(input("please input your password: "))