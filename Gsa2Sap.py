import Rhino as rh
import re

def Main(geometry):

	obj = rh.RhinoDoc.ActiveDoc.Objects.Find(geometry)
	layerNames = rh.RhinoDoc.ActiveDoc.Layers[obj.Attributes.LayerIndex].Name

	group, secString = layerNames.rsplit("{")sec.rstrip("}")
	#secName = sec.rstrip("}")#.replace("%",",")

	GroupTable(group)

	secName = GetSectionName(secString)

	SectionTable(secName)


def GetSectionName( secString ):

	try:
	    secType = re.search(r"(RHS|CHS|SHS|UC|UB|UKC|UKB|R|IT)", secString).groups(1)
	    secDim = re.search(r"((?:[\d]{1,6}(?:\.[\d]{0,6})?(?:x|%)){1,6}(?:[\d]{1,6}(?:\.[\d]{0,6})?))", secString).groups(1)
	except:
	    return secString	

    secType = secType.replace("CHS","CHCF").replace("RHS","RHCF")
    secDim = secDim.replace("%","X").replace("x","X").replace(".X","X").rstrip("X201107").rstrip("X201007").rstrip("X199904").rstrip(".")
    return secType + secDim


def GroupTable( group ):
	return "{0}, Frame, {1}".format( group, n )

def SectionTable( secName ):
	return "{0}, N.A., {1}, Default".format( n, section )

def FrameConnexTable( frameID, frameI, frameJ ):
	return "{0}, {1}, {2}, Yes".format( n, i, j )

def JointCoordTable( jointID, coordXYZ ):
	return "{0}, GLOBAL, Cartesian, {1}, Yes".format( n, xyz )
