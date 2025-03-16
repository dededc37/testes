import speech_recognition as sr
import pyttsx3
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar o modelo e o tokenizer GPT-2 do Hugging Face
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Inicializar a engine de fala
engine = pyttsx3.init()

# Função para gerar resposta usando GPT-2
def gerar_resposta(texto):
    inputs = tokenizer.encode(texto, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50)
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta

# Função para reconhecer áudio e transcrever para texto
def reconhecer_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando 'OK Google'...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto.lower()
        except sr.UnknownValueError:
            print("Não consegui entender o áudio")
            return ""
        except sr.RequestError as e:
            print(f"Erro ao tentar se conectar ao Google Speech Recognition; {e}")
            return ""

# Função para reproduzir o texto como áudio
def reproduzir_audio(texto):
    engine.say(texto)
    engine.runAndWait()

# Função principal
def executar():
    while True:
        texto_comando = reconhecer_audio()
        
        # Verificar se o comando 'OK Google' foi detectado
        if "ok google" in texto_comando:
            print("Comando 'OK Google' detectado. Iniciando transcrição...")
            
            texto_usuario = reconhecer_audio()  # Captura o texto após o comando 'OK Google'
            if texto_usuario:
                # Gerar a resposta usando o modelo GPT-2
                resposta = gerar_resposta(texto_usuario)
                print(f"Resposta da IA: {resposta}")
                
                # Reproduzir a resposta gerada pela IA
                reproduzir_audio(resposta)
            else:
                print("Nenhum texto foi reconhecido após o comando.")
        else:
            print("Aguardando comando 'OK Google'...")

# Iniciar o processo
if __name__ == "__main__":
    executar()
