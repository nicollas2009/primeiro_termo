# primeiro_termo
material de aula

# 🌐 Arquitetura IoT: Do Requisito à Programação

Este guia consolida os fundamentos de Engenharia de Requisitos, Sistemas Operacionais e Lógica de Programação aplicados ao desenvolvimento de soluções IoT.

---

## 1. 📋 Levantamento de Requisitos (O "Porquê")
Antes de programar, precisamos entender as necessidades do projeto.

### Requisitos Funcionais (RF) - *O que o sistema faz*
*   **RF01:** O dispositivo deve ler a umidade do solo a cada 10 minutos.
*   **RF02:** O sistema deve acionar uma bomba d'água se a umidade for < 40%.

### Requisitos Não Funcionais (RNF) - *Como o sistema se comporta*
*   **RNF01 (Conectividade):** O sistema deve operar via protocolo MQTT.
*   **RNF02 (Energia):** O hardware deve funcionar por 6 meses com uma bateria 18650.
*   **RNF03 (SO):** O gateway deve rodar sobre uma distribuição Linux minimalista.

---

## 2. 🖥️ Sistemas Operacionais (A Base)
O SO gerencia o hardware e permite que nossos programas funcionem.

*   **Ambiente de Desenvolvimento (Windows/Linux):** Onde escrevemos o código e usamos Máquinas Virtuais (VMs) para simular servidores.
*   **O Terminal (CLI):** Ferramenta essencial para acessar dispositivos remotos (via SSH) e gerenciar arquivos no Linux.
*   **Diferença Fundamental:**
    *   **RTOS (C++):** Sistemas de Tempo Real para microcontroladores (Arduino/ESP32).
    *   **Geral (Linux/Python):** Sistemas multitarefa para Gateways e Cloud.

---

## 3. 💡 Lógica de Programação (A Execução)
A lógica integra os componentes através de algoritmos.

### Fluxo de Dados: C++ ➡️ Python

#### Nível de Borda (C++ / Arduino)
Foco em leitura de hardware e eficiência.
```cpp
// Lógica de leitura e envio
void loop() {
  int sensorValue = analogRead(A0);
  if (sensorValue < 400) {
    digitalWrite(RELAY_PIN, HIGH); // Atuador
  }
  Serial.println(sensorValue);   // Envia para o SO/Gateway
  delay(1000);
}
```

#### Nível de Gateway (Python / Linux)
Foco em processamento, logs e conectividade.
```python
# Lógica de recebimento e decisão superior
import serial

porta = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    dado = porta.readline().decode().strip()
    if int(dado) < 400:
        print("LOG: Alerta de umidade baixa detectado!")
```

---

## 🔄 Integração da Arquitetura

1.  **Requisito:** "Preciso monitorar uma estufa remotamente."
2.  **Sistemas Operacionais:** Uso um **Linux (VM)** para rodar um Broker MQTT e o **Windows** para programar o Arduino.
3.  **Lógica:** O **C++** lê os sensores; o **Python** recebe esses dados no Linux e os exibe em um Dashboard.

---

## 🛠️ Exercício Sugerido
**Desafio:** Desenhe um diagrama simples onde um **Requisito** de segurança (ex: detectar invasão) seja traduzido em uma **Lógica** (se sensor == 1) rodando em um **SO Linux**.


