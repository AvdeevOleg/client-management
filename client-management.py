import psycopg2
from psycopg2 import sql


# Функция для создания структуры базы данных
def create_db():
    with psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass") as conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE IF NOT EXISTS clients (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    email VARCHAR(100)
                );
            ''')
            cur.execute('''
                CREATE TABLE IF NOT EXISTS phones (
                    id SERIAL PRIMARY KEY,
                    client_id INTEGER REFERENCES clients(id) ON DELETE CASCADE,
                    phone VARCHAR(20)
                );
            ''')


# Функция для добавления нового клиента
def add_client(first_name, last_name, email):
    with psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass") as conn:
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO clients (first_name, last_name, email)
                VALUES (%s, %s, %s) RETURNING id;
            ''', (first_name, last_name, email))
            client_id = cur.fetchone()[0]
            return client_id


# Функция для добавления телефона существующему клиенту
def add_phone(client_id, phone):
    with psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass") as conn:
        with conn.cursor() as cur:
            cur.execute('''
                INSERT INTO phones (client_id, phone)
                VALUES (%s, %s);
            ''', (client_id, phone))


# Функция для изменения данных о клиенте
def update_client(client_id, first_name=None, last_name=None, email=None):
    with psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass") as conn:
        with conn.cursor() as cur:
            if first_name:
                cur.execute('''
                    UPDATE clients SET first_name = %s WHERE id = %s;
                ''', (first_name, client_id))
            if last_name:
                cur.execute('''
                    UPDATE clients SET last_name = %s WHERE id = %s;
                ''', (last_name, client_id))
            if email:
                cur.execute('''
                    UPDATE clients SET email = %s WHERE id = %s;
                ''', (email, client_id))


# Функция для удаления телефона клиента
def delete_phone(client_id, phone):
    with psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass") as conn:
        with conn.cursor() as cur:
            cur.execute('''
                DELETE FROM phones WHERE client_id = %s AND phone = %s;
            ''', (client_id, phone))


# Функция для удаления клиента
def delete_client(client_id):
    with psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass") as conn:
        with conn.cursor() as cur:
            cur.execute('''
                DELETE FROM clients WHERE id = %s;
            ''', (client_id,))


# Функция для поиска клиента по его данным
def find_client(first_name=None, last_name=None, email=None, phone=None):
    with psycopg2.connect(database="yourdbname", user="yourdbuser", password="yourdbpass") as conn:
        with conn.cursor() as cur:
            query = '''
                SELECT c.id, c.first_name, c.last_name, c.email, p.phone FROM clients c
                LEFT JOIN phones p ON c.id = p.client_id WHERE 1=1
            '''
            params = []
            if first_name:
                query += " AND c.first_name = %s"
                params.append(first_name)
            if last_name:
                query += " AND c.last_name = %s"
                params.append(last_name)
            if email:
                query += " AND c.email = %s"
                params.append(email)
            if phone:
                query += " AND p.phone = %s"
                params.append(phone)

            cur.execute(query, tuple(params))
            results = cur.fetchall()
            return results


if __name__ == "__main__":
    # Создание структуры базы данных
    create_db()

    # Добавление нового клиента
    client_id = add_client('John', 'Doe', 'john.doe@example.com')
    print(f"Added client with id {client_id}")

    # Добавление телефонов для клиента
    add_phone(client_id, '123456789')
    add_phone(client_id, '987654321')

    # Обновление данных клиента
    update_client(client_id, first_name='Jonathan')

    # Поиск клиента
    clients = find_client(first_name='Jonathan')
    for client in clients:
        print(client)

    # Удаление телефона
    delete_phone(client_id, '123456789')

    # Удаление клиента
    delete_client(client_id)
