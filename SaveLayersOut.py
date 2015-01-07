import rhinoscriptsyntax as rs
import os.path

layers = rs.LayerNames()
filetype = ".iges"

path = """P:\\028927 Jeff Koons Sculptures\\02_Ballet Couple\\F04 - Structural\\Analysis\\ANSYS\\20131028_JT\\"""

#layers[:] = [item for item in layers if item.startswith("T")]

rs.EnableRedraw(False)

rs.UnselectAllObjects()

for layer in layers:
    rs.CurrentLayer(layer)
    geom = rs.ObjectsByLayer(layer)
    rs.ObjectName(geom,layer)
    #geom.append(rs.ObjectsByLayer("Body"))
    #geom.append(rs.ObjectsByLayer("NewBase"))
    rs.SelectObjects(geom)
    thisPath = path + layer + filetype
    #print thisPath
    rs.Command('_-export "%s" _enter' % (thisPath))
    rs.UnselectAllObjects()
    
rs.EnableRedraw(True)    