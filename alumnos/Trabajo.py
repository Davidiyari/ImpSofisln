alumno=input("ingresa el nombre: ")
nacimiento_=input("fecha de nacimiento: ")
edades_=input("edad alumno: ")
 
lineas=[alumno+'\n',
        nacimiento_+'\n',
        edades_+'\n']
  
class writed_doctxt():
    def doctxt (lineas):
        with open('alumnos.txt','a') as texto:
            texto.writelines(lineas)
    doctxt(lineas)
class close_doctxt():
    def leer_doctxt():
        mensaje=""
        with open('alumnos.txt','r') as texto:
            mensaje=texto.read()
    
        return mensaje
    print(leer_doctxt())