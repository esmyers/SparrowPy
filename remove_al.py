#written by Erik Myers for WiM 10/5/2017
#note: to change field names to upper case you must first change the original field name text .gdb
#feature classes are not case-sensitive here so an upper() or lower() won't register as a change.

import arcpy

arcpy.env.workspace = r"D:\---path-----.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb





for fc in fcList: #loop through all feature classes in the .gdb
        if fc != 'mrb7_rf1_tp_catchment_state_results' or fc != 'mrb7_rf1_tn_catchment_state_results':
               
                fields = arcpy.ListFields(fc)

                for field in fields:
                    if field.name.lower()[-3:] == '_al':
                        newName = field.name.upper()[:-3]  #get all but the last 3 characters of the string
                        print newName
                        arcpy.AlterField_management(fc, field.name, newName, newName)
                        















print "Job Complete"
