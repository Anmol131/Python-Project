from password_manager import load_password_file, encrypt_password, user_exists

file_path = 'passwd.txt'
data = load_password_file(file_path)

username = input("User: ").strip()

if not user_exists(username, data):
    print("User not found.")
else:
    password = input("Password: ")
    index = [i for i, user in enumerate(data) if user[0] == username][0]
    if data[index][2] == encrypt_password(password):
        print("Access granted.")
    else:
        print("Access denied.")
