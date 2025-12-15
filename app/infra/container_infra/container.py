# infra/lambda/container.py
import os
from infra.aws.secrets_manager_adapter import SecretsManagerAdapter
from infra.auth.token_adapter import TokenAdapter
from infra.pessoa.pessoa_adapter import PessoaAdapter
from core.usecases.buscar_pessoa import BuscarPessoaUseCase

class LambdaContainer:
    def __init__(self):
        self._secrets = SecretsManagerAdapter(
            secret_id=os.environ["SECRET_ID"],
            ttl_seconds=int(os.getenv("SECRET_TTL_SECONDS", "21600")),
        )

    def build_usecase(self) -> BuscarPessoaUseCase:
        secrets = self._secrets.get()

        token_provider = TokenAdapter(
            auth_url=os.environ["AUTH_URL"],
            client_id=secrets.auth_client_id,
            client_secret=secrets.auth_client_secret,
        )

        pessoa = PessoaAdapter(
            base_url=os.environ["PESSOA_API_URL"],
            token_provider=token_provider,
        )

        return BuscarPessoaUseCase(pessoa_gateway=pessoa)
