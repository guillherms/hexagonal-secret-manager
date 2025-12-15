from typing import Protocol
from core.model.app_secrets import AppSecrets

class SecretsPort(Protocol):
    def get(self) -> AppSecrets: ...