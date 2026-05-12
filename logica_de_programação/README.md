# 💻 Lógica de Programação Aplicada: C++ vs Python em IoT

Este guia compara as duas linguagens fundamentais da Arquitetura IoT, mostrando como a lógica se traduz em cada nível do sistema.

---

## 1. 🏗️ Onde cada linguagem atua?
*   **C++ (Low-Level):** Executado diretamente no hardware (Arduino, ESP32). Foco em performance, controle de pinos e baixo consumo de energia.
*   **Python (High-Level):** Executado em Gateways (Raspberry Pi) ou Servidores Cloud. Foco em tratamento de dados, IA e integração de APIs.

---

## 2. 🔢 Variáveis e Tipos (Tipagem Forte vs Dinâmica)

Enquanto no C++ precisamos declarar o tipo de dado para economizar memória, no Python a linguagem identifica o tipo automaticamente.

### Em C++ (Arduino)
```cpp
int pinoSensor = A0;       // Inteiro
float temperatura = 26.5;  // Decimal
bool estaLigado = true;    // Booleano
```

### Em Python
```python
pino_sensor = 0            # O Python entende como int
temperatura = 26.5         # O Python entende como float
esta_ligado = True         # O Python entende como bool
```

---

## 3. 🚦 Estruturas Condicionais

A lógica é a mesma, mas a sintaxe muda (chaves `{}` no C++ vs identação no Python).

### Em C++
```cpp
if (temperatura > 30.0) {
  digitalWrite(13, HIGH); 
} else {
  digitalWrite(13, LOW);
}
```

### Em Python
```python
if temperatura > 30.0:
    print("Ligando cooler...")
else:
    print("Temperatura normal.")
```

---

## 4. 🔄 Estruturas de Repetição (Loops)

### O Loop de Controle (C++)
No Arduino, o `void loop()` é o motor que nunca para de ler os sensores.
```cpp
void loop() {
  // Código que roda infinitamente
  int valor = analogRead(A0);
  delay(1000); 
}
```

### O Loop de Monitoramento (Python)
Geralmente usado para verificar filas de mensagens ou bancos de dados.
```python
while True:
    print("Verificando mensagens do Broker MQTT...")
    time.sleep(1)
```

---

## 5. 🛠️ Comparativo de Funções


| Característica | C++ (Hardware) | Python (Software/Cloud) |
| :--- | :--- | :--- |
| **Velocidade** | Extremamente alta | Média (Interpretada) |
| **Sintaxe** | Complexa (requer `;`) | Simples e legível |
| **Uso em IoT** | Firmware, Drivers, RTOS | Gateways, Dashboards, Big Data |
| **Memória** | Gerenciamento manual | Automático (Garbage Collector) |

---

## 6. 🔗 Exercício de Arquitetura
**Cenário:** Um sensor de solo envia dados via Serial.
1.  **Lógica C++:** Leia o pino analógico e envie o valor via `Serial.print`.
2.  **Lógica Python:** Leia a porta Serial, converta para porcentagem e salve em um arquivo `.txt`.
