from src.domain.normalItem import *
from src.domain.items.agedBrie import *
from src.domain.items.backstage import *
from src.domain.items.conjured import *
from src.domain.items.sulfuras import *
import pytest

with open("report.txt") as f:
	currentDay = f	

pytest.mark.collectedITems
def changeFormat(currentDay):
	itemsCurrentDay = []
	for item in currentDay:
		name, sellIn, quality = item.split(',')
		
		if name == '+5 Dexterity Vest':
			itemsCurrentDay.append(NormalItem(name, int(sellIn), int(quality)))
    	
		elif name == 'Aged Brie':
			itemsCurrentDay.append(AgedBrie(name, int(sellIn), int(quality)))
		
		elif name == 'Elixir of the Mongoose':
			itemsCurrentDay.append(NormalItem(name, int(sellIn), int(quality)))
    	
		elif name == 'Sulfuras, Hand of Ragnaros':
			itemsCurrentDay.append(Sulfuras(name, int(sellIn), int(quality)))
	
		elif name == 'Backstage passes to a TAFKAL80ETC concert':
			itemsCurrentDay.append(Backstage(name, int(sellIn), int(quality)))
      	
		elif name == 'Conjured Mana Cake':
			itemsCurrentDay.append(Conjured(name, int(sellIn)), int(quality))

		else:
			itemsCurrentDay.append(NormalItem(name, int(sellIn)), int(quality))
