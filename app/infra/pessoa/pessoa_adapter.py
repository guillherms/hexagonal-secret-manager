import requests
from core.ports.pessoa_gateway import PessoaGatewayPort
from core.ports.token_provider import TokenProviderPort

class PessoaAdapter(PessoaGatewayPort):
    def __init__(self, base_url: str, token_provider: TokenProviderPort):
        self._base_url = base_url.rstrip("/")
        self._token_provider = token_provider

    def get_pessoa(self, id_pessoa: str) -> dict:
        token = self._token_provider.get_token()
        resp = requests.get(
            f"{self._base_url}/pessoas/{id_pessoa}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5,
        )
        resp.raise_for_status()
        return resp.json()