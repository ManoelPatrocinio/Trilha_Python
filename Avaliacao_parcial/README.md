
## FLUXO DE EXECUÇÃO
1º  É executado a função main().

2º  A função main() estancia a classe Estacões,  e executa o método requisicaoDeDados(), que irá usar o webdriver do Selenium para acessar o site do inmet em busca do anos de dados históricos e retornar um dicionário onde a chave é o ano e o valor o link para o arquivo .zip. 

3º  Caso o método retorne  um valor e chamada a função telaPrincipal() 