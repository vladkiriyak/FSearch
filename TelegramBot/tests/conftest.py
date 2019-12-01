import pytest


@pytest.yield_fixture()
def my_fixture(request):
    print("\n" + "setup " * 10)

    yield "hello"

    print("\n" + "teardown" * 10)
