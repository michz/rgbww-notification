from json import JSONEncoder

class JSONEncodable(object):
    def json(self):
        return vars(self)

class Device(JSONEncodable):
    ip: ''
    name: ''
    factorR: 1.0
    factorG: 1.0
    factorB: 1.0
    factorWW: 1.0
    factorCW: 1.0

    def __init__(self, ip, name, factorR, factorG, factorB, factorWW, factorCW):
        self.ip = ip
        self.name = name
        self.factorR = factorR
        self.factorG = factorG
        self.factorB = factorB
        self.factorWW = factorWW
        self.factorCW = factorCW
