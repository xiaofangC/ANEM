# coding: utf-8
from common.cache import memory_cache
from common.logger import *
from common.pipeline import Task


class Task0(Task):
    @trace
    def run(self):
        super().run()


class Task1(Task):
    @trace
    def run(self):
        super().run()


class Task2(Task):
    @trace
    def run(self):
        super().run()


class Task3(Task):
    @trace
    def run(self):
        super().run()


class Task4(Task):
    @trace
    def run(self):
        super().run()


class Task5(Task):
    @trace
    def run(self):
        super().run()
        input_a = memory_cache['input_a']
        logger.info(f'input_a = {input_a}')
        memory_cache['output_a'] = 42
