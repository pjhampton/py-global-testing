from services.srvb import secret

def hello() -> str:
    return "Hello, World!"

def get_secret_from_service_b() -> str:
    return f"The secret is {secret.get_secret()}"
