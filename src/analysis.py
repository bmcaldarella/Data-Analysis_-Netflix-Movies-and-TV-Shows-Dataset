import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "data/Netflix_movies_and_tv_shows_clustering.csv"

def top_countries(df, n=10):
    """Q1: Top N countries by number of titles (filter + count + sort)."""
    # FILTER: keep only rows where country is not missing
    df_country = df[df["country"].notna()]

    # AGGREGATE (count) + SORT (value_counts sorts descending by default)
    return df_country["country"].value_counts().head(n)

def titles_added_per_year(df):
    """Q2: Number of titles added to Netflix per year using date_added (filter + conversion + groupby + sort)."""
    # FILTER + COPY: avoid SettingWithCopyWarning
    df_dates = df[df["date_added"].notna()].copy()

    # CONVERSION: text -> datetime (invalid values become NaT)
    df_dates["date_added"] = pd.to_datetime(df_dates["date_added"], errors="coerce")

    # Extract year
    df_dates["added_year"] = df_dates["date_added"].dt.year

    # AGGREGATE (count) + SORT (by year)
    return (
        df_dates.dropna(subset=["added_year"])
                .groupby("added_year")
                .size()
                .sort_index()
    )

def longest_movie(df):
    """Q3: Find the longest movie (filter + conversion + sort)."""
    # FILTER: only movies
    movies = df[df["type"] == "Movie"].copy()

    # FILTER: duration must exist
    movies = movies[movies["duration"].notna()].copy()

    # CONVERSION: "142 min" -> 142 (numeric)
    movies["duration_minutes"] = (
        movies["duration"]
        .astype(str)
        .str.replace(" min", "", regex=False)
        .str.strip()
    )
    movies["duration_minutes"] = pd.to_numeric(movies["duration_minutes"], errors="coerce")

    # Remove rows that couldn't be converted
    movies = movies.dropna(subset=["duration_minutes"])

    # SORT: longest first
    longest = movies.sort_values("duration_minutes", ascending=False).iloc[0]
    return longest

def main():
    df = pd.read_csv(FILE_PATH)

    # Quick exploration (useful for README and learning)
    print("=== Shape (rows, columns) ===")
    print(df.shape)

    print("\n=== Columns ===")
    print(df.columns.tolist())

    print("\n=== First 5 rows ===")
    print(df.head())

    print("\n=== Missing values per column ===")
    print(df.isna().sum().sort_values(ascending=False))

    # ----------------------------
    # Q1
    # ----------------------------
    print("\n=== Q1: Top 10 countries by number of titles ===")
    q1 = top_countries(df, 10)
    print(q1)

    # ----------------------------
    # Q2
    # ----------------------------
    print("\n=== Q2: Titles added per year (last 10 years) ===")
    q2 = titles_added_per_year(df)
    print(q2.tail(10))

    # ----------------------------
    # Q3
    # ----------------------------
    print("\n=== Q3: Longest movie on Netflix ===")
    longest = longest_movie(df)
    print(f"Title: {longest['title']}")
    print(f"Duration: {int(longest['duration_minutes'])} minutes")
    print(f"Country: {longest.get('country', 'Unknown')}")
    print(f"Release Year: {int(longest['release_year'])}")

    # ----------------------------
    # Extra Requirement: Graph
    # ----------------------------
    plt.figure(figsize=(10, 5))
    q2.plot(marker="o")

    plt.title("Number of Movies and TV Shows Added to Netflix Each Year")
    plt.xlabel("Year Content Was Added to Netflix")
    plt.ylabel("Number of Titles Added")
    plt.grid(True, linestyle="--", alpha=0.5)

    # Highlight the peak year
    max_year = q2.idxmax()
    max_value = q2.max()
    plt.annotate(
        f"Peak year: {int(max_year)} ({max_value} titles)",
        xy=(max_year, max_value),
        xytext=(max_year - 3, max_value),
        arrowprops=dict(arrowstyle="->")
    )

    plt.tight_layout()
    plt.savefig("outputs/titles_added_per_year.png")
    print("\nSaved graph -> outputs/titles_added_per_year.png")

if __name__ == "__main__":
    main()
