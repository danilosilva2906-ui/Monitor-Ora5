import os
import requests

# Obtém os segredos configurados no GitHub Actions
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

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

if __name__ == "__main__":
    send_telegram_message("🚀 *Monitoramento Ativo!* O script rodou com sucesso no GitHub Actions.")
