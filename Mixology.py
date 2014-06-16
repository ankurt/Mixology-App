
from Tkinter import *

def run():
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=500, height=500)
    canvas.pack()
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 500
    canvas.data.height = 500
    init(canvas)
    root.bind("<Key>", lambda event: keyPressed(canvas, event))
    #root.bind("<Button-1>", lambda event: mousePressed(canvas,event))
    root.mainloop()

def keyPressed(canvas, event):
    return 

def mousePressed(canvas,event):
    if canvas.data.mainMenu == True:
        mainMenuMousePresses(canvas, event)
    redrawAll(canvas)

def mainMenuMousePresses(canvas, event):
    if ((canvas.data.xmargin < event.x < canvas.data.xmargin + canvas.data.buttonWidth) and
        canvas.data.ymargin < event.y < canvas.data.ymargin + canvas.data.buttonWidth):
            recipe(canvas)
    return
    
def sToL(s):
    l = []
    for i in s:
        l += [i]
    return l

def ltoS(l):
    s = ''.join(l)
    return s

def formatTxt(s):
    a = sToL(s)
    b = []
    for i in a:
        if i.isalnum() ==  True:
            b += [i.lower()]
    return ltoS(b)
    
def parser(canvas, s):
    if type(s) != str:
        return False
    s = formatTxt(s)
    for line in open('recipes.txt', 'r'):
        if s == "": return False
        elif (s) in line:
            if "_" in line:
                Recipe.name = line.split('_')[0]
                Recipe.codeName = line.split('_')[1]
                Recipe.ingredients = line.split('_')[2]
                Recipe.glassType = line.split('_')[3]
                Recipe.volume = float(line.split('_')[4])
                Recipe.assembly = line.split('_')[5]
                if s == Recipe.codeName: break
        else:
            continue
    if len(Recipe.name) == 0 or Recipe.codeName != s:
        Recipe.name = ""
        return False

def getAllDrinkNames():
    allDrinks = []
    for line in open('recipes.txt', 'r'):
        if ("_") in line:
            s = line.split('_')[0]
            allDrinks += [s]
    return allDrinks

def selectMainMenu(canvas):
    canvas.data.mainMenu = True
    canvas.data.recipeBook = False
    canvas.data.makeMeADrink = False
    canvas.data.currentDrink = False
    canvas.data.About = False
    canvas.data.Build = False
    selectMenu(canvas)

def selectMakeMeADrink(canvas):
    canvas.data.mainMenu = False
    canvas.data.recipeBook = False
    canvas.data.makeMeADrink = True
    canvas.data.currentDrink = False
    canvas.data.About = False
    canvas.data.Build = False
    selectMenu(canvas)
    
def selectAbout(canvas):
    canvas.data.mainMenu = False
    canvas.data.recipeBook = False
    canvas.data.makeMeADrink = False
    canvas.data.currentDrink = False
    canvas.data.About = True
    canvas.data.Build = False
    selectMenu(canvas)

def selectBuild(canvas):
    canvas.data.mainMenu = False
    canvas.data.recipeBook = False
    canvas.data.makeMeADrink = False
    canvas.data.currentDrink = False
    canvas.data.About = False
    canvas.data.Build = True
    selectMenu(canvas)
    
def selectRecipeBook(canvas):
    canvas.data.recipeBook = True
    canvas.data.mainMenu = False
    canvas.data.makeMeADrink = False
    canvas.data.currentDrink = False
    canvas.data.About = False
    canvas.data.Build = False
    selectMenu(canvas)
    
def drawMainMenuButtons(canvas):
    def doRecipeBook():
        selectRecipeBook(canvas)
        
    def doMakeMeADrink():
        selectMakeMeADrink(canvas)
        
    def doAbout():
        selectAbout(canvas)
    
    def doBuild():
        selectBuild(canvas)
    
    numButtons = canvas.data.numButtons = 5
    width = canvas.data.width
    height = canvas.data.height
    buttonWidth = canvas.data.buttonWidth = 110
    buttonHeight = canvas.data.buttonHeight = 50
    ymargin = canvas.data.ymargin = (height - (buttonHeight * numButtons))/numButtons
    xmargin = canvas.data.xmargin = width / 10
    canvas.data.left = left = xmargin
    canvas.data.top = top = (ymargin + onHeight)
    canvas.data.right = right = xmargin + buttonWidth
    canvas.data.bottom = bottom = (ymargin + buttonHeight)
    canvas.create_window(xmargin +100, 300 + ymargin,
                         window=Button(canvas,command=doAbout,text="About"))
    canvas.create_window(xmargin + 100, ymargin,
                         window=Button(canvas, text="Recipe Book",
                                              command = doRecipeBook,
                                              state = 'active'))
    canvas.create_window(xmargin + 100, 100 + ymargin,
                         window = Button(canvas,
                                         text="Make Me A Drink",
                                         command = doMakeMeADrink))
    canvas.create_window(xmargin + 100, 200 + ymargin,
                         window=Button(canvas,
                                       text="Build A Drink",
                                       command = doBuild))


def drawMainMenuGlass(canvas):
    width = canvas.data.width
    height = canvas.data.width
    x0 = width/2
    y0 = height/10
    x1 = width/2 + 75
    y1 = height/10 + 100
    separation = 20
    canvas.create_line(x0, y0, x1, y1)
    canvas.create_line(x1 + 75 + separation, y0, x1 + separation, y1)
    canvas.create_line(x1, y1, x1, y1 * 2)
    canvas.create_line(x1 + separation, y1, x1 + separation, y1 * 2)
    canvas.create_line(x0, y0, x1 + 75 + separation, y0)
    canvas.create_oval(x0, .9 * y1*2, x1  + 75 + separation, 1.1 * y1 * 2)

def recipeBook(canvas):
    width = canvas.data.width
    a = getAllDrinkNames()
    drawFakeButtons(canvas, a)
    drawRecipeBookButtons(canvas)
    

def drawRecipeBookButtons(canvas):
    width = canvas.data.width
    canvas.data.save = StringVar()
    canvas.data.saveEntry = Entry(canvas, textvariable = canvas.data.save)
    canvas.data.saveEntry.insert(0, "Enter Drink Name Here")
    canvas.data.saveEntry.place(x = width/2, y=20, anchor='center')
    def doBack():
        canvas.data.saveEntry.destroy()
        selectMainMenu(canvas)
    
    def doEnterDrink():
        canvas.data.saveEntry.destroy()
        enterDrinkButton(canvas)
        
    canvas.create_window(width/8, 20,
                         window = Button(canvas,
                                         command=doBack,
                                         text="Back"))
    
    canvas.create_window(width - width/8, 20,
                         window=Button(canvas,
                                       command=doEnterDrink,
                                       text="Select"))

def selectCurrentDrink(canvas):
    canvas.data.mainMenu = False
    canvas.data.recipeBook = False
    canvas.data.makeMeADrink = False
    canvas.data.currentDrink = True
    canvas.data.About = False
    canvas.data.Build = False
    selectMenu(canvas)
    
def makeAllIngredientsList(canvas, allIngredients):
    canvas.create_text(430, 110, text ="All Ingredients",
                       font=("Underline"))
    width = canvas.data.width
    s =""
    for x in allIngredients:
        s += "-"+ x + "," + "\n"
    msg = s
    canvas.data.listOfAllIngredients = Text(canvas, wrap=WORD,
                                            bg="gray",
                                            yscrollcommand =1000,
                                            width = 15,
                                            height = 14,
                                            borderwidth=0)
    canvas.data.listOfAllIngredients.insert(END, msg)
    canvas.data.listOfAllIngredients.place(x=width - width/4, y=120)
    canvas.data.listOfAllIngredients.config(state=DISABLED)
    
def currentDrink(canvas):
    drawCurrentDrinkButtons(canvas)
    canvas.data.allIngredients = sorted(getAllIngredients(canvas))
    makeAllIngredientsList(canvas, canvas.data.allIngredients)
    if type(Recipe.ingredients) != list:
        Recipe.ingredients = convertIngredients(canvas)
    drawGlass(canvas)
    fillGlass(canvas)
    writeAssembly(canvas)
    drawChangeIngredients(canvas)

def drawChangeIngredients(canvas):
    canvas.data.changeIngredients = StringVar()
    canvas.data.changeIngredientsEntry = Entry(canvas,
                                               textvariable=canvas.data.changeIngredients)
    canvas.data.changeIngredientsEntry.insert(END,"ingredient, quantity")
    canvas.data.changeIngredientsEntry.place(x=175,y=45)
    def doChange():
        canvas.data.nonLiquids.destroy()
        canvas.data.assemblyText.destroy()
        canvas.data.listOfAllIngredients.destroy()
        canvas.data.changeIngredientsEntry.destroy()
        canvas.data.saveNameEntry.destroy()
        change = canvas.data.changeIngredients.get()
        changeIngredients(canvas, change)
    
    def doAdd():
        canvas.data.saveNameEntry.destroy()
        canvas.data.nonLiquids.destroy()
        canvas.data.assemblyText.destroy()
        canvas.data.listOfAllIngredients.destroy()
        canvas.data.changeIngredientsEntry.destroy()
        addIngredients(canvas)
    canvas.create_window(390, 60, window=Button(canvas,command=doChange,
                                                           text="Change"))
    canvas.create_window(150, 60, window=Button(canvas, command=doAdd,
                                                text="+"))

def addIngredients(canvas):
    change = canvas.data.changeIngredients.get()
    try:
        ingredient = change.split(",")[0]
        ingredient.strip()
        ingredient.lower()
        quantity = change.split(",")[1]
        quantity = float(quantity.strip())
    except:
        return selectCurrentDrink(canvas)
    actualVolumeOfRest = 0
    totalQuantity = 0
    for x in xrange(len(Recipe.ingredients)):
        if Recipe.ingredients[x][0].find("*") == -1:
            if Recipe.ingredients[x][0] == ingredient:
                return selectCurrentDrink(canvas)
            else:
                actualVolumeOfRest += float(Recipe.ingredients[x][1])
        else: continue
    totalQuantity = actualVolumeOfRest + quantity
    if canvas.data.allIngredients.count(ingredient) == 0:
        pass
    else:
        if ingredient.find("*") == -1:
            if totalQuantity > Recipe.volume:
                Recipe.ingredients += [[ingredient, quantity]]
                volumeOfRest = float(Recipe.volume) - quantity
                for x in xrange(len(Recipe.ingredients)):
                    if Recipe.ingredients[x][0].find("*") == -1:
                        if Recipe.ingredients[x][0] != ingredient:
                            Recipe.ingredients[x][1] = str(float(Recipe.ingredients[x][1])*(volumeOfRest/actualVolumeOfRest))
            else:
                Recipe.ingredients += [[ingredient, quantity]]
        else:
            Recipe.ingredients += [[ingredient, quantity]]
    selectCurrentDrink(canvas)
    
def changeIngredients(canvas, change):
    totalQuantity = 0
    actualVolumeOfRest = 0
    if change is not "":    
        if change.find(",") != -1:
            try:
                ingredient = change.split(",")[0]
                ingredient.strip()
                ingredient.lower()
                quantity = change.split(",")[1]
                quantity = float(quantity.strip())
            except:
                return selectCurrentDrink(canvas)
            for x in xrange(len(Recipe.ingredients)):
                if quantity <= 0.0:
                    if Recipe.ingredients[x][0] == ingredient:
                        Recipe.ingredients = Recipe.ingredients[:x] + Recipe.ingredients[x+1:]
                        return selectCurrentDrink(canvas)
                elif Recipe.ingredients[x][0].find("*") == -1:
                    if ingredient == Recipe.ingredients[x][0]:
                        if quantity <= Recipe.volume:
                            Recipe.ingredients[x][1] = quantity
                            changedQuantity = quantity
                        else:
                            selectCurrentDrink(canvas)
                    else:
                        actualVolumeOfRest += float(Recipe.ingredients[x][1])
                    totalQuantity += float(Recipe.ingredients[x][1])
                else:
                    if Recipe.ingredients[x][0] == ingredient:
                        Recipe.ingredients[x][1] = quantity
                        return selectCurrentDrink(canvas)
            if totalQuantity > Recipe.volume:
                volumeOfRest = float(Recipe.volume) - float(changedQuantity)
                for x in xrange(len(Recipe.ingredients)):
                    if Recipe.ingredients[x][0].find("*") == -1:
                        if Recipe.ingredients[x][0] != ingredient:
                            Recipe.ingredients[x][1] = str(float(Recipe.ingredients[x][1])*(volumeOfRest/actualVolumeOfRest))
    selectCurrentDrink(canvas)
            

def writeAssembly(canvas):
    width = canvas.data.width
    height = canvas.data.height
    msg = Recipe.assembly
    canvas.data.assemblyText = Text(canvas, wrap=WORD,width=35,
                                    height=4, bg="gray",
                                    borderwidth=1)
    canvas.data.assemblyText.insert(END,msg)
    canvas.data.assemblyText.place(x=width/4, y=height - 130)
    canvas.data.assemblyText.config(state=DISABLED)
    
def listIngredients(canvas, ingredients):
    s = ""
    a = []
    for char in ingredients:
        if char is not ",":
            s += char
        else:
            a.append(s)
            s = ""
    return a

def getAllIngredients(canvas):
    listAllIngredients = []
    for line in open('recipes.txt', 'r'):
        if "allIngredients" in line:
            listAllIngredients += line.split(":")[1]
    return listIngredients(canvas, listAllIngredients)

def convertIngredients(canvas):
    s = ""
    a = []
    a1 = []
    count = 0
    ingredients = Recipe.ingredients
    for char in ingredients:
        if char == ",":
            a1 += [s]
            s = ""
        elif char == ":":
            a1 += [s]
            s = ""
            a += [a1]
            a1 = []
        else:
            s += char
    return a

#When different glassTypes are available
#def fillGlass(canvas):
#    if Recipe.glassType == "collins":
#        fillCollinsGlass(canvas)
#    if Recipe.glassType == "oldfashioned":
#        fillOldFashionedGlass(canvas)

def fillOldFashionedGlass(canvas):
    width = canvas.data.width
    height = canvas.data.height
    volume = Recipe.volume
    b1 = width/2 - width/4
    b2 = (width/2 + 30) - (width/4 - 30)
    Filling.top = 150
    Filling.bottom = 300
    area = 0.5 * (b1 + b2) * (Filling.bottom - Filling.top)
    i = 0
    

def fillGlass(canvas):
    width = canvas.data.width
    height = canvas.data.height
    ingredients = Recipe.ingredients
    volume = Recipe.volume
    Filling.top = 100
    Filling.bottom = 335
    area = (width/2 - width/4) * (Filling.bottom - Filling.top)
    #for future if there are different glassTypes
    #elif Recipe.glassType == "old fashioned":
    #    area = 0.5 * (b1 + b2) * (Filling.bottom - Filling.top)
    i = 0
    countOfNonLiquids = 0
    canvas.data.nonLiquids = Text(canvas, width=15, height=15,
        wrap=WORD, yscrollcommand=100, bg="orange", borderwidth=0, font=("Arial","10"))
    for x in xrange(len(ingredients)):
        if ingredients[x][0].find("*") != -1:
            drawNonLiquids(canvas, ingredients[x][0].strip("*"), ingredients[x][1])
            countOfNonLiquids += 1
        elif float(ingredients[x][1]) > 0.0:
            colors = ["red","blue","green","yellow","purple","white","violet","cyan","magenta","gray"]
            filling(canvas, Filling.top, Filling.bottom, area, ingredients[x][0], float(ingredients[x][1]), volume, colors[i%10])
            i += 1
    if countOfNonLiquids != 0:
        canvas.data.nonLiquids.place(x=22, y=100)
        canvas.data.nonLiquids.config(state=DISABLED)

def filling(canvas, top, bottom, area, ingredient, quantity, volume, color):
    width = canvas.data.width
    pixelsPerOunce = int(area/volume)
    widthOfGlass = width/2 - width/4
    quantityFilled = (quantity * pixelsPerOunce)/widthOfGlass
    nudge = 100
    canvas.create_rectangle(width/2 + nudge, bottom, width/4 + nudge, bottom - quantityFilled, fill = color)
    Filling.bottom = bottom - quantityFilled
    recipeIngredients(canvas, ingredient, quantity, bottom, quantityFilled)
    
def drawNonLiquids(canvas, ingredient, quantity):
    msg = "%.1f %s\n" % (float(quantity), ingredient)
    canvas.data.nonLiquids.insert(END, msg)
    
def recipeIngredients(canvas, ingredient, quantity, bottom, quantityFilled):
    msg = "%s: %.1foz" % (ingredient,quantity)
    nudge = 100
    xc = 75 + nudge
    yc = (bottom - quantityFilled/2)
    canvas.create_text(xc, yc, text = msg, anchor = 'center',
                       font=("Arial", "10"))

def saveDrink(canvas):
    width = canvas.data.width
    Recipe.name = canvas.data.saveName.get()
    Recipe.codeName = formatTxt(Recipe.name)
    open('recipes.txt','a+').write(Recipe.name + "_" + Recipe.codeName + "_")
    for x in Recipe.ingredients:
        open('recipes.txt','a+').write("%s,%.1f:" %(x[0],float(x[1])))  
    open('recipes.txt','a+').write("_" + Recipe.glassType + "_" + str(Recipe.volume) + "_" + Recipe.assembly + "\n")
    canvas.data.nonLiquids.destroy()
    canvas.data.assemblyText.destroy()
    canvas.data.listOfAllIngredients.destroy()
    canvas.data.changeIngredientsEntry.destroy()
    canvas.data.saveNameEntry.destroy()
    selectCurrentDrink(canvas)
    canvas.create_text(width - width/3, 20, text = "Saved!", fill = "red")
    
def drawCurrentDrinkButtons(canvas):
    width = canvas.data.width
    height = canvas.data.width
    def doMainMenu():
        canvas.data.nonLiquids.destroy()
        canvas.data.assemblyText.destroy()
        canvas.data.listOfAllIngredients.destroy()
        canvas.data.changeIngredientsEntry.destroy()
        canvas.data.saveNameEntry.destroy()
        selectMainMenu(canvas)
    
    def doSave():
        if canvas.data.saveName.get() != "":
            saveDrink(canvas)
    
    canvas.create_window(width/8, 20, window=
        Button(canvas, command=doMainMenu, text="Main Menu"))
    canvas.create_window(width - width/8, 480, window=
        Button(canvas, command=doSave, text="Save Drink"))
    canvas.data.saveName = StringVar()
    canvas.data.saveNameEntry = Entry(canvas, textvariable = canvas.data.saveName)
    canvas.data.saveNameEntry.insert(END, "Save as...")
    canvas.data.saveNameEntry.place(x=width/4+85, y=465)
    if Recipe.name == '':
        text = "New Custom Drink"
    else:
        text = Recipe.name
    canvas.create_text(width/2, 20, text=text)

def drawFakeButtons(canvas, a):
    count = 0
    numButtons = canvas.data.numButtons = len(a)
    width = canvas.data.width
    height = canvas.data.height
    buttonWidth = 95
    buttonHeight = 24
    ymargin = 50
    xmargin = 13
    numCols = width/buttonWidth
    numRows = int((height - ymargin)/buttonHeight)
    for row in xrange(numRows):
        for col in xrange(numCols):
            left = xmargin + col * buttonWidth
            top = ymargin + row*buttonHeight
            right = left + buttonWidth
            bottom = top + buttonHeight
            try:
                canvas.create_rectangle(left, top, right, bottom
                                        , fill = "white")
                canvas.create_text(left + buttonWidth/2, top + buttonHeight/2, text = a[count],
                                   font=("Arial"))
                count += 1
            except:
                continue

def drawMainMenuText(canvas):
    left = canvas.data.left
    top = canvas.data.top
    buttonWidth = canvas.data.buttonWidth
    buttonHeight = canvas.data.buttonHeight
    ymargin = canvas.data.ymargin
    canvas.create_text(canvas.data.width/2 + 75, canvas.data.height - 100,
                       text = "Let's Mix!", font = ("Arial", "36"))

def selectMenu(canvas):
    redrawAll(canvas)
    if canvas.data.mainMenu:
        mainMenu(canvas)
    elif canvas.data.recipeBook:
        recipeBook(canvas)
    elif canvas.data.makeMeADrink:
        makeMeADrink(canvas)
    elif canvas.data.currentDrink:
        currentDrink(canvas)
    elif canvas.data.About:
        about(canvas)
    elif canvas.data.Build:
        build(canvas)

def build(canvas):
    Recipe.name = ""
    Recipe.codeName = ""
    Recipe.glassType="collins" #for future, when glassTypes are available
    Recipe.assembly="Enjoy!"
    Recipe.ingredients = []
    def doBack():
        canvas.data.volumeBuildEntry.destroy()
        selectMainMenu(canvas)
        
    def doSaveVolume():
        volume = canvas.data.volumeBuild.get()
        s = ""
        for x in volume:
            if x.isdigit() or x == ".":
                s += x
        volume = s
        if float(volume) > 0.0:
            Recipe.volume = float(volume)
            canvas.data.volumeBuildEntry.destroy()
            selectCurrentDrink(canvas)
        else:
            selectBuild(canvas)
    width = canvas.data.width
    height = canvas.data.height
    canvas.data.volumeBuild= StringVar()
    canvas.data.volumeBuildEntry = Entry(canvas, textvariable=canvas.data.volumeBuild)
    canvas.data.volumeBuildEntry.insert(END, "Enter here...")
    canvas.data.volumeBuildEntry.place(x=width/4+40,y=100)
    canvas.create_window(390, 115,window=Button(canvas,command=doSaveVolume,text="Select"))
    canvas.create_window(width/8, 50,window=Button(canvas,command=doBack,text="Back"))
    canvas.create_text(width/2, 65, text = "Start from scratch!")
    canvas.create_text(width/2, 150, text = "Insert a glass volume in ounces", font=("Verdana","12"))
    canvas.create_text(width/2, height/2, text ="Happy Mixing!",
                       font=("Verdana","36"))

def about(canvas):
    width = canvas.data.width
    height = canvas.data.height
    msg= """My name is Ankur Toshniwal, and this is my 15-112 term project for the spring semester of 2013. I first thought of this idea when brainstorming term projects with my roommate. He suggested to do something that could actually be used rather than an arcade game. I like to eat, but since programming food wouldn't really work, the next best thing was drinks! I hope to improve this project even after the course has ended because I have truly enjoyed working on this.\n-Ankur

Specs:
-Programmed strictly in python
-Visual Package: Tkinter

References:
-15112 course site: http://www.cs.cmu.edu/~112/
-Python documentation: http://docs.python.org/2/contents.html
-stackoverflow site: http://docs.python.org/2/contents.html
-effbot site: http://effbot.org/
-Visual reference: Drawn by: F. Roemhild, Designed by: R.J. Dinino, Filename: DRINKS.DWG, Title: HAPPY HOUR ASSEMBLIES & DETAILS OF MIXED DRINKS RIGHT OR LEFT HAND
"""
    def doBack():
        canvas.data.aboutText.destroy()
        selectMainMenu(canvas)
    canvas.create_text(width/2, 50, text="About The Project", font=("Arial", "36"))
    canvas.data.aboutText = Text(canvas, wrap=WORD,width = 50, height=15,
                                 yscrollcommand = 100)
    canvas.data.aboutText.insert(END, msg)
    canvas.data.aboutText.place(x=75,y=width/4)
    canvas.create_window(width/8,50,
                         window=Button(canvas,command=doBack,text="Back"))

def makeMeADrink(canvas):
    drawMakeMeADrinkButtons(canvas)
    canvas.data.allIngredients = sorted(getAllIngredients(canvas))
    makeAllIngredientsList(canvas, canvas.data.allIngredients)
    canvas.data.listOfAllIngredients.config(state=DISABLED)

def drawMakeMeADrinkButtons(canvas):
    def doAddIngredient():
        canvas.data.enterIngredientsEntry.destroy()
        canvas.data.listOfAllIngredients.destroy()
        canvas.data.makeDrinkInstructions.destroy()
        addIngredientToList(canvas)
    def doBack():
        canvas.data.enterIngredientsEntry.destroy()
        canvas.data.listOfAllIngredients.destroy()
        canvas.data.makeDrinkInstructions.destroy()
        selectMainMenu(canvas)
    def doFindDrink():
        canvas.data.enterIngredientsEntry.destroy()
        canvas.data.listOfAllIngredients.destroy()
        canvas.data.makeDrinkInstructions.destroy()
        findDrink(canvas)
        
    width = canvas.data.width
    height = canvas.data.height
    canvas.create_text(width/2,50,text="?", font=("Arial","48"))
    canvas.data.makeDrinkInstructions = Text(canvas, width=30,height=8,
                                             wrap=WORD, bg="orange")
    msg = "Select ingredients that you have on hand from list to the right. Enter them into the text box exactly as they appear without the dash or comma and the program will recommend the best drink for you!"    
    canvas.data.makeDrinkInstructions.insert(END, msg)
    canvas.data.makeDrinkInstructions.config(state=DISABLED)
    canvas.data.makeDrinkInstructions.place(x=width/4,y=250)
    canvas.data.enterIngredients = StringVar()
    canvas.data.enterIngredientsEntry = Entry(canvas, textvariable = canvas.data.enterIngredients)
    canvas.data.enterIngredientsEntry.place(x=width/2, y= height/4, anchor='center')
    canvas.create_window(width/8, 50, window=Button(canvas,command=doBack,text="Back"))
    canvas.create_window(width/2,160,window=Button(canvas,command=doAddIngredient, text="Add Ingredient"))
    canvas.create_window((width- width/8), 50, window=Button(canvas,command=doFindDrink,text="Find Drink"))

def findDrink(canvas):
    comparingIngredients = []
    matches = 0
    maxMatches = [0, [], ""]
    for line in open('recipes.txt','r'):
        if "_" in line:
            comparingIngredients = convertIngredientsToL(canvas,line.split("_")[2])
            for i in xrange(len(canvas.data.chosenIngredients)):
                for j in xrange(len(comparingIngredients)):
                    if canvas.data.chosenIngredients[i] == comparingIngredients[j][0]:
                        name = line.split("_")[1]
                        matches += 1
            if matches > maxMatches[0]:
                maxMatches = [matches, comparingIngredients, name]
            elif matches == maxMatches[0]:
                if len(maxMatches[1]) <= len(comparingIngredients):
                    continue
                else:
                    maxMatches[1] = comparingIngredients
                    maxMatches[2] = name
        matches = 0
    if maxMatches[0] == 0:
        canvas.data.enterIngredientsEntry.destroy()
        canvas.data.makeDrinkInstructions.destroy()
        selectRecipeBook(canvas)
    else:
        canvas.data.enterIngredientsEntry.destroy()
        canvas.data.makeDrinkInstructions.destroy()
        parser(canvas, maxMatches[2])
        selectCurrentDrink(canvas)
    
def convertIngredientsToL(canvas,s1):    
    s = ""
    a = []
    a1 = []
    ingredients = s1
    for char in ingredients:
        if char == ",":
            a1 += [s]
            s = ""
        elif char == ":":
            a1 += [s]
            s = ""
            a += [a1]
            a1 = []
        else:
            s += char
    return a

def addIngredientToList(canvas):
    addedIngredient = canvas.data.enterIngredients.get()
    addedIngredient.strip()
    s = ""
    for i in addedIngredient:
        if i.isalnum() or i.isspace():
            s += i
    if canvas.data.chosenIngredients.count(s) > 0:
        selectMakeMeADrink(canvas)
    else:
        canvas.data.chosenIngredients += [s]
        selectMakeMeADrink(canvas)
        canvas.create_text(250,215, text=("%s added" %(s)))

def mainMenu(canvas):
    drawMainMenuButtons(canvas)
    drawMainMenuText(canvas)
    drawMainMenuGlass(canvas)

def init(canvas):
    width = canvas.data.width
    height = canvas.data.height
    canvas.create_rectangle(0,0, width, height, fill="orange")
    canvas.data.mainMenu = True
    canvas.data.recipeBook = False
    canvas.data.makeMeADrink = False
    canvas.data.currentDrink = False
    canvas.data.About = False
    canvas.data.Build = False
    canvas.data.chosenIngredients=[]
    selectMenu(canvas)

def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,
                            fill= "orange")

def enterDrinkButton(canvas):
    drink = canvas.data.save.get()
    if parser(canvas, drink) != False:
        selectCurrentDrink(canvas)
    else:
        selectRecipeBook(canvas)

class Recipe(object):
    glassType = ""
    name = ""
    ingredients = []
    volume = ""
    assembly = ""
    codeName = ""

class Filling(object):
    top = 0
    bottom = 0
    
def drawCollinsGlass(canvas):
    width = canvas.data.width
    height = canvas.data.height
    top = 100
    bottom = 335
    wedge = 15
    nudge = 100
    canvas.create_line(width/4 + nudge,top,width/4 + nudge,bottom + wedge)
    canvas.create_line(width/4 + nudge, bottom + wedge,width/2 + nudge, bottom + wedge)
    canvas.create_line(width/2 + nudge, bottom + wedge,width/2 + nudge, top)
    canvas.create_line(width/4 + nudge, bottom, width/2 + nudge, bottom)

def drawOldFashionedGlass(canvas):
    # for the future if I decide to add glass types
    width = canvas.data.width
    height = canvas.data.width
    top = 150
    bottom = 300
    angle = 30
    wedge = 10
    canvas.create_line(width/4, top, width/4 + angle, bottom + wedge)
    canvas.create_line(width/4 + angle, bottom + wedge, width/2, bottom + wedge)
    canvas.create_line(width/2, bottom + wedge, width/2 + angle, top)
    canvas.create_line(width/4 + angle, bottom, width/2, bottom)

def drawGlass(canvas):
    drawCollinsGlass(canvas)
    #for the future when I want to add different glassTypes

def convertCharToS(canvas, word):
    s = ""
    for char in word:
        s += char
    return s

        

#from bs4 import BeautifulSoup
run()