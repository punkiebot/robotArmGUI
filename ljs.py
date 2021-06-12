import time
import json
import serial


# para escanear puertos en python -m serial.tools.list_ports

dev = serial.Serial("COM7", 115200)


print("programa para controlar rutinas y movimientos de un brazo robotico controlado por el Raspbery Pi Pico")
print("intefaz entre PC y Raspberry Pico")


def ejercutarRutina(letra, print1):
    cad = letra
    dev.write(cad.encode("ascii"))
    print(print1)

    lecturaPico = dev.read(2).decode("ascii")
    time.sleep(0.2)
    print("lectura de RP es: ", lecturaPico)


def rutinaMoverMotor(letra, motor):
    angulo = data["mover"][motor]
    print("mover: ", motor, " en grados: ", angulo)
    cad = letra
    dev.write(cad.encode("ascii"))
    # time.sleep(0.1)

    # se debe enviar un string de 3 caracteres para que
    # la pico lo pueda leer bien, por ejemplo "000", "060", "005"
    angulo = str(angulo)

    if (len(angulo) == 2):
        angulo = "0" + angulo
    elif (len(angulo) == 1):
        angulo = "00" + angulo

    angulo = angulo+"\n"

    # envia angulo
    dev.write(angulo.encode("ascii"))

    lecturaPico = dev.read(5).decode("ascii")
    time.sleep(0.2)
    print("lectura de RP es: ", lecturaPico)


def limpiarRutinas():
    f = open("documento.json")
    data = json.load(f)
    data["necesitaRutina"] = 0
    s = json.dumps(data)
    f = open("documento.json", "w")
    f.write(s)
    f.close()


def limpiarMover():
    f = open("documento.json")
    data = json.load(f)
    data["necesitaMover"] = 0
    s = json.dumps(data)
    f = open("documento.json", "w")
    f.write(s)
    f.close()


while True:
    f = open("documento.json")
    data = json.load(f)
    time.sleep(0.1)

    if (data["necesitaRutina"] == 1):
        print("necesita ejectuar rutina")

        if(data["rutinas"] == "rut1"):
            ejercutarRutina("a", "rut1")
            # cuando retorna de ejectuar la rutina pone en cero necesitaRutina
            limpiarRutinas()

        elif(data["rutinas"] == "rut2"):
            ejercutarRutina("b", "rut2")
            limpiarRutinas()

        elif(data["rutinas"] == "rut3"):
            ejercutarRutina("c", "rut3")
            limpiarRutinas()

        elif(data["rutinas"] == "rut4"):
            ejercutarRutina("d", "rut4")
            limpiarRutinas()

        elif(data["rutinas"] == "rut5"):
            ejercutarRutina("e", "rut5")
            limpiarRutinas()

        elif(data["rutinas"] == "rut5"):
            ejercutarRutina("e", "rut5")
            limpiarRutinas()

        elif(data["rutinas"] == "rut6"):
            ejercutarRutina("f", "rut6")
            limpiarRutinas()

        elif(data["rutinas"] == "rutDef"):
            ejercutarRutina("g", "rutDef")
            limpiarRutinas()

        elif(data["rutinas"] == "rutAll"):
            ejercutarRutina("h", "rutAll")
            limpiarRutinas()
        # fin de rutinas

    elif (data["necesitaMover"] == 1):
        print("necesita mover")
        # funcionanes para mover servos con angulo como parametro
        if (data["queMotor"] == "mov1"):
            rutinaMoverMotor("i", "mov1")
            # cuando retornar de mover servo necesitaMover lo pone en cero
            limpiarMover()

        elif (data["queMotor"] == "mov2"):
            rutinaMoverMotor("j", "mov2")
            limpiarMover()

        elif (data["queMotor"] == "mov3"):
            rutinaMoverMotor("k", "mov3")
            limpiarMover()

        elif (data["queMotor"] == "mov4"):
            rutinaMoverMotor("l", "mov4")
            limpiarMover()

        elif (data["queMotor"] == "mov5"):
            rutinaMoverMotor("m", "mov5")
            limpiarMover()

        elif (data["queMotor"] == "mov6"):
            rutinaMoverMotor("n", "mov6")
            limpiarMover()

        else:
            print("Motor a mover no existe")

    else:

        print(".")
        cad = "x"
        dev.write(cad.encode("ascii"))


"""
Tabla de equivalencias
a  --->  rutm1()
b  --->  rutm2()
c  --->  rutm3()
d  --->  rutm4()
e  --->  rutm5()
f  --->  rutm6()
g  --->  defValues()
h  --->  runAll()

i  --->  mm1()
j  --->  mm2()
k  --->  mm3()
l  --->  mm4()
m  --->  mm5()
n  --->  mm6()

"""
