"""
RivNox — Marketing Website
===========================
A modern FastAPI application serving the marketing site for RivNox,
an AI-driven forecasting and planning company.

Run with:
    uvicorn main:app --reload

Then visit http://127.0.0.1:8000
"""

from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="RivNox",
    description="AI-driven forecasting and planning for operations that run on precision.",
    version="1.0.0",
)

# Mount static files (CSS, images, JS, etc.)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Landing page — hero, capabilities, solutions, CTA."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page — mission, values, and leadership team."""
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/origin-story", response_class=HTMLResponse)
async def origin_story(request: Request):
    """Origin story page — senior-led agentic engineering model."""
    return templates.TemplateResponse("origin_story.html", {"request": request})


@app.get("/solutions/asset-replenishment", response_class=HTMLResponse)
async def asset_replenishment(request: Request):
    """Asset replenishment forecasting solution page."""
    return templates.TemplateResponse("asset_replenishment.html", {"request": request})


@app.get("/solutions/supply-chain-workforce", response_class=HTMLResponse)
async def supply_chain_workforce(request: Request):
    """Supply chain workforce planning solution page."""
    return templates.TemplateResponse("supply_chain_workforce.html", {"request": request})


@app.get("/solutions/beer-production-plan", response_class=HTMLResponse)
async def beer_production_plan(request: Request):
    """Beer production planning solution page."""
    return templates.TemplateResponse("beer_production_plan.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact page — enquiry form."""
    return templates.TemplateResponse("contact.html", {"request": request, "submitted": False})


@app.post("/contact", response_class=HTMLResponse)
async def contact_submit(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
):
    """Handle contact form submission (demo — just re-renders with a thank-you)."""
    return templates.TemplateResponse(
        "contact.html",
        {
            "request": request,
            "submitted": True,
            "form_name": name,
            "form_email": email,
            "form_message": message,
        },
    )
