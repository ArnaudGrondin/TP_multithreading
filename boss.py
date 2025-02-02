import manager
import task


class Boss(manager.QueueClient):
    def __init__(self, nb_task=10, task_size=1000):
        super().__init__()
        self.nb_task = nb_task
        self.task_size = task_size

    def put_work(self):
        cpt = 0
        while cpt < self.nb_task:
            tache = task.Task(cpt, self.task_size)
            self.task_queue.put(tache)
            cpt = cpt + 1

    def get_result(self):
        sum = 0.0
        time_list = []
        for _ in range(self.nb_task):
            tache = self.result_queue.get()
            print(tache.time)
            time_list.append(tache)
        for t in time_list:
            sum = sum + t.time

        print(
            f"temps total pour {self.nb_task} tâches de taille {self.task_size} = {sum}"
        )


if __name__ == "__main__":
    boss = Boss()

    boss.put_work()
    boss.get_result()
