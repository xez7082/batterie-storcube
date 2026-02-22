# Storcube Stacker to MQTT Bridge

Ce projet permet d'intégrer les batteries **Storcube Stacker** dans **Home Assistant** via MQTT. 

## Fonctionnalités
- Récupération en temps réel (WebSocket) du SOC et de la puissance.
- Auto-discovery : Les capteurs apparaissent automatiquement dans HA.
- Contrôle de la puissance de sortie via MQTT.

## Installation via Docker
1. Créez un fichier `.env` avec vos accès :
   ```env
   MQTT_BROKER=192.168.1.XX
   MQTT_USERNAME=votre_user
   MQTT_PASSWORD=votre_pass
   LOGIN_NAME=email_storcube
   PASSWORD=pass_storcube
   DEVICE_ID=votre_id_batterie
