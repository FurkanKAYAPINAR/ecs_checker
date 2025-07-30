# EDNS Client Subnet (ECS) Remote Detection Tool - CVE-2025-40766

This tool checks whether a remote DNS resolver supports **EDNS Client Subnet (ECS)** — a DNS extension that could expose systems to cache poisoning or information leakage vulnerabilities such as **CVE-2025-40776**.

## 🔍 What It Does

- Sends a DNS query with ECS options
- Detects whether ECS is enabled on the target resolver
- Works on both Linux/macOS (Python) and Windows (PowerShell)

## 💻 Usage

### Python (Linux/macOS)
```bash
pip install -r requirements.txt
python3 ecs_check.py --domain example.com --dns 8.8.8.8
