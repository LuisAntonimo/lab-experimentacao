from datetime import datetime
import matplotlib.pyplot as plot
import numpy


def get_age(time):
  date_now = datetime.now()
  creation_date = datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")
  age = date_now - creation_date
  return age.days



def make(arr):
  median = numpy.median(arr)

  plot.boxplot(arr, vert=False, whis=[25, 75])
  plot.title('Idade dos Repositórios')
  plot.xlabel('Idade (em dias)')

  plot.scatter([median], [1], color='red', marker='o', label='Mediana')

  plot.yticks([])
  plot.grid(True)
  plot.legend()
  plot.savefig('rq01.png')