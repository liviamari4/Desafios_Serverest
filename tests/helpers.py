import uuid

BASE_URL = "https://compassuol.serverest.dev"


def generate_email():
    return f"user_{uuid.uuid4().hex}@test.com"
