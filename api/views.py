from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class VideoStream(APIView):
    "Nessa classe, tu vai botar todo o teu código de processamento dos videos"
    def get(self, request):
        #Nessa função, é aonde tu pega os dados que vieram no body do get
        #Os dados ficam armazenados na variavel request, que é um dict
        #Aqui fiz só um código de exemplo, pra te mostrar como tu pode fazer validações e etc.
        if "text" in request.data:
            text = request.data["text"]
            #pra retornar alguma coisa, por exemplo o video, usa o return + Response
            return Response({"text" : text})
        else:
            return Response(
                {
                    "error": "texto não enviado"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    #Aqui tu pode definir também como esse endpoint se comporta no post
    #Usa a mesma estrutura do get, na qual os dados do post são armazenados no dict request
    def post(self, request):
        return Response({"text" : "success"}) 