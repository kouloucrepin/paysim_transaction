from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd
import plotly.express as px






# Exemple de données avec des URLs d'images
personnes = [
    {
        "nom": "KOULOU Anaklasse crepin",
        "role": "Software Engineer",
        "email": "mamipash@example.com",
        "twitter": "@Mamipash",
        "photo": "/assets/profis/crepin.png"
    },
    {
        "nom": "Christian TEYANBAYE BERTORNGAÏ",
        "role": "Data Scientist",
        "email": "johndoe@example.com",
        "twitter": "@JohnDoe",
        "photo": "/assets/profis/chistian.png"
    },
    {
        "nom": "Assa Allo",
        "role": "Product Manager",
        "email": "janesmith@example.com",
        "twitter": "@JaneSmith",
        "photo": "/assets/profis/allo.png"
    },
    {
        "nom": "DOMEVENOU KOMLA Wisdom",
        "role": "Designer",
        "email": "alicejohnson@example.com",
        "twitter": "@AliceJohnson",
        "photo": "/assets/profis/wisdom.png" 
    },
    {
        "nom": "AZONFACK Myriam Dolvianne",
        "role": "Analyst",
        "email": "bobbrown@example.com",
        "twitter": "@BobBrown",
        "photo": "/assets/profis/azonfack.png"
    },
    {
        "nom": "OGNIMBA sadri",
        "role": "Developer",
        "email": "charliedavis@example.com",
        "twitter": "@CharlieDavis",
        "photo": "/assets/profis/sadri.png"
    },
    {
        "nom": "SEYDOU Ferdinand",
        "role": "Developer",
        "email": "charliedavis@example.com",
        "twitter": "@CharlieDavis",
        "photo": "/assets/profis/seydou.png"
    },
    {
        "nom": "leonard FOUDA MANGA",
        "role": "Developer",
        "email": "charliedavis@example.com",
        "twitter": "@CharlieDavis",
        "photo": "/assets/profis/manga.png"
    },
    {
        "nom": "AMBASSA LUMIERE",
        "role": "Developer",
        "email": "charliedavis@example.com",
        "twitter": "@CharlieDavis",
        "photo": "/assets/profis/ambassa.png"
    },
]

prf = [html.H1("Présentation de l'équipe de conception", style={'color': 'green','text-align': 'right'})]

profils = [
    dbc.Row(
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    dbc.Row([
                        dbc.Col(html.Img(src=person["photo"], style={'borderRadius': '50%', 'marginRight': '10px','width':'200px'}), width="auto"),
                        dbc.Col(
                            html.Div([
                                html.H4(person["nom"]),
                                html.P(person["role"]),
                                html.A(person["email"], href=f'mailto:{person["email"]}'),
                                html.Br(),
                                html.A(person["twitter"], href=f'https://twitter.com/{person["twitter"].lstrip("@")}', target="_blank")
                            ]),style={'margin-left':'15%'}
                        )
                    ])
                ),
                style={'display': 'flex', 'alignItems': 'left'}
            ),
            width=12
        ),
        style={'marginBottom': '20px'}
    ) for person in personnes
]

prf.extend(profils)

layout = html.Div(prf, style={'padding': '20px','margin-left':'10%','margin-right':'10%',
        'background-image': 'url("/assets/image.png")',  # Chemin vers l'image
        'background-size': 'cover',  # Ajuster l'image pour couvrir tout l'arrière-plan
        'background-position': 'center',  # Centrer l'image
        'background-repeat': 'no-repeat',  # Ne pas répéter l'image
          # Hauteur de la page (100% de la vue)
    })