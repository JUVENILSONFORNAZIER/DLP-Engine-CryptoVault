import os
from core.crypto_vault import CryptoVault

def run_recovery_tool():
    print("=" * 60)
    print("🔓 CRYPTOVAULT RECOVERY UTILITY v1.0 🔓")
    print("=" * 60)
    
    # Instancia o cofre (ele vai ler automaticamente a chave existente 'vault.key')
    vault = CryptoVault()
    
    # Caminho do arquivo que está trancado no cofre
    encrypted_file = "vault_storage/vulneravel.txt.enc"
    # Onde queremos salvar o arquivo aberto
    output_file = "vulneravel_recuperado.txt"
    
    if not os.path.exists(encrypted_file):
        print(f"❌ Arquivo criptografado '{encrypted_file}' não foi encontrado no cofre.")
        return
        
    print(f"[*] Localizado arquivo protegido: {encrypted_file}")
    print("[*] Decodificando carga útil usando AES-256...")
    
    try:
        # Executa a decriptografia
        vault.decrypt_file(encrypted_file, output_file)
        print(f"✅ Sucesso! Arquivo extraído com segurança para: {output_file}")
        print("-" * 60)
        
        # Mostra o conteúdo direto no terminal para o Admin
        print("📝 CONTEÚDO DO ARQUIVO RECUPERADO:")
        with open(output_file, "r", encoding="utf-8") as f:
            print(f.read())
        print("-" * 60)
        
    except Exception as e:
        print(f"❌ Erro crítico na extração do cofre: {e}")

if __name__ == "__main__":
    run_recovery_tool()