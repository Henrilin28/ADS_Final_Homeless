import sys
import urllib
import pandas as pd
import numpy as np


def read_date (filelist):
    file_link = []
    with open(filelist,"r") as f:
        
        for idx, line in enumerate(f):
            if idx !=0:
                 a = line.strip("\n").split(" ")
                 file_link.append(a)

    return file_link
def check_data (filename,link):

    df = pd.read_csv(link)
    print ("{} download complete".format(filename))
    with open(filename+"metadata.txt","w") as f:
        for column in df.columns.values:
            f.write(column)
            f.write("\n")
            if df[column].dtype == "object" : 
                f.write("unique_value: \n")   
                f.write("/".join(str(val) for val in df[column].unique()))
                f.write("\n")
            else:
                f.write("    numerical")
                f.write("\n")
        f.write(str(df.shape))
    print ("{} metadata complete".format(filename))
if __name__ == '__main__':

    index = 0 
    file_link = read_date (sys.argv[1])

    while(index<len(file_link)):
        temp = file_link[index]
        check_data (temp[0],temp[1])

        index +=1

