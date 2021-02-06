# coding: utf-8
from argparse import ArgumentParser, Namespace
from configparser import ConfigParser

from common.const import CONF_DIR
from common.pipeline import Pipeline
from pipelines.sample_tasks import *


def main(args: Namespace, config: ConfigParser):
    logger.debug(f'args = {args}')
    logger.debug(f'config = {config}')

    task0 = Task0(name='0')
    task1 = Task1(name='1')
    task2 = Task2(name='2')
    task3 = Task3(name='3')
    task4 = Task4(name='4')
    task5 = Task5(name='5')

    task5 >> task2
    task5 >> task0
    task4 >> task0
    task4 >> task1
    task2 >> task3
    task3 >> task1

    memory_cache['input_a'] = 12
    pipeline_a = Pipeline(from_tasks=[task4, task5], name='Pipeline A')
    pipeline_a.run()
    logger.info(f"output_a = {memory_cache['output_a']}")


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_args()

    config = ConfigParser()
    config.read(CONF_DIR / 'sample.ini')

    main(args, config)
