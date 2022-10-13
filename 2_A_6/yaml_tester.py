
# import libraries
import logging                      # releasing log messages form python programs
import os                           # provides functions for creating & removing directories, fetching contents, changing and identifying current directory
import subprocess                   #execute / manage subprocesses: logical collection of activities that exists only within its parent process
import yaml                         # writing configuration files
import pandas as pd
import datetime 
import gc                           # optional garbage collector interface: frees / reclaims blocks of memory that are no longer in use
import re                           # regular expression: specifies a set of strings that matches it

# can also do this for json file
# reading YAML file

def read_config_file(filepath):                         # filepath = filename
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)               # if it can read it --> will safe_load
        except yaml.YAMLError as exc:
            logging.error(exc)


def replacer(string, char):
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string

def col_header_val(df,table_config):
    '''
    replace whitespaces in the column
    and standardized column names
    '''
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace('[^\w]','_',regex=True)
    df.columns = list(map(lambda x: x.strip('_'), list(df.columns)))
    df.columns = list(map(lambda x: replacer(x,'_'), list(df.columns)))
    expected_col = list(map(lambda x: x.lower(),  table_config['columns']))
    expected_col.sort()
    df.columns =list(map(lambda x: x.lower(), list(df.columns)))
    df = df.reindex(sorted(df.columns), axis=1)
    if len(df.columns) == len(expected_col) and list(expected_col)  == list(df.columns):
        print("column name and column length validation passed")
        return 1
    else:
        print("column name and column length validation failed")
        mismatched_columns_file = list(set(df.columns).difference(expected_col))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_col).difference(df.columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'df columns: {df.columns}')
        logging.info(f'expected columns: {expected_col}')
        return 0
