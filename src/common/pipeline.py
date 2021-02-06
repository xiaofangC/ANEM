# coding: utf-8
import abc
import typing
from uuid import uuid4

from networkx import DiGraph, topological_sort

from common.logger import *


class Task(abc.ABC):
    def __init__(self, name: str = None):
        self.next_tasks: typing.List['Task'] = list()
        self.name = name or f'Task_{uuid4()}'

    def __rshift__(self, other: 'Task'):
        if not other or not isinstance(other, Task):
            raise TypeError("type of 'other' should be Node")

        self.next_tasks.append(other)

    @abc.abstractmethod
    def run(self):
        logger.info(f'running node [{self.name}]')


class Pipeline:
    def __init__(self,
                 from_tasks: typing.Sequence[Task],
                 *,
                 name: str = 'Pipeline'):
        self.task_queue = self._topological_sort(from_tasks)
        self.name = name

    def _traveling_tasks(self, from_tasks: typing.Sequence[Task]) \
            -> typing.Iterator[typing.Tuple[Task, Task]]:
        all_next_tasks = list()
        for task in from_tasks:
            for next_task in task.next_tasks:
                yield task, next_task
                all_next_tasks.append(next_task)

            yield from self._traveling_tasks(all_next_tasks)

    def _topological_sort(self, from_tasks: typing.Sequence[Task]) -> typing.Iterable[Task]:
        """Topological sort algorithm for a DAG"""
        di_graph = DiGraph(self._traveling_tasks(from_tasks))
        return topological_sort(di_graph)

    @trace
    def run(self):
        logger.info(f'running pipeline [{self.name}]')

        for task in self.task_queue:
            task.run()
