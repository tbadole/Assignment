#!/usr/bin/env python
# coding: utf-8

# 2. Create a program to cater to the following functionalities
# 
# 	a.date time coversions between timezones ( Example UTC to US/Eastern etc)
#     
# 	b.date operations to add/subtract days from a given date 
#     
# 	c.fetch number of days between two dates supplied
#     
# 	d.fetch number of days excluding weekends 
#     
# 	e.fetch number of days since EPOCH
#     
# 	f.fetch number of business days between two days excluding holidays
#     
# 	  (holiday calendar provided in a file in the following format)
#       
#          holidays.dat
#          
# 	 TIMEZONE,DATE,HOLIDAY
# 	 US/Eastern, 20211225, Christmas Day
# 
# Create a class called DateUtility 
# 
# 	Define the following methods,
#     
# 	ALL These should return datetime objects
#     
# 	1.convert_dt(from_date, from_date_TZ , to_date_TZ) 
#     
# 	2.add_dt(from_date, number_of_days)
#     
# 	3.sub_dt(from_date, number_of_days)
#     
# 	4.get_days(from_date, to_date)
#     
#         5.get_days_exclude_we(from_date, to_date)
#         
#  	6.get_days_since_epoch(from_date)
#     
#  	7.get_business_days(from_date, to_date) --> This should look at holidays.dat to exclude
# 

# In[2]:


from datetime import datetime, timedelta
from pytz import timezone
import csv


# In[6]:


class DateUtility:
    '''A. Date time coversions between timezones (Example UTC to US/Eastern)'''
    def convert_dt(from_date_TZ, to_date_TZ):
        format = "%Y-%m-%d %H:%M:%S"
        
        #current date & time according to given timezone
        current_datetime = datetime.now(timezone(from_date_TZ))
        
        
        #convert date & time according to required timezone
        convert_datetime = current_datetime.astimezone(timezone(to_date_TZ))
        return convert_datetime.strftime(format)
    
    '''B(a). Date operation to add days to a given date'''
    def add_dt(from_date, number_of_days):
        
        #date object from_date string
        date_object = datetime.strptime(from_date, '%d/%m/%Y')
        
        #add days to given_date
        add_days = date_object + timedelta(days=number_of_days)
        return add_days.date()
    
    '''B(b). Date operation to subtract days from a given date'''
    def sub_dt(from_date, number_of_days):
        #date object from date string
        date_object = datetime.strptime(from_date, '%d/%m/%Y')
        
        #subtract days from given_date
        subtract_days = date_object - timedelta(days=number_of_days)
        return subtract_days.date()
    
    '''C. Fetch number of days between two dates supplied'''
    def get_days(from_date, to_date):
        format = '%d/%m/%Y'
        
        #date objects from from_date & to_date string
        from_date_obj = datetime.strptime(from_date, format)
        to_date_obj = datetime.strptime(to_date, format)
        
        #number of days between two dates
        number_of_days = to_date_obj.date() - from_date_obj.date()
        return number_of_days.days
    
    
    '''D. Fetch number of days excluding weekends'''
    def get_days_exclude_we(from_date, to_date):
        format = '%d/%m/%Y'
        
        #date objects from from_date & to_date string
        from_date_obj = datetime.strptime(from_date, format)
        to_date_obj = datetime.strptime(to_date, format)

    
        #ecxluding day 6=Sat & day 7=Sun
        exclude = (6,7)
        days = []
        
        while(from_date_obj.date() <= to_date_obj.date()):
            # from_date_obj.isoweekday() returns the day of week as int
            if from_date_obj.isoweekday() not in exclude:
                days.append(from_date_obj)
            from_date_obj += timedelta(days=1)
        return len(days)
    
    '''E. Fetch number of days since EPOCH'''
    def get_days_since_epoch(from_date):
        format = '%d/%m/%Y'
        #date objects from from_date & to_date string
        from_date_obj = datetime.strptime(from_date, format)
        epoch_date_obj = datetime.strptime('01/01/1970', format)
        
        #days since epoch
        days_since_epoch = from_date_obj - epoch_date_obj
        return days_since_epoch.days
    
    '''F. fetch number of business days between two days excluding holidays from holidays.dat'''
    def get_business_days(from_date, to_date):
        format = '%d/%m/%Y'
        #date objects from from_date & to_date string
        from_date_obj = datetime.strptime(from_date, format)
        to_date_obj = datetime.strptime(to_date, format)

        #ecxluding day 6=Sat & day 7=Sun
        exclude = (6,7)
        days = []
        while(from_date_obj.date() <= to_date_obj.date()):
            # from_date_obj.isoweekday() returns the day of week as int
            if from_date_obj.isoweekday() not in exclude:
                days.append(from_date_obj)
            from_date_obj += timedelta(days=1)
            
        with open('holidays.dat','r') as file:
            # Printing last line of second column
            lines = list(csv.reader(file, delimiter = ','))
            holiday_date_obj = datetime.strptime(lines[-1][1], '%Y%m%d')
            
        #remove holiday date
        if holiday_date_obj in days:
            days.remove(holiday_date_obj)
            
        return (len(days))
    
    
convert_datetime = DateUtility.convert_dt('UTC', 'US/Eastern')
print(convert_datetime)

add_days = DateUtility.add_dt('20/02/2023', 12)
print(add_days)

sub_days = DateUtility.sub_dt('24/02/2023', 10)
print(sub_days)

get_days = DateUtility.get_days('14/02/2023', '18/02/2023')
print(get_days)

get_days_ex_we = DateUtility.get_days_exclude_we('01/02/2023', '12/02/2023')
print(get_days_ex_we)

get_days_epoch = DateUtility.get_days_since_epoch('12/02/2023')
print(get_days_epoch)

get_bussiness_days = DateUtility.get_business_days('01/1/2023', '31/1/2023')
print(get_bussiness_days) 


# In[ ]:




