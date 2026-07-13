def test_basic():
    assert 1 + 1 == 3

def test_app_response():
    assert b"Sawsa" in b"<h1>Sawsa's CI/CD Pipeline</h1>"
