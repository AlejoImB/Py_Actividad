import os
from dotenv import load_dotenv


entorno = input("Selecciona el entorno (dev/pro): ")

if entorno == "dev":
    load_dotenv('.env.dev')
elif entorno == "pro":
    load_dotenv('.env.pro')
else:
    print("Entorno no válido. Cargando entorno 'dev' por defecto.")
    load_dotenv('.env.dev')


user_name = os.getenv('USER_NAME')
api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')
database_url = os.getenv('DATABASE_URL')

print(f"USER_NAME: {user_name}")
print(f"API_KEY: {api_key}")
print(f"EMAIL: {email}")
print(f"DATABASE_URL: {database_url}")
