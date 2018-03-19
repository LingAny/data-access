from uuid import uuid4


def make_str() -> str:
    return uuid4().hex
