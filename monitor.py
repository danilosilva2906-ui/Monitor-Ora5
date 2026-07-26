import os
import requests
from bs4 import BeautifulSoup

# Obtém os segredos configurados no GitHub Actions
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TARGET_URL = "https://ora5-monitor.vercel.app/"

def send_telegram_message(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("Erro: TELEGRAM_TOKEN ou TELEGRAM_CHAT_ID não configurados.")
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Mensagem enviada com sucesso para o Telegram!")
        else:
            print(f"Falha ao enviar mensagem: {response.text}")
    except Exception as e:
        print(f"Erro ao conectar com a API do Telegram: {e}")

def check_cars():
    try:
        response = requests.get(TARGET_URL)
        if response.status_code != 200:
            print(f"Erro ao acessar o site: {response.status_code}")
            return

        # Analisa o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        # Condição de busca: Procura por "DF" e termos que indiquem disponibilidade
        if "DF" in page_text and ("disponível" in page_text.lower() or "disponivel" in page_text.lower()):
            send_telegram_message("🚨 *Carro disponível no DF encontrado!* Acesse o site para conferir: " + TARGET_URL)
        else:
            print("Nenhum carro disponível no DF no momento.")

    except Exception as e:
        print(f"Erro ao fazer o scraping da página: {e}")
        
        if __name__ == "__main__":
    send_telegram_message("🤖 *Teste:* O bot de monitoramento está ativo e conseguindo enviar mensagens para o seu celular!")
    check_cars()

