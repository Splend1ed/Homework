class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def my_boss(self):
        return self.name, self.id_, self.company, self.workers

    @my_boss.setter
    def my_boss(self, worker: 'Worker'):
        if worker not in self.workers:
            self.workers.append(worker.my_worker)
        else:
            print('This worker is already work for this boss')
        if worker.company != self.company:
            print(f'This worker does not work for {self.company} company')

    @my_boss.deleter
    def my_boss(self):
        del self.id_, self.name, self.company

    def __repr__(self):
        return f'Boss:\nid: {self.id_}\nName: {self.name}\nCompany: {self.company}\nWorkers:\n{self.workers}'


class Worker:
    def __init__(self, id_, name: str, company: str, *boss: Boss):
        self.id_ = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def my_worker(self):
        return self.name, self.id_, self.company,

    @my_worker.setter
    def my_worker(self, boss: 'Boss'):
        self.boss = boss

    @my_worker.deleter
    def my_worker(self):
        del self.id_, self.name, self.company

    def __repr__(self):
        return f'{self.id_}, {self.name}, {self.company}'


b1 = Boss(1, 'Tony', 'Samsung')
b2 = Boss(2, 'Tony', 'Samsung')
b3 = Boss(3, 'Tony', 'Samsung')
w1 = Worker(156, 'John', 'Samsung')
w2 = Worker(321, 'Piter', 'Samsung')
w3 = Worker(171, 'Antonio', 'Samsung')
b1.my_boss = w1
b1.my_boss = w2
b1.my_boss = w3
print(b1)
print(b2)