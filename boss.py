import manager
import task


class Boss(manager.QueueClient):
    def __init__(self):
        super().__init__()

    def put_work(self):
        tache = task.Task()
        self.task_queue.put(tache)

    def get_result(self):
        tache = self.result_queue.get()
        print(tache.time)


if __name__ == "__main__":
    boss = Boss()
    while True:
        boss.put_work()
        boss.get_result()
