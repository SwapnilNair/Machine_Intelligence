'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random
from math import log2


def fun(x):
    if(x == 'yes' or x == 'true' or x == 'True' or x=='Yes'):
        return 1
    else:
        return 0


def entropycalc(x, y):
    n = x+y
    if x==0 or y==0:
        return 0
    return -((x/n)*log2(x/n) + (y/n)*log2(y/n))


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float


def get_entropy_of_dataset(df):
    k = list(map(fun, list(df[df.columns[-1]])))
    length = len(k)
    ok = k.count(1)
    notok = length - ok
    entropy = entropycalc(ok,notok)
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float


def get_avg_info_of_attribute(df, attribute):
    k = df[ [attribute,df.columns[-1] ] ]
    ks = list(set(df[attribute]))
    ks2 = list(df[attribute])
    length = len(ks2)
    entropies = []
    for x in ks:
        frac = ks2.count(x) / length
        entropies.append( get_entropy_of_dataset(k[k[attribute] == x] ) *frac ) 
    avg_info = sum(entropies) 
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float


def get_information_gain(df, attribute):
    return 1
    total_ent = get_entropy_of_dataset(df)
    col_ent = get_avg_info_of_attribute(df, attribute)
    information_gain = total_ent - col_ent
    return information_gain


#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected
    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    colgains = {}
    for x in df.columns[:-1]:
        colgains[x] = get_information_gain(df,x)
    ans = (colgains,max(colgains,key = lambda x: colgains[x]))
    return ans
    
    
def get_avg_info_of_attribute(df, attribute):
    
    vc = df[attribute].value_counts(normalize=True, sort=False)
    avg_info = -(vc * np.log(vc) ).sum()
    print(avg_info)
    return avg_info
