#importing pandas and the dataframe
import pandas as pd
pd.set_option('display.max_columns',None)
df = pd.read_excel(r'C:\Users\Dell\Downloads\Vendas.xlsx',engine='openpyxl')

#filtering and grouping the dataframe to find out the revenues of each store
revenue = df[['ID Loja','Valor Final']].groupby('ID Loja').sum()

#filtering and grouping the dataframe to find out the sales amount of each store
quantidade = df[['ID Loja','Quantidade']].groupby('ID Loja').sum()

#calculating the average revenue per sale -> problem if as_index=False is active
ticket_medio = (revenue['Valor Final'] / quantidade['Quantidade']).to_frame()

#importing pywin32
import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'marcosemn@hotmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{revenue.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Marcos</p>
'''

mail.Send()

print('Email Enviado')