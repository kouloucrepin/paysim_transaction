from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd
import dash


layout = html.Div([
    html.Div([
        html.Div([
    html.Button("Télécharger le Rapport", id="btn-download",style={'color': 'white','text-align': 'left'}),
    dcc.Download(id="download")
    ]),
    html.H1("Contexte", style={'color': 'green','text-align': 'right'}),
    html.H4(
        "Il existe un manque de datasets publics disponibles sur les services financiers, en particulier dans le domaine émergent des transactions d'argent mobile. "
        "Les datasets financiers sont importants pour de nombreux chercheurs, notamment pour nous qui menons des recherches dans le domaine de la détection de fraude. "
        "Une partie du problème réside dans le caractère intrinsèquement privé des transactions financières, ce qui explique l'absence de datasets publics.",
        style={'lineHeight': '1.6', 'textAlign': 'justify'}
    ),
    html.H4(
        "Nous présentons un Dashboard base sur un dataset synthétique généré à l'aide d'un simulateur appelé PaySim comme solution à ce problème. "
        "PaySim utilise des données agrégées issues d'un dataset privé pour générer un dataset synthétique qui reproduit le fonctionnement normal des transactions, "
        "tout en injectant des comportements malveillants afin d'évaluer par la suite les performances des méthodes de détection de fraude.",
        style={'lineHeight': '1.6', 'textAlign': 'justify'}
    ),
    html.H1("Contenu", style={'color': 'green','text-align': 'right'}),
    html.H4(
        "PaySim simule des transactions d'argent mobile en se basant sur un échantillon de transactions réelles extraites d'un mois de logs financiers provenant d'un service d'argent mobile "
        "mis en œuvre dans un pays africain. Les logs originaux ont été fournis par une entreprise multinationale, fournisseur du service financier mobile qui est actuellement opérationnel "
        "dans plus de 14 pays à travers le monde.",
        style={'lineHeight': '1.6', 'textAlign': 'justify'}
    ),
    html.H1("Presentation des variables du datasets", style={'color': 'green','text-align': 'right'}),
     html.Table(style={'width': '100%', 'borderCollapse': 'collapse', 'marginBottom': '20px'}, children=[
        html.Thead(style={'backgroundColor': '#f2f2f2','color':'black'}, children=[
            html.Tr(children=[
                html.Th("Variable", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Th("Description", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ])
        ]),
        html.Tbody(children=[
            html.Tr(children=[
                html.Td("step", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Représente une unité de temps dans la simulation. 1 pas équivaut à 30 minutes. Total : 1440 étapes (30 jours).", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("type", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Type de transaction : DÉPÔT, RETRAIT, TRANSFERT, PAIEMENT et FRAIS.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("amount", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Montant de la transaction en monnaie locale.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("origin", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Identifiant du client initiateur de la transaction.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("origin_balance", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Solde initial du client initiateur avant la transaction.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("new_origin_balance", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Nouveau solde du client initiateur après la transaction.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("destination", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Identifiant du client destinataire de la transaction.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("destination_balance", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Solde initial du destinataire avant la transaction. Note : Non disponible pour les transactions de type FRAIS.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("new_destination_balance", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Nouveau solde du destinataire après la transaction. Note : Non disponible pour les transactions de type FRAIS.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
            html.Tr(children=[
                html.Td("is_fraud", style={'padding': '10px', 'border': '1px solid #ddd'}),
                html.Td("Indicateur binaire (1 ou 0) indiquant si la transaction est frauduleuse. Ces transactions sont injectées pour simuler des activités suspectes.", style={'padding': '10px', 'border': '1px solid #ddd'}),
            ]),
        ],style={'color':'white'})
    ])
   
    ]
             ,style={
        'width': '90%',
        'margin-left': '60px',
        'padding-top': '2%',
        'color': 'white',
    })
    
    
],style={
        'background-image': 'url("/assets/image.png")',  # Chemin vers l'image
        'background-size': 'cover',  # Ajuster l'image pour couvrir tout l'arrière-plan
        'background-position': 'center',  # Centrer l'image
        'background-repeat': 'no-repeat',  # Ne pas répéter l'image
          # Hauteur de la page (100% de la vue)
    })


@app.callback(
    Output("download", "data"),
    Input("btn-download", "n_clicks"),
    prevent_initial_call=True
)
def download_file(n_clicks):
    return dcc.send_file("Rapport_BigData_Gp_7.pdf")
