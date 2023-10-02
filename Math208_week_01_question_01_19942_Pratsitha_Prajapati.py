import random
import matplotlib.pyplot as plt

def get_random_numbers():
    random_numbers = []
    for i in range(0,500):
        num = random.uniform(-20, 20)
        random_numbers.append(round(num,2))
    return random_numbers

def get_mean(array):
    sum=0
    for i in array:
       sum=sum + i
    
    mean=sum/len(array)
    return mean

def get_median(array):
    array.sort()
    n=len(array)
    if n%2==1:
        median_index=(n//2)
        median=array[median_index]
    else:
        median_index=n//2
        median=(array[median_index]+array[(median_index-1)])/2
    return median 

def get_standard_deviation(array):
    n=len(array)
    m=mean
    sub=0 
    standard_deviation= 0

    for i in array:
        sub=int(int(i)-mean)**2
        standard_deviation=(sub/n)**0.5
        return standard_deviation
        

def plot_histogram(list, num_bins=10):
  
     plt.hist(list, bins=num_bins)
     plt.xlabel("Value")
     plt.ylabel("Frequency")
     plt.title("Histogram of Random Numbers")
     plt.show()
    


list = get_random_numbers()

mean=get_mean(list)
print("your mean is:",round(mean,2))

median=get_median(list)
print("your median is:",round(median,2))

standard_deviation=get_standard_deviation(list)
print("your standard deviation is:",(standard_deviation))

plot_histogram(list)
