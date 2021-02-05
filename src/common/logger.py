# coding: utf-8
import typing
from functools import wraps
from time import time

from loguru import logger

from common.decorator import omittable_parentheses

__all__ = ['logger', 'trace']


def _func_full_name(func: typing.Callable):
    if not getattr(func, '__module__', None):
        return getattr(func, '__qualname__', repr(func))
    return f'{func.__module__}.{func.__qualname__}'


def _human_readable_time(elapsed: float):
    mins, secs = divmod(elapsed, 60)
    hours, mins = divmod(mins, 60)

    if hours > 0:
        message = f'{hours}h{mins:02d}m{secs:02d}'
    elif mins > 0:
        message = f'{mins}m{secs:02d}'
    elif secs >= 1:
        message = f'{secs:.2f}s'
    else:
        message = f'{secs * 1000.0:.0f}ms'

    return message


@omittable_parentheses()
def trace(enter_msg: str = 'entering', leave_msg: str = 'leaving'):
    def _decorator(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            fn_name = _func_full_name(func)
            logger.info(f'[{fn_name}] {enter_msg}')
            now = time()
            result = func(*args, **kwargs)
            then = time()
            elapsed = then - now
            logger.info(f'[{fn_name}] running took {_human_readable_time(elapsed)} ({elapsed})')
            logger.info(f'[{fn_name}] {leave_msg}')
            return result

        return _wrapper

    return _decorator


if __name__ == '__main__':
    logger.info('info log')
    logger.error('error log')


    @trace
    def func_1(a, b):
        from time import sleep
        sleep(3)
        return a + b


    @trace(enter_msg='进来啦', leave_msg='出去啦')
    def func_2(a, b):
        from time import sleep
        sleep(.5)
        return a + b


    @trace
    def func_3(a, b):
        from time import sleep
        sleep(1)
        return a * b


    print(f'func_1 result = {func_1(1, 2)}')
    print(f'func_2 result = {func_2(3, 4)}')
    print(f'func_3 result = {func_3(10, 10)}')
