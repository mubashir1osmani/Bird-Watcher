from flask import Flask, request, render_template_string
import folium
import wolframalpha
from wolframclient.language import wl
from wolframclient.evaluation import WolframLanguageSession

import pandas as pd

#we need huge datasets of a particular country to use a proper UI

#testing dataset
endangered_species_data = [
    {"species": "California Condor", "lat": 34.0522, "lon": -118.2437},  # Los Angeles, CA
    {"species": "Florida Panther", "lat": 27.9944, "lon": -81.7603},      # Florida
    {"species": "Hawaiian Monk Seal", "lat": 21.3069, "lon": -157.8583},  # Honolulu, HI
    {"species": "Red Wolf", "lat": 35.7796, "lon": -78.6382},             # Raleigh, NC
    {"species": "Whooping Crane", "lat": 29.7604, "lon": -95.3698},       # Houston, TX
    {"species": "Kemp's Ridley Sea Turtle", "lat": 30.6954, "lon": -88.0399}, # Mobile, AL
]
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Add the endangered species data to the map
for species in endangered_species_data:
    folium.Marker(
        location=[species["lat"], species["lon"]],
        popup=f"{species['species']}",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

# Save the map to an HTML file
m.save("endangered_species_map.html")

m