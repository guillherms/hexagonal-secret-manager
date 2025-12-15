from typing import Protocol

class PessoaGatewayPort(Protocol):
    def get_pessoa(self, id_pessoa: str) -> dict: ...