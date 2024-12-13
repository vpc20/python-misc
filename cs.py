import os

dirname = raw_input('Directory name for new C# project : ')
if dirname:
    projdir = 'C:\\Users\\vpc\CSharpProjects\\CodeWars\\' + dirname
    os.makedirs(projdir)

    os.chdir(projdir)
    os.system('dotnet new')
    os.system('dotnet restore')