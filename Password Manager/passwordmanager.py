import hashlib
import random
import string
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.passwords = {}
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
    
    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def evaluate_strength(self, password):
        if len(password) < 8:
            return "Weak"
        elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
            return "Strong"
        else:
            return "Moderate"
    
    def encrypt_password(self, password):
        encrypted_password = self.fernet.encrypt(password.encode())
        return encrypted_password
    
    def decrypt_password(self, encrypted_password):
        decrypted_password = self.fernet.decrypt(encrypted_password).decode()
        return decrypted_password
    
    def add_password(self, website, username, password):
        encrypted_password = self.encrypt_password(password)
        self.passwords[website] = {'username': username, 'password': encrypted_password}
    
    def get_password(self, website):
        if website in self.passwords:
            username = self.passwords[website]['username']
            encrypted_password = self.passwords[website]['password']
            decrypted_password = self.decrypt_password(encrypted_password)
            return f"Website: {website}\nUsername: {username}\nPassword: {decrypted_password}"
        else:
            return "Website not found in password manager."
    
    def list_websites(self):
        return list(self.passwords.keys())

# Example usage
if __name__ == "__main__":
    manager = PasswordManager()
    website = "example.com"
    username = "user123"
    password = manager.generate_password()
    
    manager.add_password(website, username, password)
    
    print("Password added successfully!")
    print(manager.get_password(website))
    print("Website List:", manager.list_websites())

