#Marit Mallberg
#Lab Section 10
#Submitted: 
# I got help from Mac Wienzeirl who I sit next to in class. 

weekdays = {0:"sunday", 1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday"}

month_len = {"01":31, "02":28, "03":31, "04":30, "05":31, "06":30, "07":30, "08":31, "09":30, "10":31, "11":30, "12":31}
leapmonth_len = {"01":31, "02":29, "03":31, "04":30, "05":31, "06":30, "07":30, "08":31, "09":30, "10":31, "11":30, "12":31}

#this code needs to: check that the date exists, check if it is a leap year
#calculate when jan 1st falls, and calculate when the date itself falls. 


def leapcheck(year):
    """check to see if the date is in a leap year"""
    if year%4 == 0 and year%100 != 0:
        return "yes"
    elif year%4000 == 0:
        return "yes"
    else:
        return "no"

def truncate(number):
    """remove the decimal values off of a float"""
    if type(number) == int:
        return number
    elif type(number) == float:
        return int(number-(number%1))

def jan1st_day(year):
    """what day of the week is january first of a certain year, gives a number that fits the dict above"""
    year += -1
    return (36 + year + truncate(year/4) - truncate(year/100) + truncate(year/400))%7

while True:
    userdate = input("Give me a numeric date MM/DD/YYYY and I'll tell you the day of the week it is. enter 'q' to quit")

    date = {}
    leap= False
    invalid=False
    day_of_year = -1
    if userdate.lower() == "quit":
        break
    else:
        date["month"]=int(userdate[0:2])
        date["day"]=int(userdate[3:5])
        date["year"]=int(userdate[6:9])

    if leapcheck(date["year"]) == "yes":
        leap = True

#Validity Checks:
    if date["day"] < 1:
        invalid = True
    if date["year"] < 1:
        invalid = True
    if date["month"] < 1 or date["month"] > 12:
        invalid = True
    if date["month"] in month_len and month_len[date["month"]] == 31 and date["day"]>31:
        invalid=True
    if date["month"] in month_len and month_len[date["month"]] == 30 and date["day"]>30:
        invalid=True
    if date["month"] == "02" and leap and date["day"] > 29:
        invalid=True
    if date["month"] == "02" and not leap and date["day"] > 28:
        invalid = True
    
    if invalid:
        print(f"date entered is invalid")
        continue

#calculating the day of week ...

    day_of_year += jan1st_day(date["year"]) + date["day"]
    if not leap:
        for month in month_len:
            if date["month"] != month:
                day_of_year += month_len[month]
            else:
                break
    if leap:
        for month in leapmonth_len:
            if date["month"] != month:
                day_of_year += leapmonth_len[month]
            else:
                break

print(f"{userdate} is/was a {weekdays[day_of_year%7]}")


