# coding=utf-8
#controllo password
password = 'Password_sicura'
insert_password = raw_input('Per favore digita la password di accesso')

if password == insert_password:
    print('Benvenuto!')
else:
    print('Password non corretta')
