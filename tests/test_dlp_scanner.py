import pytest
from core.dlp_scanner import DLPScanner

def test_dlp_scanner_detection():
    """Garante que o Caçador encontra os padrões sensíveis corrigidos"""
    scanner = DLPScanner()
    fake_log = "ALERTA: CPF: 123.456.789-00 e AWS_SECRET=super_secret_token_alpha_omega_99"
    
    results = scanner.scan_text(fake_log)
    
    assert "CPF" in results
    assert "Chave_API_Generica" in results
    assert results["CPF"][0] == "123.456.789-00"