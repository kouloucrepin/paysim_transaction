from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd

# Connect to main app.py file 
from app import app
from app import server

# Connect to your pages
from app_pages import page1, page2
import page3

app.layout = html.Div([
    html.Link(rel="icon", href="/assets/statistics.ico"),
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content', children=[]),
    html.Div(
        [
            html.Div([
                    html.Img(src="/assets/statistics.png", style={"width": "5.6rem", "margin-bottom": "60px"}),
                    html.H5("PaySim", style={'color': 'white', 'margin-top': '20px'}),
                ], className='image_title'),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-house"),
                        html.Span("Home", style={'margin-top': '4px'})], className='icon_title')],
                        href="/",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-gauge"),
                        html.Span("Dashboard", style={'margin-top': '4px'})], className='icon_title')],
                        href="/app_pages/page1",
                        active="exact",
                        className="pe-3"
                    ),
                    dbc.NavLink([html.Div([
                        html.I(className="fa-solid fa-database"),
                        html.Span("Auteur", style={'margin-top': '4px'})], className='icon_title')],
                        href="/app_pages/page2",
                        active="exact",
                        className="pe-3"
                    )
                ],
                vertical=True,
                pills=True, 
            )
           

        ],
        id="bg_id",
        className="sidebar",
        
    )

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return page3.layout
    elif pathname == '/app_pages/page1':
        return page1.layout
    elif pathname == '/app_pages/page2':
        return page2.layout
    else:
        return page3.layout
    

 


if __name__ == '__main__':
    app.run_server(debug=True)
