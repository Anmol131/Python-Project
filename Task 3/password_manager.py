import codecs
file_path = 'passwd.txt'

def load_password_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip().split(':') for line in lines]

def save_password_file(file_path, data):
    with open(file_path, 'w') as file:
        for entry in data:
            file.write(':'.join(entry) + '\n')

def encrypt_password(password):
    return codecs.encode(password, 'rot_13')

def user_exists(username, data):
    return any(user[0] == username for user in data)

def get_user_index(username, data):
    for i, user in enumerate(data):
        if user[0] == username:
            return i
    return -1
