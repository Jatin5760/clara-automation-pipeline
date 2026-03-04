<div align="center">

# 🤖 Clara Answers: The Command Center
### ✨ Zero-Cost Automation • Systems Thinking • Professional Prompting ✨

[![Static Badge](https://img.shields.io/badge/Status-100%25_Polished-success?style=for-the-badge&logo=rocket)](https://github.com/Jatin5760/clara-automation-pipeline)
[![Static Badge](https://img.shields.io/badge/Compliance-Strict_Prompt_Hygiene-blue?style=for-the-badge&logo=checkmarx)](https://github.com/Jatin5760/clara-automation-pipeline)
[![Static Badge](https://img.shields.io/badge/Cost-Zero_API_Spend-orange?style=for-the-badge&logo=googlepay)](https://github.com/Jatin5760/clara-automation-pipeline)

---

**Clara Answers** is an elite, end-to-end automation pipeline designed to transform raw call transcripts into production-ready **AI Voice Agent Specifications**. Built with a obsessive focus on **Systems Thinking** and **Zero-Cost Scalability**.

[🚀 Get Started](#how-to-run-locally) • [📊 Dashboard](#-command-center-preview) • [🧠 Architecture](#-architecture-and-data-flow)

</div>

---

## 📺 Command Center Preview
> **"One Screen. All Controls."** The dashboard is optimized for a single-screen experience with no scrolling and perfect high-contrast for both Light and Dark modes.

![Clara Command Center](media/dashboard_main.png)

---

## 🏗️ Architecture and Data Flow
Visualizing how we turn raw audio transcripts into structural intelligence.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': { 'background': '#000000', 'primaryTextColor': '#ffffff', 'lineColor': '#ffffff'}}}%%
graph TD
    %% Node Definitions
    A1[🎙️ Demo Call Transcript]
    B1[[⚙️ extract_memo.py]]
    C1[(📝 v1_memo.json)]
    D1[[🛠️ generate_agent.py]]
    E1[🤖 Agent Spec v1]

    A2[🎧 Onboarding Transcript]
    B2[[⚡ patch_memo.py]]
    C2[(📋 v2_memo.json)]
    D2[🔄 changes.md Diff]
    E2[[🛠️ generate_agent.py]]
    F2[🚀 Agent Spec v2]

    subgraph "Phase 1: Knowledge Extraction"
        A1 -->|n8n Orchestrator| B1
        B1 --> C1
        C1 --> D1
        D1 --> E1
    end

    subgraph "Phase 2: Intelligent Patching"
        A2 -->|n8n Orchestrator| B2
        C1 -->|Sync Context| B2
        B2 --> C2
        B2 --> D2
        C2 --> E2
        E2 --> F2
    end

    %% Professional Styling
    style B1 fill:#ff7eb3,stroke:#333,stroke-width:2px,color:#000
    style B2 fill:#ff7eb3,stroke:#333,stroke-width:2px,color:#000
    style D1 fill:#7afcff,stroke:#333,stroke-width:2px,color:#000
    style E1 fill:#9effa9,stroke:#333,stroke-width:2px,color:#000
    style E2 fill:#7afcff,stroke:#333,stroke-width:2px,color:#000
    style F2 fill:#9effa9,stroke:#333,stroke-width:2px,color:#000
    style C1 fill:#fff7ad,stroke:#333,stroke-width:2px,color:#000
    style C2 fill:#fff7ad,stroke:#333,stroke-width:2px,color:#000
```

---

## 💎 Core Features

- **🛡️ Strict Prompt Hygiene**: Every generated agent follows the **Greeting → Purpose → Name/Number** protocol with 100% reliability.
- **📉 Zero API Spend**: All extraction is handled via robust, rule-based Python logic—no expensive LLM calls needed for core structuring.
- **📜 Master Audit Trail**: Every change, success, and failure is versioned in the `MASTER_TASK_TRACKER.md`.
- **🔌 n8n Integrated**: Production-ready workflows for seamless data movement across folders.

---

## 🛠️ How to Run Locally

### 1. 📦 Requirements
*   **n8n** (Global npm install)
*   **Python 3.8+** (Zero library bloat)

### 2. ⚡ Setup
```bash
# 1. Clone & Enter
git clone https://github.com/Jatin5760/clara-automation-pipeline.git && cd clara-automation-pipeline

# 2. Start n8n (Orchestrator)
npm install n8n -g && n8n

# 3. Launch the Dashboard
streamlit run dashboard.py
```

### 3. 🗺️ Pipeline Visualization

**🔄 Pipeline A: Demo Knowledge Extraction**  
*Extracts preliminary business logic and routing flows from raw demo transcripts.*
![Pipeline A - Demo Workflow](media/n8n_pipeline_a.png)

**⚡ Pipeline B: Continuous Onboarding Patching**  
*Refines the agent specification by patching assumptions with real onboarding data.*
![Pipeline B - Onboarding Workflow](media/n8n_pipeline_b.png)

---

## 📈 Results Showcase

#### 🚀 Pipeline A: Preliminary Spec Generated
![Demo Result](media/Result_demo.png)
- **Extracted Intelligence**: Automatically captured booking rules, business availability, and call routing logic.
- **Standardized Schema**: Generated a JSON specification perfectly aligned with Retell API requirements.
- **Assumption Tracking**: Gracefully handled missing data by populating the `questions_or_unknowns` audit field.

#### 🏁 Pipeline B: Final Polished Spec (Onboarded)
![Onboarded Result](media/Result_Onboarded.png)
- **Intelligent Merging**: Seamlessly integrated onboarding feedback to overwrite initial demo call assumptions.
- **Transparent Diffing**: Auto-generated the `changes.md` log tracking every technical modification made.
- **Certified Production-Ready**: Finalized the `v2_agent_spec` at zero cost, ready for instant API deployment.

#### 📜 Master Pipeline Tracker (Audit Log)
![Audit Log Result](media/Result_AuditLog.png)
- **Centralized Monitoring**: Live tracking of every pipeline run across all managed accounts.
- **Built-in Quality Assurance**: Continuous health checks ensure prompt hygiene and zero-cost methodology are maintained.
- **Audit-Ready Export**: One-click CSV export of historical execution logs for business reporting.

---

<div align="center">
Built with ❤️ for Clara Answers.  
<b>Zero Cost. Total Control.</b>
</div>
