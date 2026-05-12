# 🖥️ Sistemas Operacionais em Arquitetura IoT

Este guia aborda os fundamentos de SO necessários para configurar, simular e gerenciar ambientes de desenvolvimento IoT, focando em ferramentas de virtualização e operação via terminal.

---

## 1. 🪟 Windows vs 🐧 Linux na IoT

Na arquitetura IoT, os sistemas operacionais desempenham papéis diferentes dependendo da camada:

*   **Windows:** Geralmente utilizado na **Camada de Aplicação**. É o ambiente principal para desenvolvimento (IDEs como VS Code, Arduino IDE) e ferramentas de design de interfaces.
*   **Linux (Kernel):** É a base da IoT. Presente em **Gateways** (Raspberry Pi OS), servidores de borda (Edge Computing) e servidores Cloud. É essencial pela sua leveza, segurança e gerenciamento de processos.

---

## 2. 💻 Máquina Virtual (VM) e Emulação
Para as aulas de IoT, utilizamos Máquinas Virtuais para isolar ambientes de desenvolvimento e testar sistemas baseados em Linux sem alterar o sistema anfitrião (Host).

*   **Ferramentas:** Oracle VirtualBox, VMware ou WSL2 (Windows Subsystem for Linux).
*   **Vantagens na IoT:**
    *   Criação de redes isoladas para testar protocolos (MQTT/HTTP).
    *   Simulação de servidores de banco de dados (InfluxDB/MongoDB).
    *   Ambiente seguro para compilação de kernels customizados.

---

## 3. ⌨️ O Terminal: A Ferramenta do Desenvolvedor
O terminal (CLI - Command Line Interface) é o meio mais eficiente de gerenciar dispositivos IoT remotos, onde muitas vezes não há interface gráfica (Monitor/Teclado).

### Comandos Essenciais (Linux/Bash):

| Comando | Função | Contexto IoT |
|:---|:---|:---|
| `lsusb` | Lista dispositivos USB | Verificar se o Arduino/ESP32 foi detectado. |
| `ip addr` | Mostra endereços de IP | Identificar o IP do dispositivo na rede local. |
| `sudo apt update` | Atualiza repositórios | Instalar dependências de bibliotecas de sensores. |
| `ssh user@ip` | Acesso Remoto | Acessar o terminal de um Raspberry Pi via rede. |
| `top` / `htop` | Gerenciador de Processos| Monitorar o consumo de CPU/RAM do script Python. |

---

## 4. 📂 Gerenciamento de Arquivos e Permissões
Em sistemas Linux, dispositivos de hardware são tratados como arquivos. Para acessar uma porta serial (USB), o usuário precisa de permissão.

```bash
# Exemplo: Adicionando usuário ao grupo 'dialout' para acessar o Arduino no Linux
sudo usermod -a -G dialout \$USER
```

---

## 5. 🛠️ Fluxo de Trabalho sugerido para a Aula
1.  **Hospedeiro (Windows):** Onde o aluno programa o código.
2.  **Convidado (VM Linux):** Onde o código é testado em um ambiente de servidor/gateway.
3.  **Terminal:** Utilizado para conectar os dois ambientes e monitorar a saída dos dados.

---

## 📑 Exercício Prático
*   **Tarefa 1:** Instalar o Ubuntu Server em uma VM.
*   **Tarefa 2:** Utilizar o terminal para instalar o Python e a biblioteca `pyserial`.
*   **Tarefa 3:** Identificar em qual porta `/dev/tty` o seu microcontrolador está mapeado.
