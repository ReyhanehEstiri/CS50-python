import unittest
from project import generate_key, load_key, encrypt_message, decrypt_message, generate_password, save_passwords, load_passwords

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        """Create a test environment."""
        self.key_file = "test_secret.key"
        self.passwords_file = "test_passwords.json"
        self.test_message = "test_password"
        self.test_password = "TestPassword123!"
        generate_key()  # Generate a key for testing

    def test_generate_password(self):
        """Test password generation."""
        password = generate_password(12)
        self.assertEqual(len(password), 12)
        self.assertIsNotNone(password)

    def test_encryption_decryption(self):
        """Test encryption and decryption of a message."""
        encrypted = encrypt_message(self.test_message)
        decrypted = decrypt_message(encrypted)
        self.assertEqual(self.test_message, decrypted)

    def test_save_load_passwords(self):
        """Test saving and loading of passwords."""
        encrypted_password = encrypt_message(self.test_password).decode()
        save_passwords({'test_service': encrypted_password})

        loaded_passwords = load_passwords()
        self.assertIn('test_service', loaded_passwords)
        decrypted_password = decrypt_message(loaded_passwords['test_service'].encode())
        self.assertEqual(self.test_password, decrypted_password)

    def tearDown(self):
        """Clean up after tests."""
        os.remove(self.key_file)
        if os.path.exists(self.passwords_file):
            os.remove(self.passwords_file)

if __name__ == "__main__":
    unittest.main()
