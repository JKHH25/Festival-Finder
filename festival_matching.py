
import pandas as pd

METALCORE_GENRES = ["metalcore", "alternative metal", "post-hardcore", "hardcore", "nu metal", "modern metal"]

def dummy_genre_score(genre_list):
    if not genre_list:
        return 0
    return sum(1 for g in genre_list if g.lower() in METALCORE_GENRES) / len(genre_list)

def match_festivals(df):
    df["Matching-Score"] = df["Genre"].apply(lambda g: dummy_genre_score(str(g).split(", ")))
    df["Empfehlung"] = df["Matching-Score"].apply(lambda s: "👍 Ja" if s >= 0.3 else "🤔 Eher nicht")
    return df.sort_values("Matching-Score", ascending=False)
