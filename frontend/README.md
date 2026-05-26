# AI Enterprise Council Frontend

A premium dark-mode UI for the AI Council evaluation system. Real-time JSON output, beautiful animations, and professional design inspired by Linear and Raycast.

## Quick Start

### Prerequisites
- Docker Compose running the API (`docker compose up -d`)
- Python 3.7+ (for the local server)

### Run the Frontend Server

```bash
cd frontend
python server.py
```

Then open your browser to:
```
http://localhost:3000
```

The API server should be running at:
```
http://localhost:8000
```

## Features

- 🎨 **Premium Design System**
  - Animated ambient gradient blobs
  - Multi-layer shadows & glow effects
  - Cinematic lighting pools
  - Responsive dark-mode UI

- 📄 **Case Input**
  - Drag-and-drop PDF upload zone
  - Textarea for decision case description
  - Example case pre-filled

- 🎯 **Live Output**
  - Real-time JSON response from `/council/run`
  - Agent vote breakdown (5 agents)
  - Risk scores & confidence metrics
  - Session tracking

- ⚡ **Interactions**
  - One-click council evaluation
  - Beautiful loader state
  - Error handling with helpful messages
  - Clear button to reset

## API Integration

The frontend calls:
```
POST /council/run
Content-Type: application/json

{
  "case": "Your decision case text...",
  "context": null
}
```

Response includes:
- `session_id`: Unique evaluation session
- `verdict`: Final council decision
- `aggregate_risk_score`: Combined risk (0-1)
- `council_confidence`: Decision confidence (0-1)
- `vote_breakdown`: Per-agent votes with metrics
- `quorum_size`: Number of agents voting

## Design System

### Colors
- **Background:** Deep near-black (`#050506`) with layered gradients
- **Accent:** Indigo (`#5E6AD2`) for interactive elements
- **Text:** Off-white (`#EDEDEF`) for contrast

### Animations
- **Timing:** 200-300ms with expo-out easing
- **Entrance:** Fade + scale effects
- **Hover:** Subtle 4-8px movement, brightness increase

### Typography
- **Font:** Inter, system-ui
- **Headers:** Bold with gradient overlay
- **Body:** Regular weight, relaxed line-height

## Customization

Edit `index.html` to:
- Change accent color: Update `--color-accent` in `:root`
- Modify title: Update `.header-title h1` text
- Adjust blob animation: Edit `@keyframes float-blob-*`
- Customize output format: Modify `renderOutput()` function

## Troubleshooting

### Frontend loads but API calls fail
- Ensure `docker compose up -d` is running
- Check API logs: `docker compose logs council-api`
- Verify API is at `http://localhost:8000/health`

### PDF upload doesn't work
- PDF parsing requires additional dependencies (currently shows file selected)
- Implement PDF text extraction using `pdfjs-dist` if needed

### Styling looks different
- Clear browser cache (Ctrl+Shift+Delete)
- Try different browser (Chrome/Firefox/Edge recommended)
- Check for browser extensions blocking styles

## Architecture

```
frontend/
├── index.html      # Main UI with embedded CSS & JS
├── server.py       # Local development server with CORS
└── README.md       # This file
```

The frontend is **self-contained** (no build process) and uses vanilla JavaScript with embedded styles for simplicity.

## Next Steps

1. ✅ Start the frontend server
2. ✅ Open http://localhost:3000
3. ✅ Enter a decision case
4. ✅ Click "Run Council Evaluation"
5. ✅ See JSON output from all 5 agents

For prompt engineering improvements, edit `/agents/base/base_agent.py` to refine agent personalities and decision logic.
