# 📡 Arquitetura IoT I: Fundamentos e Prática

Este guia serve como material de apoio para as aulas de Arquitetura IoT, cobrindo desde o hardware básico até a integração com linguagens de alto nível.

---

## 1. 🤖 Ecossistema Arduino
O Arduino atua como a **Camada de Percepção** na arquitetura IoT, responsável por interagir com o mundo físico.

*   **Microcontrolador:** Geralmente ATmega328P (no caso do Uno).
*   **Entradas/Saídas:** 
    *   **Digitais:** Estados ON/OFF (Sensores de presença, botões).
    *   **Analógicas:** Valores variáveis (Temperatura, luminosidade via LDR).
*   **Protocolos de Comunicação:** UART (Serial), I2C e SPI.

---

## 2. ⚙️ Programação em C++ (Firmware)
O Arduino é programado em uma variante de C++. É a linguagem de **baixo nível** que gerencia os recursos do hardware.

### Estrutura Básica:
```cpp
// Executa uma vez ao ligar o dispositivo
void setup() {
  pinMode(13, OUTPUT); // Configura o pino 13 como saída
  Serial.begin(9600);  // Inicia comunicação serial
}

// Executa em loop infinito
void loop() {
  digitalWrite(13, HIGH); // Liga o LED
  delay(1000);            // Aguarda 1 segundo
  digitalWrite(13, LOW);  // Desliga o LED
  Serial.println("Dado enviado via IoT");
}
```

---

## 3. 🐍 Programação em Python (Middleware/Cloud)
Na IoT, o Python é frequentemente usado na **Camada de Aplicação ou Gateway** para processar dados vindos do Arduino.

### Integração Serial (PySerial):
O Python "escuta" o que o Arduino envia via porta USB.

```python
import serial

# Configuração da porta (ajuste 'COM3' ou '/dev/ttyUSB0')
arduino = serial.Serial('COM3', 9600)

while True:
    if arduino.in_waiting > 0:
        dado = arduino.readline().decode('utf-8').rstrip()
        print(f"Dados recebidos do sensor: {dado}")
```

---

## 4. 🏗️ Fluxo de Dados na Arquitetura
1.  **Sensor** capta a grandeza física.
2.  **Arduino (C++)** processa o sinal e envia via Serial/Wi-Fi.
3.  **Script Python** recebe os dados, armazena em um banco de dados ou envia para um Dashboard (Nuvem).
