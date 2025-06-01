
# 🔮 Jyotishi -A Kundali Chart Generator & Summarizer

- 🚀 **Jyotishi** is a Streamlit-based web app that automates the generation of Kundali (birth chart) visuals from [AstroSage.com](https://www.astrosage.com/) using Selenium and Python. It captures key astrological charts and presents them through a user-friendly interface. The primary goal is to help users access all the essential charts and insights needed for astrological analysis.
- 🔴App Demo: (https://drive.google.com/file/d/1kNf4TbPiH9hdp7DGzivU4rY3Hg5zHjyn/view?usp=drive_link)

---

## 📸 Features

- 🪔 Generates **8 essential Kundali charts**:
  - Birth Chart
  - Mangal Dosh
  - Kal Sarpa Dosh
  - Dasha Analysis
  - Ascendant Chart
  - Career Chart
  - Today’s Horoscope
  - Numerology
- 🧠 Summarizes charts
- ⚙️ Powered by **Selenium** automation and **Streamlit** UI
- 💻 Designed for **local use or web deployment**

---

## 🗂️ Project Structure

```
Jyotishi/
│
├── app.py                 # Selenium scraper that logs into AstroSage and takes chart screenshots
├── app2.py                # Streamlit frontend that calls app.py and displays charts
├── requirements.txt       # All dependencies
└── README.md              # You're here!
```

---

## 🛠️ Tech Stack

| Component   | Tech                       |
|------------|----------------------------|
| Frontend   | 🧾 Streamlit                |
| Backend    | 🕸 Selenium (Firefox)       |
| Charts     | 📷 Screenshots from AstroSage |
| Language   | 🐍 Python                   |

---

## 📦 Setup Instructions

### 1. Clone this Repo

```bash
git clone https://github.com/imabhnv/Kundali-Summarizer.git
cd jyotishi
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> `requirements.txt` should include:
```txt
streamlit
selenium
webdriver-manager
```

### 3. Run Locally

```bash
streamlit run app2.py
python -m streamlit run app2.py
```

---

## 🧪 Usage

1. Enter full name, gender, birth date, time, and place.
2. Click **"🔮 Analyze Kundali"**
3. Wait 20–30 seconds while charts are fetched via Selenium.
4. View your astrological charts rendered below the form.

---


## 🚀 Deployment

You can deploy it easily using:

| Platform       | Support |
|----------------|---------|
| 🏗 Railway      | ✅ Headless Selenium (recommended) |
| 🔧 Render (Docker) | ✅ |
| 🌐 Streamlit Cloud | ❌ (no Selenium support) |

---

## ⚠️ Notes

- 🛑 **AstroSage.com** is being scraped, ensure you do not abuse the site.
- 🧩 Firefox & Geckodriver are used by default.
- 📍 Update hardcoded image paths if deploying remotely.
- 🛡 Make sure to handle exceptions when site structure changes.

---

## ✨ Credits

- Developed by **Abhinav Varshney**
- Astrology data via **[AstroSage](https://www.astrosage.com/)** 
- UI powered by **Streamlit**
- Automation by **Selenium WebDriver**

---

## ❤️ Footer

> 🧠 *“Coding meets Cosmos.”*  
> Developed with love, powered by coffee ☕ and curiosity 🌌.
