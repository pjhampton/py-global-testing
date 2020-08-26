from services.srvb import goodbye

def test_goodbye_world_returns_correctly():
    assert goodbye.goodbye() == "Goodbye, World!"

