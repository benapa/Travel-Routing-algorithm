# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:55:19 2019

@author: User
"""

# importing googlemaps module 
import googlemaps 
import json
import geopy.distance
#tsl_test
from tsp_solver.greedy import solve_tsp # require solve_tsp2
import pickle


"""
1. get distance matric between all points in 
distanceMatric[(loc1,loc2)] = (double)
"""




# some JSON:





start_loc={'p_1': (13.913077, 100.490025)}
start_loc.update({'p_2': (13.903077, 100.490025)})



def getList(loc, list_categories, duration):
    get_list_categories#list_categories
    get_list_places#list_places
    list_t_spend



    return list1,list2,list3

def init():
    f = open('distanceFile.pkl', 'rb')
    distanceMatric= pickle.load(f)
    lst_Name= pickle.load(f)
    list_categories= pickle.load(f)
    list_loc= pickle.load(f)
    list_score= pickle.load(f)
    list_t_spend = pickle.load(f)
    list_all_categories = pickle.load(f)
    f.close()
    return distanceMatric,lst_Name,list_categories,list_loc,list_score,list_t_spend,list_all_categories

def filter_categories(lst_Name,list_categories,list_loc,list_score,
                      list_t_spend,list_filtered_categories): 
    for key in list(list_categories):       
        if not (list_categories[key] in list_filtered_categories):
            del lst_Name[key]
            del list_categories[key]
            del list_loc[key]
            del list_score[key]
            del list_t_spend[key]
            
    
    return lst_Name,list_categories,list_loc,list_score,list_t_spend
#
def compute_list(duration,current_loc, list_filtered_categories):#list_categories,
#                 list_t_spend,list_score,list_all_categories,distanceMatric):
    distanceMatric,lst_Name,list_categories,list_loc,list_score,list_t_spend,list_all_categories = init()       
    lst_Name,list_categories,list_loc,list_score,list_t_spend \
    = filter_categories(lst_Name,list_categories,\
                      list_loc,list_score,list_t_spend,list_filtered_categories)

    total_time = 0          #minutes    
#    total_t_spend = 0
#    total_t_travel = 0
    list1 = [];
    all_place_count=0.01    
    
    
    ref_origin = 97#poramai temple  {'p_1': (13.913098, 100.490080)}
    temp_dist ={}
    for key,value in list_loc.items():   
        temp_dist[key] = geopy.distance.distance(current_loc, list_loc[key]).km        
    ref_point = min(temp_dist, key=temp_dist.get)  
    if temp_dist[ref_point]>10:
        ref_point = ref_origin           
    total_time = 0          #minutes    
    list1.append(ref_point);
    categories_count = {}
    for i in list_filtered_categories:
        categories_count[i] = 0
    place_util = {}
    while  total_time<duration:     
        for key,value in list_loc.items():        
#        for i in list_places:
            category = list_categories[key]
            if not key in list1:
                div_score = 1- categories_count[category]/all_place_count
                place_util[key] = (duration-list_t_spend[key])*list_score[key]*div_score#*rand    
            else:
                place_util[key] = 0                 
        place = max(place_util, key=place_util.get) 
        all_place_count = all_place_count+1
        """        place_util[place] = 0;
        place1 = max(place_util, key=place_util.get)  
        place_util[place1] = 0;
        place2 = max(place_util, key=place_util.get)  
        """
        list1.append(place)
        categories_count[list_categories[place]] = categories_count[list_categories[place]]+1

#D
        list1.append(ref_point)  
        D = [] 
        for i in range(0,len(list1)):
            temp = []
            for j in range(0,i):
                temp.append( distanceMatric[list1[i]][list1[j]])
#            print(i, temp)    
            D.append(temp)
        path = solve_tsp( D,endpoints = (0,len(list1)-1) )        
        travel_time = 0;
        spend_time = 0
        for j in range(0,len(path)):
            if j>0:
                loc1 = list1[path[j-1]]
            else:
                loc1 = ref_point
            loc2 =  list1[path[j]]
            travel_time = travel_time+distanceMatric[loc1][loc2]
        for j in range(1,len(path)-1):
            spend_time = spend_time+list_t_spend[list1[j]]
        total_time = spend_time+travel_time
        print("spending_time = ",spend_time)
        print("travel_time = ",travel_time)        
        print("total_time = ",total_time)
        list1.pop()
    print(total_time)
    list1.pop()
    list1.pop(0)
    print('visiting node:',tour_list)
    print([list_categories[k] for k in tour_list if k in list_categories])
    print([list_score[k] for k in tour_list if k in list_score])
    print([lst_Name[k] for k in tour_list if k in lst_Name])
    print([list_t_spend[k] for k in tour_list if k in list_t_spend])

    return list1
list_filtered_categories = ['product','shop','homestay']

tour_list = compute_list(200,(13.913098, 100.490080), list_filtered_categories)
#first_loc = tour_list.pop(0)
#tour_list.pop(0)
