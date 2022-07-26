import requests

response = requests.get('https://www.google.com/')

print("Status Code: ",response.status_code)

print("Cabeçalho:")
print(response.headers)

print('Conteudo:')
print(response.content)