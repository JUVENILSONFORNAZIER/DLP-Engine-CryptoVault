import os
import pytest
from core.crypto_vault import CryptoVault

def test_crypto_vault_flow(tmp_path):
    """Testa se o cofre consegue cifrar e decifrar mantendo o dado original intacto"""
    # Cria diretórios isolados temporários para o teste não sujar seu projeto real
    temp_vault_dir = tmp_path / "vault_storage"
    temp_key = temp_vault_dir / "vault.key"
    
    vault = CryptoVault(key_path=str(temp_key))
    
    # 1. Cria um arquivo falso sensível
    dummy_file = tmp_path / "vulneravel.txt"
    dummy_file.write_text("senha_secreta_123", encoding="utf-8")
    
    # 2. Criptografa
    enc_path = vault.encrypt_file(str(dummy_file), dest_dir=str(temp_vault_dir))
    assert os.path.exists(enc_path)
    
    # 3. Descriptografa em outro arquivo
    dec_file = tmp_path / "recuperado.txt"
    vault.decrypt_file(enc_path, str(dec_file))
    
    # 4. O conteúdo final deve ser idêntico ao inicial
    assert dec_file.read_text(encoding="utf-8") == "senha_secreta_123"