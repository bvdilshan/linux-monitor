# Linux Monitor 🚀

A lightweight **Linux system monitoring platform** built with **FastAPI, Prometheus, Grafana, and Docker**.
This project collects Linux system metrics and visualizes them through modern monitoring dashboards.

---

## 📌 Features

* CPU monitoring
* Memory monitoring
* Disk usage monitoring
* Process monitoring
* Linux kernel metrics (`/proc`)
* Network statistics
* System load monitoring
* Prometheus metrics endpoint
* Grafana dashboard visualization
* Fully containerized using Docker

---

## 🧠 Architecture

```
Linux Kernel (/proc)
        │
        ▼
linux-monitor API (FastAPI)
        │
        ▼
Prometheus (metrics collection)
        │
        ▼
Grafana (visual dashboards)
```

---

## 🛠 Tech Stack

* Python
* FastAPI
* Prometheus
* Grafana
* Docker
* Docker Compose

---

## 📁 Project Structure

```
linux-monitor
│
├── api
│   └── main.py
│
├── monitor
│   ├── cpu.py
│   ├── memory.py
│   ├── disk.py
│   ├── process.py
│   ├── kernel_cpu.py
│   ├── kernel_memory.py
│   ├── load.py
│   └── network.py
│
├── prometheus
│   └── prometheus.yml
│
├── Dockerfile
├── docker-compose.yml
│
├── requirements.txt
├── README.md
│
├── .gitignore
└── .dockerignore
```

---

## ⚙️ Installation

### Clone repository

```
git clone https://github.com/your-username/linux-monitor.git
cd linux-monitor
```

---

### Run with Docker

Start the monitoring stack:

```
docker compose up --build
```

Run in background:

```
docker compose up -d
```

Stop services:

```
docker compose down
```

---

## 🌐 Access Services

| Service     | URL                        |
| ----------- | -------------------------- |
| FastAPI API | http://localhost:8000/docs |
| Prometheus  | http://localhost:9090      |
| Grafana     | http://localhost:3000      |

Grafana login:

```
username: admin
password: admin
```

---

## 📊 Example Metrics

Prometheus collects metrics from:

```
http://linux-monitor:8000/metrics
```

Example metrics:

```
system_cpu_usage_percent
system_memory_usage_percent
```

---

## 📈 Grafana Dashboard

Create panels using queries:

```
system_cpu_usage_percent
system_memory_usage_percent
```

Visualization types:

* Time series
* Stat panels
* Gauge charts

---

## 🐳 Docker Services

The project uses Docker containers:

```
linux-monitor
prometheus
grafana
```

Start all services using Docker Compose.

---

## 🚀 Future Improvements

* Kubernetes deployment
* Alerting with Prometheus Alertmanager
* Grafana auto-provisioned dashboards
* CI/CD pipeline with GitHub Actions
* Authentication for API

---

## 👨‍💻 Author

Vinoth Dilshan

---

