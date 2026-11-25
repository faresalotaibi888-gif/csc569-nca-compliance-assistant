# CSC 569 Course Project: NCA Compliance Assistant (ECC + CCC)

A Retrieval-Augmented Generation (RAG) assistant that answers questions about two public Saudi National
Cybersecurity Authority (NCA) documents, with a guardrail layer and a before/after red-team evaluation.

- **ECC-2:2024**, Essential Cybersecurity Controls
- **CCC-2:2024**, Cloud Cybersecurity Controls

King Saud University, CSC 569: Selected Topics in Artificial Intelligence, Fall 2026.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/faresalotaibi888-gif/csc569-nca-compliance-assistant/blob/main/NCA_Compliance_Assistant.ipynb)

## How to run

1. Click the Colab badge above.
2. In Colab, open the key icon in the left sidebar and add a secret named `GEMINI_API_KEY` (free key from
   Google AI Studio). Switch on notebook access.
3. Runtime > Run all. The full run makes about 240 model calls and takes 25-30 minutes on the free tier (model: gemini-3.5-flash-lite, 500 free requests per day).
   Responses are cached, so an interrupted run resumes where it stopped.
4. Results are committed to this repo automatically if a Colab secret named `GITHUB_TOKEN` is set (a fine-grained
   token limited to this repo, with Contents: read and write). Otherwise download `project_outputs.zip` at the end.

## Results and the answer cache

| Path | Content |
|---|---|
| `results/latest/` | outputs of the most recent complete run (overwritten each run) |
| `results/runs/<date_time>/` | archived copy of every complete run |
| `results/llm_cache.json` | every model response so far, pushed after each stage |

A new Colab session restores `results/llm_cache.json` first, so prompts that have not changed are answered from the
cache and use no API quota. Only new or edited prompts are sent to the model.

## What the notebook does

| Section | Project part | Output |
|---|---|---|
| 1-4 | System design: control-level chunking, local embeddings, hybrid retrieval | index of ECC and CCC controls |
| 5 | Prompt engineering: minimal, structured, few-shot, chain-of-thought | `strategy_results.csv` |
| 6-8 | Red-teaming the unprotected baseline (24 adversarial + 8 normal prompts) | `redteam_results.csv` |
| 9-10 | Nine-layer guardrail system and before/after comparison | `summary.csv`, `before_after.png` |
| 11-12 | Export and optional Gradio demo | `project_outputs.zip` |

## Repository layout

```
NCA_Compliance_Assistant.ipynb   main notebook (generated from tools/nb_source.py)
data/                            source PDFs (public NCA documents, TLP: White)
results/                         outputs of the evaluation run
tools/nb_source.py               notebook source as a plain Python file
tools/build_nb.py                converts nb_source.py to the notebook
tools/test_nb.py                 offline test of the pipeline logic with a stub model
```

## Data

`data/CCC-2-2024-EN.pdf` is included. The notebook looks for `data/ECC-2-2024-EN.pdf` in this repo first, then
downloads ECC from nca.gov.sa, and asks for an upload if both fail. Source pages:
[ECC](https://nca.gov.sa/en/regulatory-documents/controls-list/ecc/),
[CCC](https://nca.gov.sa/en/regulatory-documents/controls-list/ccc/).

## Disclaimer

Academic project. The assistant is informational only and is not an official NCA interpretation or a
compliance attestation.
