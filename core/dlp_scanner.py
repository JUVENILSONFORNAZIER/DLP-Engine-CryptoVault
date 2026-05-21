import re

class DLPScanner:
    def __init__(self):
        # O arsenal do Caçador: Dicionário com os padrões Regex de dados sensíveis
        self.patterns = {
            "CPF": r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",
            "Cartao_Credito": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
            "Chave_API_Generica": r"(?i)[a-z0-9_\-]*(?:key|secret|token|senha|password)[a-z0-9_\-]*\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}['\"]?"
        }

    def scan_text(self, text: str) -> dict:
        """
        Analisa uma string de texto bruta e retorna tudo o que encontrar de vazamento.
        """
        findings = {}
        
        for data_type, pattern in self.patterns.items():
            matches = re.findall(pattern, text)
            if matches:
                findings[data_type] = matches
                
        return findings

    def scan_file(self, file_path: str) -> dict:
        """
        Abre um arquivo local na máquina, lê o conteúdo e passa pelo scan_text.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return self.scan_text(content)
        except Exception as e:
            # Se o arquivo não puder ser lido (ex: arquivo corrompido), reporta o erro
            return {"ERRO": [f"Não foi possível ler o arquivo: {str(e)}"]}