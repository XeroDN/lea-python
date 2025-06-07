# c_num = 4
# while c_num <= 10:
#     print(c_num)
#     c_num += 1

prompt = ("let's talk ")
prompt += ("\nenter the message you want: ")
message = ""
while message != 'quit':
    message=input(prompt)
    if message != 'quit':
       print(message)