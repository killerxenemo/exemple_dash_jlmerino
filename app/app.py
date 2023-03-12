import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from datetime import date,datetime,timedelta
from flask import Flask
from sqlalchemy import create_engine


# Load data
dialect="mysql+pymysql://sistemesbd:bigdata2223@192.168.193.133:3306/ree" #Aquest es el servido de clase i la BD
sqlEngine=create_engine(dialect)
dbConnection = sqlEngine.connect()
df= pd.read_sql('esios', dbConnection) #Aqui va la vostra taula

df['fecha']=pd.to_datetime(df['fecha'])
df.sort_values(by='fecha',inplace=True)
df.set_index('fecha',inplace=True)
df2=df[0:100]
listaTags=["pmmd","pmfd"]
fig = go.Figure()
for tag in listaTags:
    tr=go.Scatter(x=df2.index,y=df2[tag],mode='lines',name=tag)
    fig.add_trace(tr)
grafica=dcc.Graph(id='grafica3', figure = fig )


# Initialize the app
server = Flask(__name__)
app = dash.Dash(server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'mpl_plotlyInteractiu'
app.config.suppress_callback_exceptions = True


app.layout =  html.Div(children=[grafica])



if __name__ == '__main__':
    app.run_server()
