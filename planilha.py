import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACe9a214ad109cdd4e81c92e9f5dab724d"
# Your Auth Token from twilio.com/console
auth_token  = "e58a89817399eb260f9e5a989fe4346f"
client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['VENDA'] > 28300).any():
        vendedor = tabela_vendas.loc[tabela_vendas['VENDA'] > 28300, 'VENDEDOR'].values[0]
        venda = tabela_vendas.loc[tabela_vendas['VENDA'] > 28300, 'VENDA'].values[0]

        print (f'no mês de {mes} o vendedor {vendedor} vendeu R${venda} ')
        message = client.messages.create(
            to="+5571992571743", 
            from_="+19789868002",
            body=f'no mês de {mes} o vendedor {vendedor} vendeu R${venda} ')

        print(message.sid)








