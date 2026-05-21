import os
import pytest
from core.integrity import IntegrityMonitor

def test_integrity_avoids_tampering(tmp_path):
    """Garante que se o arquivo for modificado, o DNA digital (SHA-256) muda"""
    file_path = tmp_path / "secure.enc"
    
    file_path.write_text("texto_original_criptografado", encoding="utf-8")
    hash_original = IntegrityMonitor.calculate_sha256(str(file_path))
    
    # Simula uma adulteração: muda o final para X
    file_path.write_text("texto_original_criptografadX", encoding="utf-8")
    hash_modificado = IntegrityMonitor.calculate_sha256(str(file_path))
    
    # Os hashes PRECISAM ser diferentes após a alteração
    assert hash_original != hash_modificado