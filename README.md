# Mini-Nmap

A lightweight Python-based TCP port scanner inspired by Nmap, developed as a learning project to practice network programming, Python development, Docker, CI/CD, and DevSecOps concepts.

---

# Project Overview

Mini-Nmap is a command-line network scanner capable of scanning TCP ports on a target host, detecting open ports, retrieving service banners, and generating scan reports.

The project was progressively improved by integrating software engineering best practices such as:

- Unit testing with pytest
- Code quality analysis with flake8
- Docker containerization
- Continuous Integration with GitHub Actions
- Continuous Delivery using GitHub Container Registry (GHCR)
- Security analysis with pip-audit and Trivy

---

# Features

- TCP port scanning
- Scan custom port ranges
- Multi-threaded scanning
- Banner grabbing
- TXT report generation
- JSON report generation
- Scan duration measurement
- Input validation
- Error handling
- Unit tests using pytest
- Code quality verification using flake8
- Docker support
- Automatic CI/CD pipeline
- Dependency vulnerability scanning
- Docker image vulnerability scanning

---

# Project Architecture

```text
                 +----------------+
                 |    main.py     |
                 +-------+--------+
                         |
         +---------------+---------------+
         |                               |
         ▼                               ▼
 +----------------+             +------------------+
 | scanner/       |             | pipeline/        |
 |                |             |                  |
 | tcp_scan.py    |             | port_stage.py    |
 | banner.py      |             | service_stage.py |
 +----------------+             | report_stage.py  |
                                +------------------+
                                         |
                                         ▼
                                  reports/
```

---

# Project Structure

```text
mini-nmap/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pipeline/
├── scanner/
├── tests/
├── reports/
├── utils/
│
├── Dockerfile
├── .dockerignore
├── .flake8
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/amal18205/mini-nmap.git
cd mini-nmap
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Usage

Basic scan:

```bash
python main.py 192.168.1.10 20 100
```

Multi-threaded scan:

```bash
python main.py 192.168.1.10 20 1000 --threads 100
```

---

# Reports

After each scan, the application generates:

- `reports/scan_report.txt`
- `reports/scan_report.json`

The reports include:

- Target IP address
- Open ports
- Service banners
- Scan summary

---

# Docker

Build the Docker image:

```bash
docker build -t mini-nmap .
```

Run the scanner:

```bash
docker run mini-nmap 127.0.0.1 20 100
```

---

# CI/CD Pipeline

Every push to the `main` branch automatically triggers GitHub Actions.

Pipeline stages:

1. Install project dependencies
2. Run flake8
3. Execute pytest
4. Build the Docker image
5. Publish the image to GitHub Container Registry
6. Scan Python dependencies using pip-audit
7. Scan the Docker image using Trivy

---

# DevSecOps

The project integrates security checks into the CI/CD pipeline.

**pip-audit**

- Detects known vulnerabilities in Python dependencies.

**Trivy**

Scans the Docker image for:

- Vulnerable packages
- Operating system vulnerabilities
- Security issues

---

# Testing

Run unit tests:

```bash
pytest
```

Check code quality:

```bash
flake8 .
```

---

# Technologies Used

- Python 3
- Socket Programming
- ThreadPoolExecutor
- Pytest
- Flake8
- Docker
- GitHub Actions
- GitHub Container Registry
- pip-audit
- Trivy

---

# Future Improvements

Possible future enhancements include:

- UDP scanning
- Service version detection
- CSV report export
- Configurable timeout
- Colorized terminal output
- OS fingerprinting
- Scan progress indicator

---

# Author

**Amal Aziz**

Cybersecurity Engineering Student

GitHub: https://github.com/amal18205

---

# License

This project is distributed under the MIT License.
