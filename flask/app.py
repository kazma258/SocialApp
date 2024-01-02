from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import sqlutils
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash

app = Flask(__name__)
CORS(app)  # 解决跨域问题

# 连接到 MySQL 数据库
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="social"
        )
        print("Connection to MySQL database successful")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# 关闭数据库连接
def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

# 定义 REST API 路由
@app.route('/api/get_alltable_info', methods=['GET'])
def get_data():
    try:
        tableinfo = sqlutils.get_alltable_info()
        return jsonify(tableinfo)
    except Exception as e:
        print(f'Error: {e}')

    return jsonify(data=None)

@app.route('/api/register', methods=['POST'])
def register():
    try:
        get_username = request.json.get('username')
        get_account = request.json.get('account')
        get_password = request.json.get('password')
        get_email = request.json.get('email')
        print(f'received: {get_username}, {get_account}, {get_password}, {get_email}')
        success = sqlutils.register(get_username, get_account, get_password, get_email)
        return jsonify({'success': success})
    except Exception as e:
        return jsonify({'error': str(e)})

def register(account, password, email, username):
    try:
        return(sqlutils.register(username, account, password, email))
    except Exception as e:
        print(f'Error: {e}')
        return False
    
@app.route('/api/login', methods=['POST'])
def login():
    try:
        get_account = request.json.get('account')
        get_password = request.json.get('password')
        print(f'received: {get_account}, {get_password}')
        success = sqlutils.login(get_account, get_password)
        if success:
            return jsonify({'success': success})
        return jsonify({'success': success})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/groups', methods=['POST'])
def group():
    current_user = request.json.get('uid')
    if request.method == 'POST':
        try:
            groupinfo = sqlutils.get_group(current_user)
            return jsonify(groupinfo)
        except Exception as e:
            print(f'Error: {e}')

        return jsonify(data=None)

@app.route('/api/creategroup', methods=['POST'])
def creategroup():
    try:
        get_groupname = request.json.get('groupname')
        get_uid = request.json.get('uid')
        print(f'received: {get_groupname}, {get_uid}')
        success = sqlutils.create_group(get_uid, get_groupname)
        return jsonify({'success': success})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
