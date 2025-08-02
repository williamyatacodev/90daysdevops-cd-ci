import subprocess
import requests
import time
import sys

def verificar_conexion_nginx_vote():
    print("🔁 Verificando conexión de NGINX -> VOTE (http://localhost)...")
    try:
        response = requests.get("http://localhost")
        if "voting" in response.text.lower():
            print("✅ NGINX puede acceder a VOTE")
        else:
            print("❌ La respuesta de VOTE no contiene texto esperado")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"❌ Falla NGINX -> VOTE: {e}")
        sys.exit(1)

def enviar_voto_a_vote():
    print("📨 Enviando voto de prueba a VOTE (http://localhost)...")
    try:
        response = requests.post("http://localhost", data={"vote": "a"})
        if response.status_code != 200:
            print(f"❌ Falla al votar desde VOTE. Código: {response.status_code}")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"❌ Falla al votar desde VOTE: {e}")
        sys.exit(1)

def esperar_worker():
    print("⏳ Esperando procesamiento por parte de WORKER...")
    time.sleep(5)

def verificar_voto_en_stats():
    print("📊 Verificando votos a través de /stats...")
    try:
        response = requests.get("http://localhost/stats")
        data = response.json()

        total_votes = data.get("total_votes", 0)
        cats_votes = data.get("cats_votes", 0)
        dogs_votes = data.get("dogs_votes", 0)

        print(f"📈 Votos actuales: total={total_votes}, cats={cats_votes}, dogs={dogs_votes}")

        if total_votes >= 1 and cats_votes >= 1:
            print("✅ Voto registrado exitosamente en la base de datos")
        else:
            print("❌ El voto no fue registrado correctamente")
            sys.exit(1)
    except (requests.RequestException, ValueError) as e:
        print(f"❌ Error accediendo a /stats: {e}")
        sys.exit(1)

def main():
    print("🧪 Iniciando pruebas de integración...")
    verificar_conexion_nginx_vote()
    enviar_voto_a_vote()
    esperar_worker()
    verificar_voto_en_stats()
    print("🎉 Todas las pruebas de integración pasaron exitosamente.")

if __name__ == "__main__":
    main()