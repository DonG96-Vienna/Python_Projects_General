from random import choice

class RandomWalk:
    """Random Walks erzeugen"""

    def __init__(self, num_points=5000):
        """Wie viele Schritte soll man gehen"""
        self.num_points = num_points

        # Immer bei (0,0) starten
        self.x_values =[0]
        self.y_values = [0]

    def fill_walk(self):
        """Zufällige Schritte berechnen"""

        # Gehen bis man die festgesetzte Grenze erreicht
        while len(self.x_values) < self.num_points:
            # Richtung und Anzahl an Schritte bestimmen
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Wenn man nirgends hingeht, dann überspringen
            if x_step == 0 and y == 0:
                continue

            # neue Positionen in Liste einfügen
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)