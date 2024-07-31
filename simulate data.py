# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:37:03 2024

@author: yg175
"""

import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

sn = np.random.randint(100001, 999999, size=150000)

pn = [''.join(random.choices(string.ascii_uppercase, k=3)) for _ in range(150000)]

name = [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(150000)]

value_lengths = [21] * 120000 + [15] * 15000 + [17] * 7500 + [random.randint(7, 8) for _ in range(7500)]
random.shuffle(value_lengths)
value = [''.join(random.choices(string.ascii_uppercase + string.digits, k=length)) for length in value_lengths]

def generate_createtime():
    days= random.randint(1,31)
    months= random.randint(1,12)
    years = random.randint(2020,2023)
    createtime = f"{years:02}{months:02}{days:02}"
    return createtime    
createtime = [generate_createtime() for _ in range(150000)]

data = {
    'SN': sn,
    'PN': pn,
    'NAME': name,
    'VALUE': value,
    'CREATETIME': createtime
}

df = pd.DataFrame(data)
df.head()
df.to_csv('C:/Users/YG175/Desktop/数据质量-创建数据/simulated_data.csv', index=False)
