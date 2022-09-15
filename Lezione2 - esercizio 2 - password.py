# coding=utf-8
#controllo password
password = 'Password_sicura'
insert_password = raw_input('Per favore digita la password di accesso')
while not insert_password:
    insert_password = raw_input('Per favore digita la password di accesso')
else:
    if password == insert_password:
        print('Benvenuto!')
    else:
        print('Password non corretta')
