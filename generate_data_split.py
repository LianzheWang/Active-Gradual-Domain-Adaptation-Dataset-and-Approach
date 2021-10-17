"""
Make the data split csv files for EVIS datset.

The datset should be organized like:

dataseta_root_name/year/month/
                            category1/ 
                                      img1.jpg img2.jpg img3.jpg ...
                            category2/
                                      img1.jpg img2.jpg img3.jpg ...
                            ...
year range 2009~2020

month range 1~12
"""

import pandas as pd
import os


def make_split(root_dir="EVIS_40", year=2009, month=1):
   
  
    base_dir = os.path.join(root_dir, str(year), str(month))
    
    train_data = {
            'path':[],
            'label':[]
            }
    
    label_mapping = {'Bus':0, 'television':1, 'electronic watch':2,
                    'laptop':3, 'phone':4, 'tablet pc':5,
                    'Taxi':6, 'Car':7, 'Truck':8,
                    'Van':9}
    
    for class_name, label_value in label_mapping.items():
        
        class_dir = os.path.join(base_dir, str(class_name))
        file_list = os.listdir(class_dir)
        
        for name in file_list:
            train_data['path'].append(os.path.join(class_name, name))
            train_data['label'].append(label_value)
    
    train_data = pd.DataFrame(train_data)
    
    # shuffle could be added here.
    
    train_data = train_data.sample(frac=1).reset_index(drop=True)
    train_data.to_csv(os.path.join(base_dir, 'data_split.csv'))

def make_split_by_year(root_dir="EVIS_40", year=2009):
    train_data = {
            'path':[],
            'label':[]
            }
    
    label_mapping = {'Bus':0, 'television':1, 'electronic watch':2,
                    'laptop':3, 'phone':4, 'tablet pc':5,
                    'Taxi':6, 'Car':7, 'Truck':8,
                    'Van':9}
    
    base_dir = os.path.join(root_dir, str(year))
    
    for month in range(1,13):
        month_dir = os.path.join(base_dir, str(month))     
       
    
        for class_name, label_value in label_mapping.items():

            class_dir = os.path.join(month_dir, str(class_name))
            file_list = os.listdir(class_dir)
            
            for name in file_list:
                train_data['path'].append(os.path.join(str(month), class_name, name))
                train_data['label'].append(label_value)
    
    train_data = pd.DataFrame(train_data)
    
    # shuffle could be added here.
    
    train_data = train_data.sample(frac=1).reset_index(drop=True)
    train_data.to_csv(os.path.join(base_dir, 'data_split_by_year.csv'))


def generate_data_split(root_dir):
    # Generate year-data-split csv writing.
    for year in range(2009, 2021):
        for month in range(1,13):
            make_split(root_dir=root_dir, year=year, month=month)
  
    # Generate month-data-split csv writing.
    for year in range(2009, 2021):
        make_split_by_year(root_dir=root_dir, year=year)

if __name__ == "__main__":
    root_dir = "data/EVIS_40"
#     root_dir = "EVIS_40" # change to where the EVIS dataset is stored.
    generate_data_split(root_dir)
