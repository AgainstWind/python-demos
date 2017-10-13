import csv
import matplotlib.pyplot as plt

def loadData(fileName):
    csv_reader = csv.reader(open(fileName))
    # print type(csv_reader)
    a_x_values = []
    a_y_values = []
    b_x_values = []
    b_y_values = []
    rv = {}

    for row in csv_reader:
        # print type(row)
        print row
        try:
            a_x_values.append(float(row[1]))
            a_y_values.append(float(row[2]))
            b_x_values.append(float(row[3]))
            b_y_values.append(float(row[4]))
        except ValueError,e:
            print e
            continue
        # for a in row:
        #     print a
    return (a_x_values,a_y_values,b_x_values,b_y_values)


data_array = loadData('iris.csv')


def draw_pic():
    # plt.plot(data_array[0],data_array[1],'',label='Sepal')
    # plt.plot(data_array[2],data_array[3],'',label='Petal')
    plt.scatter(data_array[0],data_array[1],color='green',marker='*',label='Sepal',alpha=0.6)
    plt.scatter(data_array[2],data_array[3],color='red',marker='x',label='Petal',alpha=0.7)
    plt.grid(True)
    plt.show()

draw_pic()


