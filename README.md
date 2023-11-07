# Laboratorio 4 de Robótica. Cinemática Directa - Phantom X - ROS
Integrantes:

***Eduardo Cuadros Montealegre***

***Oscar Javier Restrepo***


## Introducción

## Objetivos
- Crear todos los Joint Controllers con ROS para manipular servomotores Dynamixel AX-12 del robot Phantom
X Pincher.
- Manipular los tópicos de estado y comando para todos los Joint Controllers del robot Phantom X Pincher.
- Manipular los servicios para todos los Joint Controllers del robot Phantom X Pincher.
- Conectar el robot Phantom X Pincher con MATLAB o Python usando ROS.

### Ejercicio en el laboratorio
- Cada grupo tendrá a cargo un robot Phantom X Pincher. Siga las indicaciones del laboratorista y profesores
para hacer buen uso de los robots del laboratorio.

### Mediciones:
- Establezca las longitudes de eslabón para cada articulación del robot Phantom X Pincher, para este proceso
apóyese en un CALIBRADOR. Recuerde que la longitud de eslabón es la mı́nima distancia que conecta dos
juntas consecutivas. Genere un diagrama como el presentado en la figura 2 con los datos medidos.
- Es posible que su grupo deba trabajar con una versión nueva del Phantom X Pincher, la cual varı́a ligeralemente su geometrı́a. Asegúrese de representar adecuadamente este cambio en el diagrama de longitudes del robot.

![image](https://github.com/EdoCuadros/Lab4/blob/main/images/DH1.png)

## Conexión ROS con Dynamixel
Con base en la documentación de los motores Dynamixel en ROS, cree un script que publique a los tópicos
y llame a los servicios correspondientes para realizar el movimiento de cada una de las articulaciones del
manipulador (waist, shoulder, elbow, wrist). La lógica del script puede ser la siguiente:
- Se debe realizar el movimiento entre dos posiciones angulares caracterı́sticas: una de home y otra objetivo.
- El movimiento de las articulaciones debe realizarse de forma secuencial iniciando por la articulacion de
la base, agregue una pequeña espera entre cada movimiento para facilitar la grabacion de videos de
demostración.

```
#Posición 1
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 1, position: 0}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 2, position: 3000}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 3, position: 1233}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 4, position: 2086}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 5, position: 1707}"

#Posición 2
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 1, position: 200}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 2, position: 2800}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 3, position: 1380}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 4, position: 1700}"
rostopic pub -1 /set_position dynamixel_sdk_examples/SetPosition "{id: 5, position: 2483}"

```
[![Mirar el video](https://github.com/EdoCuadros/Lab4/blob/main/images/ros1.png)](https://youtu.be/--UTZC1VN2I)
### Toolbox:
Utilice el comando SerialLink para crear el robot con los parámetros de su tabla DH.
Obtenga la matriz de transformación homogénea desde la base hasta el efector final, la idea es realizar el
análisis en el TCP, este punto puede ser elegido en la mitad de la pinza (Cinemática directa del robot).
Grafique varias posiciones del robot incluyendo la de HOME utilizando las funciones del toolbox (Seria-
lLink.plot).
Importante: Para la correcta orientación del marco de coordenadas del efector final, revise la propiedad .tool
del robot creado mediante SerialLink.

Comenzando con la práctica se miden las lóngitudes del _Phantom X Pincher_ y posteriormente se realiza la cinemática directa con la tabla Denavit-Hatenberg.

| Joint | Theta | d | a | alpha |
| -------- | -------- | -------- | -------- | -------- |
| 1  | q1     | 0    | 0 | pi/2 |
| 2  | q2     | 0    | 106.3 | 0 |
| 3  | q3     | 0    | 99.2 | 0 
| 4  | q4     | 0    | 83.2 | 0 |

Se corroboran los parámetros graficando el robot con ayuda del Toolbox de Peter Corke en MATLAB para las distintas posiciones requeridas.

### Matlab o Python + ROS + Toolbox:
- Cree un código en Matlab que env´ıe la posición en ángulos deseada a cada articulación del robot utilizando las herramientas de ROS + Dynamixel, el programa deberá graficar la configuración del robot usando las herramientas del toolbox, esta configuración deberá coincidir con la obtenida en el robot real.
- Pruebe las siguientes poses generadas a partir de los valores articulares de q1, q2, q3, q4, q5 (Recuerde que los valores de configuración se toman respecto a home, para el cual todos los valores articulares son cero):
1. 0, 0, 0, 0, 0.
2. 25, 25, 20, -20, 0.
3. -35,35, -30, 30, 0.
4. 85, -20, 55, 25, 0.
5. 80, -35, 55, -45, 0.
Cuide que las poses no interfieran con los limites articulares o algún objeto en el espacio de trabajo. Puede
ajustar el valor de los ´angulos de las poses para esquivar algún obstáculo

### Posición 1 : [0,0,0,0,0]
![Pos1](https://github.com/EdoCuadros/Lab4/assets/69473568/af1eb7d9-7ec5-4e08-8a30-e20c4c12faee)

### Posición 2 : [25,25,20,-20,0]
![Pos2](https://github.com/EdoCuadros/Lab4/assets/69473568/827ea91f-dc1e-46da-b074-aa0c2a0c5f55)

### Posición 3 : [-35,35,-30,30,0]
![Pos3](https://github.com/EdoCuadros/Lab4/assets/69473568/b532adfb-e141-4b63-b66a-bd9abf3b0680)

### Posición 4 : [85,-20,55,25,0]
![Pos4](https://github.com/EdoCuadros/Lab4/assets/69473568/e099b85a-544e-4704-ac2e-6695442da6a0)

### Posición 5 : [80,-35,55,-45,0]
![Pos5](https://github.com/EdoCuadros/Lab4/assets/69473568/79b82139-c8c4-43bc-8d63-7a876d5ba62f)

## Script de Python

Primero se importan las librerías para la conexión con ROS.

```
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
```
Luego se define la función para mandar las coordenadas al robot. Inicialmente se instancia el objeto para publicar y se inicia el nodo en la red.

```
def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
 ```
Posteriormente en un bucle se mandan las trayectorias. El bucle tiene como condición de parada la desconexión del nodo. 
 ```
while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5",]
        point = JointTrajectoryPoint()
        point.positions = [0, 0, 0, 0, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)
 ```
En la linea de _positions_ se escogen las ubicaciones de cada articulación. Exceptuando la linea del _while_, el bloque de código se repite para cada posición del robot, es decir, se tendrán 5 bloques iguales con diferentes ángulos en cada articulación.

Finalmente se cierra el bucle y se inicia el método main, donde se hace el llamado al método creado anteriormente. Dentro de dicho método, se utiliza el bloque _try / except_ para encapsular algún error relacionado con la conexión con ROS.

 ```
if __name__ == '__main__':
    try:
        joint_publisher()
    except rospy.ROSInterruptException:
        pass
 ```
### Video del movimiento del robot en las 5 posiciones
[![Mirar el video](https://github.com/EdoCuadros/Lab4/blob/main/images/ros2.png)](https://youtu.be/rAujGf27mbs)

Cree una interfaz de usuario, o HMI, donde se muestre al usuario lo siguiente:
1. Nombres, logos y datos de los integrantes del grupo.
2. Imagen perspectiva de la posici´on actual del manipulador con la ultima posición enviada.
3. Opción para seleccionar 1 de las 5 poses y enviarlas al manipulador.
4. Valores de los valores articulares reales de cada motor.
5. Imagen perspectiva de la posición actual del manipulador con los valores articulares.
 ```
print("Integrante 1: Oscar Javier Restrepo")
print("Integrante 2: Eduardo Cuadros Montealegre")
A=input("Digite la posición deseada 1, 2, 3, 4 o 5: ")
posicion_1=[0,0,0,0,0]
posicion_2=[25,25,20,-20,0]
posicion_3=[-35,35,-30,30,0]
posicion_4=[85,-20,55,25,0]
posicion_5=[80,-35,55,-45,0]
match A:
    case 1: posicionar(posicion_1)
    case 2: posicionar(posicion_2)
    case 3: posicionar(posicion_3)
    case 4: posicionar(posicion_4)
    case 5: posicionar(posicion_5)


def posicionar(pos):
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5",]
    point = JointTrajectoryPoint()
    point.positions = pos    
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)
 ```
