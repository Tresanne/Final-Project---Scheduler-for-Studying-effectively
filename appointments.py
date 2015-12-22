#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""appointments"""

class Appointment():
  def __init__(self, name, start, end):
    self.name = name
    self.start = start
    self.end = end

  def start_time(self):
    return str(self.start.hour) + ":" + str(self.start.minute) + ":" + str(self.start.second)
    
  def end_time(self):
    return str(self.end.hour) + ":" + str(self.end.minute) + ":" + str(self.start.second)
    
  def total_time(self):
    return (self.end - self.start).seconds
    
  def to_string(self):
    return self.name + "___" + str(self.start.hour) + ":" + str(self.start.minute) + ":" + str(self.start.second) + '___' + str(self.end.hour) + ":" + str(self.end.minute) + ":" + str(self.start.second) + '\n'
