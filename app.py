
import streamlit as st
import pandas as pd
from scripts.festival_matching import match_festivals

st.title("Black Stains Festival Finder 2026")

st.markdown("🔍 Finde passende Festivals für Metalcore / Alternative / Metal mit max. 10.000 Besuchern in Deutschland.")

uploaded_file = st.file_uploader("Lade eine Festival-Excel-Datei hoch", type=["xlsx", "csv"])

if uploaded_file:
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(".xlsx") else pd.read_csv(uploaded_file)
    st.write("🎪 Festivals geladen:", df.shape[0])
    results = match_festivals(df)
    st.success("✅ Analyse abgeschlossen!")
    st.dataframe(results)
    st.download_button("📥 Ergebnis herunterladen", data=results.to_csv(index=False), file_name="festival_matching_result.csv")
