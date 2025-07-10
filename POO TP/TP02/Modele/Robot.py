import random
import string
from enum import Enum

class Orientation(Enum):
    NORD = "NORD"
    EST = "EST"
    SUD = "SUD"
    OUEST = "OUEST"

class StatusText(Enum):
    STATUS_1 = "EN SERVICE"
    STATUS_2 = "HORS SERVICE"
    STATUS_3 = "EN REPARATION"

class Robot:
    cpt = 0

    def __init__(self, robot_type = "Générique", statut = StatusText.STATUS_1, orientation=Orientation.NORD ):
        Robot.cpt += 1
        self._robot_type = robot_type if len(robot_type) > 2 else "Générique"
        self._numero_serie = self.generate_numero_serie()
        self._orientation = orientation if isinstance(orientation, Orientation) else Orientation.NORD
        self.statut = statut


    @property
    def robot_type(self):
        return self._robot_type

    @robot_type.setter
    def robot_type(self, robot_type_string):
        self._robot_type = robot_type_string if len(robot_type_string) > 2 else "Générique"

    @property
    def numero_serie(self):
        return self._numero_serie

    @property
    def orientation(self):
        return self._orientation
    @orientation.setter
    def orientation(self, value):
        self._orientation = value

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        if status == 1 | 2 | 3 :
            self.status = status
        else: raise Exception("Nombre incorrect")

    def generate_numero_serie(self):
        lettres = ''.join(random.choices(string.ascii_uppercase, k=2))
        nombre = random.randint(0, 999999999)
        return f"{lettres}{nombre:010}"

    def __str__(self):
        return (f"Robot {self.numero_serie} - {self.robot_type}\n"
                f"Statut: {self.statut.value}\n"
                f"Orientation: {self.orientation.value}")


    def tourner(self, direction):
        if direction not in (1, -1):
            raise ValueError("Direction invalide. Utilisez 1 (droite) ou -1 (gauche).")

        orientations = [Orientation.NORD, Orientation.EST, Orientation.SUD, Orientation.OUEST]
        index = orientations.index(self.orientation)
        self.orientation = orientations[(index + direction) % 4]





r1 = Robot()
r2 = Robot("Mécanique")
r3 = Robot("Electrique")

print("------------------------------------")
print("------- TP : PREMIERE PARTIE -------")
print("------------------------------------")

print("-------- CREATION DE ROBOTS --------")
print(r1)
print('_'*36)
print(r2)
print('_'*36)
print(r3)
print('_'*36)
print("Nombre de robots créés au total : ", Robot.cpt)
print("------------------------------------")

print("--------- TEST SETTER TYPE ---------")
r4 = Robot("T")  # Doit afficher un message d'erreur
print(r4)  # Doit afficher un type Générique
print('_'*36)
r2.robot_type = "K"  # Doit afficher un message d'erreur
print(r2)  # Le type ne doit pas avoir été modifié
print("------------------------------------")

print("--------- TEST STATUT ---------")
r2.statut = 2
print(r2)
print('_'*36)
r2.statut = 5  # Doit afficher un message d'erreur
print(r2)  # Le statut ne doit pas avoir été modifié
print("------------------------------------")

print("--------- TEST TOURNER ---------")
r3.tourner(1)
print(r3)
print('_'*36)
r3.tourner(-1)
print(r3)
print('_'*36)
r3.tourner(12)  # Doit afficher un message d'erreur
print(r3)  # Le robot ne doit pas avoir tourné
print("------------------------------------")