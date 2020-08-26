from services.srva import hello

def test_hello_world_returns_correctly():
    assert hello.hello() == "Hello, World!"

def test_xservice_secret_is_correct():
    assert hello.get_secret_from_service_b() == "The secret is <<super secret>>"
