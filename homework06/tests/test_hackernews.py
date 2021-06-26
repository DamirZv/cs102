from hw06 import hackernews


def test_clear() -> None:
    assert hackernews.clean("DAMIR") == "DAMIR"
    assert hackernews.clean("C, A, T, S") == "C A T S"
    assert hackernews.clean("RAIN.ny()") == "RAINny"
