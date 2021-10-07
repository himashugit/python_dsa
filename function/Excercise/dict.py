# nesting dictionary inside a dict

travel_log = {

    "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "total_visit": 12},
    "India": {"Cities_Visited": ["Delhi", "Gurgaon", "Faridabad"], "total_visit": 11 },
}

# Nesting Dict inside List
travel_log = [

    {"Country": "France","Cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visit": 12
    
    },
    {
    "Country":"India", "Cities_Visited": ["Delhi", "Gurgaon", "Faridabad"], 
    "total_visit": 11 
    },
]

print (travel_log[1]['Country'])