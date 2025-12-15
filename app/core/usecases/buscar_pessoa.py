from core.ports.pessoa_gateway import PessoaGatewayPort

class BuscarPessoaUseCase:
    def __init__(self, pessoa_gateway: PessoaGatewayPort):
        self._pessoa_gateway = pessoa_gateway

    def execute(self, id_pessoa: str) -> dict:
        return self._pessoa_gateway.get_pessoa(id_pessoa)