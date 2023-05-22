import pandas

with open('fraudtrain.csv', newline='') as csvfile:
        f = pandas.read_csv(csvfile)

print(f)

        