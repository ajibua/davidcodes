from django.shortcuts import render

BACKEND = [
    {
        "name": "PayoutIQ",
        "blurb": "Turns messy payout lists (pasted text or CSV) into verified records with Gemini, "
                 "flags duplicate accounts, and only disburses after a manual trigger and OTP confirmation.",
        "stack": ["FastAPI", "React", "Gemini API", "Supabase"],
        "links": [("Live", "https://payout-iq.vercel.app"), ("Code", "https://github.com/ajibua/PayoutIQ")],
    },
    {
        "name": "Momentum",
        "blurb": "Turns brain-dump text into an actionable plan. A two-stage Gemini pipeline surfaces "
                 "assumptions with confidence scores and blocks planning until ambiguity is resolved.",
        "stack": ["FastAPI", "Gemini API", "Python"],
        "links": [("Live", "https://momentum-rho-lac.vercel.app")],
    },
    {
        "name": "DevPrep.ai",
        "blurb": "Voice-based AI interview prep with a real-time WebSocket backend, Gemini and Deepgram in the loop.",
        "stack": ["Django", "PostgreSQL", "Celery/Redis", "Gemini API", "Deepgram"],
        "links": [],
    },
    {
        "name": "Mathify",
        "blurb": "Full-stack math social platform: seven-app Django architecture, DRF with JWT auth, "
                 "and a custom dark design system.",
        "stack": ["Django 5", "DRF", "SimpleJWT", "Tailwind"],
        "links": [("Live", "https://mathify-coral.vercel.app")],
    },
    {
        "name": "IFashion",
        "blurb": "E-commerce website for fashion lovers and Fashion designers. Ever experienced difficulty in reaching customers or don't have the funds to get a portfolio website for yourself? well, i guess this is for you.",
        "stack": ["FastAPI", "React", "Supabase", "Vercel"],
        "links": [("Live", "https://frontend-gamma-indol-3rqffdrv0i.vercel.app")],
    },
]

DATA_SCIENCE = [
    {
        "name": "BNPL Default Risk",
        "blurb": "Analysis of buy-now-pay-later default risk, and what breaks when a US-style dataset "
                 "meets a Nigerian market. Modeling and full write-up in progress.",
        "stack": ["Python", "pandas", "seaborn"],
        "status": "In progress",
        "links": [],
    },
]

CONTACT = [
    ("GitHub", "https://github.com/ajibua"),
    ("Email", "mailto:ajibuadomts@gmail.com"),
    ("Twitter", "https://x.com/murewa.py"),
    ("LinkedIn", "https://www.linkedin.com/in/david-ajibua-a471893a7"),
]


def index(request):
    return render(request, "index.html", {
        "backend": BACKEND,
        "data_science": DATA_SCIENCE,
        "contact": CONTACT,
    })