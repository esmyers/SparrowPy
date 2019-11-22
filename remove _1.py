#written by Erik Myers for WiM 10/5/2017
#useage: Can be used to remove duplicate fields after and join "keep all" operation.  ArcGIS will add a "_1" to the duplicate fields.
#This script is used to remove them.  It won't, however delete shape_Length or Shape_Area fiels even if they are duplicates.

import arcpy

arcpy.env.workspace = r"D:\ESMData\MapperFiles\SparrowFiles\SparrowMidwest\test.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb





for fc in fcList:
	if fc == 'Export_cat':
                fields = arcpy.ListFields(fc)
		for field in fields:
                        if field.name[-2:] == '_1':
                                print field.name
				arcpy.DeleteField_management(r"D:\ESMData\MapperFiles\SparrowFiles\SparrowMidwest\test.gdb\Export_cat", field.name)
				print field.name
                        
                        















print "Job Complete"
