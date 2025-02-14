import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

pd.set_option('display.max_columns', None)
pd.set_option("display.expand_frame_repr", False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Reading dataset.
df = pd.read_excel("eurovision_song_contest_1975_2019.xlsx", sheet_name="Data")
df.head()
df.columns
df.rename(columns={"Points      ": "Points"}, inplace=True)

# region Seperating of Semi Final and Final votes.
semi_final_votes = df[df['(semi-) final'] == 'sf']
final_votes = df[df['(semi-) final'] == 'f']
# endregion

# region All points to Turkey.
turkey_points_all_years = df[df['To country'] == 'Turkey'].copy()

turkey_semi_points_all_years = semi_final_votes[semi_final_votes['To country'] == 'Turkey'].copy()

turkey_final_points_all_years = final_votes[final_votes['To country'] == 'Turkey'].copy()
# endregion

# region Top voting countries to Türkiye
final_top_voting_countries = (
    turkey_final_points_all_years
    .groupby("From country", as_index=False)
    .agg({"Points": "sum"})
    .rename(columns={"Points": "Total Points"})
    .sort_values("Total Points", ascending=False)
)
final_top_voting_countries.head()

final_top_voting_countries['Years Together'] = final_top_voting_countries['From country'].apply(
    lambda country: len(
        set(df[(df['From country'] == country) & (df['(semi-) final'] == 'f')]['Year'])
        & set(df[(df['To country'] == 'Turkey') & (df['(semi-) final'] == 'f')]['Year'])
    )
)

final_top_voting_countries["Points per Year"] = final_top_voting_countries["Total Points"] / final_top_voting_countries[
    "Years Together"]

semi_final_top_countries = (
    turkey_semi_points_all_years
    .groupby('From country', as_index=False)
    .agg({'Points': 'sum'})
    .rename(columns={'Points': 'Total Points'})
    .sort_values('Total Points', ascending=False)
)

semi_final_top_countries['Semi Finals Together'] = semi_final_top_countries['From country'].apply(
    lambda country: len(
        set(df[(df['From country'] == country) & (df['(semi-) final'] == 'sf')]['Year'])
        & set(df[(df['To country'] == 'Turkey') & (df['(semi-) final'] == 'sf')]['Year'])
    )
)

semi_final_top_countries["Points per Semi Final"] = semi_final_top_countries["Total Points"] / semi_final_top_countries[
    "Semi Finals Together"]

final_top_voting_countries = final_top_voting_countries.sort_values(by="Points per Year", ascending=False)

final_top_voting_countries['Adjusted Togetherness Score'] = (final_top_voting_countries['Total Points'] /
                                                             final_top_voting_countries['Years Together']) * np.log(
    final_top_voting_countries['Years Together'] + 1)

final_top_voting_countries = final_top_voting_countries.sort_values(by="Adjusted Togetherness Score",
                                                                    ascending=False).reset_index(drop=True)

# endregion

# region Turkey's most voted countries
turkeys_votes = final_votes[final_votes['From country'] == 'Turkey'].copy()

turkey_top_voting_countries = (
    turkeys_votes.groupby('To country', as_index=False)
    .agg({'Points': 'sum'})
    .rename(columns={'Points': 'Total Points'})
    .sort_values(by='Total Points', ascending=False)
)

turkey_top_voting_countries['Years Together'] = turkey_top_voting_countries['To country'].apply(
    lambda country: len(
        set(df[(df['To country'] == country) & (df['(semi-) final'] == 'f')]['Year'])
        & set(df[(df['From country'] == 'Turkey') & (df['(semi-) final'] == 'f')]['Year'])
    )
)

turkey_top_voting_countries["Points per Year"] = turkey_top_voting_countries["Total Points"] / \
                                                 turkey_top_voting_countries["Years Together"]

turkey_top_voting_countries = turkey_top_voting_countries.sort_values(by="Points per Year", ascending=False)

turkey_top_voting_countries['Adjusted Togetherness Score'] = (turkey_top_voting_countries['Total Points'] /
                                                              turkey_top_voting_countries['Years Together']) * np.log(
    turkey_top_voting_countries['Years Together'] + 1)

turkey_top_voting_countries = turkey_top_voting_countries.sort_values(by="Adjusted Togetherness Score",
                                                                      ascending=False).reset_index(drop=True)
# endregion

#region Who is the Best Friend of Turkey?
togetherness = pd.merge(final_top_voting_countries[['From country', 'Adjusted Togetherness Score']],
                        turkey_top_voting_countries[['To country', 'Adjusted Togetherness Score']],
                        left_on='From country',
                        right_on='To country',
                        how='outer')

togetherness.columns = ['Country', 'Score_From_Others', 'Country_2', 'Score_From_Turkey']

togetherness = togetherness.drop('Country_2', axis=1)

togetherness = togetherness.fillna(0)

togetherness['Relationship_Score'] = np.sqrt(togetherness['Score_From_Others'] *
                                             togetherness['Score_From_Turkey'])

togetherness = togetherness.sort_values('Relationship_Score', ascending=False).reset_index(drop=True)
#endregion

