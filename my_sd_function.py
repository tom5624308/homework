import statistics
list= (1,2,4,8,16,32,64,128)
sd=statistics.stdev(list)
n=len(list)
x=((len(list)-1)/(len(list)))**0.5
print(sd*x)
