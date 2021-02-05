# coding: utf-8
from argparse import ArgumentParser, Namespace
from configparser import ConfigParser

from common.const import CONF_DIR
from common.logger import logger, trace


@trace
def func_need_know_running_time():
    a = 0
    for _ in range(10_000_000):
        a += 1
    logger.info(f'a = {a}')


def main(args: Namespace, config: ConfigParser):
    logger.debug(f'args = {args}')
    logger.debug(f'config = {config}')

    func_need_know_running_time()


if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_args()

    config = ConfigParser()
    config.read(CONF_DIR / 'sample.ini')

    main(args, config)
