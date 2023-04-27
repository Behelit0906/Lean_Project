import os
import re
import xlwings as xw

def fillBacklog():
    fleets = ("Cam320", "Kom320", "Camion240", "Car789C", "Hit EX3600R", "Hitachi EX5500", "L1350","LIE984C", "MotoNiv 16M", 
            "TraillaC631E", "P&H_XPC", "TalDML35", "TalDMLSP", "TalPV271", "Tanq. CAT", "TOruga D9T", "TOruga D10T", "TOruga D11T")

    # Expresión regular para buscar archivos que contienen "ots" en el nombre
    regex = re.compile("ots")
    regex2 = re.compile("mst")

    #Ruta de los archivos del backlog
    filesPath = r"C:\lean\backlog_files"

    #Creo una instancia de Excel
    app = xw.App(visible=False)

    #Abro el archivo y selecciono la hoja Backlog
    leanFile = app.books.open(r"C:\lean\lean.xlsm")
    leanSheet = leanFile.sheets['Backlog']
    print('aca')
    #Obtengo la lista de archivos de las ots de las flotas
    otsFiles = [filename for filename in os.listdir(filesPath) if filename.endswith(".xls") and regex.search(filename)]
    
    #Lista de los archivos de las mst de las flotas
    mstFiles = [filename for filename in os.listdir(filesPath) if filename.endswith(".xls") and regex2.search(filename)]

    #Recorro la lista de archvios de ots
    for filename in otsFiles:
        #Abro el archivo, selecciono la hoja 1 y obtengo el valor de las ots 
        workbook = app.books.open(os.path.join(filesPath, filename))
        worksheet = workbook.sheets['Sheet1']
        otsValue = worksheet.range(2,17).value
        
        #Defino el nombre de la flota en base al nombre dle archivo "Cam320_ots", hago un split y escojo el primer item que retorna "Cam320"
        fleetName = filename.split("_")[0]
        
        #Si se está leyendo el Cam320 le cambio el nombre al correspondiente en el lean "Hit320"
        if(fleetName == 'Cam320'):
            fleetName = 'Hit320'
        
        #Busco en la hoja Backlog del Lean, la celda donde debo insertar la información, recorro la columna B para encontrar la fila de la flota de la iteración actual (B2:B23)
        for row in range(2, 23):
            #obtengo el valor de la celda para compararlo con el dato a buscar (el nombre de la flota que obtuve antes)
            cell_value = leanSheet.range((row, 2)).value
            
            #Asigno el valor sacado de archivo ots a la celda pertinente si la encuentra
            if cell_value == fleetName:
                leanSheet.range((row, 5)).value = otsValue
                break
        
        workbook.close()
    
    #Lo mismo del primer ciclo for pero para las mst  
    for filename in mstFiles:
        workbook = app.books.open(os.path.join(filesPath, filename))
        worksheet = workbook.sheets['Sheet1']
        mstValue = worksheet.range(2,12).value
        
        fleetName = filename.split("_")[0]
        if(fleetName == 'Cam320'):
            fleetName = 'Hit320'
        
        for row in range(2, 23):
            cell_value = leanSheet.range((row, 2)).value
            if cell_value == fleetName:
                leanSheet.range((row, 7)).value = mstValue
                break
    
        workbook.close()
        
    leanFile.save()
    leanFile.close() 