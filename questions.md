Diego Miquélez de Mendiluce

***1. How long did you spend on the coding test? What would you add to your solution if you had more time? If you didn't spend much time on the coding test then use this as an opportunity to explain what you would add.***

30 minutes. I have focused on doing integration testing from a developer perspective, I would have done unitary testing so I could check my code was working as expected. 

***2. What was the most useful feature added to the latest version of your chosen language? Please include a snippet of code that shows how you've used it.***

Python 3.11 added a feature improving the traceback error system. Before the upgrade, Python did not perform the traceback of the erros specifying which the error was in a proper way. Here is an example:

    scientists = [

    {
        "name": {"first": "Grace", "last": "Hopper"},
        "birth": {"year": 1906, "month": 12, "day": 9},
        "death": {"year": 1992, "month": 1, "day": 1},
    },
    {"name": {"first": "Euclid"}},
    {"name": {"first": "Abu Nasr", "last": "Al-Farabi"}, "birth": None},
    {
        "name": {"first": "Srinivasa", "last": "Ramanujan"},
        "birth": {"year": 1887},
        "death": {"month": 4, "day": 26},
    }
    
    ]

***Before the update:***

    > scientists[1]

    {'name': {'first': 'Euclid'}}

    > dict_to_person(scientists[1])

    Traceback (most recent call last):
    ...
  
    File "/home/realpython/scientists.py", line 12, in dict_to_person
  
    name=f"{info['name']['first']} {info['name']['last']}",
    KeyError: 'last'


***After the update:***

    > dict_to_person(scientists[0])

    Person(name='Grace Hopper', life_span=(1906, 1992))

    > scientists[1]

    {'name': {'first': 'Euclid'}}

    > dict_to_person(scientists[1])

    Traceback (most recent call last):
      ...
  
    File "/home/realpython/scientists.py", line 12, in dict_to_person
  
    name=f"{info['name']['first']} {info['name']['last']}",
                                    ~~~~~~~~~~~~^^^^^^^^
    KeyError: 'last'

***3. How would you track down a performance issue in production? Have you ever had to do this?***

I could review production or execution logs and check the hardware specific specs. Yes, I used to work in the maintenance area of a company checking for the logs and fixing performance issues.

***4. How would you improve the Lantek API that you just used?***

I would add an API so I can restart the DB to its initial values in dev/stage environments when the data was not corrupted/polluted.

