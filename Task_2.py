#SECOND TASK
filename=input("Input the Filename:")
indice=filename.index(".")
extension=filename[indice+1:]
if extension == "py":
    print("The extension of the file is : 'python'")
elif extension == "java":
    print("The extension of the file is : 'java'")
