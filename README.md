# Introdução

Essa SDK foi construída com o intuito de torná-la flexível, de forma que todos possam utilizar todas as features, de todas as versões de API.

Você pode acessar a documentação oficial do Pagar.me acessando esse [link](https://docs.pagar.me).

## Index

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Transações](#transações)
- [Criando uma transação](#criando-uma-transação)
- [Capturando uma transação](#capturando-uma-transação)
- [Estornando uma transação](#estornando-uma-transação)
  - [Estornando uma transação parcialmente](#estornando-uma-transação-parcialmente)
  - [Estornando uma transação com split](#estornando-uma-transação-com-split)
- [Retornando transações](#retornando-transações)
- [Retornando uma transação](#retornando-uma-transação)
- [Retornando recebíveis de uma transação](#retornando-recebíveis-de-uma-transação)
- [Retornando um recebível de uma transação](#retornando-um-recebível-de-uma-transação)
- [Retornando o histórico de operações de uma transação](#retornando-o-histórico-de-operações-de-uma-transação)
- [Retornando eventos de uma transação](#retornando-eventos-de-uma-transação)
- [Calculando Pagamentos Parcelados](#calculando-pagamentos-parcelados)
- [Testando pagamento de boletos](#testando-pagamento-de-boletos)
- [Cartões](#cartões)
  - [Criando cartões](#criando-cartões)
  - [Retornando cartões](#retornando-cartões)
  - [Retornando um cartão](#retornando-um-cartão)
- [Planos](#planos)
  - [Criando planos](#criando-planos)
  - [Retornando planos](#retornando-planos)
  - [Retornando um plano](#retornando-um-plano)
  - [Atualizando um plano](#atualizando-um-plano)
- [Assinaturas](#assinaturas)
  - [Criando assinaturas](#criando-assinaturas)
  - [Split com assinatura](#split-com-assinatura)
  - [Retornando uma assinatura](#retornando-uma-assinatura)
  - [Retornando assinaturas](#retornando-assinaturas)
  - [Atualizando uma assinatura](#atualizando-uma-assinatura)
  - [Cancelando uma assinatura](#cancelando-uma-assinatura)
  - [Transações de assinatura](#transações-de-assinatura)
  - [Pulando cobranças](#pulando-cobranças)
- [Postbacks](#postbacks)
  - [Retornando postbacks](#retornando-postbacks)
  - [Retornando um postback](#retornando-um-postback)
  - [Reenviando um Postback](#reenviando-um-postback)
  - [Validando uma requisição de postback](#validando-uma-requisição-de-postback)
- [Saldo do recebedor principal](#saldo-do-recebedor-principal)
- [Operações de saldo](#operações-de-saldo)
  - [Histórico das operações](#histórico-das-operações)
  - [Histórico de uma operação específica](#histórico-de-uma-operação-específica)
- [Recebível](#recebível)
  - [Retornando recebíveis](#retornando-recebíveis)
  - [Retornando um recebível](#retornando-um-recebível)
- [Transferências](#transferências)
  - [Criando uma transferência](#criando-uma-transferência)
  - [Retornando transferências](#retornando-transferências)
  - [Retornando uma transferência](#retornando-uma-transferência)
  - [Cancelando uma transferência](#cancelando-uma-transferência)
- [Antecipações](#antecipações)
  - [Criando uma antecipação](#criando-uma-antecipação)
  - [Obtendo os limites de antecipação](#obtendo-os-limites-de-antecipação)
  - [Confirmando uma antecipação building](#confirmando-uma-antecipação-building)
  - [Cancelando uma antecipação pending](#cancelando-uma-antecipação-pending)
  - [Deletando uma antecipação building](#deletando-uma-antecipação-building)
  - [Retornando antecipações](#retornando-antecipações)
- [Contas bancárias](#contas-bancárias)
  - [Criando uma conta bancária](#criando-uma-conta-bancária)
  - [Retornando uma conta bancária](#retornando-uma-conta-bancária)
  - [Retornando contas bancárias](#retornando-contas-bancárias)
- [Recebedores](#recebedores)
  - [Criando um recebedor](#criando-um-recebedor)
  - [Retornando recebedores](#retornando-recebedores)
  - [Retornando um recebedor](#retornando-um-recebedor)
  - [Atualizando um recebedor](#atualizando-um-recebedor)
  - [Saldo de um recebedor](#saldo-de-um-recebedor)
  - [Operações de saldo de um recebedor](#operações-de-saldo-de-um-recebedor)
  - [Operação de saldo específica de um recebedor](#operação-de-saldo-específica-de-um-recebedor)
- [Clientes](#clientes)
  - [Criando um cliente](#criando-um-cliente)
  - [Retornando clientes](#retornando-clientes)
  - [Retornando um cliente](#retornando-um-cliente)
- [Links de pagamento](#links-de-pagamento)
  - [Criando um link de pagamento](#criando-um-link-de-pagamento)
  - [Retornando links de pagamento](#retornando-links-de-pagamento)
  - [Retornando um link de pagamento](#retornando-um-link-de-pagamento)
  - [Cancelando um link de pagamento](#cancelando-um-link-de-pagamento)

## Instalação

Instale a biblioteca utilizando o comando:

```shell
$ pip install pagarme-python
```

## Configuração

Para incluir a biblioteca em seu projeto, basta fazer o seguinte:

```python
import pagarme

pagarme.authentication_key('SUA_API_KEY')
```

## Transações

Nesta seção será explicado como utilizar transações no Pagar.me com essa biblioteca.

### Criando uma transação

```python
transaction = pagarme.transaction.create({
  "amount": "21000",
  "card_number": "4111111111111111",
  "card_cvv": "123",
  "card_expiration_date": "0922",
  "card_holder_name": "Morpheus Fishburne",
  "customer": {
    "external_id": "#3311",
    "name": "Morpheus Fishburne",
    "type": "individual",
    "country": "br",
    "email": "mopheus@nabucodonozor.com",
    "documents": [
      {
        "type": "cpf",
        "number": "30621143049"
      }
    ],
    "phone_numbers": ["+5511999998888", "+5511888889999"],
    "birthday": "1965-01-01"
  },
  "billing": {
    "name": "Trinity Moss",
    "address": {
      "country": "br",
      "state": "sp",
      "city": "Cotia",
      "neighborhood": "Rio Cotia",
      "street": "Rua Matrix",
      "street_number": "9999",
      "zipcode": "06714360"
    }
  },
  "shipping": {
    "name": "Neo Reeves",
    "fee": "1000",
    "delivery_date": "2000-12-21",
    "expedited": True,
    "address": {
      "country": "br",
      "state": "sp",
      "city": "Cotia",
      "neighborhood": "Rio Cotia",
      "street": "Rua Matrix",
      "street_number": "9999",
      "zipcode": "06714360"
    }
  },
  "items": [
    {
      "id": "r123",
      "title": "Red pill",
      "unit_price": "10000",
      "quantity": "1",
      "tangible": True
    },
    {
      "id": "b123",
      "title": "Blue pill",
      "unit_price": "10000",
      "quantity": "1",
      "tangible": True
    }
  ]
})
```

### Capturando uma transação

```python
transactionCapture = pagarme.transaction.capture(
    'ID_TRANSAÇÃO_OU_TOKEN',
    {"amount": "Valor a ser capturado"}
)
```

### Estornando uma transação

```python
transactionRefund = pagarme.transaction.refund(
  'ID_TRANSAÇÃO',
  {"amount": "Valor a ser estornado"}
)
```

Esta funcionalidade também funciona com estornos parciais, ou estornos com split. Por exemplo:

#### Estornando uma transação parcialmente

```python
pagarme.transaction.refund(
  'ID_TRANSACAO',
  {"amount": "Valor a ser estornado parcialmente"}
)
```

#### Estornando uma transação com split

```python
pagarme.transaction.refund(
  'ID_TRANSACAO',
  {
    "amount": "Valor a ser estornado",
    "split_rules": [
      {
          "id": "ID_SPLIT_RULE",
          "amount": "60000",
          "recipient_id": "ID_RECEBEDOR"
      },
      {
          "id": "ID_SPLIT_RULE",
          "amount": "11000",
          "recipient_id": "ID_RECEBEDOR",
          "charge_processing_fee": "true"
      }
    ]
  }
)
```

### Retornando Transações

```python
transactions = pagarme.transaction.find_all()
```

### Retornando uma transação 

```python
transaction = pagarme.transaction.find_by({"id":"ID_TRANSAÇÃO"})
```

### Retornando recebíveis de uma transação

```python
transactionPayables = pagarme.transaction.payables('ID_TRANSAÇÃO')
```

### Retornando um recebível de uma transação

```python
transactionPayable  = pagarme.transaction.specific_payable('ID_TRANSAÇÃO', "ID_DO_RECEBIVEL")
```

### Retornando o histórico de operações de uma transação

```python
transactionOperations = pagarme.transaction.operations('ID_TRANSAÇÃO')
```

### Retornando eventos de uma transação 

```python
transacionEvents = pagarme.transaction.events("ID_TRANSAÇÃO")
```

### Calculando pagamentos parcelados

Essa rota não é obrigatória para uso. É apenas uma forma de calcular pagamentos parcelados com o Pagar.me.

Para fins de explicação, utilizaremos os seguintes valores:

`amount`: 1000, `free_installments`: 4, `max_installments`: 12, `interest_rate`: 3

O parâmetro `free_installments` decide a quantidade de parcelas sem juros. Ou seja, se ele for preenchido com o valor `4`, as quatro primeiras parcelas não terão alteração em seu valor original.

Nessa rota, é calculado juros simples, efetuando o seguinte calculo:

valorTotal = valorDaTransacao * ( 1 + ( taxaDeJuros * numeroDeParcelas ) / 100 )

Então, utilizando os valores acima, na quinta parcela, a conta ficaria dessa maneira:

valorTotal = 1000 * (1 + (3 * 5) / 100)

Então, o valor a ser pago na quinta parcela seria de 15% da compra, totalizando 1150.

Você pode usar o código abaixo caso queira utilizar essa rota:

```python
transactionCalculate = pagarme.transaction.calculate_installments_amount({
    "amount": "10000",
    "free_installments": "1",
    "interest_rate": "13",
    "max_installments": "3"
  })
})
```

### Testando pagamento de boletos

```python
transactionPayBoleto = pagarme.transaction.pay_boleto(
    "ID_TRANSAÇÃO",
    {"status": "paid"}
)
```

## Cartões

Sempre que você faz uma requisição através da nossa API, nós guardamos as informações do portador do cartão, para que, futuramente, você possa utilizá-las em novas cobranças, ou até mesmo implementar features como one-click-buy.


### Criando Cartões

```python
card = pagarme.card.create({
    "card_expiration_date": "1122",
    "card_number": "4018720572598048",
    "card_cvv": "123",
    "card_holder_name": "Cersei Lannister"
})
```

### Retornando cartões

```python
cards = pagarme.card.find_all()
```

### Retornando um cartão

```python
card = pagarme.card.find_by({"id": "ID_CARTÃO"})
```

## Planos

Representa uma configuração de recorrência a qual um cliente consegue assinar.
É a entidade que define o preço, nome e periodicidade da recorrência

### Criando planos

```python
plan = pagarme.plan.create({
    "amount": "15000",
    "days": "30",
    "name": "Curso com o Alto Pardal"
})
```

### Retornando planos

```python
plans = pagarme.plan.find_all()
```

### Retornando um plano

```python
plan = pagarme.plan.find_by({"id":"ID_PLANO"})
```

### Atualizando um plano

```python
planUpdate = pagarme.plan.update(
  "ID_PLANO",
  {
      "name": "Esgrima com Syrio Forel",
      "trial_days": "7"
  }
)
```

## Assinaturas

### Criando assinaturas

```python
subscription = pagarme.subscription.create({
  "card_id": "card_cj6qvosem04w3nu6dm20nu8od",
  "customer":{
      "email":"jorah.mormont@gameofthrones.com",
      "name":"Sir Jorah Mormont",
      "document_number":"18152564000105",
      "address":{
          "zipcode":"04571020",
          "neighborhood":"Cidade Moncoes",
          "street":"R. Dr. Geraldo Campos Moreira",
          "street_number":"240"
      },
      "phone": {
          "number":"987654321",
          "ddd":"11"
      }
  },
  "payment_method": "credit_card",
  "plan_id": "201836",
  "postback_url": "http://requestb.in/zyn5obzy"
})
```

### Split com assinatura

```python
subscriptionSplit = pagarme.subscription.create({
  "card_id": "ID_CARTÃO",
  "customer":{
      "email":"aardvark.silva@gmail.com",
      "name":"Sir Jorah Mormont",
      "document_number":"18152564000105",
      "address":{
          "zipcode":"04571020",
          "neighborhood":"Cidade Moncoes",
          "street":"R. Dr. Geraldo Campos Moreira",
          "street_number":"240"
      },
      "phone": {
          "number":"987654321",
          "ddd":"11"
      }
  },
  "split_rules":[
      {
          "recipient_id": "ID_RECEBEDOR",
          "percentage": "25"
      },
      {
          "recipient_id": "ID_RECEBEDOR",
          "percentage": "75"
      }
  ],
  "payment_method": "credit_card",
  "plan_id": "ID_PLANO",
  "postback_url": "http://requestb.in/zyn5obzy"
})
```

### Retornando uma assinatura

```python
  subscription = pagarme.subscription.find_by({"id": "ID_ASSINATURA"})

```

### Retornando assinaturas

```python
  subscriptions = pagarme.subscription.find_all()

```

### Atualizando uma assinatura

```python
subscriptionUpdate= pagarme.subscription.update(
  "ID_ASSINATURA",
  {
      "card_id": "ID_CARTÃO",
      "payment_method": "credit_card",
      "plan_id": "ID_PLANO"
  }
)
```

### Cancelando uma assinatura

```python
  subscriptionCancel = pagarme.subscription.cancel("ID_ASSINATURA")

```

### Transações de assinatura
```python
  subscriptionTransactions = pagarme.subscription.transactions("ID_ASSINATURA")

```

### Pulando cobranças

```python
  subscriptionSettleCharges = pagarme.subscription.settle_charges("ID_ASSINATURA")

```

## Postbacks

Ao criar uma transação ou uma assinatura você tem a opção de passar o parâmetro postback_url na requisição. Essa é uma URL do seu sistema que irá então receber notificações a cada alteração de status dessas transações/assinaturas.

Para obter informações sobre postbacks, 3 informações serão necessárias, sendo elas: `model`, `model_id` e `postback_id`.

`model`: Se refere ao objeto que gerou aquele POSTback. Pode ser preenchido com o valor `transaction` ou `subscription`.

`model_id`: Se refere ao ID do objeto que gerou ao POSTback, ou seja, é o ID da transação ou assinatura que você quer acessar os POSTbacks.

`postback_id`: Se refere à notificação específica. Para cada mudança de status de uma assinatura ou transação, é gerado um POSTback. Cada POSTback pode ter várias tentativas de entregas, que podem ser identificadas pelo campo `deliveries`, e o ID dessas tentativas possui o prefixo `pd_`. O campo que deve ser enviado neste parâmetro é o ID do POSTback, que deve ser identificado pelo prefixo `po_`. 

### Retornando postbacks

```python
postbacks = pagarme.transaction.postbacks("ID_DA_TRANSAÇÃO")
```

### Retornando um postback

```python
postback = pagarme.transaction.specific_postback("ID_DA_TRANSAÇÃO", "ID_POSTBACK")
```

### Reenviando um Postback

```python
postbackRedeliver = pagarme.transaction.postback_redeliver("ID_DA_TRANSAÇÃO", "ID_POSTBACK")
```

### Validando uma requisição de postback

```python
postbackValidate = pagarme.postback.validate("signature", "payload", "api_key")
```

## Saldo do recebedor principal

Para saber o saldo de sua conta, você pode utilizar esse código:

```python
balance = pagarme.balance.default_recipient_balance()
```

Observação: o código acima serve somente de exemplo para que o processo de validação funcione. Recomendamos que utilize ferramentas fornecidas por bibliotecas ou frameworks para recuperar estas informações de maneira mais adequada.

## Operações de saldo

Com este objeto você pode acompanhar todas as movimentações financeiras ocorridas em sua conta Pagar.me.

### Histórico das operações

```python
balanceOperations = pagarme.balance_operation.find_all()
```

### Histórico específico de uma operação

```python
balanceOperation = pagarme.balance_operation.find_by({"id": "ID_BALANCE_OPERATION"})
```

## Recebível

Objeto contendo os dados de um recebível. O recebível (payable) é gerado automaticamente após uma transação ser paga. Para cada parcela de uma transação é gerado um recebível, que também pode ser dividido por recebedor (no caso de um split ter sido feito).

### Retornando recebíveis

```python
payables = pagarme.payable.find_all()
```

### Retornando um recebível

```python
payable = pagarme.payable.find_by({"id": "ID_RECEBÍVEL"})
```

## Transferências
Transferências representam os saques de sua conta.

### Criando uma transferência

```python
transfer = pagarme.transfer.create({
    'amount': '10000',
    'recipient_id': 'ID_RECEBEDOR'
})
```

### Retornando transferências

```python
transfers = pagarme.transfer.find_all()
```

### Retornando uma transferência

```python
transfer = pagarme.transfer.find_by({"id": "ID_TRANSFERÊNCIA"})
```

### Cancelando uma transferência

```python
transferCancel = pagarme.transfer.cancel("ID_TRANSFERÊNCIA")
```

## Antecipações

Para entender o que são as antecipações, você deve acessar esse [link](https://docs.pagar.me/docs/overview-antecipacao).

### Criando uma antecipação

```python
bulkAnticipation = pagarme.bulk_anticipation.create('ID_RECEBEDOR', {
  'payment_date': '1462999741870',
  'timeframe': 'start',
  'requested_amount': '100000'
})
```

### Obtendo os limites de antecipação

```python
bulkAnticipationData = {
    'payment_date': 1503921427000,
    'timeframe': 'start'
}

defaultRecipientId = pagarme.recipient.default_recipient()['test'] #test ou live
limits = pagarme.bulk_anticipation.limits(defaultRecipientId,  bulkAnticipationData)
```

### Confirmando uma antecipação building

```python
defaultRecipientId = pagarme.recipient.default_recipient()['test'] #test ou live
confirmBulkAnticipation = pagarme.bulk_anticipation.confirm(defaultRecipientId, "ID_ANTECIPAÇÃO")
```

### Cancelando uma antecipação pending

```python
canceledBulkAnticipation = pagarme.bulk_anticipation.cancel(recipient['id'], bulk_anticipation['id'])
```

### Deletando uma antecipação building

```python
defaultRecipientId = pagarme.recipient.default_recipient()['test'] #test ou live
deleteBulkAnticipation = pagarme.bulk_anticipation.delete(defaultRecipientId, "ID_ANTECIPAÇÃO")
```

### Retornando antecipações

```python
defaultRecipientId = pagarme.recipient.default_recipient()['test']
bulkAnticipations = pagarme.bulk_anticipation.find_all(defaultRecipientId)
```

## Contas bancárias

Contas bancárias identificam para onde será enviado o dinheiro de futuros pagamentos.

### Criando uma conta bancária

```python
bankAccount = pagarme.bank_account.create({
  'agencia': '0932',
  'agencia_dv': '5',
  'bank_code': '341',
  'conta': '58054',
  'conta_dv': '1',
  'document_number': '26268738888',
  'legal_name': 'HOUSE TARGARYEN'
})
```

### Retornando uma conta bancária

```python
bankAccount = pagarme.bank_account.find_by({"id":"ID_BANK_ACCOUNT"})
```

### Retornando contas bancárias

```python
bankAccounts = pagarme.bank_account.find_all()
```

## Recebedores

Para dividir uma transação entre várias entidades, é necessário ter um recebedor para cada uma dessas entidades. Recebedores contém informações da conta bancária para onde o dinheiro será enviado, e possuem outras informações para saber quanto pode ser antecipado por ele, ou quando o dinheiro de sua conta será sacado automaticamente.

### Criando um recebedor

```python
recipient = pagarme.recipient.create({
  'anticipatable_volume_percentage': '80',
  'automatic_anticipation_enabled': 'true',
  'transfer_day': '5',
  'transfer_enabled': 'true',
  'transfer_interval': 'weekly',
  'bank_account':{
      'agencia': '0932',
      'agencia_dv': '5',
      'bank_code': '341',
      'conta': '58054',
      'conta_dv': '1',
      'document_number': '26268738888',
      'legal_name': 'HOUSE TARGARYEN'
  }
})
```

### Retornando recebedores

```python
recipients = pagarme.recipient.find_all()
```

### Retornando um recebedor

```python
recipient - pagarme.recipient.find_by({"id":"ID_RECEBEDOR"})
```

### Atualizando um recebedor

```python
recipientUpdate = pagarme.recipient.update_recipient(
  "ID_RECEBEDOR",
  {
      "anticipatable_volume_percentage": "80",
      "bank_account_id": "ID_BANK_ACCOUNT"
  }
)
```

### Saldo de um recebedor

```python
recipientBalance = pagarme.recipient.recipient_balance("ID_RECEBEDOR")
```

### Operações de saldo de um recebedor

```python
recipientBalanceOperations = pagarme.recipient.recipient_balance_operation("ID_RECEBEDOR")
```

### Operação de saldo específica de um recebedor

```python
recipientBalanceOperation = balance_operation = pagarme.recipient.recipient_balance_operation_id("ID_RECEBEDOR", "ID_OPERAÇÃO")
```

## Clientes

Clientes representam os usuários de sua loja, ou negócio. Este objeto contém informações sobre eles, como nome, e-mail e telefone, além de outros campos.

### Criando um cliente

```python
customer = pagarme.customer.create({
  'external_id': '#123456789',
  'name': 'João das Neves',
  'type': 'individual',
  'country': 'br',
  'email': 'joaoneves@norte.com',
  'documents': [
    {
      'type': 'cpf',
      'number': '11111111111'
    }
  ],
  'phone_numbers': ['+5511999999999', '+5511888888888'],
  'birthday': '1985-01-01'
})
```

### Retornando clientes

```python
customers = pagarme.customer.find_all()
```

### Retornando um cliente

```python
customer = pagarme.customer.find_by({"id": "ID_CUSTOMER"})
```

## Links de pagamento

### Criando um link de pagamento

```python
paymentLink = pagarme.paymentLinks.create({
  'amount' : 10000,
  'items' : {
    {
      'id' : '1',
      'title' : "Fighter's Sword",
      'unit_price' : 4000,
      'quantity' : 1,
      'tangible' : true,
      'category' : 'weapon',
      'venue' : 'A Link To The Past',
      'date' : '1991-11-21'
    },
    {
      'id' : '2',
      'title' : 'Kokiri Sword',
      'unit_price' : 6000,
      'quantity' : 1,
      'tangible' : true,
      'category' : 'weapon',
      'venue' : "Majora's Mask",
      'date' : '2000-04-27'
    },
  },
  'payment_config' : {
    'boleto' : {
      'enabled' : true,
      'expires_in' : 20
    },
    'credit_card' : {
      'enabled' : true,
      'free_installments' : 4,
      'interest_rate' : 25,
      'max_installments' : 12
    },
    'default_payment_method' : 'boleto'
  },
  'max_orders' : 1,
  'expires_in' : 60
})
```

### Retornando links de pagamento

```python
paymentLinks = pagarme.payment_link.find_all()
```

### Retornando um link de pagamento

```python
paymentLink = pagarme.payment_link.find_by_id('ID_LINK_PAGAMENTO')
```

### Cancelando um link de pagamento

```python
paymentLinkCancel = pagarme.payment_link.cancel('ID_LINK_PAGAMENTO')
```

## Support
Caso você tenha algum problema ou sugestão crie uma issue [here](https://github.com/pagarme/pagarme-python/issues).

## License

Clique [aqui](LICENSE).
