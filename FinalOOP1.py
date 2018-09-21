class AppointmentBook:
    '''Tracks multiple appointments'''
   def __init__(self,appointments):
       self.appointments={}
   def addAppointment(self, day, description):
       if description not in self.appointments.values:
       self.appointments[day]= description
   def isScheduled(self, appointment):
       for appointment in self.appointments:
       return appointment in self.appointments
import appointmentbook
ab=appointmentbook.AppointmentBook()
ab.addAppointment('Monday', 'Dentist')
ab.addAppointment('Saturday', 'Personal Trainer')
ab.isScheduled('Physician')
