###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
#================================
# Part A: Transporting Space Cows
#================================
        
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

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
 
    result = []
    ignore = []
    #sort cows by weight from heaviest to lightest
    herd = sorted(cows.items(), key=lambda cows:cows[1], reverse=True)    
    
    #iterate over the list of cows 
    for i in range(len(herd)):
        
        #create a list of list + remove the cows that have taken a trip and puts them into the ignore list
        j = [x for x in herd if x[0] not in ignore]
        #sets number of trips in the first for loop
        trips = []            
        totalWeight = 0.0            
        #iterate over each cow in the list of list
        for k in range(len(j)):
            #adds cows until reaches the weight limit
            if (totalWeight + j[k][1]) <= limit:
                #adds weight of next cow without exceeding weight limit
                totalWeight += j[k][1]     
                #adds trips
                trips.append(j[k][0])
                #moves cows into ignore list
                ignore.append(j[k][0])
                
        if len(trips) >= 1:    
            result.append(trips)
            
    return (result) 

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

    #sort cows by weight from heaviest to lightest
    herd = sorted(cows.items(), key=lambda cows:cows[1], reverse=True)    
    #sets maximum number of trips to number of cows
    number_of_trips=len(cows)
    results=[]
    #enumerate all possible ways that the cows can be divided into separate trips
    for trips in get_partitions(herd):   
        weights=[]
        #determine weight of the trips
        for trip in trips:
            weight=([v for x, v in trip])
            #determine total weight of each trip
            weights.append(sum(weight))
        #determine if total weight is under limit
        if max(weights)<=limit and (len(trips) <= number_of_trips):
            #sets maximum number of trips to the number of separate trips by cows
            number_of_trips=len(trips)
            #if the total weight is under limit and number of trips is less than or equal to number of cows, place cows in spaceship            
            results = trips
    return (results)
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    brute_force_cow_transport(cows,limit)
    end = time.time()
    print('brute force ', end - start)

    start = time.time()
    greedy_cow_transport(cows,limit)
    end = time.time()
    print('greedy ', end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""
#cows = ({'Miss Bella': 25, 'MooMoo':50,'Lotus':40,'Milkshake':40,'Boo':20,'Horns':25},100)
cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


