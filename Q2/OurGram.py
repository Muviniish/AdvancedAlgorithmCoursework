from UDGraph import UDGraph
from Person import Person

class OurGram:

    my_graph = None

    def __init__(self):
        self.my_graph = UDGraph()

    def add_new_profile(self, name, privacy, biography):
        person = Person(name, privacy, biography)
        self.my_graph.addVertex(person)
        return person
    
    def add_follow(self, follower, following):
        self.my_graph.addEdge(follower, following)

    def remove_follow(self, follower, following):
        self.my_graph.remove_edge(follower, following)
    
    def display_profile(self, index):
        person = list(self.my_graph.get_vertices())[index-1]
        print(f"Name: {person.getName()}")
        if person.getPrivacy().upper()=='U':
            print(f"Biography: {person.getBiography()}")
        else:
            print(f"{person.getName()} has a private profile")

    def display_all_profile(self):
        for i, person in enumerate(self.my_graph.get_vertices()):
            print(f"{i+1}.) {person.getName()}")

    def display_neighbours(self, vertex):
        neighbours = self.my_graph.get_vertices()
        for i, person in enumerate(neighbours):
            if person != vertex:
                print(f"{i+1} {person.getName()}")
    
    def display_followers(self, vertex):
        followers = self.my_graph.listIncomingAdjacentVertex(vertex)
        print("Followers List: ")
        for person in followers:
            print(f"- {person.getName()}")

    def display_following(self, vertex):
        following = self.my_graph.listOutgoingAdjacentVertex(vertex)
        print("Following List: ")
        for person in following:
            print(f"- {person.getName()}")


def main():
    global gram
    gram = OurGram()

    karen = gram.add_new_profile("Karen", "P", "Just an ordinary woman")
    susy = gram.add_new_profile("Susy", "U", "Just a normal person")
    brian = gram.add_new_profile("Brian", "U", "Just an ordinary teenager")
    calvin = gram.add_new_profile("Calvin", "U", "Just an ordinary man")
    elon = gram.add_new_profile("Elon", "P", "Just a hardworking man")

    gram.add_follow(karen, susy)
    gram.add_follow(karen, brian)
    gram.add_follow(karen, elon)

    gram.add_follow(elon, karen)
    gram.add_follow(elon, calvin)

    gram.add_follow(brian, karen)
    gram.add_follow(brian, susy)

    mainMenu()

def mainMenu():
    print("***********************************************")
    print("Welcome to Our Gram, Your New Social Media App:")
    print("***********************************************")
    print("1. View names of all profiles")
    print("2. View details for any profiles")
    print("3. View followers of any profile")
    print("4. View followed accounts of any profile")
    print("5. Add a user profile")
    print("6. Follow a user profile")
    print("7. Unfollow a user profile")
    print("8. Quit")
    print("***********************************************")
    while True:
        opt = int(input("Enter your choice (1-8): "))
        if opt == 1:
            opt1()
            break
        elif opt == 2:
            opt2()
            break
        elif opt == 3:
            opt3()
            break
        elif opt == 4:
            opt4()
            break
        elif opt == 5:
            opt5()
            break
        elif opt == 6:
            opt6()
            break
        elif opt == 7:
            opt7()
            break
        elif opt == 8:
            print("Have a great day")
            break
        else:
            print("Wrong input. Please enter again")

def opt1():
    print("=======================================")
    print("View All Profile Names:")
    print("=======================================")
    gram.display_all_profile()
    mainMenu()

def opt2():
    print("=======================================")
    print("View Details for Any Profile:")
    print("=======================================")
    gram.display_all_profile()
    view = int(input("Select whose profile to view : "))
    gram.display_profile(view)
    mainMenu()
    
def opt3():
    print("=======================================")
    print("View Followers for Any Profile:")
    print("=======================================")
    gram.display_all_profile()
    view = int(input("Select whose profile to view: "))
    person = list(gram.my_graph.get_vertices())[view-1]
    gram.display_followers(person)
    mainMenu()

def opt4():
    print("=======================================")
    print("View Followed Accounts for Any Profile:")
    print("=======================================")
    gram.display_all_profile()
    view = int(input("Select whose profile to view: "))
    person = list(gram.my_graph.get_vertices())[view-1]
    gram.display_following(person)
    mainMenu()

def opt5():
    print("=======================================")
    print("Add User Profile:")
    print("=======================================")
    name = str(input("Please enter user name: "))
    while True:
        privacy = str(input("Please select your privacy (P - protected || U - unprotected): "))
        if privacy.upper()=='U':
            break
        elif privacy.upper()=='P':
            break
    biography = str(input("Please enter your biography: "))
    gram.add_new_profile(name, privacy, biography)
    print(f"{name} has been added")
    mainMenu()

def opt6():
    print("=======================================")
    print("Follow a User Profile:")
    print("=======================================")
    gram.display_all_profile()
    from_profile = int(input("Select your profile: "))
    person1 = list(gram.my_graph.get_vertices())[from_profile-1]
    gram.display_neighbours(person1)
    to_profile = int(input("Select the profile you wish to follow: "))
    person2 = list(gram.my_graph.get_vertices())[to_profile-1]
    gram.add_follow(person1, person2)
    print(f"{person2.getName()} Followed")
    mainMenu()

def opt7():
    print("=======================================")
    print("Unfollow a User Profile:")
    print("=======================================")
    gram.display_all_profile()
    from_profile = int(input("Select your profile: "))
    person1 = list(gram.my_graph.get_vertices())[from_profile-1]
    gram.display_neighbours(person1)
    to_profile = int(input("Select the profile you wish to unfollow: "))
    person2 = list(gram.my_graph.get_vertices())[to_profile-1]
    gram.remove_follow(person1, person2)
    print(f"{person2.getName()} Unfollowed")
    mainMenu()

if __name__=="__main__":
    main()