# SafeStride 🚶‍♂️🔊

### Real-Time Assistive Navigation System for the Visually Impaired

SafeStride is a smartphone-based assistive navigation system designed to help visually impaired users understand their surroundings, navigate outdoors, and stay connected with caregivers.

It uses **AI-based scene understanding, GPS navigation, voice guidance, and caregiver monitoring** without requiring specialized hardware.

## ✨ Features

* 👁️ **AI Scene Understanding** – Describes objects and surroundings using Google Gemini AI.
* 🚧 **Obstacle Detection** – Identifies obstacles and provides voice alerts.
* 🏠 **Indoor Assistance** – Provides real-time scene information using the smartphone camera.
* 🗺️ **Outdoor Navigation** – Provides walking directions using GPS and Google Maps.
* 🔊 **Voice Guidance** – Converts scene descriptions and navigation instructions into speech.
* 👨‍👩‍👦 **Caregiver Monitoring** – Allows caregivers to monitor the user's location and route.
* 🆘 **Emergency SOS** – Sends the user's location to the registered emergency contact.
* 🔐 **Secure Authentication** – Uses BCrypt and JWT for user authentication.

## 🏗️ Architecture

```text
Smartphone
    │
    ├── Camera
    ├── GPS
    ├── Microphone
    └── Speaker
          │
          ▼
   Python + Kivy App
          │
    ┌─────┴─────┐
    │           │
    ▼           ▼
Indoor Mode   Outdoor Mode
    │           │
    ▼           ▼
Gemini AI    Google Maps
    │           │
    └─────┬─────┘
          ▼
     Voice Guidance
          │
          ▼
    Flask Backend
          │
     ┌────┴────┐
     ▼         ▼
 Database   Caregiver Portal
```

## 🛠️ Technologies

* **Python 3.10**
* **Kivy 2.2**
* **OpenCV**
* **Google Gemini AI**
* **Google Maps Directions API**
* **pyttsx3**
* **geopy**
* **Flask**
* **MySQL / PostgreSQL**
* **BCrypt**
* **PyJWT**

## 🔄 How It Works

### Indoor Mode

```text
Camera
  ↓
OpenCV
  ↓
Gemini AI
  ↓
Scene Description
  ↓
Obstacle Detection
  ↓
Voice Alert
```

### Outdoor Mode

```text
GPS Location
  ↓
Google Maps Directions API
  ↓
Walking Route
  ↓
Turn-by-Turn Instructions
  ↓
Voice Guidance
```

The user's GPS location and route information can also be logged to the caregiver portal.

## 🚀 Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/SafeStride.git
cd SafeStride
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
DATABASE_URL=your_database_url
JWT_SECRET=your_jwt_secret
```

**Do not upload `.env` or API keys to GitHub.**

### Run Backend

```bash
python app.py
```

### Run Application

Launch the SafeStride Kivy application.

For Android deployment, the application can be packaged using **Buildozer**.

## 📁 Project Structure

```text
SafeStride/
│
├── app/
│   ├── main.py
│   ├── camera.py
│   ├── gps.py
│   ├── navigation.py
│   ├── analyze.py
│   └── tts.py
│
├── backend/
│   ├── app.py
│   ├── models/
│   ├── routes/
│   └── database/
│
├── caregiver_portal/
│   ├── templates/
│   └── static/
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## 🔮 Future Scope

* Offline AI assistance
* Haptic feedback through a wearable device
* Multilingual voice guidance
* Improved outdoor route handling
* Larger real-world usability studies

## 📌 Project

**SafeStride – Real-Time Scene Intelligence and Contextual Navigation for the Visually Impaired**

Developed as an academic project using Python, AI, computer vision, GPS, and web technologies.

## SafeStride

SafeStride is a safety and navigation assistance project.

## Main Modules

- Navigation
- AI Scene Analysis
- Backend Server
- Automated Testing
