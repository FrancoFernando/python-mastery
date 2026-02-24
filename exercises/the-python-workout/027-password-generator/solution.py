"""Exercise 27: Password Generator"""
import random

def create_password_generator(valid_chars):

    def password_generator(length):
        psw = [valid_chars[random.randint(0,len(valid_chars)-1)] for _ in range(length)]
        return "".join(psw)
    
    return password_generator

alpha_password = create_password_generator('abcdef')
print(alpha_password(5)) 