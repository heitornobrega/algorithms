import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    with pytest.raises(TypeError):
        encrypt_message("12345678", "chave")

    with pytest.raises(TypeError):
        encrypt_message(1234, 2)

    assert encrypt_message("12345678", 8) == "87654321"

    assert encrypt_message("12345678", 3) == "321_87654"

    assert encrypt_message("mensagem", 4) == "mega_snem"