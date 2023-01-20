from src.domain.item import *
from src.domain.interfaz import *

class NormalItem(Item, Updateable):
    def __init__(self,  name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)
    
    def getName(self):
        return self.name

    def getQuality(self):
        return self.quality

    def getSellIn(self):
        return self.sellIn

    def setSellIn(self):
        self.sellIn = self.getSellIn()-1

    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality = self.quality + value
        else:
            self.quality = 0
        assert 0 <= self.quality <= 50, "Calidad de %s fuera de rango" %self.__class__.__name__
    
    def sumQuality(self, value):
        if self.getQuality() + value > 50:
            self.setQuality(50)
        elif self.getQuality() + value >= 0:
            self.setQuality(self.getQuality() + value)
        else:
            self.setQuality(0)

    def updateQuality(self):
        if self.getSellIn() > 0:
            self.sumQuality(-1)
        else:
            self.sumQuality(-2)
        self.setSellIn()  


        