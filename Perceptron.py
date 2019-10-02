from Entry import Entry
from Threshold import Threshold


class Perceptron:
    __trainingValues = ([0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1])

    __entry1 = Entry()
    __entry2 = Entry()
    __threshold = Threshold()
    __iterations = 0

    def __init__(self):
        self.__learn()

    def __learn(self):
        cases = 0
        while cases != 4:

            cases = 0
            for case in self.__trainingValues:
                self.__entry1.set_value(case[0])
                self.__entry2.set_value(case[1])
                t_output = case[2]

                formula = self.__formula(self.__entry1.get_value(), self.__entry2.get_value())
                output = self.__activate(formula)

                if t_output == output:
                    cases += 1
                else:
                    self.__change_weights()

            self.__iterations += 1



    def __formula(self, value1, value2):
        return (
            float(value1) * self.__entry1.get_weight()
            + float(value2) * self.__entry2.get_weight()
            + float(self.__threshold.get_value()) * self.__threshold.get_weight()
        )

    def __activate(self, x):
        if x < 0:
            return 0
        else:
            return 1

    def __change_weights(self):
        self.__entry1.new_weight()
        self.__entry2.new_weight()
        self.__threshold.new_weight()

    def get_iterations(self):
        return self.__iterations

    def get_output(self, value1, value2):
        formula = self.__formula(value1, value2)
        return self.__activate(formula)
