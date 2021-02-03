# coding: utf-8
from functools import wraps
from time import time

from loguru import logger

from common.decorator import omittable_parentheses

__all__ = ['logger', 'trace']


@omittable_parentheses()
def trace(enter_msg: str = 'entering', leave_msg: str = 'leaving'):
    def _decorator(func):
        @wraps(_decorator)
        def _wrapper(*args, **kwargs):
            fn_name = func.__name__
            logger.info(f'[{fn_name}] {enter_msg}')
            now = time()
            result = func(*args, **kwargs)
            then = time()
            logger.info(f'used time: {round(then - now, 3)}s')
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
