import csv
import copy
import math
from math import sqrt, pow
class Graph:
    def __init__(self):
        self.list_node = []
        self.list_distance = []
        self.name_city = {}

    def define(self):
        with open('vietnam_cities.csv') as csvfile:
            contents = csv.reader(csvfile)
            count = 1
            for city in contents:
                self.list_node.append(Node(city[0],city[1],city[2]))
                self.name_city[count] = city[0]
                count += 1



    def distance(self,y1, x1, y0, x0):
        dis = round(sqrt(pow((y1-y0),2) + pow((x1-x0),2)),4)
        return dis
    # def distance()
    def get_distance(self):
        for i in self.list_node:
            dis_node = []
            for j in self.list_node:
                dis = self.distance(i.latitue, i.longitude, j.latitue, i.longitude)
                dis_node.append(dis)
            self.list_distance.append(dis_node)
        print(self.list_distance)


    def tsp(self):
        number_city = list(self.name_city.keys())
        print(number_city)
        n = len(self.name_city)
        save = {}
        output = []
        for x in range(1, n):
            save[x + 1, ()] = self.list_distance[x][0]
        self.get_min(output, save,number_city[0],tuple(number_city[1:]))


    def get_min(self, output, save,start_node,other_node):
        if (start_node, other_node) in save:
            return save[start_node, other_node]
        values = []
        all_min = []
        for i in other_node:
            set_a = copy.deepcopy(list(other_node))
            set_a.remove(i)
            all_min.append([i, tuple(set_a)])
            result = self.get_min(output,save, i, tuple(set_a))
            print(self.list_distance[start_node - 1][i -1])
            values.append((self.list_distance[start_node][i] + result))
        save[start_node, other_node] = min(values)
        output.append(((start_node, other_node), all_min[values.index(save[start_node, other_node])]))
        return save[start_node, other_node]





class Node:
    def __init__(self, city_name, latitue, longitude):
        self.city_name = city_name
        self.latitue = float(latitue)
        self.longitude = float(longitude)
a = Graph()
a.define()
# a.city()
a.get_distance()
a.tsp()
