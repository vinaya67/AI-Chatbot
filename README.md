🚀 AI-powered Jenkins Log Analyzer (Stage 3)
This project provides a secure, on-premises AI log analyzer that:

Accepts Jenkins logs (text / screenshot / file)

Uses LLM (Ollama) for advanced log analysis

If unresolved → Automatically creates a Rally ticket for DevOps team

Fully self-hosted (No cloud dependency)

Enforced HTTPS + reverse proxy (Nginx)

📂 Project Structure
bash
Copy
Edit
.
├── frontend/       # React + TypeScript UI
├── backend/        # FastAPI backend (AI + Rally integration)
├── nginx/          # Reverse proxy + SSL termination
├── docker-compose.yml
└── README.md
🌐 Architecture
bash
Copy
Edit
User → https://yourdomain.com → Nginx (SSL/Proxy)
 ↓
Frontend (React)
 ↓
API → /api/analyze/
 ↓
Backend (FastAPI) → Ollama (LLM analysis)
               ↘ If failed → Rally ticket
⚙️ Prerequisites
Docker + Docker Compose installed

Valid domain name + SSL certs (or self-signed for testing)

Rally API Key + Project URL

🛠️ Setup Guide
1️⃣ Clone repo
bash
Copy
Edit
git clone https://your-company-git/repo.git
cd repo
2️⃣ Configure Rally credentials
Edit .env file or directly in docker-compose.yml (backend section):

env
Copy
Edit
RALLY_API_KEY=your-rally-api-key
RALLY_PROJECT=https://rally1.rallydev.com/slm/webservice/v2.0/project/12345
3️⃣ Configure SSL certs
Place certs inside nginx/ssl/
(For testing — self-signed cert:)

bash
Copy
Edit
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout nginx/ssl/server.key -out nginx/ssl/server.crt \
  -subj "/C=IN/ST=Karnataka/L=Bangalore/O=MyCompany/CN=yourdomain.com"
4️⃣ Build and start all services
bash
Copy
Edit
docker compose up --build -d
💡 Usage
Access UI: https://yourdomain.com

Upload Jenkins log (text / file / screenshot)

AI (Ollama) analyzes

If unresolved → Ticket created automatically in Rally

📊 Tech Stack
Layer	Tech
Frontend	React + TypeScript + Tailwind
Backend	FastAPI (Python)
AI Engine	Ollama (on-prem LLM)
Reverse Proxy	Nginx
Ticketing	Rally API

🔐 Security Features
HTTPS enforced (SSL certs)

Reverse proxy with security headers

Secrets (Rally API key) injected via environment vars

🧹 Maintenance
To stop all services

bash
Copy
Edit
docker compose down
To rebuild

bash
Copy
Edit
docker compose up --build -d

