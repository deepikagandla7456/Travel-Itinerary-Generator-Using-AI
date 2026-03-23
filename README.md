# [Travel Itinerary Generator Using AI](https://deepikagandla7456.pythonanywhere.com/)


[![GitHub license](https://img.shields.io/github/license/deepikagandla7456/Travel-Itinerary-Generator-Using-AI)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/deepikagandla7456/Travel-Itinerary-Generator-Using-AI)]()
[![GitHub contributors](https://img.shields.io/github/contributors/deepikagandla7456/Travel-Itinerary-Generator-Using-AI)]()
[![GitHub last-commit](https://img.shields.io/github/last-commit/deepikagandla7456/Travel-Itinerary-Generator-Using-AI)]()


<img title="Travel-Itinerary-Generator" align='right' src="/static/logo.png" alt="Travel Itinerary Generator Logo" width="250"/>

Plan your dream trip effortlessly with the Travel Itinerary Generator Using AI! This powerful trip planner is your ultimate companion for crafting seamless travel experiences. Whether you're embarking on a road trip, city excursion, or overseas adventure, our tool simplifies the entire planning process.


<p align="left">
Make your travel dreams a reality. Start planning your next adventure with the Travel Itinerary Generator today!
</p>
<p align="center">
<i>Explore, discover, and make every trip unforgettable.</i>
</p>

## Table of Contents

- [Travel Itinerary Generator Using AI](#travel-itinerary-generator-using-ai)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Limitations \& Future Work](#limitations--future-work)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Setup and Installation](#setup-and-installation)
  - [API Keys](#api-keys)
  - [Usage](#usage)
  - [Screenshots](#screenshots)
  - [License](#license)

## About

Travel Itinerary Generator Using AI is a computer program that empowers travelers to effortlessly create personalized travel itineraries. By considering user's interests, budgets, and travel dates, this application generates comprehensive lists of activities, attractions, and accommodations. Whether you're an experienced traveler or a novice, the Travel Itinerary Generator is your key to saving time and ensuring an enriching and well-rounded travel experience.

## Limitations & Future Work
- The Travel Itinerary Generator works only based on the user's source and destination and time of travel.

***Future Work***

- The Travel Itinerary Generator Using AI is not able to generate itineraries for multiple destinations.
- The Travel Itinerary Generator Using AI is not able to suggest hotels and flights.
- **Real-time Collaboration:** In an increasingly interconnected world, we plan to introduce real-time collaboration features. Users will be able to share their itineraries with travel companions or collaborators, making group travel planning an effortless and collaborative experience.

## Features

- **Weather Forecast:** The Travel Itinerary Generator Using AI provides a weather forecast of the destination for the whole travel time.
- **Travel Itinerary:** The Travel Itinerary Generator Using AI provides a travel itinerary for the whole travel time in an optimum budget.
- **Translation Feature:** The Travel Itinerary Generator Using AI includes a translation tool to help users to communicate in the local language of their destination
## Requirements

- Python 3.13
- Flask
- Flask-SQLAlchemy
- deep_translator

## Setup and Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/deepikagandla7456/Travel-Itinerary-Generator-Using-AI.git
  
   cd Travel-Itinerary-Generator-Using-AI
2. Install required packages:

   ```shell
   pip install -r requirements.txt
   ```

## API Keys
- Visual Crossing Weather API Key: [Sign up](https://www.visualcrossing.com/weather-api) for a free account and get your API key.
- Groq API Key: [Sign up](https://console.groq.com/keys) for a free account and get your API key.

## Usage
- Please follow the instructions below to run the application locally.

Write API keys: In a `.env` file.
```shell
WEATHER_API_KEY='Your Visual Crossing Weather API Key'
SECRET_KEY='Your Flask secret key'
GROQ_API_KEY='Your Groq API Key'
```
and save it in the root directory of the project.

Run the following command to start the application:
```shell
python wsgi.py
```

## Screenshots

**Home Page of Travel Itinerary Generator without Login.**
![Image](https://github.com/user-attachments/assets/d4e9e71e-d68b-4e56-bc22-c5bda4aa4cc9)

**Register Page / Sign Up**
![Image](https://github.com/user-attachments/assets/490fcab4-b7e6-455a-a604-76020fc3af40)

**Login Page**
![Image](https://github.com/user-attachments/assets/1940ae76-43d6-46d4-a135-fd219108c18f)

**For Testing, I have taken Source Point as Hyderabad & Destination as Delhi, Starting Date of Journey: 25/03/2026, Return Date: 30/03/2026**
![Image](https://github.com/user-attachments/assets/3099135c-96a5-4d89-85f7-cdff95672fb7)

**Itinerary Page's**
![Image](https://github.com/user-attachments/assets/20044f5b-4307-440e-bd27-b769dcbc8b7b)

![Image](https://github.com/user-attachments/assets/58d1ab9c-9dcc-4244-a464-750f1de6acd3)

**Wheather Forecast**
![Image](https://github.com/user-attachments/assets/d5384d48-2864-456a-bbd5-04a3e70cb630)

**Translation Feature**
![Image](https://github.com/user-attachments/assets/94547878-a72b-421f-aee9-4488173e75f6)

![Image](https://github.com/user-attachments/assets/609fb1fb-96af-405d-ab79-c7664fb0702d)

## License

This project is licensed under the [Apache License 2.0](LICENSE) - see the [LICENSE](LICENSE) file for details.
