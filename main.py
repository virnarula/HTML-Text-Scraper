import re

def readFromFile(fileLocation):
    f = open(fileLocation, "r")
    return f.read()


def writeToFile(str, fileDestination):
    f = open(fileDestination, "w")
    f.write(str)
    f.close()


def removeTags(html):
    reg = re.compile('<.*?>')
    return re.sub(reg, '', html)

fileDirectory = ''
fileDestination = ''

writeToFile(removeTags(readFromFile(fileDirectory)), fileDestination)
