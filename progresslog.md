This file will track progress of the proj since development.

 Before 16/08/26

This proj was initially a python backend-only project that runs on terminal. It has a single file called "main.py" with 7 elif statements for each functionality spanning over 200+ lines of code only.
The target is to convert this to a fullstack project- with its own frontend, backend, and DB. 

16/08/26

Created UI Design for the project- each webpage: how it shld look and what functionality it should hold, altho drawn on paper for now... the structure will soon be added and the architechture will be built

17/08/26

Improved UI, Finalized interface and functionalities. Physical mades-
4 Webpages: Homepage, then based on logins, will have 3 roles and pages for each: Patients, Doctors, Admins.
Each role's mainpage will have tabbed interfaces.
1. Patients will have Profile, Schedule/Appointments, Book an appointment, Doctors (basic info, select), Report.
2. Doctors will have Dashboard with basic info and todays todo, Profile to view, their assigned Patients details with a list and more details within it and an option to edit their report and the schedule for today.
3. Admins will have Dashboard showing basic info: sortby time data- pats treated, appts booked; todays appts and active patients, graph: apts by day and recent appts.. Patients, viewing and editing their details, same with doctors, then appointments shown as lists that can be rescheduled, cancelled, edited, etc... analytics that shows graphs: pat. stats by status, pats by docs, apt analytics like monthly apts graph.. finally settings, to edit hospital info or admins own profile.

The project will initially have a single database with 7 tables-
Users for login, Patient details, Doc details, appointments, doc schedule, med reports and hospital settings.
