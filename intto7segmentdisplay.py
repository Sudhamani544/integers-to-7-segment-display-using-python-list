num_pattern = [('###','# #','# #','# #','###'),
               ('  #','  #','  #','  #','  #'),
               ('###','  #','###','#  ','###'),
               ('###','  #','###','  #','###'),
               ('# #','# #','###','  #','  #'),
               ('###','#  ','###','  #','###'),
               ('###','#  ','###','# #','###'),
               ('###','  #','  #','  #','  #'),
               ('###','# #','###','# #','###'),
               ('###','# #','###','  #','###') ]

num = int(input("please enter a interger number >= zero: "))
if num>= 0:
    for i in range(5):
        #join each corresponding segment line of every number in string
        print("  ".join(num_pattern[int(j)][i] for j in str(num)))
