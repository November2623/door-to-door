import csv
from time import time
from math import sqrt, pow
class Graph:
    def __init__(self):
        self.list_node = []
        # self.list_distance = []
        self.output = []

    def define(self):
        start = time()
        with open('usa_cities.csv') as csvfile:
            contents = csv.reader(csvfile)
            for city in contents:
                self.list_node.append(Node(city[0], city[1], city[2]))
        end = time()
        print(end - start)


    def distance(self,y1, x1, y0, x0):
        dis = round(sqrt(pow((y1-y0),2) + pow((x1-x0),2)),4)
        return dis

    # def get_distance(self):
    #     for i in self.list_node:
    #         dis_node = []
    #         for j in self.list_node:
    #             dis = self.distance(i.latitude, i.longitude, j.latitude, i.longitude)
    #             dis_node.append(dis)
    #         self.list_distance.append(dis_node)
    #     print(self.list_distance)


    def tsp(self):
        self.output.append(self.list_node[0].city_name)
        self.get_min(self.list_node[0],self.list_node[1:])
        print(self.output)


    def get_min(self, start_node, other_node):
        temp = True
        start1 = time()
        list_node = other_node
        start_node = start_node
        end2 = time()
        print(end2 - start1)
        count = 0
        while temp:
            dis_node = []
            self.process()
            temp = start_node.city_name
            list_node = other_node
            if len(list_node) == 0:
                self.output.append(self.list_node[0].city_name)
                temp = False
            else:
                for i in list_node:
                    dis = self.distance(start_node.latitude, start_node.longitude, i.latitude, i.longitude)
                    dis_node.append(dis)
                value = min(dis_node)
                index = dis_node.index(value)
                city = list_node[index]
                list_node.remove(list_node[index])
                self.output.append(city.city_name)
                start_node = city

    def process(self):
        print("Processing: " + str(round((len(self.output)/len(self.list_node))*100,2)) + "%")

class Node:
    def __init__(self, city_name, latitude, longitude):
        self.city_name = city_name
        self.latitude = float(latitude)
        self.longitude = float(longitude)

if __name__ == '__main__':
    start = time()
    a = Graph()
    a.define()
    a.tsp()
    end = time ()
    print(end - start)
