projeto desenvolvido no senai 


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


#regras de negocio

RN - 001: Cosulta a tabela FIPE. Deve ser feita pelo codigo oficial do veiculo. Todo o veiculo possui um codigo gerenciado pela organização que 
cuida da FIPE. (Requisito funcional - 001)

https://parallelum.com.br/fipe/api/v2/cars/brands

https://parallelum.com.br/fipe/api/v2/{vehicleType}/{fipeCode}/years/{yearId}

<h2>Caso de Uso</h2>

![umlUC](https://user-images.githubusercontent.com/100955133/164120587-68ff8ad6-cafe-457e-9e85-9fdd6b5d5dd4.jpg)


