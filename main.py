from owlready2 import *

onto = get_ontology("goa.owl").load()

user_interest = "Adventure"

for destination in onto.Destination.instances():

    for activity in destination.hasActivity:

        interests = [i.name for i in activity.recommendedFor]

        if user_interest in interests:
            print("Recommended Destination:", destination.name)
            print("Activity:", activity.name)