import numpy as np
years = np.arange(1899, 2020+3, 1)
def days(func,month,year):
    return '28' if len(func(year))==0 and month==2 else '29' if len(func(year))==1 and month==2 else '30' if month in [4,6,9,11] else '31' 
def leap_year(years):
   if len(str(years).split()) == 1:
      years = [int(i) for i in list(str(years).split())]
   return list(filter(lambda x: x%400==0 or x%4==0 and x%100!=0, years))
#print(leap_year(years))
try:
  month = str(input('Input month number (1-12): '))
  if month.isdigit() == False or int(month) not in range(1,13):
          raise Exception('You inputed incorrect number month!')
  year = str(input('Input year (4-digit number): '))
  if year.isdigit() == False or len(year)!=4:
          raise Exception('You inputed incorrect year!')
  month, year = int(month), int(year)
  print(days(leap_year, month, year))
except Exception as exc:
       print(exc)

