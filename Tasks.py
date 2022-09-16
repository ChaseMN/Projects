# How do I name this? I guess it's staying as Untitled-1 for now
# I realised instantly after typing this^ that all I need to do it save it

from datetime import date
import os

#Creates a Folder for the day's QuickBooks files and opens it
var = date.today()
today = var.strftime("%B %d")
path = os.path.join("C:/QB CSVs/", today)
os.mkdir(path)
os.startfile(path)

#Other things I could (probably not, but maybe) automate

#Inserting the new values from the initial download into the spreadsheet, then redownloading the new csv

