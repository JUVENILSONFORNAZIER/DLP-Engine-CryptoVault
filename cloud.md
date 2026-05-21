# Specification: DLP Engine & CryptoVault

## 1. Visão Geral do Sistema
Este sistema é uma engine corporativa de Prevenção de Vazamento de Dados (DLP) e Proteção de Integridade. Ele varre diretórios em busca de dados sensíveis expostos (Chaves de API, CPFs, Cartões de Crédito), isola e criptografa esses arquivos usando criptografia militar AES-256, e monitora a integridade dos dados protegidos via hashes SHA-256.

## 2. Stack Tecnológica
- Linguagem: Python 3.10+
- Bibliotecas Principais: 
  - `cryptography` (Para o módulo CryptoVault - AES-256)
  - `re` (Regex nativo para o motor de DLP)
  - `hashlib` (Para cálculo de hashes SHA-256)
  - `pytest` (Para cobertura total de testes via TDD)

## 3. Estrutura de Diretórios Proposta
DLP_CryptoVault/
│
├── core/
│   ├── __init__.py
│   ├── dlp_scanner.py     # Motor de busca por Regex (Chaves, CPFs, etc)
│   ├── crypto_vault.py    # Criptografia AES-256 (Cipher)
│   └── integrity.py       # Monitor de integridade com SHA-256
│
├── tests/                 # Pasta central de testes (TDD)
│   ├── __init__.py
│   ├── test_dlp_scanner.py
│   ├── test_crypto_vault.py
│   └── test_integrity.py
│
├── vault_storage/         # Pasta segura (Sandbox) onde os arquivos ficam criptografados
├── logs/                  # Logs de auditoria do sistema
├── .gitignore             # Proteção de arquivos locais
├── cloud.md               # Este arquivo de especificação
└── main.py                # Orquestrador do sistema