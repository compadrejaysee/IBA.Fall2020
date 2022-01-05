#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from random import randrange
import random
import uuid


# In[7]:


list_states = []
list_cities = []
travelCode = [[1, "Air"], [2, "Bus"], [3, "Rail"]]
list_orgs = []


def randomizer(arg):
    return randrange(arg) + 1


def randomAddress():
    return (
        str(randrange(3000))
        + " Building "
        + str(randrange(21))
        + ", Street "
        + str(randrange(11))
    )


def randomContact():
    return "(021) 921" + str(randrange(10000, 99999))


def randomWebsite(arg):#websites
    return "https://www.organization" + str(arg) + ".com/" + uuid.uuid1().hex


for x in range(10000):#States
    list_states.append([(x + 1), "State " + str(x + 1)])

for x in range(1000000):#organizations
    list_orgs.append(
        [
            (x + 1),
            randomizer(len(list_states)),
            randomizer(len(travelCode)),
            "Organization " + str(x + 1),
            randomAddress(),
            randomContact(),
            randomWebsite(x + 1),
        ]
    )

for x in range(50000):#cities
    list_cities.append([(x + 1), randomizer(len(list_states)), "City " + str(x + 1)])

data_states = pd.DataFrame(list_states, columns=["State_ID", "Name"])
data_cities = pd.DataFrame(list_cities, columns=["City_ID", "State_FK", "Name"])
data_orgs = pd.DataFrame(
    list_orgs,
    columns=[
        "Org_ID",
        "State_FK",
        "TravelCode_FK",
        "Name",
        "Address",
        "Contact",
        "Website",
    ],
)
data_travelType = pd.DataFrame(travelCode, columns=["TravelType_ID", "TravelType"])
data_orgs.to_csv(r"C:\DWCSV\tourism_organisations.csv", index=False)
print(1)


# In[15]:


TOI_Type = [
    [1, "Monument"],
    [2, "Restaurant"],
    [3, "Museum"],
    [4, "Hotel"],
    [5, "Cafe"],
]
Event_Type = [
    [1, "Party"],
    [2, "Drama"],
    [3, "Dinner"],
    [4, "Concert"],
    [5, "Festival"],
]
Recurring = ["Yes", "No"]
list_TOI = []
list_TOI_Events = []


def randomOpeningTime():
    return str(randrange(8, 12)) + ":00 AM"


def randomClosingTime():
    return str(randrange(9, 12)) + ":00 PM"


def randomTOIWebsite(arg):
    return "https://www.thingsofIntereset" + str(arg) + ".com/" + uuid.uuid1().hex


def randomPriceRange():
    return [randrange(2000, 10000, 1000), randrange(15000, 30000, 1000)]


def randomDateGenerator():
    randYear = randrange(00, 21)
    randMonth = randrange(1, 12)
    randDay = randrange(1, 20)
    return [
        (str(randMonth) + "/" + str(randDay) + "/20" + ("0" if randYear < 10 else "") + str(randYear)),
        (str(randMonth) + "/" + str(randDay + randrange(1, 10)) + "/20" + ("0" if randYear < 10 else "") + str(randYear)),
    ]


for x in range(1000000):
    priceRange = randomPriceRange()
    list_TOI.append(
        [
            (x + 1),
            randomizer(len(list_cities)),
            randomizer(len(TOI_Type)),
            "Things of Interest " + str(x + 1),
            randomAddress(),
            randomContact(),
            randomOpeningTime(),
            randomClosingTime(),
            priceRange[0],
            priceRange[1],
            randrange(1, 6),
            randomTOIWebsite(x + 1),
        ]
    )

for x in range(5000000):
    randomDate = randomDateGenerator()
    list_TOI_Events.append(
        [
            (x + 1),
            randomizer(len(list_TOI)),
            randomizer(len(Event_Type)),
            "Event " + str(x + 1),
            randomDate[0],
            randomDate[1],
            random.choice(Recurring),
        ]
    )

data_TOI_Type = pd.DataFrame(TOI_Type, columns=["TOI_Type_ID", "TOI_Type"])
data_TOI_EventType = pd.DataFrame(Event_Type, columns=["EventType_ID", "EventType"])
data_TOI = pd.DataFrame(
    list_TOI,
    columns=[
        "TOI_ID",
        "City_FK",
        "TOI_Type_FK",
        "Name",
        "Address",
        "Contact",
        "Opening Time",
        "Closing Time",
        "Lower Price(Rs.)",
        "Higher Price(Rs.)",
        "Rating",
        "Website",
    ],
)
data_TOI_Events = pd.DataFrame(
    list_TOI_Events,
    columns=[
        "Event_ID",
        "TOI_FK",
        "EventType_FK",
        "Name",
        "Start Date",
        "End Date",
        "Recurring",
    ],
)
data_TOI_Events.to_csv(r"C:\DWCSV\TOI_Events.csv", index=False)
print(1)


# In[ ]:




