from src.domain.normalItem import *
class Sulfuras(NormalItem):

    def __init__(self, name, SellIn, quality):
        Item.__init__(self, name, SellIn, quality)

    
    def updateQuality(self):
        assert self.quality == 80, "Calidad de %s distinta de 80" % self.__class__.__name__
        pass