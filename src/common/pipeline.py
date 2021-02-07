# coding: utf-8
import abc
import typing
from argparse import Namespace
from configparser import ConfigParser
from uuid import uuid4

from networkx import DiGraph, topological_sort

from common.logger import *


class Task(abc.ABC):
    def __init__(self, name: str = None):
        self.parents: typing.List['Task'] = list()
        self.name = name or f'Task_{uuid4()}'

    def __rshift__(self, other: 'Task'):
        if not other or not isinstance(other, Task):
            raise TypeError("type of 'other' should be Node")

        other.parents.append(self)

    @abc.abstractmethod
    def run(self, cmd_args: Namespace, config: ConfigParser):
        logger.info(f'running node [{self.name}]')


class Pipeline:
    def __init__(self,
                 to_tasks: typing.Sequence[Task],
                 *,
                 name: str = 'Pipeline'):
        self.task_queue = self._topological_sort(to_tasks)
        self.name = name

    def _traveling_tasks(self, to_tasks: typing.Sequence[Task]) \
            -> typing.Iterator[typing.Tuple[Task, Task]]:
        all_prev_tasks = list()
        for task in to_tasks:
            for prev_task in task.parents:
                yield prev_task, task
                all_prev_tasks.append(prev_task)

            yield from self._traveling_tasks(all_prev_tasks)

    def _topological_sort(self, to_tasks: typing.Sequence[Task]) -> typing.Iterable[Task]:
        """Topological sort algorithm for a DAG"""
        di_graph = DiGraph(self._traveling_tasks(to_tasks))
        return topological_sort(di_graph)

    @trace
    def run(self, cmd_args: Namespace, config: ConfigParser) -> None:
        logger.info(f'running pipeline [{self.name}]')

        for task in self.task_queue:
            task.run(cmd_args, config)
