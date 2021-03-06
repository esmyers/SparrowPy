## taken from http://www.bgcarto.com/export-map-layers-to-gdb-with-python/
import arcpy

mxdCurrent = arcpy.mapping.MapDocument(r"D:\ESMData\MapperFiles\SparrowFiles\SparrowSoutheast\Update_10.8.2019\process.mxd")

##use mxdCurrent if pasting directly into python window in ArcMap
#mxdCurrent = arcpy.mapping.MapDocument("CURRENT")

out = r"D:\ESMData\MapperFiles\SparrowFiles\SparrowSoutheast\Update_10.8.2019\process.gdb"
for lyr in arcpy.mapping.ListLayers(mxdCurrent):
    if lyr.supports("DATASOURCE"):
        ds = lyr.dataSource
        nm = lyr.name
        print "starting: " + nm
        arcpy.FeatureClassToFeatureClass_conversion(ds, out, nm)
        print "finished: " + nm

print "Job Complete"
