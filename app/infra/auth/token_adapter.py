# infra/auth/token_adapter.py
import time
import requests
from core.ports.token_provider import TokenProviderPort

class TokenAdapter(TokenProviderPort):
    def __init__(self, auth_url: str, client_id: str, client_secret: str):
        self._auth_url = auth_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._token: str | None = None
        self._expires_at: float = 0.0

    def get_token(self) -> str:
        now = time.time()
        if self._token is not None and now < self._expires_at:
            return self._token

        resp = requests.post(
            self._auth_url,
            data={
                "grant_type": "client_credentials",
                "client_id": self._client_id,
                "client_secret": self._client_secret,
            },
            timeout=5,
        )
        resp.raise_for_status()
        data = resp.json()

        self._token = data["access_token"]
        self._expires_at = now + float(data.get("expires_in", 300))
        return self._token
