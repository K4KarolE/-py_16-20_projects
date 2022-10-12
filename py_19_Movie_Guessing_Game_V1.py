# It is a variation of the 04_Movie_Title_Randomizer.py in py_03-08_projects
# randomly picking a movie from Movies excel sheet
# give a hint about the movie (release year, stars, director,..)
# asking the user to guess the title

import random
from openpyxl import Workbook, load_workbook
wb = load_workbook('D:/Movies.xlsx', data_only=True)
ws = wb.active

#data_only=True -> copying values from excel instead of formulas for the Haveseen cell value

cellnumber = random.randrange(6,6952)

cell = 'C' + str(cellnumber)
movietitle = ws[cell].value

cellRYear = 'E' + str(cellnumber)
ReleaseYear = ws[cellRYear].value


cellHSeen = 'N' + str(cellnumber)
HaveSeen = ws[cellHSeen].value


cellDirector 1-3


cellStar 1-3









print()


if movietitle != None:
    print('Your movie this afternoon: ' + str(movietitle) + '(' + str(ReleaseYear) + ')')
    if HaveSeen == 1: 
        print('You have seen this movie only once since 05/2012.\n')
    else:
        print('You have seen this movie ' + str(HaveSeen) +  ' times since 05/2012.\n')
    quit() 

while movietitle == None:
    cellnumber += 1
    cell = 'C' + str(cellnumber)
    movietitle = ws[cell].value
    cellRYear = 'E' + str(cellnumber)
    ReleaseYear = ws[cellRYear].value
    cellHSeen = 'N' + str(cellnumber)
    HaveSeen = ws[cellHSeen].value
    
print('Your movie tonight: ' + str(movietitle) + '(' + str(ReleaseYear) + ')')

if HaveSeen == 1: 
    print('You have seen this movie only once since 05/2012.\n')
else:
    print('You have seen this movie ' + str(HaveSeen) +  ' times since 05/2012.\n')