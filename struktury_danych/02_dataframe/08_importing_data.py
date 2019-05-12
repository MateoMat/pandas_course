# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


# importing dataset
df = pd.read_csv('./data/aapl_us_d.csv', index_col=0)

# %% useful method
df.info()
df.describe()
