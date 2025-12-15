import os, json, time
import boto3
from botocore.exceptions import ClientError
from core.ports.secrets_port import SecretsPort
from core.model.app_secrets import AppSecrets

_sm = boto3.client("secretsmanager")  # ✅ fora do handler

class SecretsManagerAdapter(SecretsPort):
    def __init__(self, secret_id: str, ttl_seconds: int = 21600):
        self._secret_id = secret_id
        self._ttl = ttl_seconds
        self._cached: AppSecrets | None = None
        self._expires_at = 0.0

    def get(self) -> AppSecrets:
        now = time.time()
        if self._cached is not None and now < self._expires_at:
            return self._cached

        try:
            raw = _sm.get_secret_value(SecretId=self._secret_id)["SecretString"]
            data = json.loads(raw)

            secrets = AppSecrets(
                auth_client_id=data["CLIENT_ID"],
                auth_client_secret=data["CLIENT_SECRET"],
            )

            self._cached = secrets
            self._expires_at = now + self._ttl
            return secrets

        except ClientError:
            if self._cached is not None:  # fallback opcional
                return self._cached
            raise