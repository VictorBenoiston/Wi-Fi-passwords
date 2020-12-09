import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('ISO-8859-1').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if 'Todos os Perfis de Usu\xa0rios' in line]


for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('ISO-8859-1').split('\n')
    passwords = [line.split(':')[1][1:-1] for line in results if 'Conte£do da Chave' in line]
    try:
        print(f'Name: {wifi}, Password: {passwords[0]}')
    except IndexError:
        print('Error')
# print(results)
