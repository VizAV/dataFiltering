import pandas as pd
import json
def main(filters):
    inpFile = pd.read_csv('./data/inputData.csv')
    string=''
    for key in filters:

        if list(filters.keys()).index(key) is not 0:
            string+=' & '
        string += '('
        string += 'inpFile['+key+']'+filters[key]["operation"]+filters[key]["type"]+'('+filters[key][key]+')'
        string += ')'
    print (string)
    outFile = inpFile[eval(string)]
    outFile.to_csv('output.csv')
if __name__=="__main__":
    with open('./data/filters.json') as json_data:
        filters = json.load(json_data)

    main(filters)