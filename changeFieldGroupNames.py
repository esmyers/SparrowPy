#written by Erik Myers for WiM 10/5/2017
#note: to change field names to upper case you must first change the original field name text .gdb
#feature classes are not case-sensitive here so an upper() or lower() won't register as a change.

import arcpy

arcpy.env.workspace = r"D:\ESMData\MapperFiles\SparrowFiles\sparrow pacnorthwest\Pac_northwest_wm.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb





for fc in fcList: #loop through all feature classes in the .gdb
        print "_____________STARTING__________" + fc
               
        fields = arcpy.ListFields(fc)

        for field in fields:
                if field.name.lower() == 'huc8':
                        newName = 'GP3'  
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                if field.name.lower() == 'huc6':
                        newName = 'GP2'
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                if field.name.lower() == 'huc4':
                        newName = 'GP1'
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                if field.name.lower() == 'state':
                        newName = 'ST'
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                if field.name.lower() == 'st_huc8':
                        newName = 'SG3'
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                if field.name.lower() == 'st_huc6':
                        newName = 'SG2'
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                if field.name.lower() == 'st_huc4':
                        newName = 'SG1'
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)






        print fc + "_________________FINISHED______________"







print "Job Complete"
