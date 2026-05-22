# 🛡️ DLP-Engine-CryptoVault: Advanced Security & Encryption Suite

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.13-blue?logo=python" alt="Python"></a>
  <a href="https://www.docker.com/"><img src="https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker" alt="Docker"></a>
  <img src="https://img.shields.io/badge/Status-Stable-green" alt="Status">
</p>

## 📑 Visão Geral da Arquitetura
O **DLP-Engine-CryptoVault** não é um simples script; é um motor de processamento de segurança de alta performance desenhado para a **mitigação ativa de vazamento de dados (DLP)** e **criptografia persistente**. Diferente de soluções convencionais, ele atua ao nível de I/O (Input/Output) do sistema de ficheiros, assegurando que nenhum dado sensível entra em estado de repouso (at-rest) sem a devida blindagem criptográfica.

## 🏗️ Core Stack e Componentes Técnicos
O sistema é modular e focado em alta disponibilidade:
- **Engine Core:** Motor de análise de padrões (regex/pattern matching) para identificação de dados sensíveis (PII, PCI-DSS).
- **CryptoVault:** Módulo de criptografia simétrica de alta performance (AES-256).
- **Sentinel Watcher:** Serviço de monitorização de diretórios em tempo real (fs-events), garantindo inspeção instantânea.
- **Integrity Manager:** Módulo de auditoria para garantia de imutabilidade dos dados.
- **Environment Isolation:** Containerização total via Docker, assegurando paridade de ambiente entre desenvolvimento e produção.

## ⚙️ Workflow de Segurança (Security Pipeline)
O fluxo de dados é determinístico e auditável:
1. **Ingestão (Sentinel):** Monitorização contínua de I/O de ficheiros.
2. **Scan DLP:** Validação de conteúdo contra políticas de segurança de segurança rigorosas.
3. **Blindagem (Vaulting):** Execução de criptografia de ponta a ponta antes da persistência em disco.
4. **Log Audit:** Registo imutável de todas as transações, tentativas de acesso e operações.

## 🚀 Guia de Implementação (Deployment)

### Requisitos
- Docker Engine v20.10+
- WSL 2 (Windows Subsystem for Linux)

### Execução via Docker
```bash
# Clone o repositório
git clone [https://github.com/JUVENILSONFORNAZIER/DLP-Engine-CryptoVault.git](https://github.com/JUVENILSONFORNAZIER/DLP-Engine-CryptoVault.git)
cd DLP-Engine-CryptoVault

# Build da Imagem
docker build -t dlp-engine-crypto .

# Execução em modo isolado (Persistência de Logs e Vault)
docker run -d --name crypto-vault-engine \
  -v $(pwd)/logs:/app/logs \
  -v $(pwd)/vault_storage:/app/vault_storage \
  dlp-engine-cryptoss