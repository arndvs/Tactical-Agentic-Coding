# Natural Language SQL Interface

A web application that converts natural language queries to SQL using AI, built with FastAPI and Vite + TypeScript.

## Features

- 🗣️ Natural language to SQL conversion using OpenAI or Anthropic
- 📁 Drag-and-drop file upload (.csv and .json)
- 📊 Interactive table results display
- 🔒 SQL injection protection
- ⚡ Fast development with Vite and uv

## Prerequisites

- Python 3.10+
- Node.js 18+
- OpenAI API key and/or Anthropic API key

## Setup

### 1. Install Dependencies

```bash
# Backend
cd app/server
uv sync --all-extras

# Frontend
cd app/client
npm install
```

### 2. Environment Configuration

Set up your API keys in the server directory:

```bash
cd app/server
cp .env.sample .env
# Edit .env and add your API keys
```

## Quick Start

Use the provided script to start both services:

```bash
./scripts/start.sh
```

Press `Ctrl+C` to stop both services.

The script will:
- Check that `.env` exists in `app/server/`
- Start the backend on http://localhost:8000
- Start the frontend on http://localhost:5173
- Handle graceful shutdown when you exit

## Manual Start (Alternative)

### Backend
```bash
cd app/server
# .env is loaded automatically by python-dotenv
uv run python server.py
```

### Frontend
```bash
cd app/client
npm run dev
```

## Usage

1. **Upload Data**: Click "Upload Data" to open the modal
   - Use sample data buttons for quick testing
   - Or drag and drop your own .csv or .json files
   - Uploading a file with the same name will overwrite the existing table
2. **Query Your Data**: Type a natural language query like "Show me all users who signed up last week"
   - Press `Cmd+Enter` (Mac) or `Ctrl+Enter` (Windows/Linux) to run the query
3. **View Results**: See the generated SQL and results in a table format
4. **Manage Tables**: Click the × button on any table to remove it

## Development

### Backend Commands
```bash
cd app/server
uv run python server.py      # Start server with hot reload
uv run pytest               # Run tests
uv add <package>            # Add package to project
uv remove <package>         # Remove package from project
uv sync --all-extras        # Sync all extras
```

### Frontend Commands
```bash
cd app/client
npm run dev                 # Start dev server
npm run build              # Build for production
npm run preview            # Preview production build
```

## Project Structure

```
app/
├── client/                 # Vite + TypeScript frontend
│   ├── src/
│   │   ├── api/           # API client
│   │   ├── types.d.ts     # TypeScript types
│   │   └── main.ts        # App entry point
│   └── vite.config.ts     # Vite configuration
│
└── server/                # FastAPI backend
    ├── core/              # Core modules
    │   ├── data_models.py # Pydantic models
    │   ├── file_processor.py
    │   ├── llm_processor.py
    │   ├── sql_processor.py
    │   └── insights.py
    ├── db/                # SQLite database
    └── server.py          # FastAPI app
```

## API Endpoints

- `POST /api/upload` - Upload CSV/JSON file
- `POST /api/query` - Process natural language query
- `GET /api/schema` - Get database schema
- `POST /api/insights` - Generate column insights
- `GET /api/health` - Health check

## Security

- Only SELECT queries are allowed
- SQL injection protection via keyword blocking
- File upload validation
- CORS configured for local development

## Troubleshooting

**Backend won't start:**
- Check Python version: `python --version` (requires 3.12+)
- Verify API keys are set: `echo $OPENAI_API_KEY`

**Frontend errors:**
- Clear node_modules: `rm -rf node_modules && npm install`
- Check Node version: `node --version` (requires 18+)

**CORS issues:**
- Ensure backend is running on port 8000
- Check vite.config.ts proxy settings