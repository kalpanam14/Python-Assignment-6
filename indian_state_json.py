import json

# Defining a dictionary
capital_dic = {
    'Karnataka': 'Bangalore',
    'Kerala': 'Trivandrum',
    'TamilNadu': 'Chennai',
    'Haryana': 'Chandigarh',
    'Bihar': 'Patna',
    'Himacha Pradesh': 'Shimla',
    'Telangana': 'Hydrebad'
}

# Writing dictionary values into JSON file
with open("indian_states.json", "w") as outfile:
    json.dump(capital_dic, outfile)
    print("JSON File Created Successfully....\n", outfile)
