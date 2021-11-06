import streamlit as st
import pandas as pd 
import base64 
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

st.title('NBA Players Stats Explorer')

st.markdown("""
This as Perform Simple Webscraping of NBA players stats data !
* **Python Libraries Use :** base64, streamlit, numpy, pandas, matplotlib
* **Data Source is :** [Basketball=reference.com](https://www.basketball-reference.com/).
""")

st.sidebar.header('User Input Feature :')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2021))))

# Webscraping of NBA Players stats
@st.cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header =0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    player_stats = raw.drop(['Rk'], axis=1)
    return player_stats

player_stats = load_data(selected_year)

# Sidebar : Team Selection
sorted_unique_team = sorted(player_stats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

# Sidebar : Position Selection
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = player_stats[(player_stats.Tm.isin(selected_team)) & (player_stats.Pos.isin(selected_pos))]

st.header('Display PLayes Stats of Selected Team(s)')
st.write('Data Dimension : '+ str(df_selected_team.shape[0]) + 'rows & '+ str(df_selected_team.shape[1]) + ' columns.')
test = df_selected_team.astype(str)
st.dataframe(test)

# NBA Playes Stats Data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="player_stats.csv" >Download CSV File </a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html = True)


# Creating HeatMap
if st.button('Intercorrelation HeatMap'):
    st.header('Intercorrelation Matrix HeatMap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style('white'):
        f, ax = plt.subplots(figsize=(7,5))
        ax = sns.heatmap(corr, mask = mask, vmax = 1, square = True)
    st.pyplot(f)
