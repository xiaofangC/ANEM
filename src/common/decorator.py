# coding: utf-8
import typing
from functools import wraps


def omittable_parentheses(maybe_decorator: typing.Callable = None, allow_partial: bool = False):
    """A decorator for decorators that allows them to be used without parentheses"""

    def _decorator(func):
        @wraps(_decorator)
        def _wrapper(*args, **kwargs):
            if len(args) == 1 and callable(args[0]):
                if allow_partial:
                    return func(**kwargs)(args[0])
                elif not kwargs:
                    return func()(args[0])
            return func(*args, **kwargs)

        return _wrapper

    if maybe_decorator is None:
        return _decorator
    else:
        return _decorator(maybe_decorator)
