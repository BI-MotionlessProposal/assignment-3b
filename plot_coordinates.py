import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot
import pylab
import pandas as pd

def plot():
    df = pd.read_csv('boliga_all_detailed_lon_lat.csv')

    x = df['longitude']
    y = df['latitude']

    matplotlib.pyplot.scatter(x, y)

    matplotlib.pyplot.show()
    matplotlib.pyplot.savefig('foo.png')

if __name__ == '__main__':
    plot()
