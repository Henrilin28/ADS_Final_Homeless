import sys
import urllib
import pandas as pd
import numpy as np

def check_data (filename,link):

    df = pd.read_csv(link)

    with open(filename+"metadata.txt","w") as f:
        for column in df.columns.values:
            f.write(column)
            f.write("\n")
    
            if ~np.isreal(df[column]).all() : 
                f.write("unique_value")   
                f.write(",".join(df[column].unique()))
                f.write("\n")
            else:
                f.write("    numerical")
                f.write("\n")
        f.write(str(df.shape))

if __name__ == '__main__':

    check_data(sys.argv[2],sys.argv[1])
