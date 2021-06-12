from machine import Pin, UART, PWM
from time import sleep_ms
import math
import time


# codigo para controlar brazo robotico con 6 motores MG 996R
# codigo va en la raspberry pi pico

######## FUNCIONES  ########

# defVales()   ==> vuelve los motores a los valores por defecto

# [90,60,120,150,110,40]  servo1...servo6

# getValues()  ==> hace un print de las lista con en angulo actual de cada servo

# mm1()... mm6()  mover motor 1... mover motor 6

# rutm1() ... rutm6() rutina moto 1... rutina motor 6

# runAll()   ==> corre todas las rutinas

########################


servo1 = PWM(Pin(15))
servo2 = PWM(Pin(16))
servo3 = PWM(Pin(2))
servo4 = PWM(Pin(4))
servo5 = PWM(Pin(6))
servo6 = PWM(Pin(9))

servo1.freq(50)
servo2.freq(50)
servo3.freq(50)
servo4.freq(50)
servo5.freq(50)
servo6.freq(50)


# valores inciales de los servos
InitValues = [90, 60, 120, 150, 110, 40]

# comunicacion por protocolo UART

port = UART(0, 115200)
time.sleep(1)
print("Inicio de RaspPico")


# funcion para mapear
def Map(numero, in_min, in_max, out_min, out_max):
    return int((numero - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def moveSoft(angulo, motor, servo):
    # funcion para evitar movimientos bruscos
    # el angulo, se refiere al alguno deseado
    # el motor es el indice del motor, va de 1 a 6 OJO!!!
    # servo es el objeto servo
    valServo = InitValues[motor-1]

    if(math.fabs(angulo-valServo) > 1 or math.fabs(valServo-angulo) > 1):
        # hay una diferencia mayor a 1 por tanto es necesario mover con cuidado
        if (angulo > valServo):

            for i in range(valServo, angulo+1, 1):
                servo.duty_ns(Map(i, 0, 180, 500000, 2500000))
                sleep_ms(20)
                InitValues[motor-1] = angulo

        elif (angulo < valServo):
            for i in range(valServo, angulo-1, -1):
                servo.duty_ns(Map(i, 0, 180, 500000, 2500000))
                sleep_ms(20)
                InitValues[motor-1] = angulo

    else:
        # solo difiere por 1
        servo.duty_ns(Map(angulo, 0, 180, 500000, 2500000))
        InitValues[motor-1] = angulo
        sleep_ms(20)


def getValues():
    print(InitValues)


def mm1(numero):
    moveSoft(numero, 1, servo1)


def mm2(numero):
    moveSoft(numero, 2, servo2)


def mm3(numero):
    moveSoft(numero, 3, servo3)


def mm4(numero):
    # servo 4 no puede tener angulo menor a 60° !!!
    if (numero < 60):
        numero = 60

    moveSoft(numero, 4, servo4)


def mm5(numero):
    moveSoft(numero, 5, servo5)


def mm6(numero):
    # entre 0 y 60
    # 0 abierto, 60° cerrado
    # servo 6 no puede tener angulo mayor a 60° !!!
    if (numero > 60):
        numero = 60

    moveSoft(numero, 6, servo6)


def defValues():
    moveSoft(90, 1, servo1)
    moveSoft(60, 2, servo2)
    moveSoft(120, 3, servo3)
    moveSoft(150, 4, servo4)
    moveSoft(110, 5, servo5)
    moveSoft(40, 6, servo6)


def rutm1():

    defValues()

    tiempo = 20
    pasos = 2

    moveSoft(0, 1, servo1)

    for i in range(0, 181, pasos):
        servo1.duty_ns(Map(i, 0, 180, 500000, 2500000))
        InitValues[0] = i
        sleep_ms(tiempo)
        getValues()

    for i in range(180, -1, -pasos):
        servo1.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[0] = i
        getValues()


def rutm2():

    tiempo = 40
    pasos = 2

    moveSoft(90, 1, servo1)
    moveSoft(90, 3, servo3)
    moveSoft(80, 4, servo4)

    moveSoft(0, 2, servo2)

    for i in range(0, 181, pasos):
        servo2.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[1] = i
        getValues()
    for i in range(180, -1, -pasos):
        servo2.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[1] = i
        getValues()


def rutm3():

    tiempo = 20
    pasos = 2

    moveSoft(90, 1, servo1)
    moveSoft(70, 2, servo2)
    moveSoft(80, 4, servo4)

    moveSoft(0, 3, servo3)

    for i in range(0, 181, pasos):
        servo3.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[2] = i
        getValues()
    for i in range(180, -1, -pasos):
        servo3.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[2] = i
        getValues()


def rutm4():

    # motor 4 tiene restriccion
    # va entre 60° y 180°

    tiempo = 20
    pasos = 2

    moveSoft(90, 1, servo1)
    moveSoft(70, 2, servo2)
    moveSoft(120, 3, servo3)

    moveSoft(60, 4, servo4)

    for i in range(60, 181, pasos):
        servo4.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[3] = i
        getValues()
    for i in range(180, 59, -pasos):
        servo4.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[3] = i
        getValues()


def rutm5():

    tiempo = 20
    pasos = 2

    moveSoft(90, 1, servo1)
    moveSoft(70, 2, servo2)
    moveSoft(120, 3, servo3)
    moveSoft(120, 4, servo4)

    moveSoft(0, 5, servo5)

    for i in range(0, 181, pasos):
        servo5.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[4] = i
        getValues()
    for i in range(180, -1, -pasos):
        servo5.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[4] = i
        getValues()


def rutm6():

    # la pinza trabaja en un rango de 0 a 60°
    # 0° es  abierta
    # 60° es cerrada

    tiempo = 20
    pasos = 2

    moveSoft(90, 1, servo1)
    moveSoft(70, 2, servo2)
    moveSoft(120, 3, servo3)
    moveSoft(120, 4, servo4)
    moveSoft(90, 5, servo5)

    moveSoft(0, 6, servo6)

    for i in range(0, 61, pasos):
        servo6.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[5] = i
        getValues()
    for i in range(60, -1, -pasos):
        servo6.duty_ns(Map(i, 0, 180, 500000, 2500000))
        sleep_ms(tiempo)
        InitValues[5] = i
        getValues()


def runAll():
    # corre todas las rutinas
    defValues()
    rutm1()
    rutm2()
    rutm3()
    rutm4()
    rutm5()
    rutm6()
    defValues()


# valores iniciales de los servos
servo1.duty_ns(Map(90, 0, 180, 500000, 2500000))
sleep_ms(200)
servo2.duty_ns(Map(60, 0, 180, 500000, 2500000))
sleep_ms(200)
servo3.duty_ns(Map(120, 0, 180, 500000, 2500000))
sleep_ms(200)
servo4.duty_ns(Map(150, 0, 180, 500000, 2500000))
sleep_ms(200)
servo5.duty_ns(Map(110, 0, 180, 500000, 2500000))
sleep_ms(200)
servo6.duty_ns(Map(60, 0, 180, 500000, 2500000))
sleep_ms(200)


# bloque de comunicacion mediante protocolo UART

"""

Tabla de equivalencias
a - - -> rutm1()
b - - -> rutm2()
c - - -> rutm3()
d - - -> rutm4()
e - - -> rutm5()
f - - -> rutm6()
g - - -> defValues()
h - - -> runAll()

i - - -> mm1()
j - - -> mm2()
k - - -> mm3()
l - - -> mm4()
m - - -> mm5()
n - - -> mm6()


"""


while True:

    try:
        time.sleep(0.1)

        if port.any() > 0:
            dato = port.read(1)
            datoPrint = str(dato, "ascii")
            print("Dato que llegó es: ", datoPrint)

            if "a" in dato:
                print("Lectura de dato a")
                rutm1()
                port.write("r1")

            elif "b" in dato:
                print("Lectura de dato b")
                rutm2()
                port.write("r2")

            elif "c" in dato:
                print("Lectura de dato c")
                rutm3()
                port.write("r3")

            elif "d" in dato:
                print("Lectura de dato d")
                rutm4()
                port.write("r4")

            elif "e" in dato:
                print("Lectura de dato e")
                rutm5()
                port.write("r5")

            elif "f" in dato:
                print("Lectura de dato f")
                rutm6()
                port.write("r6")

            elif "g" in dato:
                print("Lectura de dato g")
                defValues()
                port.write("r8")

            elif "h" in dato:
                print("Lectura de dato h")
                runAll()
                port.write("r7")
            # rutinas para mover servos
            elif "i" in dato:
                print("Lectura de dato i")
                # leer angulo a mover
                time.sleep(0.1)
                valEnt = port.readline()
                print("numero leido es: ", str(valEnt, "ascii"))
                angulo = int(str(valEnt, "ascii"))
                mm1(angulo)
                port.write("m1-ok")

            elif "j" in dato:
                print("Lectura de dato j")
                # leer angulo a mover
                time.sleep(0.1)
                valEnt = port.readline()
                print("numero leido es: ", str(valEnt, "ascii"))
                angulo = int(str(valEnt, "ascii"))
                mm2(angulo)
                port.write("m2-ok")

            elif "k" in dato:
                print("Lectura de dato k")
                # leer angulo a mover
                time.sleep(0.1)
                valEnt = port.readline()
                print("numero leido es: ", str(valEnt, "ascii"))
                angulo = int(str(valEnt, "ascii"))
                mm3(angulo)
                port.write("m3-ok")

            elif "l" in dato:
                print("Lectura de dato l")
                # leer angulo a mover
                time.sleep(0.1)
                valEnt = port.readline()
                print("numero leido es: ", str(valEnt, "ascii"))
                angulo = int(str(valEnt, "ascii"))
                mm4(angulo)
                port.write("m4-ok")

            elif "m" in dato:
                print("Lectura de dato m")
                # leer angulo a mover
                time.sleep(0.1)
                valEnt = port.readline()
                print("numero leido es: ", str(valEnt, "ascii"))
                angulo = int(str(valEnt, "ascii"))
                mm5(angulo)
                port.write("m5-ok")

            elif "n" in dato:
                print("Lectura de dato n")
                # leer angulo a mover
                time.sleep(0.1)
                valEnt = port.readline()
                print("numero leido es: ", str(valEnt, "ascii"))
                angulo = int(str(valEnt, "ascii"))
                mm6(angulo)
                port.write("m6-ok")

            else:
                print("dato leido es erroneo")

        else:
            print(".")
    except:
        print("error de lectura... going back")
