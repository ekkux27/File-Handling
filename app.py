from datetime import datetime
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------- config
BASE_DIR = Path("workspace")
BASE_DIR.mkdir(exist_ok=True)

st.set_page_config(
    page_title="FileVault",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------- styling
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }

/* App background */
.stApp {
    background:
        radial-gradient(900px 500px at 10% -10%, rgba(124,58,237,.28), transparent 60%),
        radial-gradient(800px 500px at 100% 0%, rgba(14,165,233,.22), transparent 55%),
        #0b0d17;
    color: #e6e8f2;
}

/* Hide default chrome */
#MainMenu, footer, header[data-testid="stHeader"] { visibility: hidden; height: 0; }
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1150px; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15,18,32,.85);
    backdrop-filter: blur(14px);
    border-right: 1px solid rgba(255,255,255,.06);
}
.brand { display:flex; align-items:center; gap:.7rem; margin: .4rem 0 1.4rem 0; }
.brand .logo {
    width:42px; height:42px; border-radius:12px; display:grid; place-items:center;
    background: linear-gradient(135deg,#7c3aed,#0ea5e9); font-size:1.3rem;
    box-shadow: 0 8px 24px rgba(124,58,237,.45);
}
.brand .name { font-weight:800; font-size:1.25rem; letter-spacing:-.02em; color:#fff; }
.brand .tag  { font-size:.72rem; color:#8b90a8; margin-top:-2px; }

/* Radio -> nav pills */
div[role="radiogroup"] { gap:.35rem; }
div[role="radiogroup"] > label {
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.06);
    padding: .65rem .9rem; border-radius: 12px; width:100%;
    transition: all .2s ease; cursor:pointer;
}
div[role="radiogroup"] > label:hover {
    background: rgba(124,58,237,.14); border-color: rgba(124,58,237,.4); transform: translateX(3px);
}
div[role="radiogroup"] > label:has(input:checked) {
    background: linear-gradient(135deg, rgba(124,58,237,.35), rgba(14,165,233,.25));
    border-color: rgba(124,58,237,.7);
}
div[role="radiogroup"] > label > div:first-child { display:none; }  /* hide radio dot */
div[role="radiogroup"] label p { font-weight:500; font-size:.95rem; }

/* Hero */
.hero {
    position:relative; overflow:hidden;
    padding: 2rem 2.2rem; border-radius: 22px; margin-bottom: 1.6rem;
    background: linear-gradient(135deg, rgba(124,58,237,.30), rgba(14,165,233,.18));
    border: 1px solid rgba(255,255,255,.10);
    box-shadow: 0 20px 60px rgba(0,0,0,.35);
}
.hero::after {
    content:""; position:absolute; right:-80px; top:-80px; width:260px; height:260px; border-radius:50%;
    background: radial-gradient(circle, rgba(255,255,255,.18), transparent 70%);
}
.hero h1 { margin:0; font-size:2rem; font-weight:800; letter-spacing:-.03em; color:#fff; }
.hero p  { margin:.4rem 0 0 0; color:#b8bdd6; font-size:1rem; }
.chip {
    display:inline-block; padding:.2rem .65rem; border-radius:999px; font-size:.72rem; font-weight:600;
    background: rgba(255,255,255,.10); color:#d9dcf0; margin-bottom:.8rem; letter-spacing:.04em;
}

/* Stat cards */
.stat {
    padding:1.3rem 1.4rem; border-radius:18px;
    background: rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08);
    backdrop-filter: blur(10px); transition: all .25s ease;
}
.stat:hover { transform: translateY(-4px); border-color: rgba(124,58,237,.55); box-shadow:0 16px 40px rgba(124,58,237,.18); }
.stat .label { color:#8b90a8; font-size:.78rem; font-weight:600; text-transform:uppercase; letter-spacing:.08em; }
.stat .value { font-size:1.9rem; font-weight:800; color:#fff; margin-top:.25rem; letter-spacing:-.02em; }
.stat .icon  { float:right; font-size:1.4rem; opacity:.9; }

/* Section card */
.card-title { font-size:1.15rem; font-weight:700; color:#fff; margin-bottom:.2rem; }
.card-sub   { color:#8b90a8; font-size:.88rem; margin-bottom:1rem; }

/* File rows */
.frow {
    display:flex; align-items:center; justify-content:space-between;
    padding:.8rem 1rem; border-radius:14px; margin-bottom:.5rem;
    background: rgba(255,255,255,.035); border:1px solid rgba(255,255,255,.06);
    transition: all .2s ease;
}
.frow:hover { background: rgba(124,58,237,.10); border-color: rgba(124,58,237,.35); }
.frow .l { display:flex; align-items:center; gap:.8rem; }
.frow .ico { width:38px; height:38px; border-radius:10px; display:grid; place-items:center;
    background: linear-gradient(135deg, rgba(124,58,237,.35), rgba(14,165,233,.25)); }
.frow .n { font-weight:600; color:#fff; font-size:.95rem; }
.frow .m { color:#8b90a8; font-size:.78rem; }
.frow .r { color:#b8bdd6; font-size:.8rem; text-align:right; }

/* Inputs */
.stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
    background: rgba(255,255,255,.04) !important;
    border: 1px solid rgba(255,255,255,.10) !important;
    border-radius: 12px !important; color:#fff !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color:#7c3aed !important; box-shadow: 0 0 0 3px rgba(124,58,237,.25) !important;
}
label, .stTextInput label p, .stTextArea label p, .stSelectbox label p { color:#b8bdd6 !important; font-weight:500; }

/* Buttons */
.stButton > button, .stDownloadButton > button {
    border:none; border-radius:12px; padding:.65rem 1.4rem; font-weight:600; color:#fff;
    background: linear-gradient(135deg,#7c3aed,#0ea5e9);
    box-shadow: 0 10px 26px rgba(124,58,237,.35); transition: all .2s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover {
    transform: translateY(-2px); box-shadow: 0 14px 34px rgba(124,58,237,.5); color:#fff;
}
.danger .stButton > button { background: linear-gradient(135deg,#ef4444,#f97316); box-shadow: 0 10px 26px rgba(239,68,68,.35); }

/* Tabs / code / alerts */
.stTabs [data-baseweb="tab-list"] { gap:.4rem; }
.stTabs [data-baseweb="tab"] { background: rgba(255,255,255,.04); border-radius:10px; padding:.5rem 1rem; }
.stTabs [aria-selected="true"] { background: rgba(124,58,237,.3); }
div[data-testid="stCodeBlock"] pre { border-radius:14px; border:1px solid rgba(255,255,255,.08); }
div[data-testid="stAlert"] { border-radius:14px; }
hr { border-color: rgba(255,255,255,.08); }
</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------- helpers
def safe_path(name: str):
    """Return a path inside BASE_DIR, or None if the name is invalid / tries to escape."""
    name = (name or "").strip()
    if not name or Path(name).name != name or name in {".", ".."}:
        return None
    return BASE_DIR / name


def list_files():
    files = [p for p in BASE_DIR.iterdir() if p.is_file()]
    return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)


def human_size(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def ago(ts: float) -> str:
    return datetime.fromtimestamp(ts).strftime("%d %b %Y · %H:%M")


def hero(chip: str, title: str, subtitle: str):
    st.markdown(
        f'<div class="hero"><span class="chip">{chip}</span><h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )


def stat(icon, label, value):
    return (
        f'<div class="stat"><span class="icon">{icon}</span>'
        f'<div class="label">{label}</div><div class="value">{value}</div></div>'
    )


def file_picker(label="Select a file"):
    files = list_files()
    if not files:
        st.info("No files yet — create your first one from the **Create** page.")
        return None
    return safe_path(st.selectbox(label, [f.name for f in files]))


# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.markdown(
        '<div class="brand"><div class="logo">🗂️</div>'
        '<div><div class="name">FileVault</div><div class="tag">Premium file manager</div></div></div>',
        unsafe_allow_html=True,
    )
    page = st.radio(
        "Navigation",
        ["📊  Dashboard", "✨  Create", "📖  Read", "✏️  Update", "🗑️  Delete"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption(f"📁 Workspace: `{BASE_DIR.resolve().name}/`")
    st.caption(f"{len(list_files())} file(s) stored")

page = page.split("  ", 1)[1]

# ---------------------------------------------------------------- pages
if page == "Dashboard":
    hero("OVERVIEW", "Welcome back 👋", "Create, read, update and delete files — beautifully.")

    files = list_files()
    total = sum(f.stat().st_size for f in files)
    latest = files[0].name if files else "—"

    c1, c2, c3 = st.columns(3)
    c1.markdown(stat("📄", "Total files", len(files)), unsafe_allow_html=True)
    c2.markdown(stat("💾", "Storage used", human_size(total)), unsafe_allow_html=True)
    c3.markdown(stat("🕒", "Last modified", latest if len(latest) < 16 else latest[:14] + "…"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="card-title">Recent files</div><div class="card-sub">Sorted by last modified</div>', unsafe_allow_html=True)

    if not files:
        st.info("Your vault is empty. Head to **Create** to add a file.")
    for f in files[:10]:
        s = f.stat()
        st.markdown(
            f'<div class="frow"><div class="l"><div class="ico">📄</div>'
            f'<div><div class="n">{f.name}</div><div class="m">{human_size(s.st_size)}</div></div></div>'
            f'<div class="r">{ago(s.st_mtime)}</div></div>',
            unsafe_allow_html=True,
        )

elif page == "Create":
    hero("NEW", "Create a file", "Give it a name, add some content and save it to your vault.")
    with st.form("create_form", clear_on_submit=True):
        name = st.text_input("File name", placeholder="notes.txt")
        data = st.text_area("Content", height=260, placeholder="Start typing…")
        submitted = st.form_submit_button("✨ Create file")

    if submitted:
        path = safe_path(name)
        try:
            if path is None:
                st.error("Please enter a valid file name (no folders or slashes).")
            elif path.exists():
                st.warning("File already exists. Use the **Update** page to modify it.")
            else:
                path.write_text(data, encoding="utf-8")
                st.toast("File created successfully", icon="✅")
                st.success(f"**{path.name}** created successfully.")
        except Exception as err:
            st.error(f"Error occurred: {err}")

elif page == "Read":
    hero("VIEW", "Read a file", "Preview any file in your vault and download a copy.")
    path = file_picker("Select a file to read")
    if path and path.exists():
        try:
            content = path.read_text(encoding="utf-8")
            s = path.stat()
            c1, c2, c3 = st.columns(3)
            c1.markdown(stat("📄", "Name", path.name if len(path.name) < 16 else path.name[:14] + "…"), unsafe_allow_html=True)
            c2.markdown(stat("💾", "Size", human_size(s.st_size)), unsafe_allow_html=True)
            c3.markdown(stat("🔤", "Characters", f"{len(content):,}"), unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.code(content if content else "(empty file)", language=None)
            st.download_button("⬇️ Download", content, file_name=path.name)
        except UnicodeDecodeError:
            st.error("This file isn't a UTF-8 text file, so it can't be previewed.")
        except Exception as err:
            st.error(f"Error occurred: {err}")

elif page == "Update":
    hero("EDIT", "Update a file", "Overwrite the whole file or append new content to the end.")
    path = file_picker("Select a file to update")
    if path and path.exists():
        try:
            current = path.read_text(encoding="utf-8")
        except Exception as err:
            st.error(f"Error occurred: {err}")
            current = None

        if current is not None:
            mode = st.radio("Operation", ["Overwrite the file", "Append to the file"], horizontal=True)
            if mode.startswith("Overwrite"):
                data = st.text_area("New content", value=current, height=280)
            else:
                data = st.text_area("Content to append", height=200, placeholder="Text added at the end…")

            if st.button("💾 Save changes"):
                try:
                    if mode.startswith("Overwrite"):
                        path.write_text(data, encoding="utf-8")
                    else:
                        with open(path, "a", encoding="utf-8") as fs:
                            fs.write(data)
                    st.toast("File updated successfully", icon="✅")
                    st.success(f"**{path.name}** updated successfully.")
                except Exception as err:
                    st.error(f"Error occurred: {err}")

elif page == "Delete":
    hero("REMOVE", "Delete a file", "Permanently remove a file from your vault. This cannot be undone.")
    path = file_picker("Select a file to delete")
    if path and path.exists():
        st.warning(f"You are about to delete **{path.name}** ({human_size(path.stat().st_size)}).")
        confirm = st.checkbox("Yes, I understand this is permanent")
        st.markdown('<div class="danger">', unsafe_allow_html=True)
        if st.button("🗑️ Delete file", disabled=not confirm):
            try:
                path.unlink()
                st.toast("File deleted successfully", icon="🗑️")
                st.success("File deleted successfully.")
                st.rerun()
            except Exception as err:
                st.error(f"Error occurred: {err}")
        st.markdown("</div>", unsafe_allow_html=True)