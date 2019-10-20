import matplotlib.pyplot as plt


with open("EA1_TEST[1, 2, 3, 4, 5, 6, 7, 8]/maxvalues.txt", "r") as f:

    for line in f:

        if "Gains" in line:

            values = []
            lines = line.strip("Gains:")

            lines = lines.split(",")
            for value in lines:
                temp = value.strip("[")
                temp = temp.strip("]\n")
                values.append(float(temp))
