from typing import Protocol

class TokenProviderPort(Protocol):
    def get_token(self) -> str: ...