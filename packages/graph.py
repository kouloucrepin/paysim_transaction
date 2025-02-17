import pandas as pd
import plotly.express as px

type_vs_jours = pd.read_csv('data/type_vs_eff_jour_T.csv',index_col=0)
type_ = pd.read_csv('data/type_vs_eff_T.csv',index_col=0)
data_sender_null = pd.read_csv('data/T_sold_sender_Null.csv',index_col=0)
data_sender_final_null = pd.read_csv('data/T_Final_sold_sender_null.csv',index_col=0)
dest_evol_sold = pd.read_csv('data/montant_type_steps.csv')

def retourne_transaction_type(type_vs_jours=type_vs_jours):
    height = 450
    width = 1050
        
    fig = px.area(type_vs_jours, x='jour_du_mois', y='count', color='type', title='Répartition des  transactions par type et par jour')
    fig.update_layout(
        margin=dict(t=30,l=0,r=0,b=0),
        yaxis=dict(title="Effectif"),legend=dict(orientation="h",yanchor="bottom",y=-0.2,xanchor="center",x=0.5),
        xaxis=dict(title="Jour",showgrid=False),template="seaborn",width=width
        
        )
    fig.update_xaxes(
        type='category',  categoryorder='array',  
        categoryarray=[i for i in type_vs_jours.sort_values(by='jour_du_mois').jour_du_mois]  
    )
    return fig


####################################

def retourne_repartition_transaction(type_=type_):
    height = 350
    width = 1050
    fig = px.bar(type_.sort_values(by='Effectif'), y='type', x='Effectif', title='Répartition des transactions par type de transactions',text_auto='.0f')
    fig.update_layout(xaxis=dict(showgrid=False,title="",
                      showticklabels=False,showline=False,zeroline=False),
                      yaxis=dict(showgrid=False,title=""),
                      margin=dict(t=30,l=0,r=0,b=0),
                      height=height,width=width,template="seaborn")
    fig.update_traces(marker_color='wheat',marker_line_color='black',opacity=1,marker_line_width=2)
    
    return fig


####################################

def retourne_repartition_transaction_sender_final_null(data_sender_final_null=data_sender_final_null):
    height = 350
    width = 1050
    fig = px.bar(data_sender_final_null.sort_values(by='jour_du_mois'), x='jour_du_mois', y='Nombre', title='Repartition des Transactions avec solde final de l envoyeur nul par jour')
    fig.update_xaxes(
        type='category',  
        categoryorder='array',  
        categoryarray=[i for i in data_sender_final_null.sort_values(by='jour_du_mois').jour_du_mois]  
    )
    fig.update_layout(xaxis=dict(showgrid=False,title="Jour"),
                          yaxis=dict(showgrid=True,title="Total Transaction"),
                          margin=dict(t=30,l=0,r=0,b=0),
                          height=height,width=width,template="seaborn")
    fig.update_traces(marker_color='wheat',marker_line_color='black',opacity=1,marker_line_width=1)
    return fig

####################################beige


def retourne_repartition_transaction_sender_null(data_sender_null=data_sender_null):
    height = 350
    width = 1050
    fig = px.bar(data_sender_null.sort_values(by='jour_du_mois'), x='jour_du_mois', y='Nombre', title='Repartition des Transactions avec solde initial de l envoyeur nul par jour')
    fig.update_xaxes(
        type='category',  
        categoryorder='array',  
        categoryarray=[i for i in data_sender_null.sort_values(by='jour_du_mois').jour_du_mois]  
    )
    fig.update_layout(xaxis=dict(showgrid=False,title="Jour"),
                          yaxis=dict(showgrid=True,title="Total Transaction"),
                          margin=dict(t=30,l=0,r=0,b=0),
                          height=height,width=width,template="seaborn")
    fig.update_traces(marker_color='wheat',marker_line_color='black',opacity=1,marker_line_width=1)
    return fig


########################################
def distribution_montant(dest_evol_sold=dest_evol_sold):
    height=400
    width=900
    fig = px.box(dest_evol_sold, y="type",x='amount', title="Répartition des montants par heure suivant les types de transferts",template='seaborn')
    fig.update_traces(marker_color='#B85C00',marker_line_color='black',opacity=1,marker_line_width=1)
    fig.update_layout(xaxis=dict(showgrid=False,title="Jour"),
                            yaxis=dict(showgrid=True,title="Total Montant"),
                            margin=dict(t=30,l=0,r=0,b=0),
                            height=height,width=width,template="seaborn")
    
    return fig

############################################

def retourne_dist_montant_type(dest_evol_sold=dest_evol_sold):
    height=400
    width=900
    fig = px.funnel(dest_evol_sold.groupby('type')['amount'].sum().to_frame().reset_index().sort_values(by='amount',ascending=False), y="type",x='amount', title="Répartition des montants par heure suivant <br>les types de transferts",template='seaborn')
    fig.update_traces(marker_color='#B85C00',marker_line_color='black',opacity=1,marker_line_width=1)
    fig.update_layout(xaxis=dict(showgrid=False,title=""),
                            yaxis=dict(showgrid=True,title=""),
                            margin=dict(t=50,l=0,r=0,b=0),
                            height=height,width=width,template="seaborn")
    
    return fig


