import hashlib
import os

class IntegrityMonitor:
    @staticmethod
    def calculate_sha256(file_path: str) -> str:
        """
        Calcula a assinatura digital única (SHA-256) de um arquivo.
        Se o arquivo mudar 1 bit, o hash muda completamente.
        """
        if not os.path.exists(file_path):
            return ""
            
        sha256_hash = hashlib.sha256()
        
        # Lê o arquivo em blocos (chunks) para não estourar a memória se for um arquivo gigante
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
                
        return sha256_hash.hexdigest()

    @staticmethod
    def save_hash_signature(file_path: str, signature_dir="vault_storage/signatures"):
        """
        Gera o hash do arquivo e guarda em um arquivo de auditoria externa.
        """
        os.makedirs(signature_dir, exist_ok=True)
        file_hash = IntegrityMonitor.calculate_sha256(file_path)
        
        if not file_hash:
            return None
            
        base_name = os.path.basename(file_path)
        signature_path = os.path.join(signature_dir, f"{base_name}.sha256")
        
        with open(signature_path, "w", encoding="utf-8") as f:
            f.write(file_hash)
            
        return signature_path