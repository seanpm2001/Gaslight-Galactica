# Start of script
'''
The player color palette script for Gaslight Galactica
'''
# Import section
import random() # Not needed, I just wanted to import something
# Definition of functions section
def monochromePalette():
	print ("Monochrome palette selected")
	colorCount = int(2)
	monochromePaletteColors = ["Black", "White"]
	print ("Palette colors: " + str(monochromePaletteColors()))
	noMore = input("End of description")
def greyscalePaletteA():
	print ("Greyscale palette selected")
	colorCount = int(3)
	greyscalePaletteAColors = ["Black", "White", "Grey"]
	print ("Palette colors: " + str(grayscalePaletteAColors()))
	noMore = input("End of description")
def grayscalePaletteB():
	print ("Grayscale palette selected")
	colorCount = int(4)
	greyscalePaletteAColors = ["Black", "White", "Light Grey", "Dark Gray"]
	print ("Palette colors: " + str(grayscalePaletteBColors()))
	noMore = input("End of description")
def threeBitPalette():
	print ("3 bit palette selected")
	colorCount = int(8)
	threeBitPaletteColors = ["", "", "", "", "", "", "", ""]
	print ("Palette colors: " + str(threeBitPaletteColors()))
	noMore = input("End of description")
def classicPalette():
	print ("Classic Palette selected")
	colorCount = int(12)
	classicPaletteColors = ["", "", "", "", "", "", "", "", "", "", "", ""]
	print ("Palette colors: " + str(classicPaletteColors()))
	noMore = input("End of description")
def fourBitPalette():
	print ("4 bit palette selected")
	colorCount = int(16)
	fourBitPaletteColors = ["", "", "", "", "", "", "", "","", "", "", "", "", "", "", ""]
	print ("Palette colors: " + str(fourBitPaletteColors()))
	noMore = input("End of description")
def fiveBitPalette():
	print ("5 bit palette selected")
	colorCount = int(32)
	fiveBitPaletteColors = ["", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", ""]
	print ("Palette colors: " + str(fiveBitPaletteColors()))
	noMore = input("End of description")
def sixBitPalette():
	print ("6 bit palette selected")
	colorCount = int(64)
	sixBitPaletteColors = ["", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", ""]
	print ("Palette colors: " + str(sixBitPaletteColors()))
	noMore = input("End of description")
def sevenBitPalette():
	print ("7 bit palette selected")
	colorCount = int(128)
	sevenBitPaletteColors = ["", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", ""]
	print ("Palette colors: " + str(sevenBitPaletteColors()))
	noMore = input("End of description")
def eightBitPalette():
	print ("8 bit palette selected")
	colorCount = int(128)
	eightBitPaletteColors = ["", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "","", "", "", "", "", "", "", ""]
	print ("Palette colors: " + str(eightBitPaletteColors()))
	noMore = input("End of description")
def idList():
	print ("Palette ID list")
	print ("Monochrome palette (2 colors) | ID: AA1")
	print ("Greyscale palette A (3 colors) | ID: AA2")
	print ("Grayscale palette B (4 colors) | ID: AA3")
	print ("3 bit palette (8 colors) | ID: AA4")
	print ("Classic palette A (10 colors) | ID: AA5")
	print ("Classic palette B (12 colors) | ID: AA6")
	print ("4 bit palette (16 colors) | ID: AA7")
	print ("5 bit palette (32 colors) | ID: AA8")
	print ("6 bit palette (64 colors) | ID: AA9")
	print ("7 bit palette (128 colors) | ID: AA10")
	print ("8 bit palette (256 colors) | ID: AA11")
''' End of imports and definitions '''
# Main output
print ("Gaslight Galactica color palettes")
print ("Select a palette to preview [type an ID]")
#print (str(idList()))
print (idList())
inputID = str(input("Enter an ID to view a palette"))
inputID == inputID.upper()
# Optimize this section by taking the first 2 letters, then adding a number via string concatenation
if (inputID == "AA1"):
	print (monochromePalette())
elif (inputID == "AA2"): # Partially optimized by using elif instead of else: \n\t if
	print (greyscalePaletteA())
elif (inputID == "AA3"):
	print (grayscalePaletteB())
elif (inputID == "AA4"):
	print (threeBitPalette())
elif (inputID == "AA5"):
	print (classicPaletteA())
elif (inputID == "AA6"):
	print (classicPaletteB())
elif (inputID == "AA7"):
	print (fourBitPalette())
elif (inputID == "AA8"):
	print (fiveBitPalette())
elif (inputID == "AA9"):
	print (sixBitPalette())
elif (inputID == "AA10"):
	print (sevenBitPalette())
elif (inputID == "AA11"):
	print (eightBitPalette())
else:
	print ("Error: ID is not recognized")
# End of script (quit condition)
noMore = input("Press [ENTER] to quit")
print ("This program should now be closed. If the window is still open, press the close button. If this doesn't work, try ending the task/process with a task manager/process manager")
"""
File info
File type: Python script file (*.py)
File version: 1 (Friday, December 11th 2020 at pm)
Line count (including blank lines and compiler line): 129
"""
# Divider
'''
ToDo:
add color names
'''
# End of script
