from src.domain.normalItem import *
from src.domain.items.agedBrie import *
from src.domain.items.backstage import *
from src.domain.items.conjured import *
from src.domain.items.sulfuras import *
from src.domain.gildedRose import *

if __name__=="__main__":

    itemList = [
                NormalItem("+5 Dexterity Vest", 10, 20),
                AgedBrie("Aged Brie", 2, 0),
                NormalItem("Elixir of the Mongoose", 5, 7),
                Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80),
                Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 10, 49),
                Backstage("Backstage passes to a TAFKAL80ETC concert", 5, 49),
                Conjured("Conjured Mana Cake", 3, 6),      
    ]

    inventory = GildedRose(itemList)

    for item in itemList:
        inventory.updateInventory()