from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
import pandas as pd
import dash
import pandas as pd
from packages.graph import retourne_transaction_type,retourne_repartition_transaction,retourne_repartition_transaction_sender_final_null,retourne_repartition_transaction_sender_null,distribution_montant,retourne_dist_montant_type
from packages.kpi import retourne_information_transaction,retourne_information_fraude,retourne_information_suspect,retourne_information_monant
from dash import dash_table



kpi1,graph1,titre1 = retourne_information_transaction()
kpi2,graph2,titre2 = retourne_information_fraude()
kpi3,graph3,titre3 = retourne_information_suspect()
kpi4,graph4,titre4 =retourne_information_monant()
data_sender_null = pd.read_csv('data/top_10_dest.csv',index_col=0)
data_recep_null = pd.read_csv('data/sender_sorted.csv')
df_sender=pd.read_csv('data/amount_top_7_dest.csv')
max_values = df_sender.max()



def create_styled_table(df):
    # Convertir tous les noms de colonnes en string
    df.columns = df.columns.astype(str)
    
    # Créer les styles conditionnels pour les barres
    style_data_conditional = []
    
    # Pour chaque colonne sauf la première
    columns_to_style = df.columns[1:]  # On exclut la première colonne
    
    for column in columns_to_style:
        max_val = df[column].max()
        for i in range(len(df)):
            val = df[column].iloc[i]
            percentage = (val / max_val) * 100 if max_val != 0 else 0
            style_data_conditional.append({
                'if': {
                    'column_id': str(column),
                    'row_index': i
                },
                'background': f'linear-gradient(90deg, rgba(173, 216, 230, 0.7) {percentage}%, transparent {percentage}%)',
                'backgroundColor': 'black'
            })

    table = dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': str(i), 'id': str(i)} for i in df.columns],
        style_table={
            'backgroundColor': 'black',
            'width': '100%',
            'height': '400px',
            'overflowY': 'auto'
        },
        style_header={
            'backgroundColor': 'gray',
            'color': 'white',
            'fontWeight': 'bold',
            'border': '1px solid gray'
        },
        style_cell={
            'backgroundColor': 'black',
            'color': 'white',
            'border': '1px solid gray',
            'padding': '10px',
            'textAlign': 'center'
        },
        fixed_rows={'headers':True,'data':0},
        style_data={
            'backgroundColor': 'black'
        },
        style_data_conditional=style_data_conditional
    )
    
    return  dbc.Col([
           html.H3("Historique des montants des transactions des dix premiers destinataires.", style={'color': 'white','backgroundColor': 'lightblue','align':'center','padding-left':'7%'}),
            table
        ], width=8)
    


layout = html.Div([
  html.Div([
        dbc.Row(
            [
               ### col1
                dbc.Col(
                   dbc.Card(
                           [dbc.CardBody(
                                [
                                    html.Div([html.B(titre1,style={'color':'lightblue'}),html.H6(kpi1)], 
                                             className="text-left"), 
                                    dcc.Graph(figure=graph1,className="float-right", responsive=True,
                                              style={'margin-left': '10px','width': '260px','height': '150px'},
                                              config={'displayModeBar': False}),  
                                ],
                                className="d-flex")]), width=3),  
                #####col2
                dbc.Col(
                   dbc.Card(
                           [dbc.CardBody(
                                [
                                    html.Div([html.B(titre2,style={'color':'lightblue'}),html.H6(kpi2)], 
                                             className="text-left"), 
                                    dcc.Graph(figure=graph2,className="float-right", responsive=True,
                                              style={'margin-left': '10px','width': '300px','height': '150px'},
                                              config={'displayModeBar': False}),  
                                ],
                                className="d-flex")]), width=3),
                ########col3
                dbc.Col(
                   dbc.Card(
                           [dbc.CardBody(
                                [
                                    html.Div([html.B(titre3,style={'color':'lightblue'}),html.H6(kpi3)], 
                                             className="text-left"), 
                                    dcc.Graph(figure=graph3,className="float-right", responsive=True,
                                              style={'margin-left': '4px','width': '300px','height': '150px'},
                                              config={'displayModeBar': False}),  
                                ],
                                className="d-flex")]), width=3),
                dbc.Col(
                   dbc.Card(
                           [dbc.CardBody(
                                [
                                    html.Div([html.B(titre4,style={'color':'lightblue'}),html.H6(kpi4)], 
                                             className="text-left"), 
                                    dcc.Graph(figure=graph4,className="float-right", responsive=True,
                                              style={'margin-left': '10px','width': '300px','height': '150px'},
                                              config={'displayModeBar': False}),  
                                ],
                                className="d-flex")]), width=3)
            ],
            className="g-0",style={'margin-left': '10px','margin-right': '10px','margin-top': '20px'}  
        )
  ]),
   
   dbc.Row(
      [
         dbc.Col(
            dbc.Card(
               dbc.CardBody(
                  [
                     dcc.Graph(figure=retourne_transaction_type(),responsive=True)
                  ]
               )
            ),width=7
         ),
         dbc.Col(
            dbc.Card(
               dbc.CardBody(
                  [
                     dcc.Graph(figure=retourne_repartition_transaction(),responsive=True)
                  ]
               )
            ),width=5
         )
      ],style={'margin-left': '10px','margin-right': '10px','margin-top': '20px'}
   ),
   
   dbc.Row(
      [
         dbc.Col(
            dbc.Card(
               dbc.CardBody(
                  [
                     html.Div([ 
                               html.Button('Solde Initial Envoyeur', id='solde1',n_clicks=0, style={'height': '30px', 'cursor': 'pointer','background-color': 'green'}),
                               html.Button('Solde Final Envoyeur', id='solde2',n_clicks=0, style={'height': '30px', 'cursor': 'pointer','background-color': 'green'}),
                                html.Button('Montant vs type', id='solde3',n_clicks=0, style={'height': '40px', 'cursor': 'pointer','background-color': 'white'})
                              ], style={'display': 'flex', 'justify-content': 'flex-end', 'margin-bottom': '20px','gap': '20px'}),
                     dcc.Graph(id='barr-plot',figure=retourne_repartition_transaction_sender_final_null(),responsive=True)
                  ]
               )
            ),width=8
         ),
          dbc.Col(
            dbc.Card(
               dbc.CardBody(
                  [
                     dcc.Graph(id='barr-pot',figure=retourne_dist_montant_type(),responsive=True,style={'height': '505px'})
                  ]
               )
            ),width=4
         ),
         
      ],style={'margin-left': '10px','margin-right': '10px','margin-top': '20px','height': '500px'}
   ),
   
   dbc.Row(
      [ 
         create_styled_table(df_sender),
         dbc.Col(
            dbc.Card(
               dbc.CardBody(
                  [
                     html.H3("TOP 10 Recepteur et Envoyeur", style={'color': 'white','backgroundColor': 'lightblue','align':'center','padding-left':'7%'}),
                     dash_table.DataTable(
                        id='table',
                        columns=[{"name": '(TOP 10) Nom du recepteur', "id": 'nameDest'} ,
                                 {"name": 'Total transaction implique', "id": 'Effectif'}],
                        data=data_sender_null.to_dict('records'),
                        style_data_conditional=[{
                        'backgroundColor': 'black',
                        'textAlign': 'center'
                      }],   
                        fixed_rows={'headers':True,'data':0},
                        style_table={'height': '160px', 'overflowY': 'auto'},
                        style_header={
                        'backgroundColor': 'gray',
                        'fontWeight': 'bold'
                     }, 
                     ),
                     html.Hr(),
                     dash_table.DataTable(
                        id='table2',
                        columns=[{"name": '(TOP 10) Nom du Envoyeur', "id": 'nameOrig'} ,
                                 {"name": 'Total transaction implique', "id": 'count'}],
                        data=data_recep_null.to_dict('records'),
                        style_data_conditional=[{
                        'backgroundColor': 'black',
                        'textAlign': 'center'
                      }],   
                        fixed_rows={'headers':True,'data':0},
                        style_table={'height': '160px', 'overflowY': 'auto'},
                        style_header={
                        'backgroundColor': 'gray',
                        'fontWeight': 'bold'
                     }, 
                     )
                  ]
               )
            ),width=4
         )
      ],style={'margin-left': '20px','margin-right': '0px','margin-top': '30px','height': '500px'}
   )
   
   
],style={
   'margin-left': '20px',
   'margin-right': '30px',
   'background-image': 'url("/assets/image.png")',  # Chemin vers l'image
   'background-size': 'cover',  # Ajuster l'image pour couvrir tout l'arrière-plan
   'background-position': 'center',  # Centrer l'image
   'background-repeat': 'no-repeat',  # Ne pas répéter l'image
          
    })






@app.callback(
    Output('barr-plot', 'figure'),
      [Input('solde1', 'n_clicks'),
      Input('solde2', 'n_clicks'),
      Input('solde3', 'n_clicks')
      ]
)
def update_graph(solde1_clicks, solde2_clicks,solde3_clicks):
    ctx = dash.callback_context

    if not ctx.triggered:
        raise dash.exceptions.PreventUpdate
    
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'solde1':
        fig = retourne_repartition_transaction_sender_null()
    elif button_id == 'solde2':
        fig = retourne_repartition_transaction_sender_final_null()
    elif button_id == 'solde3':
       fig = distribution_montant()
    return fig



@app.callback(
    [Output('solde1', 'style'), Output('solde2', 'style')],
    [Input('solde1', 'n_clicks'), Input('solde2', 'n_clicks')]
)
def update_button_styles(n_clicks1, n_clicks2):
    style1 = {'background-color': 'white'}
    style2 = {'background-color': 'white'}
   
    if n_clicks1 is not None and n_clicks1 > 0:
        style1['background-color'] = 'lightblue' # Bouton 1 cliqué
       
    
    if n_clicks2 is not None and n_clicks2 > 0:
        style2['background-color'] = 'lightblue' # Bouton 2 cliqué
        
        
        
        
    return style1, style2