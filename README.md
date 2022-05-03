<h1>Projeto Desenvolvido no Senai</h1> 


Uma concessionario de veiculos realiza consultas online a tabela FIPE(tabela de valores de automoveis ) mensalmente. O tempo gasto nessas
consultas é em media de 2 horas diarias, pois são cosultado cerca de 400 veiculos. Visando solucionar esse problema criamos um siste,a que consulta os dados
oline e os armazena em uma planilha excel. Utilizamos o sistema o tempo gasto cai em media 5 minutos. 



<h2>#requisitos funcionais do sistema</h2>

RF - 001: O sistema deve permitir a busca de informação dos veiculos a partir de um codigo e ano de fabricação.

RF - 002: O sistema de gravar os dados retornado em um arquivo excel. Os dados são: Codigo, marca, modelo, Ano, preço, 
tipo de combustível, mês de referencia



<h2>#requisitos não funcionais</h2>

RFN - 001: O sistema deve salvar o arquivo em XLSX versão 2007 ou superior.

RFN - 002: O sistema de ter acesso a internet.

RFN - 003: O usuario de ter no seu computador o Python na versão 3.7 ou superior.


<h2>#regras de negocio</h2>

RN - 001: Cosulta a tabela FIPE. Deve ser feita pelo codigo oficial do veiculo. Todo o veiculo possui um codigo gerenciado pela organização que 
cuida da FIPE. (Requisito funcional - 001)

https://parallelum.com.br/fipe/api/v2/cars/brands

https://parallelum.com.br/fipe/api/v2/{vehicleType}/{fipeCode}/years/{yearId}

<h2>Caso de Uso</h2>

![umlUC](https://user-images.githubusercontent.com/100955133/164120587-68ff8ad6-cafe-457e-9e85-9fdd6b5d5dd4.jpg)

<h3>Caso de uso: Gerar excel com Fipe dos veículos.</h3>
<h4>Visão geral</h4>
O usuário acessa o sistema e seleciona em uma caixa de seleção o tipo de veículo que ele está buscando (caminhão, carro, moto), deve informar tambem o ano inicial da busca e o ano final da busca. Após o usuario clicar é gerado a planilha e o sistema começa a busca baseando nos parametros passado pelo usuário. Após isso o sistema devera emitir um alerta dizendo planilha criada com sucesso. O arquivo excel deve conter os seguintes campos (nome do veiculo, ano, modelo, tipo de combustível).

<h3>Caso de uso: Consultar tabela fipe.</h3>
<h4>Visão geral</h4>
O sistema deve realizar uma busca através de uma API Web que traz dados oficiais da tabela FIPE. E gera os dados de acordo com o parametro que for selecionado pelo usuário. 

<h3>Caso de uso: Enviar por email</h3>
<h4>Visão geral</h4>
O usuario deve acessa a opção de envio de e-mail. O mesmo insere o e-mail desejado e clica no botão para procuara a planilha logo apos clicar no botão enviar.
O sistema devera emitir um alerta de planilha enviada com sucesso.
Depois de pronta a planilha ela deverá ser enviada por email que o usuário escolher. 

<h2>Diagrama de classes</h2>

![Untitled](https://user-images.githubusercontent.com/100955133/165190711-b35ad160-84e3-4426-90ef-2d03f0297b21.png)


<h2>Diagrama de atividade</h2>

![diagrama de atividade FIPE EXCEL](https://user-images.githubusercontent.com/100955133/166344923-b6a4c8f2-4ea6-442f-88f3-3bccc7f096bb.png)



