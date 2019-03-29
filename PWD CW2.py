#Phase 1
def myHealthcare(n=1000,seed=404):
    import random as r
    r.seed(seed)
    column_names = ['timestamp', 'temperature', 'heart rate',\
                    'pulse','blood pressure', 'respiratory rate',\
                    'oxygen saturation', 'ph']
    timestamp = [i for i in range(101, 101 + n)]
    temperature = [r.randint(36, 39) for i in range(n)]
    heart_rate = [r.randint(55, 100) for i in range(n)]
    pulse = [r.randint(55, 100) for i in range(n)]
    blood_pressure = [r.choice([120, 121]) for i in range(n)]
    respiratory_rate = [r.randint(11, 17) for i in range(n)]
    oxygen_saturation = [r.randint(93, 100) for i in range(n)]
    ph = [r.randint(71,76)/10 for i in range(n)]
    
    health_care = [column_names, timestamp, temperature,\
                   heart_rate, pulse, blood_pressure,\
                   respiratory_rate, oxygen_saturation, ph]
    return health_care

generated= myHealthcare()
###################################
#Phase 2
#a)
def sample(record, sample_size=50):#generates a sample of a record
    samp_list=[]#list of sample
    samp_list.append(record[0])
    for i in range(1,9):
        samp_list.append(record[i][6:6+sample_size])
    return samp_list


def abnormalSignAnalytics(vital_sign,sample):
    sign_analytics = []#list to be returned
    records=[]#list of abnormal signs
    m=0
    if vital_sign == 'pulse rate':
        sign_analytics.append('pulse')
        for i in range(len(sample[4])):
            if sample[4][i] in [55,56,57,58,59,100]:
                m+=1
                records.append([sample[1][i],sample[4][i]])
    elif vital_sign == 'blood pressure':
        sign_analytics.append('blood pressure')
        for i in range(len(sample[5])):
            if sample[5][i] == 121:
                m+=1
                records.append([sample[1][i],sample[5][i]])
    else:
        return 'unknown vital sign!!'
    sign_analytics.append(m)
    sign_analytics.append(records)
    return sign_analytics
####################    
#b)
def frequencyAnalytics(sample):
    pulse=sample[4]
    freq={}
    for i in pulse:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    return freq
        
#####################        
#c)i
import time
import matplotlib.pyplot as plt
sample1=sample(generated,50)


#plot for 2a
a=abnormalSignAnalytics('pulse rate',sample1)
b=abnormalSignAnalytics('blood pressure',sample1)

x=[]
y=[]
for i in a[2]:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x,y,color='black',label='pulse')
x=[]
y=[]
for i in b[2]:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x,y,color='red',label='blood pressure')
plt.title('ABNORMAL PULSE RATES AND BLOOD PRESSURES FOR SAMPLE')
plt.xlabel('timestamp')
plt.ylabel('values')
plt.legend()
plt.show()


#######################
#plots for 2b. Two methods used
a=frequencyAnalytics(sample1)
print('For a sample of 50 records:')
t=time.time()
#unpacking a dictionary and plotting a histogram with the values
histogram_list=[]#list will contain every pulse data in frequncyAnalytics
for i in a.items():
    for j in range(i[1]):
        histogram_list.append(i[0])

plt.hist(histogram_list,bins=[i-0.5 for i in range(55,102,1)])
print('Time to create histogram in seconds: ', time.time()-t)
plt.title('Pulse Rate Frequency')
plt.xlabel('pulse rate')
plt.ylabel('frequency')
plt.xticks([i for i in range(55,100,2)])
plt.show()

#c)ii  using a bar plot, plotting a tuple pair at a time
t=time.time()
for i in a.items():
    plt.bar(i[0],i[1],color='blue')
print('Time to create barchart in seconds: ',time.time()-t)
print('\n')
print('\n')
plt.title('Pulse Rate Frequency')
plt.xlabel('pulse rate')
plt.ylabel('frequency')
plt.xticks([i for i in range(55,100,2)])
plt.show()

####################################
#Phase 3)
#a
def healthAnalyzer(value,vital_sign='pulse rate',record=generated):
    #dictionary gives name of column to index in record relationship
    d={'timestamp':1, 'temperature':2, 'heart rate':3,\
       'pulse rate':4,'blood pressure':5,'respiratory rate':6,\
       'oxygen saturation':7, 'ph':8}
    if vital_sign not in d.keys():
        return 'vital sign not in record!!!'
    else:
        index = d[vital_sign]
        m=-1#index counter
        ans=[]#list to be returned
        for i in record[index]:
            m+=1
            if i == value:
                new_record=[]
                for j in range(1,9):
                    new_record.append(record[j][m])
                ans.append(new_record)
    return ans
##########
#c
data= healthAnalyzer(56,'pulse rate',generated)
x=[]
y=[]
for i in data:
    x.append(i[0])
    y.append(i[2])
plt.scatter(x,y,marker = 'x',color='green')
plt.xlabel('timestamp')
plt.ylabel('heart rate')
plt.title('Heart Rate against Timestamp')
plt.yticks([i for i in range(55,102,2)])
plt.show()

##################################
#Phase 4
#a)
def benchmarking(function):
    import time
    import matplotlib.pyplot as plt
    n=[1000,2500,5000,7500,10000]
    N=1000 #done 1000 times and averaged
    tim=[]#to be filled with time values
    for j in n:
        a=time.time()
        for i in range(N):
            function(n=j)
        tim.append((time.time()-a)/N)
    plt.plot(n,tim)
    plt.scatter(n,tim)
    plt.title('Size of Record Against avg. Time to Create it')
    plt.ylabel('time(seconds)')
    plt.xlabel('number of records')
    plt.xticks([i for i in range(1000,11000,1000)])
    plt.show()

#benchmarking(myHealthcare)
################################
    ############################
    ##############################
def myHealthcare2(n=1000,seed=404):
    '''returns a record with pulse rate and blood record in ascending
    order. This is not a reordering of record produced by myHealthcare.'''
    import random as r
    r.seed(seed)
    a= myHealthcare()
    a[4]=[]
    z=55
    for i in range(n):
        z = (r.random()*0.09)+z
        if z < 101:
            a[4].append(int(z))
        else:
            a[4].append(100)
    a[5] = []
    z=120
    for i in range(n):
        z = (r.random()*0.004)+z
        if z < 122:
            a[5].append(int(z))
        else:
            a[5].append(121)
    return a
generated2= myHealthcare2()

########################################

def abnormalSignAnalytics2(vital_sign,sample):
    sign_analytics = []#list to be returned
    records=[]#list of abnormal signs
    m=0
    if vital_sign == 'pulse rate':
        sign_analytics.append('pulse')
        for i in range(len(sample[4])):
            if sample[4][i] < 60:
                m+=1
                records.append([sample[1][i],sample[4][i]])
            else:
                break
        for i in range(-1,-(len(sample[4])),-1):
            if sample[4][i] == 100:
                m+=1
                records.append([sample[1][i],sample[4][i]])
            else:
                break
    elif vital_sign == 'blood pressure':
        sign_analytics.append('blood pressure')
        for i in range(len(sample[5])):
            if sample[5][i] < 60:
                m+=1
                records.append([sample[1][i],sample[5][i]])
            else:
                break
        for i in range(-1,-(len(sample[5])),-1):
            if sample[5][i] == 100:
                m+=1
                records.append([sample[1][i],sample[5][i]])
            else:
                break
    else:
        return 'unknown vital sign!!'
    sign_analytics.append(m)
    sign_analytics.append(records)
    return sign_analytics
##############
#benchmarking abnormalSignAnalytics vs abnormalSignAnalytics2
N=1000
print('For %d records:'%N)
a=time.time()
for i in range(N):
    abnormalSignAnalytics('pulse rate', generated2)
    abnormalSignAnalytics('blood pressure', generated2)
print('Average time to execute abnormalSignAnalytics in seconds:', (time.time()-a)/N)

a=time.time()
for i in range(N):
    abnormalSignAnalytics2('pulse rate', generated2)
    abnormalSignAnalytics2('blood pressure', generated2)
print('Average time to execute abnormalSignAnalytics2 on same data in seconds:', (time.time()-a)/N)
print('\n')
print('\n')
###############################
def healthAnalyzer2(value,record):
    '''searches for all values equal to a given
    value in the sorted array pulse rate and
    prints out all entire records'''
    a=record[4]
    low=0
    high=999
    if 55<=value<=100:
        while low<=high and value>=a[low] and value<=a[high]:
            search_bite = low+((high-low)/(a[high] - a[low]))*(value - a[low])
            #since the array is randomly generated,we expect
            #it to contain roughly equal number of elements
            #for each value. search_bite calculates the
            #expected index of a given value
            v=int(search_bite+0.5)#rounds up the expected index to a whole number
            if a[v] == value:
                index = v
                break
            if a[v] > value:
                high=v-1
            else:
                low=v+1
    else:
        return 'value not in pulse rate column'
    #now we have the index of one of the values we are searching for.
    #we now look to its left and right to find other values
    ans=[]#list to be returned
    while value == record[4][index] and index>=0:#so v does not go below index 0
        new_record=[]
        for j in range(1,9):
            new_record.append(record[j][index])
        ans.append(new_record)
        index -= 1
    index = v + 1#reset index to value to the right of the value we found at first
    while index <=len(record[4])-1 and value == record[4][index]:#so v does not go above list range
        new_record=[]
        for j in range(1,9):
            new_record.append(record[j][index])
        ans.append(new_record)
        index += 1

    return ans
######################################
def healthAnalyzer3(value,record):
    '''searches for all values equal to a given
    value in the sorted array pulse rate and
    prints out all entire records'''
    a=record[4]
    low=0
    high=999
    if 55<=value<=100:
        while low<=high and value>=a[low] and value<=a[high]:
            v = low+ int((high-low)/2)
            if a[v] == value:
                index = v
                break
            if a[v] > value:
                high=v-1
            else:
                low=v+1

    else:
        return 'value not in pulse rate column'
    #now we have the index of one of the values we are searching for.
    #we now look to its left and right to find other values
    ans=[]#list to be returned
    while value == record[4][index] and index>=0:#so v does not go below index 0
        new_record=[]
        for j in range(1,9):
            new_record.append(record[j][index])
        ans.append(new_record)
        index -= 1
    index = v + 1#reset index to value to the right of the value we found at first
    while index <=len(record[4])-1 and value == record[4][index]:#so v does not go above list range
        new_record=[]
        for j in range(1,9):
            new_record.append(record[j][index])
        ans.append(new_record)
        index += 1

    return ans

####################################    
#benchmarking healthAnalyzer vs healthAnalyzer2
N=1000
print('For %d records:' %N)
x=time.time()
for p in range(N):
    for q in range(55,101):
        healthAnalyzer(q,vital_sign='pulse rate',record=generated2)
print('Average time to execute healthAnalyzer in seconds:',(time.time()-x)/N)

y=time.time()
for r in range(N):
    for s in range(55,101):
        healthAnalyzer2(s,generated2)
print('Average time to execute healthAnalyzer2 in seconds:',(time.time()-y)/N)

z=time.time()
for t in range(N):
    for u in range(55,101):
        healthAnalyzer3(u,generated2)
print('Average time to execute healthAnalyzer3 in seconds:',(time.time()-z)/N)



def he2(value,record):
    '''searches for all values equal to a given
    value in the sorted array pulse rate and
    prints out all entire records'''
    a=record[4]
    low=0
    high=999
    if 55<=value<=100:
        while low<=high and value>=a[low] and value<=a[high]:
            search_bite = low+((high-low)/(a[high] - a[low]))*(value - a[low])
            #since the array is randomly generated,we expect
            #it to contain roughly equal number of elements
            #for each value. search_bite calculates the
            #expected index of a given value
            v=int(search_bite+0.5)#rounds up the expected index to a whole number
            if a[v] == value:
                index = v
                break
            if a[v] > value:
                high=v-1
            else:
                low=v+1
    a=record[4]
    low=0
    high=999
    if 55<=value<=100:
        while low<=high and value>=a[low] and value<=a[high]:
            v = low+ int((high-low)/2)
            if a[v] == value:
                index = v
                break
            if a[v] > value:
                high=v-1
            else:
                low=v+1

zz=time.time()
for t in range(N):
    for u in range(55,101):
        he2(u,generated2)
print('Average time to execute he2 in seconds:',(time.time()-zz)/N)
