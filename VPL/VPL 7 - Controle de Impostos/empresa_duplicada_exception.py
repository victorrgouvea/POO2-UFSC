class EmpresaDuplicadaException(Exception):
    def __init__(self):
        super().__init__("Erro: Empresa duplicada")
