from password_manager import load_password_file, save_password_file, encrypt_password, user_exists

file_path = 'passwd.txt'
data = load_password_file(file_path)

new_username = input("Enter new username: ").strip()
real_name = input("Enter real name: ").strip()
password = input("Enter password: ")

if user_exists(new_username, data):
    print("Cannot add. Username already exists.")
else:
    encrypted_password = encrypt_password(password)
    new_entry = [new_username, real_name, encrypted_password]
    data.append(new_entry)
    save_password_file(file_path, data)
    print("User Created.")
