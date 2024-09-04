from dotenv import dotenv_values


config = {
    **dotenv_values('.env')
}


db_host = config.get('DB_HOST')
db_port = config.get('DB_PORT')
db_user = config.get('DB_USER')
db_password = config.get('DB_PASS')
db_name = config.get('DB_NAME')

db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'