import json
def convertFile(path):
    fichero = open(path, 'r')
    matrixDays = []
    for linea in fichero:
        if linea.find("day") != -1:
            day = []
        elif linea == "\n":
            matrixDays.append(day)
        elif linea.find("name") != -1:
            numeroPropiedadesItem = len(linea.split(','))
        else:
            item = linea.rstrip().rsplit(',', maxsplit=numeroPropiedadesItem-1)
            day.append(item)
    
    fichero.close()
    return matrixDays



def createFile(content,file): 
    with open(file, "w+") as htmlFile:
        htmlFile.write(str(content))
    with open('reportDays.json', 'w') as f:
        json.dump(content, f)





path = "./src/tests.txt"
file = "./src/reportDays.json"
content = convertFile(path)
createFile(content, file)