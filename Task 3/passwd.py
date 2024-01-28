from password_manager import load_password_file, save_password_file, encrypt_password, user_exists, get_user_index

file_path = 'passwd.txt'
data = load_password_file(file_path)

username = input("User: ").strip()

if not user_exists(username, data):
    print("User not found.")
else:
    current_password = input("Current Password: ")
    index = get_user_index(username, data)
    if data[index][2] == encrypt_password(current_password):
        new_password = input("New Password: ")
        confirm_password = input("Confirm: ")
        if new_password == confirm_password:
            data[index][2] = encrypt_password(new_password)
            save_password_file(file_path, data)
            print("Password changed.")
        else:
            print("Passwords do not match.")
    else:
        print("Invalid current password.")
