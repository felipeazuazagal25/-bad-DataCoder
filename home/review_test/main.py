import pandas as pd
import numpy as np
import openpyxl as opxl
from .rubric import *
from .review import *
from zipfile import ZipFile
import os



def get_results(tests,rubric):
    pre_results = []
    for test in tests:
        if (not os.path.isfile(test)):
            test_file = test_dir + '/' + os.listdir(test_dir)[0]
            pre_results.append(review_file(test_file,rubric))
        
    preg = ['P' + str(i) for i in range(1,len(pre_results[0]))]
    cols = ['Correo'] + preg

    results = pd.DataFrame(data = pre_results,columns = cols)
    return results

