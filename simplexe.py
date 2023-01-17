import sys

def display_format_number(number):
    if number == 0:
        return 0
    else:
        return '%.2f' % number

class Simplexe():
    def __init__(self, args):
        self.parameters = args
        self.ressources_result = {
            'oat': -1,
            'wheat': -1,
            'corn': -1,
            'barley': -1,
            'soy': -1,
        }
        self.saved_result = [-1, -1, -1, -1]
        self.matrix = [
            [1, 0, 1, 0, 2, 1, 0, 0, 0, self.parameters['n1']],
            [1, 2, 0, 1, 0, 0, 1, 0, 0, self.parameters['n2']],
            [2, 1, 0, 1, 0, 0, 0, 1, 0, self.parameters['n3']],
            [0, 0, 3, 1, 2, 0, 0, 0, 1, self.parameters['n4']],
            [
                -self.parameters['po'],
                -self.parameters['pw'],
                -self.parameters['pc'],
                -self.parameters['pb'],
                -self.parameters['ps'],
                0, 0, 0, 0, 0
            ]
        ]
        self.pivot = {
            'var_entrante': None,
            'var_sortante': None,
        }

    def calculate_result(self):
        buff = [0, 0, 0, 0, 0]
        for i, value in enumerate(self.saved_result):
            if value != -1:
                buff[value] = self.matrix[i][len(self.matrix[i]) - 1]
        self.ressources_result = dict(zip(self.ressources_result.keys(), buff))

    def save_pivot_result(self):
        self.saved_result[self.pivot['var_sortante']] = self.pivot['var_entrante']

    def print_result(self):
        """Print the final result
        """
        print(f"Resources: {self.parameters['n1']} F1, {self.parameters['n2']} F2, {self.parameters['n3']} F3, {self.parameters['n4']} F4\n")
        print(f"Oat: {display_format_number(self.ressources_result['oat'])} units at ${self.parameters['po']}/unit")
        print(f"Wheat: {display_format_number(self.ressources_result['wheat'])} units at ${self.parameters['pw']}/unit")
        print(f"Corn: {display_format_number(self.ressources_result['corn'])} units at ${self.parameters['pc']}/unit")
        print(f"Barley: {display_format_number(self.ressources_result['barley'])} units at ${self.parameters['pb']}/unit")
        print(f"Soy: {display_format_number(self.ressources_result['soy'])} units at ${self.parameters['ps']}/unit")
        print(f"\nTotal production value: ${'%.2f' % self.matrix[-1][-1]}")

    def set_pivot(self, var_entrante, var_sortante):
        self.pivot = {
            'var_entrante': var_entrante,
            'var_sortante': var_sortante,
        }

    def find_pivot(self):
        if min(self.matrix[-1][0:5]) >= 0:
            return (self.set_pivot(-1, -1))
        var_entrante, var_sortante = self.matrix[-1].index(min(self.matrix[-1][0:5])), -1
        min_value = float('inf')
        for i, value in enumerate(self.matrix[:-1]):
            if self.matrix[i][-1]:
                if self.matrix[i][var_entrante] > 0 and self.matrix[i][-1] / self.matrix[i][var_entrante] < min_value and self.matrix[i][-1] / self.matrix[i][var_entrante] > 0:
                    var_sortante = i
                    min_value = self.matrix[i][-1] / self.matrix[i][var_entrante]
            elif min_value > self.matrix[i][var_entrante] and self.matrix[i][var_entrante] > 0:
                var_sortante = i
                min_value = self.matrix[i][-1] / self.matrix[i][var_entrante]
        self.set_pivot(var_entrante, var_sortante)

    def use_pivot(self):
        pivotPoint = self.matrix[self.pivot['var_sortante']][self.pivot['var_entrante']]
        if pivotPoint == 0:
            return
        for index, value in enumerate(self.matrix[self.pivot['var_sortante']]):
            self.matrix[self.pivot['var_sortante']][index] = value / pivotPoint
        for i in range(len(self.matrix)):
            if i == self.pivot['var_sortante']:
                continue
            buff = self.matrix[i][self.pivot['var_entrante']]
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] -= buff * self.matrix[self.pivot['var_sortante']][j]

    def run(self):
        for _ in range(0, 6):
            self.find_pivot()
            if any(v < 0 for _, v in self.pivot.items()):
                break
            self.use_pivot()
            self.save_pivot_result()
        self.calculate_result()
