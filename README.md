# _TravelAdvisor_ 🚢🌊

  **TravelAdvisor** is an AI-powered travel planning assistant that uses a multi-agent system built with [CrewAI](https://docs.crewai.com/). It creates a **personalized 7-day itinerary** based on your _starting point, destination, travel date, and interests_ — all powered by real-time data and intelligent agents.

  ## ✨ Overview

  _TravelAdvisor_ leverages two key agents working together:
  
  - **Local Tour Guide** – Finds places, events, and activities based on your interests.
  - **Travel Concierge** – Handles logistics, costs, and ensures a balanced itinerary.
  
  Features Include:
  
  - ✅ **Real-time internet search** (via Serper API)
  - ✅ **Cost estimation tool**
  - ✅ **Agent + Task configurations in YAML**
  - ✅ **Groq-powered LLaMA 3.3 70B for reasoning and generation**

Output Screenshots:
1. Local Tour Guide's response
![Local Tour Guide's Output](https://github.com/user-attachments/assets/72104080-9f1a-4547-8393-7bc19d8f2963)

2. Travel Concierge's response
![image](https://github.com/user-attachments/assets/01321111-d590-4cdf-8c9c-82b71f104a8e)
![image](https://github.com/user-attachments/assets/6c19f89b-b71b-492b-9d5b-bc6b21029b9a)


## ⚙️ Installation
Clone the repo
  ```bash
  git clone https://github.com/its-shrivatsavan/TravelAdvisor.git
  ```
Go to TravelAdvisor Folder
  
```bash
# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # .\venv\Scripts\Activate.ps1 [Powershell]
```
Install the Dependencies
```bash
# Install dependencies
pip install -r requirements.txt
```

Setup your .env file
```bash
GROQ_API_KEY = "INSERT YOUR KEY HERE"
SERPER_API_KEY = "INSERT YOUR KEY HERE"
```

Run the main.py file
```bash
python main.py
```
