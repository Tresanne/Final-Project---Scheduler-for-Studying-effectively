==============
SCHEDULEME
==============

SCHEDULEME is a program that takes the courses you are doing in school and schedule a study time based on the number of hours
you have available during the day. 

Personas
========

Name 
-------
Tresanne Bonnick

Details
^^^^^^^
Tresanne Bonnick works and goes to school full-time. She has an Associates Degree in Biology and working on completing her Bachelors.
She seems to always be busy and hardly have enough time to finish everything. 

Goals
^^^^^
She wants to earn her Bachelors degree while working full-time. She needs to work to pay for expenses, so having a scheduler that
manages the hours she has in one day and breaking it up to fulfill the tasks she has to do on a daily basis, should help her to finish 
her Bachelors degree on time and still able to work.

Problem Scenarios
=================

No Time To Study
-----------------------

Tresanne works on average 8 hours per day. It takes her 3 hour and 30 minutes to commute to and from work
and she sleeps for 7 hours per day. For some odd reason, during the time that is left, she hardly finds time to do school work.
She may get to do an hour of work but it seems life and distractions always get in the way so her time management is off.

Current Alternatives
^^^^^^^^^^^^^^^^^^^^
Currently Tresanne can just study whenever she gets to without it being organized. This would be hard to do because not having
a set amount of time to do school activities throughout the week can affect her overall classes.

Value Proposition
^^^^^^^^^^^^^^^^^

Having a scheduler that inputs the tasks she does on a daily basis and the amount of time she takes to do them should help her 
to figure out how much time she has left during the day to study at least one class. She have to spend at least 25 hours a week
to study school materials, so having a program that works this out for her, may help her to study better provided that life does
not throw too much stones. 

User Stories
============
As Tresanne, I will input my work and life schedule into the a scheduler to manage my time and give me an 
idea of how much hours I have available to be able to study daily while working a full-time job. 

Acceptance Stories
^^^^^^^^^^^^^^^^^^

::

[Inputing Schedule]

    Given that I input my life and work schedule, I would like the program to hold a record of the time and hours that are taken up during that day. The program would take a snapshot of my schedule and hold that data. 
    
[Calculating hours]

    Given that the scheduler has my work and life schedule, I would like it to calculate the amount of hours I have free to study for that particular day. After counting the hours that is taken up by my daily activities, the prgram will calculate how much hours I have free. This free time would be study time. 
    
[Calculating Study Time]
    Given that I inputed my schedule and the calculated study time for the week is less than 20 hours, an alarm should go off
    that 'You have not reached the minimum study time of 20 hours per week'.
