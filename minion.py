import manager


class Minion(manager.QueueClient):
    def __init__(self):
        super().__init__()

    def work(self):
        t = self.task_queue.get()
        t.work()
        self.result_queue.put(t)
        print("tache faite")


if __name__ == "__main__":
    minion = Minion()
    while True:
        minion.work()
