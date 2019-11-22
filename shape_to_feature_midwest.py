## taken from http://www.bgcarto.com/export-map-layers-to-gdb-with-python/
import arcpy

mxd = arcpy.mapping.MapDocument(r"D:\ESMData\MapperFiles\SparrowFiles\SparrowMidwest\SparrowMidwest_3.29.19\Midwest_wm.mxd")

##use mxdCurrent if pasting directly into python window in ArcMap
#mxdCurrent = arcpy.mapping.MapDocument("CURRENT")

out = r"D:\ESMData\MapperFiles\SparrowFiles\SparrowMidwest\SparrowMidwest_3.29.19\midwest_3.19.2019.gdb"
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("DATASOURCE"):
        ds = lyr.dataSource
        nm = lyr.name
        print nm
        arcpy.FeatureClassToFeatureClass_conversion(ds, out, nm)


print "JOB COMPLETE"
