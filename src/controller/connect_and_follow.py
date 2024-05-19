# Controller
from flask import jsonify
from src.model.login_to_instagram import login_to_instagram
from src.service.follow_accounts import follow_accounts

def connect_and_follow(instagram_username, instagram_password, accounts_to_follow):
    try:
        client = login_to_instagram(instagram_username, instagram_password)
        print("!connect_and_follow", client)
        follow_accounts(client, accounts_to_follow)
        return jsonify({'message': 'Operação concluída com sucesso.'})  # Retorna uma mensagem de sucesso
    except Exception as e:
        error_message = str(e)
        print("!connect_and_follow_ERROR", error_message)

        if "Please wait a few minutes before you try again" in error_message:
            return jsonify({'error': 'Por favor, aguarde alguns minutos antes de tentar novamente. O Instagram está limitando as ações no momento.'})
        else:
            return jsonify({'error': f'Ocorreu um erro inesperado: {error_message}'})

