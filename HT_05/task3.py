"""
На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
"""
from task2 import validation, ValidationError

users = [
    ['username1', 'password1'],
    ['nagibator2008', 'xXtraktorXx'],
    ['Killer_Jack', '13092006Sobaka'],
    ['i', '1q2w3e4R5t']
]

for user in users:
    try:
        validation(user[0], user[1])
    except ValidationError as er:
        status = er.message
    else:
        status = "OK"
    finally:
        print(f"Username: {user[0]}\nPassword: {user[1]}\nStatus: {status}\n")