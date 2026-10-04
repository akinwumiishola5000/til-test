"""HoloSift: structure and ligand explorer for The Insilico Lab CADD Toolkit.

The tool itself is the single page in holosift.html. It runs in the visitor's
browser (3Dmol.js), so this Streamlit app only serves it full-width.
Run locally with:  streamlit run app.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

APP_DIR = Path(__file__).parent
HTML_FILE = APP_DIR / "holosift.html"
LOGO_ICON = APP_DIR / "logo_icon.png"
FRAME_HEIGHT = 1150  # px; the page scrolls inside this frame

st.set_page_config(
    page_title="HoloSift | The Insilico Lab",
    page_icon=str(LOGO_ICON) if LOGO_ICON.exists() else ":material/deployed_code:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Let the tool use the whole window: hide Streamlit's header, menu, footer and padding.
st.markdown(
    """
<style>
header[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stSidebar"], [data-testid="collapsedControl"], #MainMenu, footer { display: none !important; }
.block-container, [data-testid="stMainBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
[data-testid="stAppViewContainer"] > .main, [data-testid="stMain"] { padding: 0 !important; }
iframe { display: block; border: 0; }
</style>
""",
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def page_html() -> str:
    return HTML_FILE.read_text(encoding="utf-8")


def start_options() -> dict:
    """Read ?pdb=1M17 and ?view=struct|mols from the app address."""
    boot: dict = {}
    pdb = str(st.query_params.get("pdb", "")).strip().upper()
    if re.fullmatch(r"[0-9][A-Z0-9]{3}", pdb):
        boot["pdb"] = pdb
    view = str(st.query_params.get("view", "")).strip().lower()
    if view in {"struct", "mols", "home"}:
        boot["view"] = view
    return boot


if not HTML_FILE.exists():
    st.error("holosift.html is missing. Upload it to the repository next to app.py.")
    st.stop()

html = page_html().replace(
    "/*HOLOSIFT_BOOT*/", "window.HOLOSIFT_BOOT = " + json.dumps(start_options()) + ";", 1
)
components.html(html, height=FRAME_HEIGHT, scrolling=True)
