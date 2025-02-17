import pandas as pd
import plotly.express as px

Nb_transaction_jour = pd.read_csv('data/J_vs_T.csv', index_col=0)
Nb_fraud_jour = pd.read_csv('data/fraud_count_by_date.csv')
Nb_suspect_jour = pd.read_csv('data/Tsuspect_count_date.csv',index_col=0).sort_values(by='jour_du_mois')
tot_montant_fraud = pd.read_csv('data/tmontant_suspect_df_jour.csv',index_col=0).sort_values(by='jour_du_mois') 




def retourne_information_transaction(Nb_transaction_jour=Nb_transaction_jour):
    Total_transaction = Nb_transaction_jour['Total Transaction'].sum()
    height = 150
    width = 270
    col="#4F4F4F"
    fig = px.area(Nb_transaction_jour, x='jour de la simulation', y='Total Transaction')
    fig.update_layout(margin=dict(t=20,l=0,r=0,b=0),
                        xaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        yaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        paper_bgcolor=col,plot_bgcolor=col,height=height,width=width,
                        title={'text':'', 'font': {'size': 14, 'color': 'white'}},)
    fig.update_traces(line=dict(color='white'))
    fig.update_traces(
    hovertemplate='<b>Jour:  %{x}</b><br><b>Nombre de Transaction : %{y:.0f}</b>'  # Format de l'affichage
    )

    return "{:,.0f}".format(Total_transaction).replace(",", " "), fig,'Total transaction'


###############################################################################


def retourne_information_fraude(Nb_fraud_jour=Nb_fraud_jour):
    Total_Frauduleux =  Nb_fraud_jour['count'].sum()
    height = 150
    width = 270
    col="#4F4F4F"
    fig = px.area(Nb_fraud_jour, x='jour_du_mois', y='count')
    fig.update_layout(margin=dict(t=20,l=0,r=0,b=0),
                        xaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        yaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        paper_bgcolor=col,plot_bgcolor=col,height=height,width=width,
                        title={'text':'', 'font': {'size': 14, 'color': 'white'}},)
    fig.update_traces(line=dict(color='white'))
    fig.update_traces(
        hovertemplate='<b>Jour:  %{x}</b><br><b>Nombre de fraude : %{y}</b>'  # Format de l'affichage
    )
    
    return "{:,.0f}".format(Total_Frauduleux).replace(",", " "), fig,'Total Fraude'

###############################################################################
 

def retourne_information_suspect(Nb_suspect_jour=Nb_suspect_jour):
    Total_suspect =  Nb_suspect_jour['count'].sum()
    height = 150
    width = 270
    col="#4F4F4F"
    fig = px.area(Nb_suspect_jour, x='jour_du_mois', y='count')
    fig.update_layout(margin=dict(t=20,l=0,r=0,b=0),
                        xaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        yaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        paper_bgcolor=col,plot_bgcolor=col,height=height,width=width,
                        title={'text':'', 'font': {'size': 14, 'color': 'white'}},)
    fig.update_traces(line=dict(color='white'))
    fig.update_traces(
        hovertemplate='<b>Jour:  %{x}</b><br><b>Nombre de transaction(>200 000) : %{y}</b>'  # Format de l'affichage
    )
    
    return Total_suspect, fig,'Total Suspect'
###################################################################################################




def retourne_information_monant(tot_montant_fraud=tot_montant_fraud):
    Total_suspect =  tot_montant_fraud['total_amount'].sum()
    height = 150
    width = 270
    col="#4F4F4F"
    fig = px.area(tot_montant_fraud, x='jour_du_mois', y='total_amount')
    fig.update_layout(margin=dict(t=20,l=0,r=0,b=0),
                        xaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        yaxis=dict(showgrid=False,color=col,title="",showticklabels=False,showline=False,zeroline=False),
                        paper_bgcolor=col,plot_bgcolor=col,height=height,width=width,
                        title={'text':'', 'font': {'size': 14, 'color': 'white'}},)
    fig.update_traces(line=dict(color='white'))
    fig.update_traces(
        hovertemplate='<b>Jour:  %{x}</b><br><b>Total Montant Frauduleux : %{y:.0f}</b>'  # Format de l'affichage
    )
    
    return  "{:,.2f} $".format(Total_suspect).replace(",", " "), fig,'Total Montant Frauduleux'

