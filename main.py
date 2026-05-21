import os
from core.dlp_scanner import DLPScanner
from core.crypto_vault import CryptoVault
from core.integrity import IntegrityMonitor

def run_dlp_and_vault_pipeline():
    print("=" * 60)
    print("🛡️ CORP-DLP ENGINE & CRYPTOVAULT SYSTEM v1.2 🛡️")
    print("=" * 60)
    
    scanner = DLPScanner()
    vault = CryptoVault()
    
    target_file = "vulneravel.txt"
    
    # Se o arquivo original sumiu porque já foi mitigado, vamos recriar um para teste rápido
    if not os.path.exists(target_file):
        print(f"[*] Criando novo arquivo '{target_file}' para fins de demonstração...")
        with open(target_file, "w", encoding="utf-8") as f:
            f.write("LOG EXPOSTO: CPF: 999.888.777-11 e STRIPE_KEY=sk_live_abcdef1234567890\n")
            
    print(f"[*] Passo 1: Escaneando ameaças em: {target_file}...\n")
    results = scanner.scan_file(target_file)
    
    if results and "ERRO" not in results:
        print("🚨 [PERIGO] VAZAMENTO DE DADOS DETECTADO!")
        print("-" * 60)
        for data_type, findings in results.items():
            print(f"📌 {data_type}: Encontradas {len(findings)} ocorrência(s).")
        print("-" * 60)
        
        print("\n[*] Passo 2: Iniciando protocolo de mitigação...")
        try:
            # 1. Criptografa
            encrypted_path = vault.encrypt_file(target_file)
            print(f"✅ Arquivo trancado com sucesso em: {encrypted_path}")
            
            # 2. Registra o DNA Digital (Integridade)
            sig_path = IntegrityMonitor.save_hash_signature(encrypted_path)
            file_hash = IntegrityMonitor.calculate_sha256(encrypted_path)
            print(f"🔒 Assinatura Digital SHA-256 gerada: {file_hash}")
            print(f"📝 Hash de auditoria salvo em: {sig_path}")
            
            # 3. Elimina o risco original
            os.remove(target_file)
            print(f"💥 Arquivo original exposto '{target_file}' foi REMOVIDO com segurança!")
            print("\n🛡️ INFRAESTRUTURA DEFENDEU E REGISTROU A INTEGRIDADE DO COFRE! 🛡️")
            
        except Exception as e:
            print(f"❌ Erro crítico no protocolo de mitigação: {e}")
            
    else:
        print("✅ [LIMPO] Nenhum dado sensível detectado.")
        print("-" * 60)

if __name__ == "__main__":
    run_dlp_and_vault_pipeline()