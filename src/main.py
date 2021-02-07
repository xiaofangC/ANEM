# coding: utf-8
from argparse import ArgumentParser, Namespace
from configparser import ConfigParser

from common.cache import memory_cache
from common.const import CONF_DIR
from common.logger import *
from common.pipeline import Pipeline
from pipelines.sample_tasks import Task0, Task1, Task2, Task3, Task4, Task5


def main(cmd_args: Namespace, config: ConfigParser):
    logger.debug(f'args = {cmd_args}')
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
    pipeline_a = Pipeline(to_tasks=[task1, task0], name='Pipeline A')
    pipeline_a.run(cmd_args, config)
    logger.info(f"output_a = {memory_cache['output_a']}")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--date', type=str, required=True)
    cmd_args = parser.parse_args()

    # sample
    print(cmd_args.date)

    config = ConfigParser()
    config.read(CONF_DIR / 'sample.ini')

    # sample
    print(config.get("mysql", "host"))
    print(config.getint("mysql", "port"))

    main(cmd_args, config)
