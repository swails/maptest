#!/usr/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import pandas as pd

# Load all cities that have populations
df = pd.read_csv('cities_with_pops.csv', header=0, engine='python', index_col=0)

# Create our map
citymap = Basemap(projection='merc', lat_0
