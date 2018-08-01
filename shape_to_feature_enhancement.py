## taken from http://www.bgcarto.com/export-map-layers-to-gdb-with-python/
import arcpy

out_folder_path = r"C:\Users\emyers\Desktop"
out_name = "temp.gdb"

def createGDB(out_folder_path, out_name):
    #create temp geodatabase args("out_folder_path", "out_name", "out_version")
    arcpy.CreateFileGDB_management(out_folder_path, out_name, "10.0")
    createNewLayers(out_folder_path, out_name)

def createNewLayers(out_folder_path, out_name):
    #if running from IDLE
    mxd = arcpy.mapping.MapDocument(r"D:\ESMData\MapperFiles\SparrowFiles\East_US_Jan2018\SparrowEAST_Jan18.mxd")

    ##use mxdCurrent if pasting directly into python window in ArcMap
    #mxd = arcpy.mapping.MapDocument("CURRENT")
    #out = r"D:Users\emyers\Desktop"

    out = out_folder_path + "\\" + out_name
    for lyr in arcpy.mapping.ListLayers(mxd):
        if lyr.supports("DATASOURCE"):
            ds = lyr.dataSource
            nm = lyr.name
            print nm
            arcpy.FeatureClassToFeatureClass_conversion(ds, out, nm)


createGDB(out_folder_path, out_name)
