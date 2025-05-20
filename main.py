
# En este codigo se va ha hacer un POO de Hermanos con dispoinibilidad. Un CRUD y un menu. este es el menu

from Hermano import Hermano

from os import system as cmd

import json


def main():

    # La funcion main se encarga de administrar en un bucle la pantalla inicial llevando a funciones segun la eleccion de el usuario

    while True:

        cmd("cls")

        print(
        """
        +-----------------------+
        +     Disponibilidad   -+
        +------------+----------+
        +   CREAR    |     1    +
        +   MENSAJE  |     2    +
        +   LISTAR   |     3    +
        +   EDITAR   |     4    +
        +   GITHUB   |     5    +
        +   FALSE M  |     6    + 
        +   SALIR    |     7    +
        +------------+----------+
        """)

        
       

        try:
            
            x = int(input(": "))
            match x:

                case 1: Crear()
                case 2: Elegir()
                case 3: Listar()
                case 4: Editar()
                case 5: Github()
                case 6: MensajeFalse()
                case 7: break

        except ValueError:
            print("Cuidadito!")

        input() #Se agrega para que cada vez al volver no se borre la pagina y espere una entrada 


def MensajeFalse():

    # Actualiza la base Json y hace que aparezca que no se le ha mandado el mensaje a todos los hermanos

    if input("Seguro? (s/n)").lower() == "s":

        datos = CargarInfo()

        for i in datos:

            i["Mensaje"] = False
        
        Actualizar(datos)

        print("Borrado!")

           




def Github():

    #Esta funcion se desarollo para que funcione en mi computador (maxi o candaku). Por lo que si se descarga habra que cambiar los directorios

    cmd("Cls")

    print("1- Guardar info")
    print("2- Cargar info")

    a = int(input(": "))

    match a:

        case 1:

            #Guarda los datos en una carpeta que está conectada con github desktop. Estos datos son los mismos que están en personas.json un copy paste
            print("Guardando datos en el repositiorio Local de github")

            info = CargarInfo()
            
            with open("C:/Users/candaku/Documents/GitHub/Disponibilidad/Github_Disponibilidad.json", "w") as archivo:
                json.dump(info, archivo, indent=4)
            
            print("Listo!") #En caso de que quieras implementar esto en otro PC. Tienes que cambiar el enlace y conectar ese repositorio con github

            print("Recuerda abrir github desktop para confirmar los cambios")

        case 2:

            #esta es una inversa de la opción anterior. Toma el archivo Json que está conectado con github y actualiza el personas.json.
            # Idealmente para cuando haces cambios que son fuera de este entorno o en otro PC y quieres actualizar la base

            print("Recuerda Abrir github y actualizar el archivo")

            input("Cuando lo hagas preciona enter...")


            with open("C:/Users/candaku/Documents/GitHub/Disponibilidad/Github_Disponibilidad.json", "r") as archivo:
                info = json.load(archivo)

            Actualizar(info)


            

def Editar():

    #Esta funcion es para editar a algun hermano. Tanto sus disponibilidades como el comentario que tiene y se mando el mensaje o no
    # OJO. Todo va a cambiar de forma 'imaginaria' hasta que se ponga actualizar. Si no no habrán cambios reales

    nombre = input("Nombre: ").lower()

    info = CargarInfo()

    for i in info:

        if i['Nombre'] == nombre:


            while True:
                cmd("cls")
                print(f"""
                      {i["Nombre"]}   
                    +------------------+
                    +   EDITANDO A     +
                    +----------+-------+
                    +  Tardes  |  1    +
                    +  Mañanas |  2    +
                    +  Coment. |  3    +
                    +  Actuali.|  4    +
                    +  Leer    |  5    +
                    +  Mens.   |  6    +
                    +  Salir   |  7    +
                    +----------+-------+                                    
                    """)
                
                try:
                    x = int(input(": "))

                    match x:

                        case 1:
                            
                            i["Tarde"] = SepararDias(input("Dias en las tardes: ").lower())
                            print("Dias en las tardes actualizado!")
                        
                        case 2: 

                            i["Manana"] = SepararDias(input("Dias en las mañanas: ").lower())
                            print("Dias en las mañanas actualizado!")
                        
                        case 3:

                            i["Comentario"] = input("Comentario: ")
                            print("Comentario actualizado!")

                        case 4:
                            Actualizar(info)

                        case 5:
                            LeerHermano(Hermano.from_dict(i))

                        case 6:
                            if input("Se mando? s/n: ").lower() == "s":
                                print("Si se mando. Guardado")

                                i["Mensaje"] = True

                            else:

                                print("No se mando. Guardado")

                                i["Mensaje"] = False

                            Actualizar(info)
                        case 7:
                            break
                except ValueError:
                    print("Cuidado con los valores")
                input("")


def LeerHermano(persona:Hermano):

    #Devuelve las caracteristicas del hermano

    cmd("cls")
    print(f""" 
          Hermano {persona.rNombre()}
          Mañana: {", ".join(persona.rMañana())}
          Tarde:  {", ".join(persona.rTarde())}
          Comentario: {persona.rComentario()}
          Mandado: {"si" if persona.rMensaje() else "no"}
          """)


def Elegir():

    # Busca a un hermano y lo manda a la funcion mensaje

    nombre = input("A quien buscas?: ").lower()

    info = CargarInfo()

    c = 0

    for i in info:


        if i["Nombre"] == nombre:
            print("Encontrado!")
            Mensaje(Hermano.from_dict(i))



            break

        c += 1

    print("No encontrado")
        


def CargarInfo():

    # Carga info del Json y la devuelve

    with open("personas.json", "r") as archivo:
        info = json.load(archivo)

    return info


def Listar():

    # Carga info de los hermanos y los lista

    for i in CargarInfo():
        print("+---------------------------------------------------+")
        print(f" {i['Nombre']}  mensaje: {i['Mensaje']}")
    print("+---------------------------------------------------+")    

def SepararDias(Dias):

    #Separa los dias por coma. Y retorna una lista. Tienen que ser sin asento y minusculas

    lista =[]

    if Dias == "todos":
        lista = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

    for i in Dias.split(","):
        
        
        lista.append(i.strip())

    
    return lista



def Crear():

    #Crea al hermano. Para ello pide el nombre y sus disponibilidades mas algun comentario

    nombre  = input("Nombre del hermano: ").lower()

    Morning = SepararDias(input("Disponibilidad de dia: ").lower())

    Tarde = SepararDias(input("Disponibilidad de tarde: ").lower())


    Comentarios= input("Algun comentario: ").lower()




    nuevo = Hermano(nombre, Morning, Tarde, False, Comentarios) #Se crea el objeto nuevo con la clase Hermano. Se pone false al mensaje porque se asume que no se ha mandado

    Guardar(nuevo)


def Guardar(Guardar:Hermano):

    #Carga la info del Json. En base a el objeto clase hermano que se le pasa toma la info y la añade con un append y lo escribe. Ademas crea un backup en caso de 

    info = CargarInfo()
    
    with open("backup.json", "w") as archivo:
      json.dump(info, archivo, indent=4)

    info.append(Guardar.to_dict())

    with open("personas.json", "w") as archivo: 
      json.dump(info, archivo, indent=4)

def Actualizar(info):

    #Al entregarle un json lo escribe en personas json. Solamente se utiliza al agregar cosas

    with open("personas.json", "w") as archivo: 
      json.dump(info, archivo, indent=4)

def Mensaje(Buscar:Hermano):

    #Verifica si el mensaje se ha mandado con aterioridad. Si es asi avisa. Despues manda un mensaje personalizado diciendo la disponibilidad del hermano. 

    if Buscar.rMensaje() == True:

        print("Este hermano ya fue revisado. OJITOO EEEE")
        input()

    else:

        info = CargarInfo()

        for i in info:

            if i["Nombre"] == Buscar.rNombre():

                i["Mensaje"] = True

                Actualizar(info)



    cmd("cls")


    print(f"""
    Hola, Estamos confirmando su disponibilidad para este mes. 
    Usted nos dijo que {("podia los " + ", ".join(Buscar.rMañana())) if len(str(Buscar.rMañana()[0])) > 0 else "no podia"} en las Mañanas. Y que {("podia los " + ", ".join(Buscar.rTarde())) if len(Buscar.rTarde()[0]) > 0 else "no podia"} en las tardes. 
    {f"Nos agrego el comentario de: {Buscar.rComentario()} " if len(Buscar.rComentario()) != 0 else " "}.
    Confirmar si mantendrá esta disponibilidad o la cambiará. *Si no responde a este mensaje vamos a asumir que la mantiene*""")
    
    input()

if __name__ == "__main__":
    main()


#Para la correcta funcion de el codigo y sus funciones poner el main al final asi se recorren todas las funciones y estan disponibles