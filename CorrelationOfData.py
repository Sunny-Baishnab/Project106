import csv
import plotly.express as px
import numpy as num

#Correlation of Marks and Prsent Student
with open('Marks&Present.csv') as f:
    reader = csv.DictReader(f)
    fig = px.scatter(reader,x = 'Days Present' , y = 'Marks In Percentage',color = 'Roll No')
    #fig.update_yaxes(categoryorder = 'category ascending')
    fig.show()

def data_frameOfMarks(data_path):
    DaysPresent = []
    Marks = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            DaysPresent.append(float(row['Days Present']))
            Marks.append(float(row['Marks In Percentage']))
    return {'x':DaysPresent,'y':Marks}

def findCorrelation(data_source):
    correlation = num.corrcoef(data_source['x'],data_source['y'])
    print('Correlation between Marks in Percentage and Days Present :- \n'+ str(correlation[0,1]))

def main():
    data_path = 'Marks&Present.csv'
    data_source = data_frameOfMarks(data_path)
    findCorrelation(data_source)

main()

#Correlation of Coffee in ML and Sleep
with open('Coffee&Sleep.csv') as f:
    reader = csv.DictReader(f)
    fig = px.scatter(reader,x = 'Coffee in ml' , y = 'sleep in hours',color = 'week')
    #fig.update_yaxes(categoryorder = 'category ascending')
    fig.show()

def data_frameOfSleep(data_path):
    DaysPresent = []
    Marks = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            DaysPresent.append(float(row['Coffee in ml']))
            Marks.append(float(row['sleep in hours']))
    return {'x':DaysPresent,'y':Marks}

def findCorrelation(data_source):
    correlation = num.corrcoef(data_source['x'],data_source['y'])
    print('Correlation between Sleep in Coffee ml and sleep :- \n'+ str(correlation[0,1]))

def Main():
    data_path = 'Coffee&Sleep.csv'
    data_source = data_frameOfSleep(data_path)
    findCorrelation(data_source)

Main()