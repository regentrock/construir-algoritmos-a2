import datetime
import requests


def cotar():
    cotacoes = []
    hoje = datetime.date.today()

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)

        while True:
            data = dia.strftime("%m-%d-%Y")

            url = (
                "https://olinda.bcb.gov.br/olinda/servico/PTAX/"
                "versao/v1/odata/CotacaoDolarDia(dataCotacao=@data)?"
                f"@data='{data}'&$top=1&$format=json"
            )

            resposta = requests.get(url)
            dados = resposta.json()["value"]

            if dados:
                cotacoes.append(dados[0]["cotacaoCompra"])
                break

            dia -= datetime.timedelta(days=1)

    return cotacoes

print(len(cotar()))
print(cotar())
