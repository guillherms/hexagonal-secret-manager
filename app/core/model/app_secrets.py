from dataclasses import dataclass

@dataclass(frozen=True)
class AppSecrets:
    auth_client_id: str
    auth_client_secret: str