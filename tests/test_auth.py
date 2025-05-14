import pytest
from auth import jwt_auth

def test_create_and_decode_token():
    data = {"user_id": "123", "role": "user"}
    token = jwt_auth.create_jwt_token(data)
    decoded = jwt_auth.decode_jwt_token(token)
    assert decoded["user_id"] == "123"
    assert decoded["role"] == "user"

def test_invalid_token():
    invalid_token = "invalid.token.string"
    decoded = jwt_auth.decode_jwt_token(invalid_token)
    assert decoded is None
