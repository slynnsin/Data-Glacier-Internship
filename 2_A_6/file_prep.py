
# import libraries
import pandas as pd

def file_name():
    name = input("File name: ")
    return name

name = file_name()

if name.endswith(('.csv')):
    file_type = 'csv'
