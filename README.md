# 🖥️ Datacenter Live Monitor

A full-stack, real-time web application designed to monitor datacenter server metrics. It tracks CPU usage and temperature, dynamically assigning health statuses (Healthy, Warning, Critical) and visualizing the data on a live NOC (Network Operations Center) dashboard.

## 🚀 Key Features

* **Robust RESTful API:** Built from scratch using Python and **FastAPI**, handling high-performance asynchronous requests.
* **Live Data Visualization:** A responsive, dark-mode dashboard built with **HTML/CSS/JS** and **Chart.js** that auto-updates without page reloads.
* **Endpoint Security:** Implemented custom header validation (`x-api-key`) to secure POST requests and prevent unauthorized metric generation.
* **Database Integration:** Utilizes **SQLite** and **SQLAlchemy ORM** to persistently store server metrics and retrieve historical data.
* **Cloud Deployment:** CI/CD pipeline integrated with **Render** for live cloud hosting.

## 🛠️ Tech Stack

**Backend:** Python 3, FastAPI, SQLAlchemy, Uvicorn
**Frontend:** JavaScript (Fetch API), Chart.js, HTML5, CSS3
**Database:** SQLite
**Deployment:** Render

## 📡 API Endpoints Quick Reference

| Method | Endpoint | Description | Security |
| :--- | :--- | :--- | :--- |
| `GET` | `/servers/` | Retrieves all active server metrics for the dashboard. | Open |
| `GET` | `/servers/{id}/history` | Retrieves the 5 most recent metrics for a specific server. | Open |
| `POST` | `/servers/` | Creates a new server metric entry. | **API Key Required** |

## 💻 Local Development Setup

To run this project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/datacenter-monitor.git](https://github.com/yourusername/datacenter-monitor.git)
   cd datacenter-monitor