import time
import random

def follow_accounts(client, accounts_to_follow):
    for account in accounts_to_follow:
        print("!follow_accounts: ", account)
        retry_count = 0
        max_retries = 3  # Número máximo de tentativas
        while retry_count < max_retries:
            try:
                user_id = client.user_id_from_username(account)
                print(f"User_id {user_id}")
                client.user_follow(user_id)
                print(f"Seguiu {account}")

                # Aumente o tempo de espera para evitar muitas solicitações
                time.sleep(random.uniform(10, 15))
                break  # Sai do loop se a ação for bem-sucedida
            except Exception as e:
                if "429" in str(e):
                    print("Muitas solicitações. Aguardando antes de tentar novamente...")
                    time.sleep(60)  # Espera 1 minuto antes de tentar novamente
                elif "401" in str(e):
                    print(f"Não autorizado para seguir {account}: Verifique suas credenciais ou se a conta foi bloqueada.")
                    break  # Interrompe o processo se não autorizado
                elif "Please wait a few minutes before you try again" in str(e):
                    print("Aguarde alguns minutos antes de tentar novamente.")
                    time.sleep(300)  # Espera 5 minutos antes de tentar novamente
                else:
                    print(f"Não foi possível seguir {account}: {str(e)}")

                retry_count += 1
        else:
            print(f"Não foi possível seguir {account} após {max_retries} tentativas. Por favor, tente novamente mais tarde.")