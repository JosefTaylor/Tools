import os

def MakeSubFolders(path, folderNames):

	root_path = path
	for folderName in folderNames:
		newPath = os.path.join(root_path, folderName)
		if not os.path.exists(newPath):
			os.makedirs(newPath)

#MakeSubFolders(os.getcwd(),['docs','work','data'])			

def FolderStructure():
	tree = {'Project':{'data':{'foo':{},'bar':{}},'work':{'foo':{},'bar':{}},'docs':{'foo':{},'bar':{}}}}
	return( tree )

def GetFolderNames(path, tree):
	currDir = os.path.basename(path)
	return list(tree[currDir].keys())


template = FolderStructure()
path = os.path.join(os.getcwd(),'Project')

try:
	folderNames=GetFolderNames(path, template)	
except KeyError:
	print ('no such folder in template')

index = input('Choose one {}'.format(folderNames))

#print(folderNames[int(index)])
MakeSubFolders(path, [folderNames[int(index)]])

