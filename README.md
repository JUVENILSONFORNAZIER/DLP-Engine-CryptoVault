# 🛡️ DLP-Engine-CryptoVault

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/Status-Stable-green" alt="Status">
</p>

## 📋 Visão Geral
O **DLP-Engine-CryptoVault** é um sistema de alta complexidade focado em **Data Loss Prevention (DLP)** e **criptografia persistente**. Diferente de soluções comuns, ele monitora o sistema de arquivos em tempo real e blinda dados sensíveis antes de qualquer repouso no disco.

## 🏗️ Estrutura Técnica
* **Core:** Motor de análise de padrões para identificação de dados sensíveis (PII, PCI-DSS).
* **CryptoVault:** Módulo de criptografia simétrica AES-256.
* **Sentinel:** Serviço de monitoramento de diretórios (fs-events).
* **Docker:** Containerização total para paridade de ambiente.

## 🚀 Guia de Implementação
```bash
# Clone o projeto
git clone [https://github.com/JUVENILSONFORNAZIER/DLP-Engine-CryptoVault.git](https://github.com/JUVENILSONFORNAZIER/DLP-Engine-CryptoVault.git)
cd DLP-Engine-CryptoVault

# Build da imagem
docker build -t dlp-engine-crypto .

# Execução com persistência de logs
docker run -d --name crypto-vault-engine \
  -v $(pwd)/logs:/app/logs \
  -v $(pwd)/vault_storage:/app/vault_storage \
  dlp-engine-crypto