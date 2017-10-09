global idcounter
idcounter = 1001

class Patient(object):

    def __init__(self, id, name, allergies=["None"], bed_number="none"):
        self.id = id
        global idcounter
        idcounter += 1
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number

    
class Hospital(object):
    def __init__(self, name, capacity, patients=[]):
        self.patients = patients
        self.name = name
        self.capacity = capacity
        self.open_beds = []
        for idx in range (1, self.capacity+1):
            self.open_beds.append(idx)
    
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "The hospital is full."
            global idcounter
            idcounter-= 1
        else:
            self.patients.append(patient)
            patient.bed_number = self.open_beds.pop(0)
            print patient.name + " has been assigned bed #", str(patient.bed_number)
        return self

    def discharge(self, patient):
        patient.bed_number = "None"
        self.open_beds.append(patient.bed_number)
        self.patients.remove(patient)
        print ""
        print "Patient {} has been discharged.".format(patient.name)
        return self
    
    def display_info(self):
        print ""
        print "There are currently {} patients at {}".format(str(len(self.patients)), self.name) 
        for search in self.patients:
            print ""
            print "Patient ID:", str(search.id)
            print "Bed #:", str(search.bed_number)
            print "Name:", search.name
            print "Allergies:", search.allergies
        return self

Tom = Patient(idcounter, "Tom")
Larry = Patient(idcounter, "Larry", "Mellon")
Kathy = Patient(idcounter, "Kathy")
Lynn = Patient(idcounter, "Lynn", "Lactose Intollerant")
Ed = Patient(idcounter, "Ed")

hospital = Hospital("Plano Medical Center", 3)

hospital.admit(Tom).admit(Larry).admit(Kathy).admit(Lynn).display_info()
hospital.discharge(Larry).display_info()
hospital.admit(Ed).display_info()
