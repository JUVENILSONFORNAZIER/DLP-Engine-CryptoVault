import os
from cryptography.fernet import Fernet

class CryptoVault:
    def __init__(self, key_path="vault_storage/vault.key"):
        self.key_path = key_path
        # Carrega a chave existente ou gera uma nova se for a primeira execução
        self.key = self._load_or_generate_key()

    def _load_or_generate_key(self):
        # Garante que a pasta de armazenamento exista
        os.makedirs(os.path.dirname(self.key_path), exist_ok=True)
        
        if os.path.exists(self.key_path):
            with open(self.key_path, "rb") as key_file:
                return key_file.read()
        else:
            # Gera uma chave forte baseada em AES-256
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt_file(self, source_path, dest_dir="vault_storage"):
        """
        Lê o arquivo vulnerável, criptografa o conteúdo e salva o monstro trancado no cofre.
        """
        try:
            os.makedirs(dest_dir, exist_ok=True)
            
            with open(source_path, "rb") as f:
                raw_data = f.read()
            
            fernet = Fernet(self.key)
            encrypted_data = fernet.encrypt(raw_data)
            
            # Define o nome do arquivo criptografado (.enc) dentro do cofre
            file_name = os.path.basename(source_path)
            dest_path = os.path.join(dest_dir, f"{file_name}.enc")
            
            with open(dest_path, "wb") as f:
                f.write(encrypted_data)
                
            return dest_path
        except Exception as e:
            raise Exception(f"Falha na criptografia do cofre: {str(e)}")

    def decrypt_file(self, encrypted_path, output_path):
        """
        Caminho inverso: abre o arquivo criptografado do cofre e recupera o original.
        """
        try:
            with open(encrypted_path, "rb") as f:
                encrypted_data = f.read()
            
            fernet = Fernet(self.key)
            decrypted_data = fernet.decrypt(encrypted_data)
            
            with open(output_path, "wb") as f:
                f.write(decrypted_data)
                
            return output_path
        except Exception as e:
            raise Exception(f"Falha na decriptografia do cofre: {str(e)}")