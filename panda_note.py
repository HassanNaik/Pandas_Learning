import pandas as pd

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])

# rank = pd.Series([3,1,2,4])

# df = pd.DataFrame({
#     "lang":languages,
#     "Rank":rank
# })

# df = pd.concat([languages,rank],axis=1)
# df.columns = ["Lang","Rank"]

#df = pd.read_csv("speeds.csv")

#df = pd.read_excel("speeds.xlsx")

#df = pd.DataFrame([("Python",3), ("JavaScript",1), ("HTML",2), ("SQL",4)],columns=["Language","Ranking"])

#df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie",55)], columns=["Name","Age"])

#print(languages)
#print(rank)
#print(df)


# Activity 1
# Create a dataframe to store information on the planets of the solar system. 
# For each planet, record:
# • its name
# • the average temperature 
# • the planet’s radius in KM
# • the planet’s colour
# • an interesting feature of the planet.


# Activity 2
# We turned an Excel file into a dataframe using .read_excel()
# Research into turning a dataframe into an Excel file and turn your planets frame into a spreadsheet.

# Mercury:
# Average temperature: 167°C
# Radius: 2,439.7 km
# Colour: Grey
# Feature: Mercury has the most eccentric orbit of all the planets, meaning it’s the least circular and changes shape as it orbits the Sun.

# Venus:
# Average temperature: 464°C
# Radius: 6,051.8 km
# Colour: Yellowish-white
# Feature: Venus has a runaway greenhouse effect that makes it hotter than Mercury, despite being further from the Sun.

# Earth:
# Average temperature: 15°C
# Radius: 6,371 km
# Colour: Blue and green
# Feature: Earth is the only planet known to support life and has liquid water on its surface.

# Mars:
# Average temperature: -60°C
# Radius: 3,389.5 km
# Colour: Reddish-brown
# Feature: Mars has the largest volcano in the solar system, Olympus Mons, which is about three times the height of Mount Everest.

# Jupiter:
# Average temperature: -145°C
# Radius: 69,911 km
# Colour: Orange and white bands
# Feature: Jupiter’s Great Red Spot is a massive storm that’s been raging for at least 400 years.

# Saturn:
# Average temperature: -178°C
# Radius: 58,232 km
# Colour: Pale gold
# Feature: Saturn’s rings are the most extensive and brightest in the solar system, made mostly of ice particles.

# Uranus:
# Average temperature: -224°C
# Radius: 25,362 km
# Colour: Light blue
# Feature: Uranus rotates on its side, making it unique among the planets, with an axial tilt of about 98 degrees.

# Neptune:
# Average temperature: -214°C
# Radius: 24,622 km
# Colour: Deep blue
# Feature: Neptune has the strongest winds in the solar system, reaching speeds of up to 2,100 km/h.

name = pd.Series(["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"])

temp = pd.Series(["167 C","464 C","15 C","-60 C","-145 C","-178 C","-224 C","-214 C"])

radius = pd.Series(["2,439.7 km","6,051.8 km","6,371 km","3,389.5 km","69,911 km","58,232 km","25,362 km","24,622 km"])

colour = pd.Series(["Grey","Yellowish-white","Blue and green","Reddish-brown","Orange and white bands","Pale gold","Light blue","Deep blue"])

feature = pd.Series(["Mercury has the most eccentric orbit of all the planets.","Venus has a runaway greenhouse effect that makes it hotter than Mercury","Earth is the only planet known to support life and has liquid water on its surface.","Mars has the largest volcano in the solar system.","Jupiter's Great Red Spot is a massive storm that's been raging for at least 400 years.","Saturn's rings are the most extensive and brightest in the solar system.","Uranus rotates on its side, making it unique among the planets.","Neptune has the strongest winds in the solar system."])


df = pd.DataFrame({
    "Planet":name,
    "Temperature":temp,
    "Radius":radius,
    "Colour":colour,
    "Feature":feature
    
})

#print(df)

with pd.ExcelWriter("planet.xlsx") as writer:
    df.to_excel(writer)

df = pd.read_excel("planet.xlsx")
