#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""Finals"""

import os
from datetime import datetime
from appointments import Appointment

def print_menu():
  print("")
  print("1. Load schedule")
  print("2. Save schedule")
  print("3. Add appointment")
  print("4. Remove appointment")
  print("5. Print schedule")
  print("6. Calculate study hours")
  print("7. Exit")
  
def list_schedules():
  print("Existing schedules: ")
  for filename in os.listdir('.'):
    if filename.endswith('.txt'):
      print(filename)
      
def print_schedule(schedule):
  counter = 1
  for appointment in schedule:
    print(str(counter) + ". " + appointment.name + "\t\t\t" + appointment.start_time() + "\t\t" + appointment.end_time())
    counter += 1
      
def main():
  schedule = None
  
  print("Welcome to the study-time calculator!")
  
  done = False
  
  while not done:
    print_menu()
    
    choice = raw_input("Please choose an action: ")
    
    while choice not in ['1', '2', '3', '4', '5', '6', '7']:
      print("Invalid choice!")
      choice = raw_input("Please choose an action: ")
      
    
    if choice == '1':
      list_schedules()
      
      filename = raw_input("Please choose which schedule to load: ")
      
      while not os.path.isfile(filename):
        print("That schedule does not exist!")
        filename = raw_input("Please choose which schedule to load: ")
      
      schedule = [] # reset the current schedule
      
      with open(filename, 'r') as f:
        for line in f:
          line = line.strip()
          parts = line.split('___')
          
          name = parts[0]
          
          start_hour, start_minute, start_second = parts[1].split(':')
          end_hour, end_minute, end_second = parts[2].split(':')
          
          start = datetime(1, 1, 1, int(start_hour), int(start_minute), int(start_second))
          end = datetime(1, 1, 1, int(end_hour), int(end_minute), int(end_second))
          
          new_appointment = Appointment(name=name, start=start, end=end)
          schedule.append(new_appointment)
      
      print("Schedule loaded!")
    elif choice == '2':
      filename = raw_input("Please choose a filename: ")
      
      while not filename.endswith('.txt'):
        print("Filename has to end with .txt!")
        filename = raw_input("Please choose a filename: ")
        
      f = open(filename, 'w')
      
      for appointment in schedule:
        f.write(appointment.to_string())
      f.close()
      print("Schedule saved to file!")
    elif choice == '3':
      if schedule is None:
        schedule = []

      name = raw_input("Please describe your appointment: ")
      
      start = None
      while start is None:
        try:
          start = raw_input("When does it start (HH:MM:SS)? ")
          start = datetime.strptime(start, '%H:%M:%S') # Convert the "start" variable into a date, using the HH:MM:SS format
          if start < datetime.strptime('06:00:00', '%H:%M:%S'):
            print("You cannot schedule appointments that early!")
            start = None
        except:
          start = None
          print("Please input a valid time!")
      
      end = None
      while end is None:
        try:
          end = raw_input("When does it end (HH:MM:SS)? ")
          end = datetime.strptime(end, '%H:%M:%S') # Convert the "end" variable into a date, using the HH:MM:SS format
          if end < datetime.strptime('06:00:00', '%H:%M:%S'):
            print("You cannot schedule appointments that late!")
            end = None
        except:
          end = None
          print("Please input a valid time!")
        
      new_appointment = Appointment(name=name, start=start, end=end)
      schedule.append(new_appointment)
      print("Appointment saved!")
    elif choice == '4':
      if schedule is None:
        print("There are no appointments to remove!")
      else:
        print_schedule(schedule)
        index = None
        while index is None:
          try:
            index = int(input("Which appointment would you like to remove? ")) - 1
            schedule.pop(index)
          except:
            print("Please enter a valid number!")
            index = None
        print("Appointment removed!")
    elif choice == '5':
      if schedule is None:
        print("There are no appointments to print!")
      else:
        print_schedule(schedule)
    elif choice == '6':
      if schedule is None:
        print("There are no appointments! Your day is completely free!")
      else:
        available_time = 18 * 60 * 60
        minimum_required_study_hours = 3
        
        for appointment in schedule:
          available_time -= appointment.total_time()
          
        if (available_time / 60 / 60) < minimum_required_study_hours:
          print("ALERT: YOU HAVE NOT RESERVED ENOUGH STUDY TIME (" + str(minimum_required_study_hours) + " hours) FOR TODAY!!!")
        else:
          print("You have enough time to study today!")
    elif choice == '7':
      done = True
      
main()
