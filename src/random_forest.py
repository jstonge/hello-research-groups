import duckdb

con = duckdb.connect("../data/clean/oa_data.db")

df = con.sql("""
    SELECT c.type, c.pub_date, c.target, c.all_times_collabo, c.yearly_collabo, c.target_type,
        c.title as coauthor_name, a.author_age as coauthor_age, a2.author_age,
        (a2.author_age-a.author_age) AS age_diff
    FROM coauthor c
    LEFT JOIN author_tidy a
    ON c.aid = a.aid AND c.pub_year = a.pub_year
    LEFT JOIN author_tidy a2
    ON c.target = a2.display_name AND c.pub_year = a2.pub_year
    """).fetchdf()