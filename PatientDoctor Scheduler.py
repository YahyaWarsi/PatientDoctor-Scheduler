#appointment times for days of week 

MondayappointmentTimes = ["9-9:30", "9:30-10",
                          ]

TuesdayappointmentTimes = ["10:30-11", "11-11:30", "11:30-12",
                           ]

WednesdayappointmentTimes = ["2:30-3", "3-3:30", "3:30-4"]

ThursdayappointmentTimes = ["1:30-2", "2-2:30", "2:30-3"]

FridayppointmentTimes = ["9-9:30", "9:30-10",
                         "10-10:30"]



class Patient():

    #self values taken from user input
    def __init__(self, day, timeSlot):
        self.day = day
        self.timeSlot = timeSlot

    
    def slotRemove():
        #when day is fully booked, remove from list
        if not appointmentTimes:
            daysOfWeek.remove(dayChosen)

        if (timeChosen == "back"):
            Doctor.run()

        #when appointment time is booked, remove from list and display appointment details to user
        if (timeChosen in appointmentTimes):
            appointmentTimes.remove(timeChosen)
            print(name + " has booked for " +
                  dayChosen + " at " + timeChosen + "\n")

            Patient.bookAnother()

        else:
            print("time not available")


    #after appointment booked, ask user if they want book another
    def bookAnother():
        book = input(
            "Would you like to book another appointment?(answer with yes or no)\n")
        if (book == "yes"):
            Doctor.run()
        else:
            print("Invalid input")
            Patient.bookAnother()


class Doctor():
    #receive input for name, the desired  day and  time slot
    def run():
        global name
        name = input("Enter your name: \n")
        global daysOfWeek
        daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if not MondayappointmentTimes:
            daysOfWeek.remove("Monday")
        if not TuesdayappointmentTimes:
            daysOfWeek.remove("Tuesday")
        if not WednesdayappointmentTimes:
            daysOfWeek.remove("Wednesday")
        if not ThursdayappointmentTimes:
            daysOfWeek.remove("Thursday")
        if not FridayppointmentTimes:
            daysOfWeek.remove("Friday")
        

        #once input for day received, assign the corresponding list 
        print(', '.join(daysOfWeek))
        global dayChosen
        dayChosen = input(
            'Please Select which day you will like to book your appointment \n')
        global appointmentTimes
        if (dayChosen == "Monday"):
            appointmentTimes = MondayappointmentTimes

        elif (dayChosen == "Tuesday"):
            appointmentTimes = TuesdayappointmentTimes

        elif (dayChosen == "Wednesday"):
            appointmentTimes = WednesdayappointmentTimes

        elif (dayChosen == "Thursday"):
            appointmentTimes = ThursdayappointmentTimes

        elif (dayChosen == "Friday"):
            appointmentTimes = FridayppointmentTimes
        else:
            print("invalid input, try again")
            Doctor.run()

        print(', '.join(appointmentTimes))
        global timeChosen
        timeChosen = input(
            'Please Select which slot you will like to book your appointment for. To go back type "back" \n')
       
        Patient.slotRemove()



Doctor.run()
docSchedule = Patient(dayChosen, timeChosen)
