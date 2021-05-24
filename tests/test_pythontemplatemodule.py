from src.pythontemplatepackage.pythontemplatemodule import get_id


def test_get_id_john():
    id_result = get_id('John')
    assert 123 == id_result
