class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} (Material: {self.material})"
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}

    def add_part(self, part):
        self.__parts[part.name] = part

    def display_state(self):
        if not self.__parts:
            return "Le bateau n'a pas de pièces."
        return "\n".join(str(part) for part in self.__parts.values())

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            self.__parts[part_name] = new_part
        else:
            print(f"La pièce {part_name} n'existe pas.")
    
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            self.__parts[part_name].change_material(new_material)
        else:
            print(f"La pièce {part_name} n'existe pas.")
# Exemple de test de changement de matériau
part1 = Part("Mât", "Bois")
print(part1)  # Affiche : Mât (Material: Bois)

# Changer le matériau du mât
part1.change_material("Acier")
print(part1)  # Affiche : Mât (Material: Acier)
class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        return f"La vitesse maximale du {self.name} est de {self.max_speed} km/h."
class ShipWithHistory(Ship):
    def __init__(self, name):
        super().__init__(name)
        self.history = []

    def log_history(self, action):
        self.history.append(action)

    def display_history(self):
        if not self.history:
            return "Aucune modification n'a été effectuée."
        return "\n".join(self.history)


def menu():
    print("Menu du bateau:")
    print("1. Afficher l'état du bateau")
    print("2. Remplacer une pièce")
    print("3. Modifier le matériau d'une pièce")
    print("4. Afficher l'historique des modifications")
    print("5. Quitter")
    
    choice = input("Que voulez-vous faire? (1/2/3/4/5): ")
    return choice


def run():
    ship = ShipWithHistory("Le Vaisseau de l'Aube")
    
    # Création de pièces
    part1 = Part("Mât", "Bois")
    part2 = Part("Voile", "Toile")
    
    ship.add_part(part1)
    ship.add_part(part2)

    while True:
        choice = menu()
        
        if choice == '1':
            print(ship.display_state())
        
        elif choice == '2':
            part_name = input("Nom de la pièce à remplacer: ")
            new_name = input("Nom de la nouvelle pièce: ")
            new_material = input("Matériau de la nouvelle pièce: ")
            new_part = Part(new_name, new_material)
            ship.replace_part(part_name, new_part)
            ship.log_history(f"Remplacé {part_name} par {new_name}.")
        
        elif choice == '3':
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            ship.change_part(part_name, new_material)
            ship.log_history(f"Modifié le matériau de {part_name} en {new_material}.")
        
        elif choice == '4':
            print(ship.display_history())
        
        elif choice == '5':
            print("Au revoir!")
            break
        
        else:
            print("Choix invalide. Essayez encore.")

run()
