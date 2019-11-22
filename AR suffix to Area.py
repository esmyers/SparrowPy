#written by Erik Myers for WiM 10/5/2017
#note: to change field names to upper case you must first change the original field name text .gdb
#feature classes are not case-sensitive here so an upper() or lower() won't register as a change.

import arcpy

arcpy.env.workspace = r"D:\ESMData\MapperFiles\SparrowFiles\SparrowPacific\9.24_update\process_wm.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb





for fc in fcList: #loop through all feature classes in the .gdb

        fields = arcpy.ListFields(fc)

        for field in fields:
                if field.name.lower()[-3:] == '_ar':
                        newName = field.name.upper()[:-3] + "_AREA"
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                        






print "Job Complete"
