#written by Erik Myers for WiM 10/5/2017
#note: to change field names to upper case you must first change the original field name text .gdb
#feature classes are not case-sensitive here so an upper() or lower() won't register as a change.

import arcpy

arcpy.env.workspace = r"D:\ESMData\MapperFiles\SparrowFiles\East_US\Sparrow_East_Us_wm.gdb"

fcList = arcpy.ListFeatureClasses()  # get all feature classes in .gdb



for fc in fcList: #loop through all feature classes in the .gdb
    print "STARTING " + fc

    fields = arcpy.ListFields(fc) #get fields in feature class
    
    for field in fields:
        if not (field.name.lower() == "shape" or field.name.lower() == "objectid" or field.name.lower() == "shape_length" or field.name.lower() == "shape_area" or field.name.lower() == "objectid_1"):
            newName = field.name.upper()
            print newName
            arcpy.AlterField_management(fc, field.name, newName + "_temp", newName) #set field name to: UPPERCASE_EXAMPLE_temp  args = ({feature class}, {field to change}, {New Name},{New Alias})

    print "_temp names complete"



    tempFields = arcpy.ListFields(fc) #get fields from newly-altered feature class
    
    for field in tempFields:
        if not (field.name.lower() == "shape" or field.name.lower() == "objectid" or field.name.lower() == "shape_length" or field.name.lower() == "shape_area" or field.name.lower() == "objectid_1"):
            fieldName = field.name
            useFieldName = fieldName[:-5]  #cut _temp off field name
            print useFieldName
            arcpy.AlterField_management(fc, fieldName, useFieldName, useFieldName)


    print fc + "FINISHED"

print "Job Complete"
