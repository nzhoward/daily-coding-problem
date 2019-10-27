class IDLogger:
    def __init__(self, n):
        self.log = []
        self.size = n
        
    def record(self, order_id):
        if len(self.log) < self.size:
            self.log.append(order_id)
        else:
            self.log.pop(0)
            self.log.append(order_id)

    def get_last(self, i):
        k = len(self.log)
        return self.log[k - i]


logger = IDLogger(5)
logger.record(1)
logger.record(2)
print(logger.log)
logger.record(3)
print(logger.log)
logger.record(4)
print(logger.log)
logger.record(5)
logger.record(6)
logger.record(7)
print(logger.log)
print(logger.get_last(2))
