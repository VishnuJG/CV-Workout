# CV-Workout

Computer-vision workout assistant built as a **PES University capstone project** (UE19CS390A). The app uses a webcam, **MediaPipe Pose/Hands**, and **OpenCV** to track reps and form for exercises such as **arm curls** and **leg curls**, with optional desktop UI flows and a web-style dashboard under `code/`.

## Team

| Name | SRN | Email |
|------|-----|-------|
| Tejas D R | PES1UG19CS537 | tejasdr01@gmail.com |
| Vishnu J G | PES1UG19CS574 | jgvishnu2001@gmail.com |
| Srujan A S | PES1UG19CS509 | srujan12077@gmail.com |
| Pradeep V | PES1UG19CS330 | pradeepdeepu3303@gmail.com |

## Features

- **Real-time pose estimation** via MediaPipe Pose on live camera input.
- **Rep counting** for targeted exercises (see `code/armscurl.py`, `code/reps.py`, `noFrontEnd/reps.py`).
- **Leg curl tracking** in the no-frontend pipeline (`noFrontEnd/legcurls.py`).
- **Desktop login / session flow** with PySimpleGUI (`noFrontEnd/entry.py`, `noFrontEnd/newUser.py`).
- **Stats and persistence helpers** (`noFrontEnd/stats.py`, `noFrontEnd/dbFuns.py`).
- **Static admin-style UI templates** (Atlantis theme HTML under `code/`) for dashboards, charts, and layout demos.
- **Literature survey** materials under `LiteratureSurvey/` (papers, abstracts, review docs).

## Repository layout

```
CV-Workout/
├── README.md                 # This file
├── requirements.txt          # Python dependencies (mediapipe, opencv)
├── code/                     # CV pipelines + HTML UI templates
│   ├── armscurl.py           # Arm curl detection (MediaPipe + OpenCV)
│   ├── reps.py               # Rep-counting utilities
│   ├── yfunctions.py         # Shared geometry / angle helpers
│   └── *.html                # Dashboard / layout demo pages
├── noFrontEnd/               # PySimpleGUI desktop app (no web front-end)
│   ├── entry.py              # Login and routing to workouts
│   ├── front.py              # Main workout UI shell
│   ├── legcurls.py           # Leg curl exercise module
│   └── dbFuns.py             # User / session DB helpers
└── LiteratureSurvey/         # Capstone literature review assets
```

## Requirements

- Python 3.8+ (project developed on 3.x with OpenCV and MediaPipe).
- Webcam for live exercise tracking.
- Dependencies listed in `requirements.txt`:

  - `mediapipe`
  - `opencv-python` (imported as `cv2` in code)

Additional modules used in the desktop app (install if you run `noFrontEnd/`):

```bash
pip install PySimpleGUI
```

## Quick start

### 1. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install PySimpleGUI opencv-python
```

### 2. Run arm-curl demo (OpenCV window)

From the repo root:

```bash
cd code
python armscurl.py
```

Allow camera access when prompted. The script draws pose landmarks and tracks movement for curl repetitions.

### 3. Run desktop app (PySimpleGUI)

```bash
cd noFrontEnd
python entry.py
```

Use **Login** with a registered name/email or **New User** to create an account (see `newUser.py` and `dbFuns.py` for persistence behavior).

### 4. Browse static UI templates

Open any file under `code/` such as `index.html` or `charts.html` in a browser to preview layout and widget demos (no build step).

## How it works (high level)

1. **Capture** frames from the default camera (`cv2.VideoCapture`).
2. **Detect** body landmarks with MediaPipe Pose (and hands where needed).
3. **Compute** joint angles or vertical displacement between frames (`yfunctions.py` and exercise-specific logic).
4. **Count reps** when the motion crosses configured thresholds (`reps.py` / exercise modules).
5. **Present** feedback in an OpenCV window or the PySimpleGUI desktop shell.

## Literature & coursework

Review presentations, requirement specs, and collected papers live under `LiteratureSurvey/`. See `LiteratureSurvey/readme.md` for folder-specific notes.

## Limitations & notes

- Models expect reasonable lighting and a full upper/lower body in frame.
- `requirements.txt` is minimal; some scripts assume OpenCV and PySimpleGUI are installed separately.
- HTML under `code/` is template/demo content and is not wired to a production backend in this repo.

## License

No license file is present in the repository. Contact the authors for reuse terms.

---

*Capstone — Computer Vision based Workout application.*
