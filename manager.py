from multiprocessing.managers import BaseManager
from queue import Queue


class QueueManager(BaseManager):
    # def __init__(self, address = None, authkey = None, serializer = "pickle", ctx = None):
    # super().__init__(address, authkey, serializer, ctx)

    pass


# QueueManager.register('Task',task.Task)


class QueueClient:
    def __init__(self):
        QueueManager.register("get_task_queue")
        QueueManager.register("get_result_queue")
        self.m = QueueManager(address=("127.0.0.1", 50000), authkey=b"abcd")
        self.m.connect()
        self.task_queue = self.m.get_task_queue()
        self.result_queue = self.m.get_result_queue()

        # m = QueueManager(address=(),authkey=())

        # m.connect()
        # self.task_queue = m.get_task_queue()
        # self.result_queue = m.get_result_queue()


if __name__ == "__main__":
    print("lancement serveur")
    task_queue = Queue(100)
    result_queue = Queue(100)

    QueueManager.register("get_task_queue", callable=lambda: task_queue)
    QueueManager.register("get_result_queue", callable=lambda: result_queue)
    m = QueueManager(address=("", 50000), authkey=b"abcd")
    s = m.get_server()
    s.serve_forever()
