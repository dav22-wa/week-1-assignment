# CryptoBuddy: Rule-Based Crypto Investment Chatbot

print("👋 Hey there! I'm CryptoBuddy – your friendly crypto guide for smart and green investments!")
print("💡 Ask me things like 'Which crypto is trending up?' or 'What's the most sustainable coin?'")
print("🔒 Disclaimer: Crypto is risky—always do your own research!")
print("-" * 60)

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def get_user_input():
    return input("\nYou: ").lower()

def crypto_advisor(query):
    if "sustainable" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "trending" in query or "up" in query:
        trending_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_coins:
            print(f"CryptoBuddy: These cryptos are trending up: {', '.join(trending_coins)} 📈")
        else:
            print("CryptoBuddy: Hmm... nothing seems to be trending up right now!")

    elif "long-term" in query or "growth" in query:
        candidates = [name for name, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7]
        if candidates:
            print(f"CryptoBuddy: I'd suggest {candidates[0]} for long-term growth. 🌿 It’s green and growing!")
        else:
            print("CryptoBuddy: Tough call! None stand out for long-term growth at the moment.")

    elif "energy" in query or "eco" in query:
        low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
        if low_energy:
            print(f"CryptoBuddy: {', '.join(low_energy)} use low energy! ⚡ Good for the planet!")
        else:
            print("CryptoBuddy: None of these coins are low-energy at the moment.")

    elif "profitable" in query or "best" in query:
        profitable = [name for name, data in crypto_db.items()
                      if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable:
            print(f"CryptoBuddy: Based on trends and market cap, {', '.join(profitable)} looks profitable! 💰")
        else:
            print("CryptoBuddy: No clear winners on profitability right now!")

    elif "exit" in query or "quit" in query:
        print("CryptoBuddy: Goodbye! 🚀 Stay sharp, stay green!")
        return False

    else:
        print("CryptoBuddy: Hmm, I didn’t get that. Try asking about sustainability, profitability, or trends.")

    return True

active = True
while active:
    user_query = get_user_input()
    active = crypto_advisor(user_query)
