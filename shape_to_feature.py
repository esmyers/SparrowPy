## taken from http://www.bgcarto.com/export-map-layers-to-gdb-with-python/
import arcpy

mxd = arcpy.mapping.MapDocument(r"C:\Project\Project_SDE1.mxd")

##use mxdCurrent if pasting directly into python window in ArcMap
mxdCurrent = arcpy.mapping.MapDocument("CURRENT")

out = r"D:\ESMData\MapperFiles\SparrowFiles\SparrowMARB_NEW\Sparrow_MARB.gdb"
for lyr in arcpy.mapping.ListLayers(mxdCurrent):
    if lyr.supports("DATASOURCE"):
        ds = lyr.dataSource
        nm = lyr.name
        print nm
        arcpy.FeatureClassToFeatureClass_conversion(ds, out, nm)
