# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 21:36:54 2019

@author: Administrator
"""

import pandas
import geopy.distance
import googlemaps
import pickle
import random as rd
df = pandas.read_csv('koh_kred.csv')
#print(df)
list_Name = (df.Name).tolist()
list_ID = (df.ID).tolist()
list_Lat = map(float, (df.Lat).tolist())
list_Long = (df.Long).tolist()
list_score = (df.Score).tolist()
list_t_spend = (df.Time_spend).tolist()
list_categories = (df.Categories).tolist()
list_all_categories = df.Categories.unique().tolist()

lst_Name = dict(zip(list_ID, list_Name))
lst_categories = dict(zip(list_ID, list_categories))
lst_loc = dict(zip(list_ID, zip(list_Lat,list_Long)))
lst_score = dict(zip(list_ID, list_score))
lst_t_spend = dict(zip(list_ID, list_t_spend))

distanceMatric = {}
# Requires API key 
gmaps = googlemaps.Client(key='AIzaSyDJh61uUcs5y7dNg9hvoL2VSf2ZA7e6ll4') 
#my_dist = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0]

for id1 in list_ID:
    lst_temp = {}
    for id2 in list_ID:
        if not (id2==id1) :
            origins = lst_loc[id1]
            destination = lst_loc[id2]
# Requires cities name 
#            my_dist = rd.uniform(2.5, 50)#gmaps.distance_matrix(origins, destination, mode='walking')['rows'][0]['elements'][0] 
            my_dist = geopy.distance.distance(origins, destination).km*1000/75
        else:
            my_dist = 0
        lst_temp[id2] = my_dist
    distanceMatric[id1] = lst_temp
                
# Printing the result 
#print(my_dist) 
#for 
#    distanceMatric[(id1,id2)] = (double)
        
f = open('distanceFile.pkl', 'wb')
pickle.dump(distanceMatric, f)
pickle.dump(lst_Name, f)
pickle.dump(lst_categories, f)
pickle.dump(lst_loc, f)
pickle.dump(lst_score, f)
pickle.dump(lst_t_spend, f)
pickle.dump(list_all_categories, f)



f.close()
