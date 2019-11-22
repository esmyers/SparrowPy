#written by Erik Myers for WiM 10/5/2017
#note: to change field names to upper case you must first change the original field name text .gdb
#feature classes are not case-sensitive here so an upper() or lower() won't register as a change.

import arcpy

arcpy.env.workspace = r"D:\ESMData\MapperFiles\SparrowFiles\SparrowNorthwest\SPARROW_NW_Updated.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb





for fc in fcList: #loop through all feature classes in the .gdb
        if not (fc == 'mrb7_cats_state_tn' or fc == 'mrb7_cats_state_tp'):
               
                fields = arcpy.ListFields(fc)

                for field in fields:
                        if field.name.lower()[-6:] == '_al_al':
                                newName = field.name.upper()[:-3]  #get all but the last 3 characters of the string
                                print newName
                                print fc
                                arcpy.AlterField_management(fc, field.name, newName, newName)
                        elif field.name.lower()[-6:] == '_ay_al':
                                newName = field.name.upper()[:-3]  #get all but the last 3 characters of the string
                                print newName
                                print fc
                                arcpy.AlterField_management(fc, field.name, newName, newName)
                        elif field.name.lower()[-7:] == '_dal_al':
                                newName = field.name.upper()[:-3]  #get all but the last 3 characters of the string
                                print newName
                                print fc
                                arcpy.AlterField_management(fc, field.name, newName, newName)
                        elif field.name.lower()[-7:] == '_day_al':
                                newName = field.name.upper()[:-3]  #get all but the last 3 characters of the string
                                print newName
                                print fc
                                arcpy.AlterField_management(fc, field.name, newName, newName)
                        
                                
                        
                        







print "Job Complete"
