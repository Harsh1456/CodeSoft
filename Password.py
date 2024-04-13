import random
import array

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

len = int(input("Enter the length of password: "))

combined_list = lower + upper + symbol + number

rand_digit = random.choice(number) 
rand_upper = random.choice(upper) 
rand_lower = random.choice(lower) 
rand_symbol = random.choice(symbol) 

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(len - 4): 
    temp_pass = temp_pass + random.choice(combined_list) 
   
    temp_pass_list = array.array('u', temp_pass) 
    random.shuffle(temp_pass_list) 

password = "" 
for x in temp_pass_list: 
        password = password + x 

print("Your password is ",password) 