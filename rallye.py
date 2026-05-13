import streamlit as st
import time

# --- SEITEN-KONFIGURATION ---
st.set_page_config(
    page_title="Terminal 2439",
    page_icon="📟",
    layout="centered"
)

# --- CUSTOM CSS FÜR DEN HACKER-LOOK ---
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #00FF00;
        font-family: 'Courier New', Courier, monospace;
    }
    input {
        background-color: #111111 !important;
        color: #00FF00 !important;
        border: 2px solid #00FF00 !important;
        text-align: center !important;
        font-size: 32px !important;
    }
    .stButton>button {
        width: 100%;
        background-color: #00FF00;
        color: black;
        border-radius: 0px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #003300;
        color: #00FF00;
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIK ---
st.title("📟 MISSION: SÜDERBRARUP")
st.write("---")
st.write("STATUS: Warte auf Entschlüsselungs-Code...")

# Eingabefeld für den Code
code_eingabe = st.text_input("ZUGANGSSCHLÜSSEL", max_chars=4, placeholder="****")

if st.button("TERMINAL ENTSPERREN"):
    if code_eingabe == "2439":
        # Der "Hack"-Effekt
        with st.status("Entschlüssele Datenbanken...", expanded=True) as status:
            st.write("Verbinde mit Mainframe...")
            time.sleep(1)
            st.write("Umgehe Firewall...")
            time.sleep(1)
            st.write("Code-Integrität bestätigt.")
            status.update(label="ZUGRIFF GESTATTET!", state="complete", expanded=False)
        
        # Das große Finale
        st.balloons()
        st.success("🏆 MISSION ERFOLGREICH BEENDET")
        
        st.markdown("""
        ### PROTOKOLL:
        - **Ort:** Süderbrarup (Zentrum)
        - **Status:** Alle Sicherheitsbarrieren überwunden.
        - **Team-Leistung:** Überragend.
        """)
        
        # Ein passendes Hacker-GIF
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzR4Mmt6ZTVyeGZ6bnR6ZTVxeGZ6bnR6ZTVxeGZ6bnR6ZTVxeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYt5jPR6QX5pnqM/giphy.gif")
        
    elif code_eingabe == "":
        st.warning("KEINE DATEN EMPFANGEN.")
    else:
        st.error("❌ ZUGRIFF VERWEIGERT. FALSCHER CODE.")
        st.snow() # Kleiner Effekt bei falscher Eingabe
