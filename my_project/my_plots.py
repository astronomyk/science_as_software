import matplotlib.pyplot as plt
import numpy as np

from my_project import reusable_functions as rf


x, y = rf.make_dataset(1000)
plt.plot(x, y, ".")
plt.show()
