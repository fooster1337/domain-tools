import time, os, sys
import platform

# Bruh...???
# © fooster1337 2k22

lines_seen = set()
output=""
url=""

os = platform.system()

menu = """
[=] Domain Tools by @fooster1337 On Github [=]
[+] Keep calm and create a world [+] 

[>_] You OS : {}

[+] Menu [+]
1. Add http:// 
2. Add https://
3. Add https://www.
4. Remove https / http 
5. Remove Duplicate Domain
6. Remove Empty Line
0. Exit
00. Contact me darling!
""" .format(os)

def http():
	print('[+] Add http on file')
	http = input('[+] You file : ')
	outfile_http = input('[+] Saved on : ')
	http = open(http, 'r').read().splitlines()
	for finish in http:
		with open(outfile_http, 'a+') as f:
			f.write('http://' + finish + '\n')
	print('[+] Add http Succes, file saved on', outfile_http)
	time.sleep(1)
	main()

def https():
	print('[+] Add https on file')
	https = input('[+] You file : ')
	outfile_https = input('[+] Saved on : ')
	https = open(https, 'r').read().splitlines()
	for finish in https:
		with open(outfile_https, 'a+') as f:
			f.write('https://' + finish + '\n')
	print('[+] Add https Succes, file saved on', outfile_https)
	time.sleep(1)
	main()

def httpswww():
	print('[+] Add https://www. on file')
	httpswww = input('[+] You file : ')
	outfile_httpswww = input('[+] Saved on : ')
	httpswww = open(httpswww, 'r').read().splitlines()
	for finish in httpswww:
		with open(outfile_httpswww, 'a+') as f:
			f.write('https://www.' + finish + '\n')
	print('[+] Add https://www. Succes, file saved on', outfile_httpswww)
	time.sleep(1)
	main()

def remove():
	print('[+] Remove http / https ')
	remove = input('[+] You File : ')
	outfile_remove = input('[+] Saved on : ')
	remove = open(remove,'r').read().splitlines()
	for finish in remove:
		remove = finish.replace("http://", "").replace("https://", "")
		with open(outfile_remove, 'a+') as f:
			f.write(remove + '\n')
	print('[+] Remove http / https Succes, file saved on', outfile_remove)
	time.sleep(1)
	main()

def remove_duplicate():	
	print('[+] Remove Duplicate Domain')
	duplicate = input('[+] You file : ')
	output_duplicate = input('[+] Saved on : ')
	outfile = open(output_duplicate, "w")
	for line in open(duplicate, "r"):
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	print('[+] Duplicate domain Remove Succes, file saved on', output_duplicate)
	time.sleep(2)
	main()

def remove_empty():
	print('[+] Remove Empty Line')
	empty = input('[+] You File : ')
	output_empty = input('[+] Saved on : ')
	with open(empty, "r") as f, open(output_empty,"w") as outfile:
		for i in f.readlines():
			if not i.strip():
				continue
			if i:
				outfile.write(i)
	print('[+] Empty Line Remove Succes, file saved on', output_empty)
	time.sleep(1)
	main()

def main():
	print(menu)
	tools = input('[?] You choice : ')
	if tools == "1":
		http()
	elif tools == "2":
		https()
	elif tools == "3":
		httpswww()
	elif tools == "4":
		remove()
	elif tools == "5":
		remove_duplicate()
	elif tools == "6":
		remove_empty()
	elif tools == "0":
		exit()
	elif tools == "00":
		print()
		print('[@] Contact author')
		print('[+] Telegran : @rey1337')
		print('[+] Discord  : TheFooster#3665')
		time.sleep(4)
		main()
	else:
		print('[!] Pilih yang bener ngab')
		time.sleep(1)
		main()	


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('')
		print('[-] Exiting...')
		exit()
	except FileNotFoundError:
		print('[-] File not found, try again')
		time.sleep(1)
		main()
