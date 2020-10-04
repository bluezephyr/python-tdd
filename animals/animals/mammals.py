class MammalsSet:
    def __init__(self, animals_db):
        """
        The mammals set object needs access to an object of the type animals.animal_db.Animals
        class. This is given as input when the mammals set is initialized.
        """
        self.mammals = []
        self.animals_db = animals_db

    def refresh(self):
        """
        Request the database to refresh the set of mammals.
        """
        self.animals_db.animals()
