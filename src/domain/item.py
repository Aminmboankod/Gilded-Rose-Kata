class Item:
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.quality = quality 
        self.sellIn = sellIn
    
    
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)
    
