<div align="center">

<p><sub><strong>오픈소스 LLM 학습 워크숍</strong></sub></p>

<h1>Jackrong LLM Fine-Tuning Guide</h1>

<p><strong>학습 → 증류 → 파인튜닝 → 정렬 → 배포</strong></p>

<p>
  원시 데이터를 재현 가능한 학습 워크플로와<br>
  로컬에서 실행할 수 있는 모델로 바꾸는 실전형 지식 베이스입니다.
</p>

<p>
  <a href="../train_code/"><strong>학습 시작</strong></a>
  ·
  <a href="../High-fidelity%20Dataset/"><strong>데이터셋 둘러보기</strong></a>
  ·
  <a href="../qwen-mtp-gguf/"><strong>GGUF로 배포하기</strong></a>
  ·
  <a href="../showcase/"><strong>디자인 쇼케이스 보기</strong></a>
</p>

<p>
  <code>SFT</code>&nbsp;&nbsp;
  <code>GRPO</code>&nbsp;&nbsp;
  <code>GSPO</code>&nbsp;&nbsp;
  <code>LoRA / QLoRA</code>&nbsp;&nbsp;
  <code>MTP → GGUF</code>
</p>

<p>
  <sub>
    <a href="../README.md">English</a> ·
    <a href="../docs/README_zh.md">中文</a> · 한국어 ·
    <a href="../docs/README_ja.md">日本語</a>
  </sub>
</p>

</div>

---

<table>
<tr>
<td align="center" width="25%"><strong>24</strong><br><sub>엄선된 데이터셋</sub></td>
<td align="center" width="25%"><strong>5</strong><br><sub>실행 가능한 레시피</sub></td>
<td align="center" width="25%"><strong>3</strong><br><sub>학습 방식</sub></td>
<td align="center" width="25%"><strong>4</strong><br><sub>지원 언어</sub></td>
</tr>
</table>

## 나에게 맞는 경로 선택

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>01 / 학습</strong></sub>
  <h3>브라우저에서 파인튜닝하기</h3>
  <p>로컬 GPU 환경을 먼저 구축하지 않아도 안내형 Colab 또는 Kaggle 레시피를 실행할 수 있습니다.</p>
  <p><a href="../train_code/"><strong>트레이닝 레시피 둘러보기 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>02 / 데이터 구축</strong></sub>
  <h3>더 나은 데이터셋 증류하기</h3>
  <p>추론, 코딩, STEM, 대화, 도메인 데이터를 후속 학습에 적합한 형태로 준비합니다.</p>
  <p><a href="../data_processing_code/"><strong>데이터 레시피 살펴보기 →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>03 / 정렬</strong></sub>
  <h3>SFT, GRPO, GSPO 실습하기</h3>
  <p>검토 가능한 코드와 함께 지도 파인튜닝에서 강화학습 워크플로까지 단계적으로 확장합니다.</p>
  <p><a href="../train_code/README.md"><strong>학습 방식 비교하기 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>04 / 배포</strong></sub>
  <h3>MTP 지원 GGUF 배포하기</h3>
  <p>Qwen 계열 모델을 검증하고 변환한 뒤 스모크 테스트, 양자화, 릴리스하여 로컬 추론에 사용합니다.</p>
  <p><a href="../qwen-mtp-gguf/"><strong>MTP GGUF 스킬 열기 →</strong></a></p>
</td>
</tr>
</table>

## 하나의 학습 루프, 처음부터 끝까지

<p align="center">
  <strong>01 · 선별</strong>
  &nbsp;→&nbsp;
  <strong>02 · 증류</strong>
  &nbsp;→&nbsp;
  <strong>03 · 학습</strong>
  &nbsp;→&nbsp;
  <strong>04 · 정렬</strong>
  &nbsp;→&nbsp;
  <strong>05 · 배포</strong>
</p>

| 단계 | 이곳에서 할 수 있는 일 | 시작점 |
|---|---|---|
| 선별 | 고품질 추론, 코딩, 대화, 도메인 데이터 선택 | [데이터셋 카탈로그](../High-fidelity%20Dataset/) |
| 증류 | 교사 모델 워크플로로 학습 데이터를 생성하거나 변환 | [데이터 처리](../data_processing_code/) |
| 학습 | Colab, Kaggle 또는 Python에서 LoRA / QLoRA 지도 파인튜닝 실행 | [트레이닝 랩](../train_code/) |
| 정렬 | 공개된 GRPO 및 GSPO 강화학습 레시피 탐색 | [RL 레시피](../train_code/README.md#-reinforcement-learning-grpo--gspo) |
| 배포 | 어댑터 내보내기, 16비트 체크포인트 병합, MTP 지원 GGUF 릴리스 제작 | [배포 스킬](../qwen-mtp-gguf/) |

## 트레이닝 랩

공개된 다섯 가지 레시피로 브라우저 중심 학습, 지도 파인튜닝, 강화학습을 실습할 수 있습니다.

| 모델 | 방식 · 환경 | 실행 |
|---|---|---|
| **Qwopus3.5 27B** | `SFT` · Google Colab | [노트북 실행](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| **Qwopus3.6 27B** | `GSPO` · Python | [튜토리얼 읽기](../train_code/Qwopus3.6-27B-GSPO/) |
| **Qwen3.5 Neo 9B** | `SFT` · Kaggle | [노트북 열기](../train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| **Qwopus3.5 35B-A3B** | `SFT` · Kaggle | [노트북 열기](../train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| **Llama3.2-R1 3B** | `GRPO` · Kaggle | [노트북 열기](../train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

**[전체 트레이닝 카탈로그 둘러보기 →](../train_code/README.md)**

## 체크포인트에서 로컬 런타임까지 이어지는 MTP GGUF

> [!TIP]
> [`qwen-mtp-gguf`](../qwen-mtp-gguf/) 하위 프로젝트는 단순한 변환 명령이 아니라 에이전트가 활용할 수 있는 릴리스 워크플로입니다. 모델 호환성과 시스템 자원을 점검하고, MTP / nextn 텐서를 검증하거나 주입하며, llama.cpp 변환과 HF 및 GGUF 스모크 테스트를 수행합니다. 이어서 양자화 매트릭스를 만들고 더욱 안전한 업로드 및 재개 작업을 지원합니다.

<p>
  <a href="../qwen-mtp-gguf/"><strong>스킬 열기</strong></a>
  ·
  <a href="../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md">파이프라인 가이드 읽기</a>
  ·
  <a href="../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md">에이전트와 함께 사용하기</a>
</p>

## 리소스 라이브러리

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>데이터</strong></sub>
  <h3>고품질 데이터셋 카탈로그</h3>
  <p>추론, 수학, 코드, 지시 이행, 대화, 도메인 작업을 위한 엄선된 24개 컬렉션입니다.</p>
  <p><a href="../High-fidelity%20Dataset/"><strong>카탈로그 둘러보기 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>가이드</strong></sub>
  <h3>심층 학습 자료실</h3>
  <p>개념을 완전한 학습 워크플로와 연결해 주는 초보자용 안내서와 기술 보고서입니다.</p>
  <p><a href="../guidePDF/"><strong>가이드 읽기 →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>자동화</strong></sub>
  <h3>Codex 목표 템플릿</h3>
  <p>RL 학습, MTP GGUF 릴리스, 반복 가능한 저장소 유지관리를 위한 편집 가능한 계획입니다.</p>
  <p><a href="../codex-goals/"><strong>목표 템플릿 사용하기 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>문서</strong></sub>
  <h3>다국어 지식 베이스</h3>
  <p>영어, 중국어, 한국어, 일본어 진입점과 프로젝트 철학 및 유지관리 안내를 제공합니다.</p>
  <p><a href="../docs/"><strong>문서 열기 →</strong></a></p>
</td>
</tr>
</table>

## 워크숍에서 다루는 내용

| 영역 | 공개된 워크플로 |
|---|---|
| 파인튜닝 | LoRA / QLoRA SFT, 브라우저 노트북, Python 튜토리얼 |
| 강화학습 | 검토 가능한 보상 및 학습 코드가 포함된 GRPO 및 GSPO 레시피 |
| 데이터 | 증류, 전처리, 데이터셋 선택, 일괄 다운로드 도구 |
| 내보내기 | LoRA 어댑터, 병합된 16비트 체크포인트, GGUF 변환 및 양자화 |
| 에이전트 도구 | 재사용 가능한 MTP 릴리스 스킬과 편집 가능한 Codex 목표 템플릿 |

<details>
<summary><strong>모델 지원 로드맵</strong></summary>

<br>

공개된 RL 레시피는 모델과 학습 목표에 따라 GRPO 또는 GSPO를 사용합니다.

| 모델 패밀리 | SFT 지원 | RL 지원 |
|---|---:|---:|
| Qwen 3.5 | 공개됨 | 예정 |
| Qwen 3.6 | 공개됨 | 공개됨 |
| Qwen 3 | 예정 | 예정 |
| Llama3.2-R1 3B | 포함됨 | 공개됨 |
| Llama 3.1 / 3.3 | 예정 | 예정 |

</details>

## 처음부터 오픈소스로

> 학습 지식은 누구나 과정을 재현하고, 의사결정을 검토하고, 자신의 모델과 데이터에 맞게 워크플로를 바꿀 수 있을 때 가장 유용합니다.

공개된 파인튜닝 모델의 소스 코드와 문서는 가능한 한 계속 열어 둡니다. 더 자세한 [프로젝트 철학](../docs/PROJECT_PHILOSOPHY.md)과 저장소 [유지관리 가이드](../docs/MAINTAINING_THE_KNOWLEDGE_BASE.md)를 확인하세요.

<details>
<summary><strong>이 프로젝트 인용하기</strong></summary>

```bibtex
@misc{jackrong-llm-finetuning,
  author = {Jackrong},
  title = {Jackrong LLM Fine-Tuning Guide: An Educational LLM Fine-Tuning Knowledge Base},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/R6410418/Jackrong-llm-finetuning-guide}}
}
```

</details>

---

<div align="center">

<p>
  함께 사용하는 도구:
  <a href="https://github.com/unslothai/unsloth">Unsloth</a> ·
  <a href="https://pytorch.org/">PyTorch</a> ·
  <a href="https://huggingface.co/Jackrong">Hugging Face</a> ·
  <a href="https://colab.research.google.com/">Google Colab</a> ·
  <a href="https://kaggle.com/">Kaggle</a>
</p>

<p><sub>오픈 모델을 만드는 모두를 위한 열린 지식.</sub></p>

</div>
