import streamlit as st
import time

# --- KONFIGURATION ---
st.set_page_config(page_title="Mission Süderbrarup", page_icon="📟")

# --- HACKER LOOK (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #00FF00; font-family: 'Courier New', Courier, monospace; }
    input { background-color: #111111 !important; color: #00FF00 !important; border: 1px solid #00FF00 !important; }
    .stButton>button { width: 100%; background-color: #00FF00; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALISIEREN ---
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# --- LOGIK DER STATIONEN ---

st.title(f"📟 LEVEL {st.session_state.stage} AKTIV")

# --- STATION 1: BAHNHOF ---
if st.session_state.stage == 1:
    st.subheader("Mission 1: Die Schienen-Kontrolle")
    st.write("Findet heraus, wie viele Gleise am Bahnhof für den Personenverkehr genutzt werden.")
    code1 = st.text_input("CODE EINGEBEN", key="c1")
    if st.button("LEVEL 1 KNACKEN"):
        if code1 == "2":
            st.success("Korrekt! Signal für Station 2 freigeschaltet.")
            time.sleep(1)
            st.session_state.stage = 2
            st.rerun()
        else:
            st.error("Falsches Gleis! Sucht weiter.")

# --- STATION 2: KIRCHE ---
elif st.session_state.stage == 2:
    st.subheader("Mission 2: Das Zeit-Rätsel")
    st.write("Sucht das Schild an der St. Jacobi Kirche. Rechnet: (Jahrhundert-Ziffern addieren) + 1.")
    code2 = st.text_input("CODE EINGEBEN", key="c2")
    if st.button("LEVEL 2 KNACKEN"):
        if code2 == "4":
            st.success("Integrität bestätigt. Weiter zum Marktplatz!")
            time.sleep(1)
            st.session_state.stage = 3
            st.rerun()
        else:
            st.error("Zeitschleife erkannt. Falscher Code.")

# --- STATION 3: MARKTPLATZ ---
elif st.session_state.stage == 3:
    st.subheader("Mission 3: Die Metall-Detektive")
    st.write("Sucht 3 Metall-Objekte. Wenn ihr sie dem Leiter gezeigt habt, gibt er euch den Code.")
    code3 = st.text_input("MASTER-CODE", key="c3")
    if st.button("LEVEL 3 KNACKEN"):
        if code3 == "3":
            st.success("Sicherheitssystem überbrückt. Finaler Ort: Bürgerpark!")
            time.sleep(1)
            st.session_state.stage = 4
            st.rerun()
        else:
            st.error("Zugriff verweigert.")

# --- STATION 4: BÜRGERPARK ---
elif st.session_state.stage == 4:
    st.subheader("Mission 4: Der Wort-Algorithmus")
    st.write("Zählt die Buchstaben von 'SÜDERBRARUP' und zieht 2 ab.")
    code4 = st.text_input("FINALE SEQUENZ", key="c4")
    if st.button("TERMINAL ENTSPERREN"):
        if code4 == "9":
            st.session_state.stage = 5
            st.rerun()
        else:
            st.error("Letzte Barriere hält stand. Versucht es erneut.")

# --- FINALE ---
elif st.session_state.stage == 5:
    st.balloons()
    st.success("🏆 SYSTEM VOLLSTÄNDIG GEHACKT!")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzR4Mmt6ZTVyeGZ6bnR6ZTVxeGZ6bnR6ZTVxeGZ6bnR6ZTVxeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYt5jPR6QX5pnqM/giphy.gif")
    st.markdown("### MISSION ERFÜLLT\nAlle Daten gesichert. Team-Status: **Legenden**.")
    if st.button("Rallye zurücksetzen"):
        st.session_state.stage = 1
        st.rerun()
