from Faculty import Faculty

class Faculties:
    def __init__(self):
        self.faculties = []
        self.faculties.append(Faculty("John Smith", "john.smith@uts.com", "user222"))
        self.faculties.append(Faculty("Jane Tyler", "jane.tyler@uts.com", "super123"))

        self.faculties.append(Faculty("Test Test", "a", "a"))

    # Lookup pattern to find matching faculty from email and password.
    def faculty(self, email, password):
        for faculty in self.faculties:
            if faculty.matches(email, password):
                return faculty
        return None
