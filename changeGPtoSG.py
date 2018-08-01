#written by Erik Myers for WiM 10/5/2017
#note: to change field names to upper case you must first change the original field name text .gdb
#feature classes are not case-sensitive here so an upper() or lower() won't register as a change.

import arcpy

arcpy.env.workspace = r"D:\ESMData\MapperFiles\SparrowFiles\sparrow pacnorthwest\Pac_northwest_wm.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb





for fc in fcList: #loop through all feature classes in the .gdb
        if fc == 'mrb7_rf1_tp_huc8_results':
               
                fields = arcpy.ListFields(fc)

                for fc in fcList:
                        if fc == 'mrb7_rf1_tp_huc8_results' or 'mrb7_rf1_tn_huc8_results':
                                fields = arcpy.ListFields(fc)
                                for field in fields:
                                        if field.name.startswith("GP1_"):
                                                oldname = field.name
                                                newname = oldname.replace("GP1_", "GP3_")
                                                print newname

                                                arcpy.AlterField_management(fc, oldname, newname, newname)

                        print fc + '_________________FINISHED__________'

                        if fc == 'mrb7_rf1_tp_huc4_results' or 'mrb7_rf1_tn_huc4_results':
                                fields = arcpy.ListFields(fc)
                                for field in fields:
                                        if field.name.startswith("GP3_"):
                                                oldname = field.name
                                                newname = oldname.replace("GP3_", "GP1_")
                                                print newname

                                                arcpy.AlterField_management(fc, oldname, newname, newname)

                        print fc + '_________________FINISHED__________'


                        if fc == 'mrb7_rf1_tp_state_results' or 'mrb7_rf1_tn_state_results':
                                fields = arcpy.ListFields(fc)
                                for field in fields:
                                        if field.name.startswith("GP4_"):
                                                oldname = field.name
                                                newname = oldname.replace("GP4_", "ST_")
                                                print newname

                                                arcpy.AlterField_management(fc, oldname, newname, newname)

                        print fc + '_________________FINISHED__________'

                        if fc == 'mrb7_rf1_tp_huc8_state_results' or 'mrb7_rf1_tn_huc8_state_results':
                                fields = arcpy.ListFields(fc)
                                for field in fields:
                                        if field.name.startswith("GP5_"):
                                                oldname = field.name
                                                newname = oldname.replace("GP5_", "SG3_")
                                                print newname

                                                arcpy.AlterField_management(fc, oldname, newname, newname)

                        print fc + '_________________FINISHED__________'

                        if fc == 'mrb7_rf1_tp_huc6_state_results' or 'mrb7_rf1_tn_huc6_state_results':
                                fields = arcpy.ListFields(fc)
                                for field in fields:
                                        if field.name.startswith("GP6_"):
                                                oldname = field.name
                                                newname = oldname.replace("GP6_", "SG2_")
                                                print newname

                                                arcpy.AlterField_management(fc, oldname, newname, newname)

                        print fc + '_________________FINISHED__________'

                        if fc == 'mrb7_rf1_tp_huc4_state_results' or 'mrb7_rf1_tn_huc4_state_results':
                                fields = arcpy.ListFields(fc)
                                for field in fields:
                                        if field.name.startswith("GP7_"):
                                                oldname = field.name
                                                newname = oldname.replace("GP7_", "SG1_")
                                                print newname

                                                arcpy.AlterField_management(fc, oldname, newname, newname)

                        print fc + '_________________FINISHED__________'





print "Job Complete"
