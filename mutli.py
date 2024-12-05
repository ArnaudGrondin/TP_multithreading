from multiprocessing.managers import BaseManager
from queue import Queue
import task 

class QueueManager(BaseManager):

	#def __init__(self, address = None, authkey = None, serializer = "pickle", ctx = None):
		#super().__init__(address, authkey, serializer, ctx)
		
	pass

	
#QueueManager.register('Task',task.Task)

class queueClient():
	#j'initialise les 2 queue pour les sous-classes
	def __init__(self, address=None, authkey=None, serializer="pickle", ctx=None):
		super().__init__(address, authkey, serializer, ctx)
		m = QueueManager(address=(),authkey=())
		
		m.connect()
		self.task_queue = m.get_task_queue()
		self.result_queue = m.get_result_queue()
		
	def put():
		pass

	def get():
		pass


class Boss(QueueManager):
	

	def put():
		i = 10
		l_tache = list
		while i <10:
			#self.task_queue.# on ajoute une tache a effectuer a la queue
			pass
	def get():
				# on recupere le resultat de la tache
		pass

	

class Minion(QueueManager):

	def put():
		pass
	def get():
		pass
	

if __name__=='__main__':

	ask_queue = Queue()
	result_queue = Queue()

	QueueManager.register('get_task_queue',callable=lambda:task_queue)
	QueueManager.register('get_result_queue',callable=lambda:result_queue)
	
	with QueueManager() as manager:
		tache = manager.Task()
		tache.work()
		print(tache.time)
