import time
from operations import OPERATION

class Segment:
    def __init__(self, operation, status, id, numberA, numberB, result):
        self.operation = OPERATION(operation)
        self.status = status
        self.id = id
        self.timestamp = time.time()
        self.numberA = numberA
        self.numberB = numberB
        self.result = result

        def pack(self):
            return "#1:O="+self.operation.name+"#2:S="+self.status+"#3:T="+self.timestamp+"#4:I="+self.id+"#5:A="+self.numberA+"#6:B="+numberB+"#7:R="+result

        def unpack(self, data):
            print("test")