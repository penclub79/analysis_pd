import pandas as pd
import json
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import math
import collections

def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0

    return r

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    # print('tourspotvisitor_table:',tourspotvisitor_table)
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())
    # print('temp_tourspotvisitor_table : ' , temp_tourspotvisitor_table)

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())

        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        # print('foreignvisitor:',foreignvisitor_table)
        foreignvisitor_table = foreignvisitor_table.set_index('date')
        # print('foreignvisor_table:',foreignvisitor_table)
        merge_table = pd.merge(
            temp_tourspotvisitor_table,
            foreignvisitor_table,
            left_index=True, right_index=True)
        # print(merge_table)
        x = list(merge_table['visit_count'])
        # print("xxxxx : ",x)
        y = list(merge_table['count_foreigner'])
        # print(y)
        country_name = foreignvisitor_table['country_name'].unique().item(0)
        # print(country_name)
        r = ss.pearsonr(x, y)[0]
        # print(r)
        # r = np.corrcoef(x, y)[0]
        # print(r)
        results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})
        print(results)
        #
        merge_table['visit_count'].plot(kind='bar')
        plt.show()

    return results

def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())
        # print(json_data)
    tourist_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    # print(tourist_table)

    tourist_spot = tourist_table['tourist_spot'].unique()
    # print(tourist_spot)

    results = []
    for temp_tourspot in tourist_spot:
        temp_tourspot = tourist_table[tourist_table['tourist_spot'] == temp_tourspot]
        # print(temp_tourspot)

        temp_tourspot = pd.DataFrame(temp_tourspot.set_index('date'))
        # print(temp_tourspot)

        data = {'tourist_spot': temp_tourspot}
        # print(data)
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())

            foreign_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            # print(foreign_table)

            foreigndata_table = pd.DataFrame(foreign_table.set_index('date'))
            # print(foreigndata_table)

            merge_table = pd.merge(
                temp_tourspot,
                foreigndata_table,
                left_index=True, right_index=True)
            # print(merge_table)

            x = list(merge_table['visit_count'])
            # print(x)
            y = list(merge_table['count_foreigner'])
            # print(y)

            tourspot_name = merge_table['tourist_spot'].unique().item(0)
            # print(tourspot_name)
            country_name = merge_table['country_name'].unique().item(0)
            # print(country_name)
            # print(tourist_spot)
            r = correlation_coefficient(x, y)
            # print(r)
            data['country_name'] = country_name
            results.append({'tourspot': tourspot_name, "r_%s" % (country_name) : r})

        print(results)



            # z = dict(collections.ChainMap(results[12]))
            # print(z)


            # merge_table['visit_count'].plot(kind='bar')
            # plt.show()

            # plt.show()
            # r = np.corrcoef(x, y)[0]






