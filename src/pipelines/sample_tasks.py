# coding: utf-8
from argparse import Namespace
from configparser import ConfigParser

from common.cache import memory_cache
from common.logger import *
from common.pipeline import Task


class Task0(Task):
    @trace
    def run(self, cmd_args: Namespace, config: ConfigParser):
        super().run(cmd_args, config)


class Task1(Task):
    @trace
    def run(self, cmd_args: Namespace, config: ConfigParser):
        super().run(cmd_args, config)


class Task2(Task):
    @trace
    def run(self, cmd_args: Namespace, config: ConfigParser):
        super().run(cmd_args, config)


class Task3(Task):
    @trace
    def run(self, cmd_args: Namespace, config: ConfigParser):
        super().run(cmd_args, config)


class Task4(Task):
    @trace
    def run(self, cmd_args: Namespace, config: ConfigParser):
        super().run(cmd_args, config)


class Task5(Task):
    @trace
    def run(self, cmd_args: Namespace, config: ConfigParser):
        super().run(cmd_args, config)

        input_a = memory_cache['input_a']
        logger.info(f'input_a = {input_a}')
        memory_cache['output_a'] = 42
