class BBOX():
    def __init__(self, object):
        self.xywh = object
        self.p1 = (self.xywh[0], self.xywh[1])
        self.p2 = (self.xywh[0]+self.xywh[2], self.xywh[1]+self.xywh[3])