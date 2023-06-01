import random

# Define tabla rhythms and details
tabla_rhythms = {
    "Teental": {"beats": 16, "division": [4, 4, 4, 4], "vibhag": "X 2 0 3"},
    "Jhoomra": {"beats": 14, "division": [3, 4, 3, 4], "vibhag": "X 2 0 3"},
    "Dhamar": {"beats": 14, "division": [5, 2, 3, 4], "vibhag": "X 2 0 3"},
    # Add more rhythms
}

# Define Gharanas
gharanas = ["Delhi Gharana", "Lucknow Gharana", "Ajrada Gharana",
            "Farukhabad Gharana", "Benares Gharana", "Punjab Gharana"]

def generate_rhythm():
    rhythm_name = random.choice(list(tabla_rhythms.keys()))
    rhythm = tabla_rhythms[rhythm_name]
    return rhythm_name, rhythm["beats"], rhythm["division"], rhythm["vibhag"]

def generate_gharana():
    return random.choice(gharanas)

# Generate random tabla pattern
rhythm_name, beats, division, vibhag = generate_rhythm()
gharana = generate_gharana()

print(f"Generated Tabla Pattern:")
print(f"Rhythm Name: {rhythm_name}")
print(f"Beats: {beats}")
print(f"Division: {'+'.join(map(str, division))}")
print(f"Vibhag: {vibhag}")
print(f"Gharana: {gharana}")
