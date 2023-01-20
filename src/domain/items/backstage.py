from src.domain.normalItem import *

class Backstage(NormalItem):

    def __init__(self, name, sellIn, quality):
        Item.__init__(self, name, sellIn, quality)

    
    def updateQuality(self):
        if 0<self.sellIn<=5:
            self.setQuality(+3)
        elif 5<self.sellIn<= 10:
            self.setQuality(+2)
        elif self.sellIn <= 0:
            self.quality = 0
        self.setSellIn()