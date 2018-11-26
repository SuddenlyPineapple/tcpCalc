import time
import re
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
        return "#1:O=" + self.operation.name + "+#2:S=" + self.status + "+#3:I=" + self.id + "+#4:T=" + self.timestamp + "+#5:A=" + self.numberA + "+#6:B=" + self.numberB + "+#7:R=" + self.result

    @classmethod
    def unpack(cls, self, data):
        compiledRe = re.compile(r"#[0-9]:[A-Z]=[A-z0-9\-]*\+")
        arrayOfContents = compiledRe.search(data)

        operation = arrayOfContents[0][5:-1]
        status = arrayOfContents[1][5:-1]
        id = arrayOfContents[2][5:-1]
        numberA = arrayOfContents[3][5:-1]
        numberB = arrayOfContents[4][5:-1]
        result = arrayOfContents[5][5:-1]

        return cls(operation, status, id, numberA, numberB, result)

    def print(self):
        print("#1:O=" + self.operation.name + "+#2:S=" + self.status + "+#3:I=" + "+#4:T=" + self.timestamp + self.id + "+#5:A=" + self.numberA + "+#6:B=" + self.numberB + "+#7:R=" + self.result)