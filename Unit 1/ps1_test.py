# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:13:35 2016

@author: chi-chu tschang
"""

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #print(cows)
    #trip=[]
    #import copy
    cowsNames=cows.keys()
    #print(cowsNames)
    cowNamesList=[]
    
    #for cowName in cowsNames:
    #    if cows[cowName] <=limit:
    #        cowNamesList.append(cowName)
    #       print(cowNamesList)

    herd = sorted(cows.items(), key=lambda cows:cows[1], reverse=True)    
    #print(herd)
    #limit = 10
    #weight = [v for x, v in cows.items()]        
    #name = [x for x, v in cows.items()]
    #print('weight', weight)
    #print('name', name)
    #for i in weight:
        #print (i)
    #    if sum(trip) <= limit:       
    #        trip.append(i)
    #        print(trip)
    #trips=[]
    number_of_trips=len(cows)
    results=None
    limit=10
    #best_trips=len(cows) + 1
    for trips in get_partitions(herd):   
        #print(trips)        
        #flag = False
        #numberOfTrips = 0
        weights=[]
        for trip in trips:
            print(trip)
            weight=(sum([v for x, v in cows.items() if x in trip]))
            #print('weight',weight)            
            weights.append(weight)
            #print('weights',weights)
            #print('max weight',max(weights))
            for w in weights:
                #print (w)
                if w <= limit: #and len(trips) <= number_of_trips:
                    #print(limit)            
                    #print(len(trips))
                    #number_of_trips=len(trips)
                    #print(number_of_trips)
                    results = trips
                    #print(trips)
    return results            
            #for cow in one_trip:
                #print('cow',cow)
                #trip_weight+=cow[1]
                #print('trip weight', trip_weight)
                #temp_results=[]             
            #if trip_weight > limit:                
                #print('name',cow[0])
                #flag = False                    
                #break
            #if flag and (len(trips) < best_trips):
                #best_trips = len(trips)
            #    print(best_trips)
                #for trip in trips:
                    #temp_results=[]
                    #print(l)
                    #for cow in trip:
                       #temp_results = trips.append(cow[0])  
                       #print(trips)
                       #print(temp_results)
                    #results.append(temp_results)
    #return results                    
                    #print('trips',trips)
        #if len(i) < fewest_trips:

                    #trips.append(i[0])


        #    trips = len(i)
        #    for j in i:
        #        temp = []
        #        for cow in i:
        #            temp.append(i[0])
        #            print(temp)
            #for k in j:
            #    print(k)
        #result=[sum(z) for z in trip[1]]
        #print(result)
        #print('limit',limit)
        #for i in result:
        #    if i <= limit:
        #        trip.append(name)
        #        print(trip)
                       
            #print(alist)
        #for p in partition:
        #    print(p)            
            #if weight <= limit:
                #result = (brute_force_cow_transport(weight, limit))
                #print(True)
    
  
    #if j==[] or limit==0:
    #    result = (0,())
     
    #elif j[1] > limit:
        #explore right branch only
    #   result = brute_force_cow_transport(cows[1], limit)        
    #    else:
    #nextItem = cows
    #print(nextItem)
            #explore left branch

