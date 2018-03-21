
from datetime import datetime

def is_odd?(num):
  return num // 2 == 0

def str_to_dt(string):
  return datetime.strptime(string, )

def read_dates(file_path):
  with open(file_path, 'r', encoding = 'utf-8) as file:
    lines_list = file.readlines()
  counter = 1
  datetimes = []
  for line in lines_list:
     if line[0].isnumeric():
        if id_odd?(counter):
          first_date = line
        else:
          datetimes.append([first_date, line])
  return datetimes

def sum_deltatimes(datetimes):
  sum = 0
  for dt_list in datetimes:
    sum += dt_list[1] - dt_list[0]
  return sum

             
calculate_proyect_time(file_path):
  return sum_deltatimes(read_dates(file_path))

