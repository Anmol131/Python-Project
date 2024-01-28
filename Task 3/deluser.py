from password_manager import load_password_file, save_password_file, user_exists, get_user_index, encrypt_password

file_path = 'passwd.txt'
data = load_password_file(file_path)

username_to_delete = input("Enter username: ").strip()

if not user_exists(username_to_delete, data):
    print("User not found.")
else:
    password_to_confirm = input("Enter your password to confirm deletion: ")

    index_to_delete = get_user_index(username_to_delete, data)

    if data[index_to_delete][2] == encrypt_password(password_to_confirm):
        del data[index_to_delete]
        save_password_file(file_path, data)
        print("User Deleted.")
    else:
        print("Invalid password.")
