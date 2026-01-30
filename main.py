# 🌍 CLIMATE ACTION INDIA - PURE PYTHON
# Works on any PC, no install needed
print("\n🌱 WELCOME TO CLIMATE ACTION INDIA")
print("Protect Today. Sustain Tomorrow\n")

# ----------------------------
# CHATBOT KNOWLEDGE
# ----------------------------
knowledge = {
    "climate change": "Climate change = long-term rise in Earth's temperature.",
    "global warming": "Global warming is caused by greenhouse gases like CO2.",
    "india": "India faces floods, heatwaves, pollution, and glacier melting.",
    "pollution": "Pollution harms health & environment.",
    "renewable energy": "Solar & wind energy reduce carbon emissions.",
    "solution": "Plant trees, save energy, reduce plastic, use clean transport.",
    "carbon footprint": "Carbon footprint measures how much CO2 you produce."
}

# ----------------------------
# FUNCTIONS
# ----------------------------
def chatbot():
    print("\n🤖 CLIMATE CHATBOT (Type 'exit' to leave)")
    while True:
        user = input("You: ").lower()
        if user == "exit":
            break
        reply = "I can answer about climate change, India, pollution, renewable energy, and solutions."
        for key in knowledge:
            if key in user:
                reply = knowledge[key]
                break
        print("Bot:", reply)

def climate_graph():
    print("\n📊 TEMPERATURE RISE IN INDIA (2000-2024)")
    years = [2000,2005,2010,2015,2020,2024]
    temp = [0.2,0.3,0.5,0.8,1.1,1.3]
    for i in range(len(years)):
        bars = int(temp[i]*10)
        print(f"{years[i]} : {'█'*bars} {temp[i]}°C")

def solutions():
    print("\n🌱 GLOBAL WARMING SOLUTIONS")
    for s in ["Use Renewable Energy","Plant Trees","Save Water","Reduce Plastic",
              "Use Public Transport","Save Electricity","Spread Awareness"]:
        print("✅", s)

def carbon_calculator():
    print("\n🧮 CARBON FOOTPRINT CALCULATOR")
    try:
        km = float(input("Enter travel km/month: "))
        electricity = float(input("Enter electricity units/month: "))
    except:
        print("❌ Please enter valid numbers!")
        return
    travel_emission = km*0.21
    electricity_emission = electricity*0.5
    total = round(travel_emission + electricity_emission,2)
    print(f"🌍 Your Carbon Footprint: {total} kg CO2/month")
    if total<100: print("💚 Great! You are eco-friendly.")
    elif total<250: print("⚠ Try reducing emissions.")
    else: print("❌ High footprint! Take climate action.")

def india_facts():
    print("\n🇮🇳 CLIMATE FACTS ABOUT INDIA")
    facts = [
        "India is among the most climate-affected countries.",
        "Heatwaves are increasing every year.",
        "Delhi is one of the most polluted cities.",
        "Glaciers in Himalayas are melting fast.",
        "Floods and droughts are becoming frequent."
    ]
    for f in facts: print("🌏",f)

# ----------------------------
# MAIN MENU
# ----------------------------
while True:
    print("\n==============================")
    print("🌍 CLIMATE ACTION MAIN MENU")
    print("1. Climate Graph (India)")
    print("2. Global Warming Solutions")
    print("3. Climate Chatbot")
    print("4. Carbon Footprint Calculator")
    print("5. India Climate Facts")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    if choice=="1": climate_graph()
    elif choice=="2": solutions()
    elif choice=="3": chatbot()
    elif choice=="4": carbon_calculator()
    elif choice=="5": india_facts()
    elif choice=="6":
        print("\n🌱 Thank you for supporting Climate Action! Bye!")
        break
    else:
        print("❌ Invalid choice. Try again.")
