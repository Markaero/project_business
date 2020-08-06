import csv
with open("C:\\python\\台大code\\project 1\\project.csv", newline = "") as test:

    rows = csv.DictReader(test)
    cin = [row for row in rows]
class test:
    def init(self,hour,minute,second):
        self.hour = int(hour)
        self.second = int(second)
        self.minute = int(minute)
    def isvalidtime(self,t_start,t_last):
        if (t_start.hour == t_last.hour):#先判斷測資 是同一個小時 or not
            if self.hour == t_start.hour:
                if (self.minute > t_start.minute) and (self.minute < t_last.minute):#同一個小時 只有last會大於start的分鐘的情況
                    return True
                elif (self.minute == t_start.minute):#那如果分鐘數相同，要比秒數
                    if (t_start.second == t_last.second):#秒數相同，回傳True
                        if (self.second == t_start.second):
                            return True
                    elif(t_last.second > t_start.second):#秒數last一定會比start大
                        if (self.second >= t_start.second):
                            return True 
        elif(t_last.hour > t_start.hour):#如果有幾個小時，就要分成在t_start小時內 ，之間 ， 和t_last小時內
            if (self.hour == t_start.hour):#情況一
                if self.minute > t_start.minute:
                    return True
                elif (self.minute == t_start.minute) :
                    if t_last.second  == t_start.second:
                        if self.second == t_start.second:
                            return True
                    else:
                        if self.second >= t_start.second:
                            return True

            elif (self.hour == t_last.hour):#情況三
                if self.minute < t_last.minute:
                    return True
                elif self.minute == t_last.minute:
                    if self.second <= t_last.second:
                        return True
            elif (self.hour > t_start.hour) and (self.hour < t_last.hour):#情況二
                return True
                
            return False


def strtotime(time):
    [time1 , time2] = time.split(" ")
    [hour1 , minute1, second1] = time1.split(":")
    [hour2 , minute2, second2] = time2.split(":")
    t1 = test()
    t2 = test()
    t1.init(hour1 , minute1, second1)
    t2.init(hour2 , minute2, second2)
    return t1,t2
def strtotime2(time):
    t3 = test()
    [hour,minute,second] = time.split(":")
    t3.init(hour,minute,second)
    return t3

time = input()
time = strtotime(time)
dict_names = {'1' : {'Accepted':0,'Compile Error':0,'Runtime Error':0,'Time Limit Exceed':0,'Wrong Answer':0},
              '2' : {'Accepted':0,'Compile Error':0,'Runtime Error':0,'Time Limit Exceed':0,'Wrong Answer':0},
              '3' : {'Accepted':0,'Compile Error':0,'Runtime Error':0,'Time Limit Exceed':0,'Wrong Answer':0},
              '4' : {'Accepted':0,'Compile Error':0,'Runtime Error':0,'Time Limit Exceed':0,'Wrong Answer':0}
              }
for i in cin:
    if strtotime2(i['SubmissionTime']).isvalidtime(time[0],time[1]) == True:
        dict_names[i['Problem']][i['Status']] += 1
        
     
print(dict_names['1'].values(),";",dict_names['2'].values(),";",dict_names['3'].values(),";",dict_names['4'].values(),";")