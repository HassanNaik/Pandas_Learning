import pandas as pd

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



# Activity 3
# Amend your solar system dataframe to add:
# • Who discovered each planet
# • The year it was discovered
# • Elements of its composition

# Mercury:
# Discoverer: Known to ancient civilizations, no single discoverer.
# Year of Discovery: Prehistoric times.
# Composition: Mostly iron and nickel with a silicate crust and mantle.

# Venus:
# Discoverer: Known to ancient civilizations, no single discoverer.
# Year of Discovery: Prehistoric times.
# Composition: Thick atmosphere of carbon dioxide, with clouds of sulfuric acid, and a rocky surface.

# Earth:
# Discoverer: Well, you're on it! Known since ancient times.
# Year of Discovery: Prehistoric times.
# Composition: Nitrogen and oxygen-rich atmosphere, liquid water, silicate rocks, and a metallic core.

# Mars:
# Discoverer: Known to ancient civilizations, no single discoverer.
# Year of Discovery: Prehistoric times.
# Composition: Iron oxide (rust), giving it a red appearance, with a thin atmosphere of carbon dioxide.

# Jupiter:
# Discoverer: Known to ancient civilizations, no single discoverer.
# Year of Discovery: Prehistoric times.
# Composition: Mostly hydrogen and helium, with traces of methane, ammonia, and water vapor.

# Saturn:
# Discoverer: Known to ancient civilizations, no single discoverer.
# Year of Discovery: Prehistoric times.
# Composition: Mostly hydrogen and helium, with methane and ammonia.

# Uranus:
# Discoverer: Sir William Herschel.
# Year of Discovery: 1781.
# Composition: Hydrogen, helium, and methane (which gives it a blue-green color).

# Neptune:
# Discoverer: Johann Galle and Urbain Le Verrier.
# Year of Discovery: 1846.
# Composition: Hydrogen, helium, and methane.

# Activity 4
# Add Pluto, and all related data, to your dataframe.

# Pluto:
# Average temperature: -229°C
# Radius: 1,188.3 km
# Colour: Brownish-yellow
# feature: Pluto has a heart-shaped glacier named Tombaugh Regio, and it’s only about two-thirds the width of Earth's moon.
# Discoverer: Clyde Tombaugh
# Year of discovery: 1930
# Composition: Mostly ice and rock, with a thin atmosphere composed of nitrogen, methane, and carbon monoxide.


name = pd.Series(["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"])

temp = pd.Series(["167 C","464 C","15 C","-60 C","-145 C","-178 C","-224 C","-214 C"])

radius = pd.Series(["2,439.7 km","6,051.8 km","6,371 km","3,389.5 km","69,911 km","58,232 km","25,362 km","24,622 km"])

colour = pd.Series(["Grey",
                    "Yellowish-white",
                    "Blue and green",
                    "Reddish-brown",
                    "Orange and white bands",
                    "Pale gold",
                    "Light blue",
                    "Deep blue"])

feature = pd.Series(["Eccentric orbit",
                     "runaway greenhouse",
                     "only planet known to support life",
                     "largest volcano",
                     "Red Spot is a massive storm",
                     "Saturn's rings are the most extensive",
                     "Uranus rotates on its side",
                     "Neptune has the strongest winds"])


df = pd.DataFrame({
    "Planet":name,
    "Temperature":temp,
    "Radius":radius,
    "Colour":colour,
    "Feature":feature
    })

#print(df)

# with pd.ExcelWriter("planet.xlsx") as writer:
#     df.to_excel(writer)

# df = pd.read_excel("planet.xlsx")


# task 3

#print(df)

# df ["Discoverer"] = ["none","N/A","N/A","N/A","N/A","N/A","Sir William Herschel","Johann Galle and Urbain Le Verrier"]

# df ["Year of Discovery"] = ["N/A","N/A","N/A","N/A","N/A","N/A","1781","1846"]

# df ["Composition"] = ["Iron","Carbon dioxide","Nitrogen and oxygen","Iron oxide","Mostly hydrogen and helium","Mostly hydrogen and helium","Hydrogen, helium, and methane","Hydrogen, helium, and methane"]

new_q_c = pd.DataFrame({
    "Discoverer": ["N/A","N/A","N/A","N/A","N/A","N/A","Sir William Herschel","Johann Galle and Urbain Le Verrier"],
    "Year of Discovery": ["N/A","N/A","N/A","N/A","N/A","N/A","1781","1846"],
    "Composition": ["Iron","Carbon dioxide","Nitrogen and oxygen","Iron oxide","Mostly hydrogen and helium","Mostly hydrogen and helium","Hydrogen, helium, and methane","Hydrogen, helium, and methane"]
    })

df = pd.concat([df,new_q_c], axis=1)

#print(df)

#task 4

# Pluto:
# Average temperature: -229°C
# Radius: 1,188.3 km
# Colour: Brownish-yellow
# feature: Pluto has a heart-shaped glacier named Tombaugh Regio, and it’s only about two-thirds the width of Earth's moon.
# Discoverer: Clyde Tombaugh
# Year of discovery: 1930
# Composition: Mostly ice and rock, with a thin atmosphere composed of nitrogen, methane, and carbon monoxide.

add_pluto = pd.DataFrame({
    "Planet":["Pluto"],
    "Temperature":["-229°C"],
    "Radius":["1,188.3 km"],
    "Colour":["Brownish-yellow"],
    "Feature":["two-thirds the width of Earth's moon"],
    "Discoverer":["Clyde Tombaugh"],
    "Year of Discovery":["1930"],
    "Composition":["Mostly ice and rock"]
})

df = pd.concat([df,add_pluto],ignore_index=True)

#print(df)


with pd.ExcelWriter("planet.xlsx") as writer:
    df.to_excel(writer)

#df = pd.read_excel("planet.xlsx")

# Activity 5
# Show the data you have for Venus – Jupiter using slice notation.

#print(df.loc[1:4:3,])

# Activity 6
# Create a program which allows a user to type in the name of the planet they want to view information about.
# Ask the user to specify the column name they wish to see, or type “all” for everything.

user_input = input("Enter Planet Name or All : ")