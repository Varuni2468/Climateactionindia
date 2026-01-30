# 🌍 CLIMATE ACTION PROJECT (PURE PYTHON)
# No Flask, No Extra Libraries Needed

print("\n🌍 WELCOME TO CLIMATE ACTION INDIA 🌱")
print("Protect Today. Sustain Tomorrow.\n")

# -------------------------
# CHATBOT KNOWLEDGE BASE
# -------------------------
knowledge = {
    "climate change": "Climate change means long-term rise in Earth's temperature.",
    "global warming": "Global warming is caused by greenhouse gases like CO2.",
    "india": "India faces heatwaves, floods, pollution, and glacier melting.",
    "pollution": "Air pollution causes health and environmental damage.",
    "renewable energy": "Solar and wind energy reduce carbon emissions.",
    "solution": "Plant trees, save energy, reduce plastic, and use clean transport.",
    "carbon footprint": "Carbon footprint is the amount of CO2 you produce.",
    "trees": "Trees absorb CO2 and reduce global warming."
}

# -------------------------
# CHATBOT FUNCTION
# -------------------------
def chatbot():
    print("\n🤖 CLIMATE CHATBOT")
    print("Ask about climate change, India climate, pollution, renewable energy, solutions.")
    print("Type 'exit' to leave chatbot.")
    
    while True:
        user = input("\nYou: ").lower()
        if user == "exit":
            break
        
        found = False
        for key in knowledge:
            if key in user:
                print("Bot:", knowledge[key])
                found = True
                break
        
        if not found:
            print("Bot: I know about climate change, India climate, pollution, renewable energy, and solutions.")

# -------------------------
# CLIMATE GRAPH (TEXT)
# -------------------------
def climate_graph():
    print("\n📊 TEMPERATURE RISE IN INDIA")
    
    years = [2000, 2005, 2010, 2015, 2020, 2024]
    temp = [0.2, 0.3, 0.5, 0.8, 1.1, 1.3]
    
    for i in range(len(years)):
        bars = int(temp[i] * 10)
        print(years[i], ":", "█" * bars, temp[i], "°C")

# -------------------------
# GLOBAL WARMING SOLUTIONS
# -------------------------
def solutions():
    print("\n🌱 SOLUTIONS FOR GLOBAL WARMING")
    sol = [
        "Use Renewable Energy",
        "Plant More Trees",
        "Save Water",
        "Reduce Plastic",
        "Use Public Transport",
        "Save Electricity",
        "Spread Awareness"
    ]
    for s in sol:
        print("✅", s)

# -------------------------
# CARBON FOOTPRINT CALCULATOR
# -------------------------
def carbon_calculator():
    print("\n🧮 CARBON FOOTPRINT CALCULATOR")
    
    km = float(input("Enter travel km per month: "))
    electricity = float(input("Enter electricity units per month: "))
    
    travel_emission = km * 0.21
    electricity_emission = electricity * 0.5
    total = round(travel_emission + electricity_emission, 2)
    
    print("\n🌍 Your Carbon Footprint:", total, "kg CO2/month")
    
    if total < 100:
        print("💚 Great! You are eco-friendly.")
    elif total < 250:
        print("⚠ Try reducing emissions.")
    else:
        print("❌ High footprint! Take climate action.")

# -------------------------
# INDIA CLIMATE FACTS
# -------------------------
def india_facts():
    facts = [
        "India is among the most climate-affected countries.",
        "Heatwaves are increasing every year.",
        "Delhi is one of the most polluted cities.",
        "Glaciers in Himalayas are melting fast.",
        "Floods and droughts are becoming frequent."
    ]
    print("\n🇮🇳 CLIMATE FACTS ABOUT INDIA")
    for f in facts:
        print("🌏", f)

# -------------------------
# MAIN MENU
# -------------------------
while True:
    print("\n==============================")
    print("🌍 CLIMATE ACTION MAIN MENU")
    print("1. Climate Change Graph (India)")
    print("2. Global Warming Solutions")
    print("3. Climate Chatbot")
    print("4. Carbon Footprint Calculator")
    print("5. India Climate Facts")
    print("6. Exit")
    
    choice = input("\nChoose an option (1-6): ")
    
    if choice == "1":
        climate_graph()
    elif choice == "2":
        solutions()
    elif choice == "3":
        chatbot()
    elif choice == "4":
        carbon_calculator()
    elif choice == "5":
        india_facts()
    elif choice == "6":
        print("\n🌱 Thank you for supporting Climate Action!")
        break
    else:
        print("\n❌ Invalid choice. Try again.")
