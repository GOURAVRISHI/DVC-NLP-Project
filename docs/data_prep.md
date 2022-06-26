# Data preperation stage

- convert my data into train and test test.tsv in 70:30 ratio

'''
data.xml
    |-train.tsv
    |-test.tsv
'''
- We are choosing only three tags in the xml data - 1. row Id, 2. title and 3. Tags(Stackoverflow tags specific to python)

|Tags|Features Name|
|-|-|
|row Id|row Id|
|title and body|text|
|stackoverflow tags|Label - Python|
