#written by Erik Myers for WiM 10/5/2017
#note: to change field names to upper case you must first change the original field name text .gdb
#feature classes are not case-sensitive here so an upper() or lower() won't register as a change.

import arcpy

arcpy.env.workspace = r"D:\ESMData\MapperFiles\SparrowFiles\SparrowNorthwest\SPARROW_NW_Updated.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb





for fc in fcList: #loop through all feature classes in the .gdb
        if fc == 'mrb7_cats_state_tp' or fc == 'mrb7_cats_state_tn':
               
                fields = arcpy.ListFields(fc)

                for field in fields:
                    if field.name.lower()[-2:] == '_s':
                        newName = field.name.upper()[:-2]  #get all but the last 2 characters of the string
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                        















print "Job Complete"
