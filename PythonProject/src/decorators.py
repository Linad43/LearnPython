from typing import Callable, Optional, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R | None]], Callable[P, R | None]]:
    """Логироваание работы функции и ее результат как в файл, так и в консоль."""
    def decorator(func: Callable[P, R]) -> Callable[P, R | None]:
        def write_log(message: str) -> None:
            if filename is None:
                print(message, end="")
            else:
                with open(filename, "a") as f:
                    f.write(message)

        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R | None:
            text_log = f"Function '{func.__name__}' is start.\n"
            try:
                result = func(*args, **kwargs)
                text_log = f"{text_log}Function '{func.__name__}' is end.\n\n"
                write_log(text_log)
                return result
            except Exception as e:
                text_log = f"{text_log}Function '{func.__name__}' is failed.\n"
                text_log = f"{text_log}>> call '{func.__name__}({args}, {kwargs})'\n"
                text_log = f"{text_log}>> return '{e}'\n\n"
                write_log(text_log)
                return None

        return wrapper

    return decorator
