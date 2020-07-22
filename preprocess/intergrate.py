import pandas as pd
from collections import defaultdict

# TODO 
# 1. change the data input  directory
# 2. change the data output directory
# Import dataset
df = pd.read_csv('/Users/AkshayKale/Documents/github/nbi-predictive-analysis/decision-tree-dataset.csv')
snow_df = pd.read_csv('/Users/AkshayKale/Documents/github/nbi-predictive-analysis/baseline_category_2_balanced.csv')

print(df.shape, snow_df.shape)

# Initialize dictionarires
structure_precp = defaultdict()
structure_snow = defaultdict()
structure_freeze = defaultdict()
structure_score  = defaultdict()

# Helper function to create dictionary of structure number (Key): snow_value (value) pair
def createMap(srno, cols, dicti):
    for struct_no, value in zip(srno, cols):
        struct_no = struct_no[:-2]
        dicti[struct_no] = value
    return dicti

def createList(str_col, str_map):
    value_list = list()
    for struct in str_col:
        try:
            val = str_map[struct]
        except:
            val = None
        value_list.append(val)
    return value_list


structure_no = snow_df['Structure Number']
precp = snow_df['Avg. Daily Precipitation']
snow = snow_df['No. of Snow Fall']
freeze = snow_df['No. of Freezethaw']
score = snow_df['Baseline Difference Score']

structure_precp = createMap(structure_no, precp, structure_precp)
structure_snow = createMap(structure_no, snow, structure_snow)
structure_freeze = createMap(structure_no, freeze, structure_freeze)
structure_score = createMap(structure_no, score, structure_score)

df['score'] = createList(df['structure number'], structure_score)
df['precipitation'] = createList(df['structure number'], structure_precp)
df['snowfall'] = createList(df['structure number'], structure_snow)
df['freezethaw'] = createList(df['structure number'], structure_freeze)

print(df['structure number'].unique())
print(df['precipitation'].unique())
print(df['snowfall'].unique())
print(df['freezethaw'].unique())

df.to_csv('decision_tree.csv')
