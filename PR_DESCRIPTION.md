# PR: Frontend Improvements — Expanded Input + Checklist UI

Summary
-------
This PR contains frontend UX improvements and documentation to make local testing easier. It expands the case input, adds a visible status checklist (green tick / red cross), and includes a PR description file with run instructions.

What changed (visual checklist)
- ✅ Expanded input textbox — larger textarea for pasting long case text
- ✅ Creative placeholder and helpful hint messaging
- ✅ Local frontend dev server (`frontend/server.py`) for quick testing
- ✅ CORS middleware added to backend to allow frontend requests
- ❌ PDF extraction integration (server-side): pending — displayed as a red cross in the UI

Files modified or added
- `frontend/index.html` — expanded textarea, hint, and checklist UI
- `frontend/server.py` — lightweight dev server (unchanged)
- `frontend/Dockerfile` — (unchanged)
- `api/main.py` — added `CORSMiddleware` for `http://localhost:3000`
- `PR_DESCRIPTION.md` — this file

Run locally
-----------
1. Create and activate a Python venv:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the API (in repo root):

```powershell
.\.venv\Scripts\python -m uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

3. Run the frontend dev server:

```powershell
cd frontend
python server.py
# open http://localhost:3000
```

Notes
-----
- PDF extraction is intentionally left as pending (❌) and displayed accordingly in the UI checklist. I can implement client-side PDF text extraction (pdf.js) or server-side extraction (`/extract_pdf`) next — tell me which you prefer.
- If you want this branch pushed to your GitHub, ensure the remote `origin` is configured with write access from this environment. The next step will create a branch `feature/frontend-checklist` and push it.

PR message (suggested)
---------------------
Add frontend UX improvements: expanded case input, creative placeholder, and visible status checklist; document run steps and note pending PDF extraction.
