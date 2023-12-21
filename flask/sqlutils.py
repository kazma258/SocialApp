import mysql.connector
import time, hashlib


# 連接到 MySQL 資料庫
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="social"
        )
        print("Connection to MySQL database successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 關閉資料庫連接
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

# 查詢所有資料表及其對應的 keyname
def get_alltable_info() -> dict:
    # 創建連接
    connection = create_connection()

    if connection:
        try:
            # 獲取 cursor
            cursor = connection.cursor(dictionary=True)

            # SQL 查詢，獲取所有資料表及其對應的 keyname
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            table_info = {}
            for table in tables:
                print(table)
                table_name = table['Tables_in_social']  # 替換為實際的資料庫名稱
                try:
                    cursor.execute(f"DESCRIBE {table_name}")
                except Exception as e:
                    print(e)
                    continue
                columns = cursor.fetchall()
                column_names = [column['Field'] for column in columns]

                print(column_names)

                table_info[table_name] = column_names

            return table_info

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # 關閉連接
            close_connection(connection)

    return None

# 根據時間由雜湊函數生成唯一的 id
def generate_id(length):
    # 獲取當前時間的字串表示
    current_time = str(time.time())
    # 將當前時間進行雜湊
    hashed_time = hashlib.sha256(current_time.encode()).hexdigest()
    # 截取指定長度的雜湊值
    result_hash = hashed_time[:length]
    result_hash = int(result_hash, 16)

    return result_hash

# create a new user
def create_user(account, password, email, username, connection: mysql.connector.connection.MySQLConnection):
    try:
        # 獲取 cursor
        cursor = connection.cursor()

        # SQL 查詢，檢查是否已經註冊過
        cursor.execute(f"SELECT * FROM logininfo WHERE account = '{account}'")
        result = cursor.fetchone()

        if result:
            print(f"Account {username} has been registered")
            return False
        elif result is None:
            # SQL 查詢，插入註冊資訊
            rndid = generate_id(20)
            cursor.execute(f"INSERT INTO logininfo \
                (userId, account, password, email) VALUES \
                ('{rndid}', '{account}', '{password}', '{email}')")
            connection.commit()
            print(f"Account {account} registered successfully")

            # 以rndid為主鍵，在userinfo中新增一筆資料
            cursor.execute(f"INSERT INTO userinfo \
                (userId, signUpDate, nickname) VALUES \
                ('{rndid}', '{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}', '{username}')") 
            print(f"Account {account} info created successfully")
            print(f'Info:\nAccount: {account} \nPassword: {password} \nEmail: {email} \nrndid: {rndid}')
            connection.commit()
            return True
    except Exception as e:
        print(e)
        return False


# 註冊功能，傳入參數為 account password email
def register(username, account, password, email) -> bool:
    # 創建連接
    connection = create_connection()

    if connection:
        try:
            return create_user(account, password, email, username, connection)
        except Exception as e:
            print(e)
            return False

if __name__ == '__main__':
    # table_info = get_alltable_info()
    # print(table_info)
    register('test', 'test', 'test', 'email@test.com')
    # print(generate_id(16))