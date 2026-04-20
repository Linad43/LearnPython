import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (1, 3, "Function 'test_fun' is start.\n" "Function 'test_fun' is end.\n\n"),
        (
            1,
            0,
            "Function 'test_fun' is start.\n"
            "Function 'test_fun' is failed.\n"
            ">> call 'test_fun((1, 0), {})'\n"
            ">> return 'division by zero'\n\n",
        ),
    ],
)
def test_decorator_log(x: int, y: int, expected: str, capsys: pytest.CaptureFixture) -> None:
    @log()
    def test_fun(x_in: int, y_in: int) -> float:
        return x_in / y_in

    test_fun(x, y)
    captured = capsys.readouterr().out
    assert captured == expected
