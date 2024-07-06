O Reader-XLSX é um programa escrito em Python (Flask), uma aplicação Web

O directorio templates contem os arquivos HTML da aplicação que representam a estrutura da aplicação, os arquivos CSS estão contidas nos proprios templates.

Ao executar o programa e inserindo o arquivo XLSX a ser lido, a aplicação salva os arquivos no directorio arquivos e apois isso faz uma leitura do mesmo

Depois da leitura os dados são passados por parametro no template e são randerizados na tela, as partes da planilha que estiverem sem dado são randerizadas como None

Ao inserir um arquivo que não seja XLSX, a aplicação retorna um erro , nesse caso... apenas arquivos XLSX podem ser inseridos.

A aplicação não possui tratamentos de erros e nem analise dos arquivos inseridos, as proximas versões seram melhoradas e tornadas mas perfomaticas.
