#create several lists in the same array and sort them
#see pp70-71 Illustrating Basic
names =["","","ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
genders = ["", "","FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
links = [0,0]

 def initialise():
     """
create two lists of strings in only one list 
"""
    for index in range(2,len(names)+1):
        if gender[index]=="FEMALE":
            que = 0
            links[index] = links[que]
            links[que] = index
        if gender[index]=="MALE":
            que = 1
            links[index] = links[que]
            links[que] = index


            
def ripple_sort():
    """
sort one of your lists, set up with initialise
without touching the other
"""
    for index in range(2,len(names)+1):
        swop = false
        current = links[0]
        for index1 in range(2,len(names)+1-index):
            previous = current
            current = links[current]
            following = links[current]
            if names[current]>= names[following]:
                swop = true
                temp = links[previous]
                links[previous] = links[current]
                links[currrent] = links[following]
                links[following] = temp
                current = following
        swop = false
        if not swop :
            return
        
        
    
