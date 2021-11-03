from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import encrypt,decrypt,crack


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    expected = "Gdkkn Sghr hr Zactkkzg"
    actual = encrypt("Hello This is Abdullah",25)
    assert actual == expected

def test_decrypt():
    expected = "Hello This is Abdullah"
    actual = decrypt("Gdkkn Sghr hr Zactkkzg",25)
    assert actual == expected

def test_crack():
    assert crack("Gdkkn Sghr hr Zactkkzg") == "Hello This is Abdullah"