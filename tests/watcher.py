import os
import time
import shutil
from core.dlp_scanner import DLPScanner
from core.crypto_vault import CryptoVault
from core.integrity import IntegrityMonitor

# Define e garante a existência da pasta de captura
WATCH_DIR = "logs"
CLEAN_DIR = os.path.join(WATCH_DIR, "arquivados_limpos")

os.makedirs(WATCH_DIR, exist_ok=True)
os.makedirs(CLEAN_DIR, exist_ok=True)

def start_continuous_monitoring():
    print("=" * 60)
    print("👁️ DLP ENGINE: MONITORAMENTO EM TEMPO REAL ATIVADO 👁️")
    print(f"[*] Escaneando a pasta '{WATCH_DIR}/' a cada 2 segundos...")
    print("[*] Pressione Ctrl + C para encerrar o sentinela.")
    print("=" * 60)
    
    scanner = DLPScanner()
    vault = CryptoVault()
    
    try:
        while True:
            # Lista apenas arquivos válidos na raiz da pasta logs/
            files = [f for f in os.listdir(WATCH_DIR) if os.path.isfile(os.path.join(WATCH_DIR, f))]
            
            for file_name in files:
                file_path = os.path.join(WATCH_DIR, file_name)
                print(f"\n📥 Novo arquivo detectado para auditoria: {file_name}")
                
                # Executa a varredura DLP
                results = scanner.scan_file(file_path)
                
                if results and "ERRO" not in results:
                    print(f"🚨 [ALERTA] Dados sensíveis encontrados em '{file_name}'!")
                    
                    # 1. Criptografa para a Sandbox externa
                    encrypted_path = vault.encrypt_file(file_path)
                    print(f"✅ Bloqueado e isolado em: {encrypted_path}")
                    
                    # 2. Gera e salva o DNA digital do arquivo protegido
                    sig_path = IntegrityMonitor.save_hash_signature(encrypted_path)
                    file_hash = IntegrityMonitor.calculate_sha256(encrypted_path)
                    print(f"🔒 Assinatura SHA-256 gerada com sucesso: {file_hash}")
                    
                    # 3. Elimina o vazamento original da pasta de entrada
                    os.remove(file_path)
                    print(f"💥 Arquivo vulnerável original '{file_name}' foi destruído!")
                    
                else:
                    # Se o arquivo estiver limpo, move para a pasta de histórico seguro para não reprocessar
                    dest_path = os.path.join(CLEAN_DIR, file_name)
                    shutil.move(file_path, dest_path)
                    print(f"🟢 [LIMPO] Nenhum risco achado. Movido para: {dest_path}")
            
            time.sleep(2) # Intervalo de varredura
            
    except KeyboardInterrupt:
        print("\n🛑 Sentinela finalizado pelo administrador. Infraestrutura segura.")

if __name__ == "__main__":
    start_continuous_monitoring()