# Hotel Booking System

# Project Overview

The Hotel Booking System is a Python based desktop application designed to manage hotel rooms, customers, bookings, authentication, administration, monitoring, logging, automated testing, deployment automation, and basic system recovery.

The application uses Tkinter for the graphical user interface and SQLite for persistent data storage.

The project has also been extended with basic Site Reliability Engineering practices.

The SRE implementation focuses on monitoring application components, detecting failures, processing application logs, running automated tests, performing continuous integration, automating deployment, recovering missing database structures, and verifying system health after recovery.


# Project Objectives

The main objectives of this project are to build a functional hotel booking application while applying basic software reliability and automation practices.

The project provides functionality for:

User registration

User login

Password hashing

Role based access

Administrator access

Room management

Room availability checking

Room booking

Booking management

Database management

Application monitoring

Failure detection

Application logging

Log processing

Automated testing

Continuous integration

Deployment automation

Automatic database recovery

Recovery verification


# Technology Stack

The project was developed using the following technologies.

Python

Tkinter

SQLite

Git

GitHub

GitHub Actions

Python unittest

Python logging


# Project Structure

The project is organized into application modules, database modules, service modules, utility modules, tests, and GitHub Actions workflows.

   text
HotelBookingSystem

    database
        connection.py
        schema.py
        init.py

    services
        booking_service.py
        monitor_service.py
        recovery_service.py
        room_service.py
        log_service.py
        init.py

    tests
        test_hotel_system.py
        test_recovery.py
        init.py

    gui
        init.py

    utils
        init.py

    logs

    about_us.py
    admin.py
    bookingapp.py
    cleanup.py
    gallery.py
    HotelDatabaseConnect.py
    logger.py
    main_hotelapp.py
    make_admin.py
    session.py
    signin.py
    signup.py
    requirements.txt

    .gitignore

    .github
        workflows
            ci.yml
            deploy.yml


## Application Features

# User Registration

The registration system allows users to create accounts using their full name, phone number, username, and password.
The system validates required fields before creating an account.
Usernames are unique.
Passwords are hashed before being stored in the database.

# User Login

Registered users can log into the application using their username and password.
The login system compares the hashed password against the stored password hash.
Successful authentication creates a user session.
The session stores the current username and role.

# Password Security

Passwords are not stored as plain text.
The application uses Bcrypt hashing before storing passwords in the SQLite database.
The hashing process converts the password into a fixed length hash before it is stored.

# Role Based Access

The application supports user roles.
The default role for a new account is user.
An administrator account can be assigned the admin role.
The administrator role provides access to administrative functionality.

# Room Management

The administrator can manage hotel rooms.

Room information includes:
Room number
Room type
Room price
Room status

The application checks room availability before allowing bookings.

# Booking Management

Users can select available rooms and provide booking information.

The booking system stores:
Room number
Customer name
Check in date
Check out date
Username

The system checks booking information against existing reservations.

This helps prevent overlapping room reservations.

## Database

The application uses SQLite as its database.
The main database file is:
hotel.db

The database contains the following main tables.

users
rooms
bookings

# The database schema is created using:

database/schema.py
The database connection is handled through:
database/connection.py

## Site Reliability Engineering Implementation

The project was extended to demonstrate basic Site Reliability Engineering practices.
The SRE implementation follows the reliability cycle:

Monitor
Detect
Recover
Verify

The system also uses automated testing and CI CD automation.

# Application Monitoring

The application contains a monitoring service that checks important components of the hotel booking system.

The monitoring service is located at:
services/monitor_service.py

The monitoring system checks:
Database
Room service
Booking service

Database Monitoring

The database monitoring function checks whether the SQLite database can be accessed successfully.

The system executes a basic database query to confirm that the database is available.

When the database check succeeds, the system records a successful monitoring message in the log.

When the database check fails, the system records the failure.

Room Service Monitoring

The room monitoring function checks whether the rooms table can be accessed.

The system performs a query against the rooms table.

If the query succeeds, the room service is considered operational.

If the query fails, the failure is recorded in the application log.

Booking Service Monitoring

The booking monitoring function checks whether the bookings table can be accessed.

The system performs a query against the bookings table.

If the query succeeds, the booking service is considered operational.

If the query fails, the failure is recorded in the application log.

# Application Health Monitoring

The main monitoring function combines the results of the database, room, and booking checks.
The system reports that all systems are healthy only when all three checks succeed.

The monitoring process follows this sequence.
Start Monitoring
Check Database
Check Rooms
Check Bookings
All Checks Successful
Application Healthy

If one or more checks fail, the system starts the recovery process.

Screenshot Application Monitoring

Add a screenshot showing the application monitoring output here.

## Screenshot
Application Monitoring

# System Failure Detection

The monitoring service detects failures by handling exceptions generated when database operations fail.
Examples of failures include:
Missing database tables
Database connection failures
Room service database failures
Booking service database failures
Detected failures are written to the application log.

## Screenshot System Failure Detection
System Failure Detection

# Application Logging

The application uses Python logging to record system activity.
The logging implementation is located in:
logger.py

The log directory is:
logs

The main application log is:
logs/hotel.log

The logging system records different levels of application activity.
INFO
WARNING
ERROR

# Log Processing

The project includes a log processing service.
The log processing functionality analyzes the application log and counts messages according to their logging level.
The log processor is located at:
services/log_service.py

The processor identifies:
INFO messages
WARNING messages
ERROR messages
The system then reports the current log summary.

# Example output:
LOG SUMMARY
INFO
WARNING
ERROR

The log processor also provides a general indication of whether historical errors or warnings were found.