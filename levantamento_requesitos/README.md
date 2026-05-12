# 📋 Levantamento de Requisitos: Arquitetura IoT

Este documento estabelece as diretrizes para o levantamento de necessidades técnicas e funcionais em projetos de Internet das Coisas.

---

## 1. 🎯 Introdução
O levantamento de requisitos em IoT é peculiar pois deve considerar não apenas o software, mas a integração com o **hardware**, a **conectividade** e as **restrições de energia**.

---

## 2. ✅ Requisitos Funcionais (RF)
Definem as funções específicas que o sistema IoT deve realizar. O que o dispositivo ou a plataforma "faz".


| ID | Requisito | Descrição |
|:---|:---|:---|
| **RF01** | Coleta de Dados | O sistema deve ler a temperatura via sensor DHT11 a cada 30 segundos. |
| **RF02** | Atuação Remota | O usuário deve ser capaz de ligar/desligar o relé através de um aplicativo móvel. |
| **RF03** | Alerta de Segurança | O sistema deve enviar uma notificação push se o sensor de presença for ativado. |
| **RF04** | Armazenamento | Os dados coletados devem ser salvos em um banco de dados SQL/NoSQL local ou nuvem. |
| **RF05** | Dashboard | Deve exibir gráficos em tempo real da telemetria capturada. |

---

## 3. ⚙️ Requisitos Não Funcionais (RNF)
Definem as propriedades e restrições do sistema. Como o sistema "se comporta" (desempenho, segurança, confiabilidade).


| Categoria | Descrição | Exemplo de RNF |
|:---|:---|:---|
| **Disponibilidade** | Tempo em que o sistema fica online. | O gateway deve estar disponível 99.9% do tempo. |
| **Latência** | Tempo de resposta entre evento e ação. | O atraso entre o comando no app e o acionamento do LED deve ser < 500ms. |
| **Segurança** | Proteção dos dados e acesso. | Toda comunicação entre Arduino e Python deve ser criptografada (ex: TLS). |
| **Consumo** | Eficiência energética (crítico para baterias). | O sensor deve operar em modo *Deep Sleep* para economizar energia. |
| **Escalabilidade** | Capacidade de crescer. | A arquitetura deve suportar o acréscimo de até 100 novos sensores sem perda de performance. |
| **Interoperabilidade**| Capacidade de conversar com outros. | O sistema deve se comunicar via protocolo padrão MQTT. |

---

## 4. 📝 Metodologia de Coleta
Para estas aulas, utilizaremos:
1. **Brainstorming:** Reunião com stakeholders para definir o propósito do dispositivo.
2. **User Stories:** "Como [usuário], eu quero [ação] para que [valor]".
3. **Análise de Cenário:** Mapear o ambiente físico onde o hardware será instalado.

---

## 5. 🛠️ Ferramentas Sugeridas
*   **Documentação:** Markdown / Notion.
*   **Prototipagem:** Wokwi (Simulação Arduino).
*   **Fluxogramas:** Draw.io ou Lucidchart.
