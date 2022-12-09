import matplotlib.pyplot as plt

class MyPlot:
    __MyPlot = plt.subplot()

    __points=[]
    __x=[]
    __y=[]

    def makeAxes(self):
        for point in self.__points:
            self.__x.append(point.x)
            self.__y.append(point.y)
    
    def AddPoint(self,point):
        self.__points.append(point)
    
    def makePlot(self):
        self.__MyPlot.axes.plot(self.__x,self.__y,'o')
        plt.show()