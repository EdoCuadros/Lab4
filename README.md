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

Se corroboran los parámetros graficando el robot con ayuda del Toolbox de Peter Corke en MATLAB.

### Posición HOME
![image](https://github.com/EdoCuadros/Lab4/assets/69473568/5912647e-29b2-45ff-b568-0651ec10a180)

### Posición 1
![image](https://github.com/EdoCuadros/Lab4/assets/69473568/8e9323a1-a5aa-4202-ad9d-c95a8d7696b9)

### Posición 2
![image](https://github.com/EdoCuadros/Lab4/assets/69473568/baaa5767-c5c7-4de9-9516-a683a8006dbd)




## Script de MATLAB

Se importan librerías y se inicia la conexión con ROS.
