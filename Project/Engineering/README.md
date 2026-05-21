# Computer Vision Quality Control System
### Applied Computing GCSE Coursework — Project README

> **Context:** HPQ Applied Computing project. Dual-purpose: meets coursework requirements and functions as an engineering internship portfolio piece.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [System Architecture](#2-system-architecture)
3. [Tech Stack](#3-tech-stack)
4. [Hardware & Bill of Materials](#4-hardware--bill-of-materials)
5. [Dataset Strategy](#5-dataset-strategy)
6. [Implementation Phases](#6-implementation-phases)
7. [Success Metrics](#7-success-metrics)
8. [Mark Scheme Mapping](#8-mark-scheme-mapping-ao1ao4)
9. [Coursework Evidence Guide](#9-coursework-evidence-guide)
10. [Project Timeline (Gantt Summary)](#10-project-timeline-gantt-summary)
11. [Internship Signalling](#11-internship-signalling)
12. [Key Risks & Mitigations](#12-key-risks--mitigations)

---

## 1. Project Overview

A desktop application that takes a camera feed (or uploaded images) of 3D printed parts and flags defects in real time, producing a pass/fail verdict with a confidence score. Built as a two-tier system:

- **Tier 1 (Stage 1):** Classical computer vision (OpenCV) as a baseline, extended by a fine-tuned MobileNetV2 CNN for harder defect types
- **Tier 2 (Stage 2):** Depth sensing via Intel RealSense D405 for dimensional accuracy checking — point cloud comparison against source STL

**The core engineering decision documented throughout:** classical CV (hand-crafted rules) vs. ML (learned features) — which to use, where, and why. The project doesn't just build the system; it argues the architecture.

**Why this project:** The subject (3D printing quality control) is a real problem faced as a business owner. The dataset is self-generated using a Bambu Lab P2S Combo. This is not a textbook exercise.

---

## 2. System Architecture

```
Camera Input (Logitech C920 / RealSense D405)
        │
        ▼
┌────────────────────────────────────────┐
│         Preprocessing Pipeline         │
│  • Resize to 224×224                   │
│  • Normalise colour channels           │
│  • Lock exposure + white balance       │
└────────────────────────────────────────┘
        │
        ├──────────────────────────────────────────┐
        ▼                                          ▼
┌─────────────────────┐              ┌─────────────────────────┐
│  TIER 1: Classical  │              │  TIER 2: Depth / 3D     │
│  ─────────────────  │              │  ────────────────────── │
│  OpenCV baseline    │              │  RealSense D405 SDK      │
│  • Edge detection   │              │  Point cloud capture     │
│  • Contour analysis │              │  Open3D ICP registration │
│  • Template match   │              │  STL vs. scan deviation  │
│                     │              │  map                     │
│  MobileNetV2        │              └─────────────────────────┘
│  • Transfer learning│                          │
│  • Fine-tuned on    │                          │
│    own dataset      │                          │
└─────────────────────┘                          │
        │                                        │
        └───────────────┬────────────────────────┘
                        ▼
        ┌───────────────────────────┐
        │     Unified UI            │
        │  • Pass / Fail verdict    │
        │  • Confidence score (%)   │
        │  • Defect overlay image   │
        │  • Depth deviation map    │
        └───────────────────────────┘
```

---

## 3. Tech Stack

| Layer | Tool / Library | Notes |
|---|---|---|
| Language | Python 3.11 | Runtime environment |
| Classical CV | OpenCV (`opencv-python`) | Baseline pipeline, preprocessing |
| ML Framework | PyTorch + torchvision | MobileNetV2 transfer learning |
| Data Augmentation | Albumentations | Handles dataset size limitation |
| Dataset Labelling | LabelImg / CVAT | Free, open source |
| Depth Sensing | pyrealsense2 (Intel RealSense SDK) | Tier 2 point cloud capture |
| Point Cloud Processing | Open3D | ICP registration, STL comparison |
| Camera | Logitech C920 (Stage 1) | MJPEG mode, locked exposure |
| Depth Sensor | Intel RealSense D405 (Stage 2) | Ideal range 7–50cm for tabletop |
| All software | Free / open source | £0 software cost |

---

## 4. Hardware & Bill of Materials

### Stage 1 — Image-Based Defect Detection

| Item | Qty | Est. Cost | Source | Status |
|---|---|---|---|---|
| Logitech C920 | 1 | ~£30 | eBay used | **Buy** |
| Lazy Susan Turntable (150mm) | 1 | ~£7 | Amazon | **Buy** |
| Part Positioning Jig | 1 | ~£1.50 | Print in-house (~15g filament) | **Print** |
| Ring light / LED panel | 1 | ~£15–25 | Amazon | **Buy** |
| Tripod / camera mount | 1 | ~£12 | Amazon | **Buy** |
| PLA Filament — White (1 kg) | 1 | ~£19 | Bambu/eSUN | **Owned** |
| PETG Filament — Black (1 kg) | 1 | ~£22 | Bambu/eSUN | **Owned** |
| PC (existing) | 1 | — | — | **Owned** |
| All Python libraries | — | £0 | PyPI / pytorch.org | **Owned** |

**Stage 1 cash outlay: ~£65–75** (excluding owned items)

### Stage 2 — Depth / Dimensional Accuracy

| Item | Qty | Est. Cost | Source | Status |
|---|---|---|---|---|
| Intel RealSense D405 | 1 | ~£150–200 | eBay used / retail | **Buy** |
| Motorised turntable | 1 | ~£28 | Amazon | **Buy** |
| External SSD (point cloud storage) | 1 | ~£32 | Amazon | **Buy** |
| Calibration target (checkerboard) | 1 | ~£2.50 | Print or buy | **Buy/Print** |

**Stage 2 additional cash outlay: ~£212–262**

**Total project budget: ~£277–337** (Stage 1 + Stage 2 hardware only)

---

### Camera Selection Rationale: Logitech C920

The global shutter cameras that dominate industrial CV discussions are solving a problem this project doesn't have. Parts sit static on a turntable — rolling shutter artifacts only occur with motion. What actually matters:

- **Lockable exposure + white balance** — auto-adjustment between shots trains the model on noise, not defects
- **MJPEG output mode** — H.264 compression bakes artifacts into the dataset
- **OpenCV compatibility** — C920's V4L2 support is the most documented of any consumer webcam
- **Fixed focus** — set once per session, consistent focal plane across entire dataset

The ELP global shutter is genuinely tempting for image pipeline purity, but you'd spend Phase 3 debugging a poorly documented camera when your time is constrained. **The C920 just works. Buy it used for ~£30.**

---

### Depth Sensor Selection Rationale: RealSense D405 over D435i

The D435i was the initial recommendation but was superseded. The D435i's minimum usable depth is ~28cm — your parts on a turntable sit at 10–30cm, squarely in its degraded accuracy zone. The **D405** is specifically designed for close-range, high-accuracy inspection at 7–50cm ideal range, which maps exactly to this use case. Its depth accuracy is significantly better in the target operating envelope. The IMU in the D435i adds nothing for a static tabletop setup.

---

## 5. Dataset Strategy

### Defect Categories

| Class | Induction Method | Notes |
|---|---|---|
| **Good** | Standard print settings | Multiple filament types (PLA, PETG) |
| **Stringing** | High nozzle temp, fast retraction | Fine strings hardest to detect |
| **Warping** | Print without brim on smooth PLA | Dramatic, should be easy for model |
| **Layer Separation** | Under-extrusion (reduce flow rate) | Requires edge detection to catch |
| **Surface Blobs** | Poor retraction / over-extrusion | Visible as raised bumps |

### Target Size

Minimum 200 labelled images per class before training begins. Apply Albumentations augmentation (rotation, brightness jitter, horizontal flip) to expand the effective dataset.

### Critical Protocol

- **Lock white balance and exposure before every dataset session.** A single auto-adjustment change invalidates consistency.
- **Use MJPEG capture mode,** not H.264.
- **Fix focus distance.** Measure and mark the physical camera-to-part distance. Consistency is more important than optical sharpness.
- White filament on a neutral background gives highest defect contrast. Black filament stress-tests the lighting setup.
- Photograph under both consistent lighting (for training) and varied lighting (for robustness testing).

### Labelling Approach

LabelImg or CVAT for bounding box / classification labelling. Maintain a metadata CSV per image: filename, class, lighting condition, filament type, print parameters used.

---

## 6. Implementation Phases

### Phase 1 — Analysis & Scoping (~2 weeks) | AO1 + AO2

- Define project aims and SMART objectives
- Research industrial QC benchmarks (Keyence, Zeiss, Tesla Autopilot manufacturing QC, Foxconn AOI lines)
- Survey CV approaches: classical (OpenCV) vs ML (CNNs, transfer learning)
- Identify stakeholders: yourself as a 3D printing business owner
- Write formal problem statement; justify the two-tier architecture
- Document hardware options for Tier 2 and confirm D405 selection

### Phase 2 — Design (~2 weeks) | AO1 + AO2

- System architecture diagram: camera → preprocessing → classifier → UI
- Define the labelled dataset schema (defect categories, metadata fields)
- Specify success metrics: **target F1 > 0.85** on held-out test set
- Design the UI (pass/fail display, confidence score, defect overlay)
- Plan Tier 2 integration points in the pipeline
- Produce Gantt chart covering all phases with contingency buffer
- Produce BOM (see §4)

### Phase 3 — Dataset Collection (~3 weeks) | AO2 + AO3

- Print batches of good and defective parts using P2S Combo
- Deliberately induce each defect type (see table in §5)
- Photograph under consistent and varied lighting
- Label dataset (min 200 images/class)
- Apply Albumentations augmentation pipeline
- Document the collection methodology for AO3

### Phase 4 — Implementation (~5–6 weeks) | AO3

**Tier 1 (weeks 1–4):**
- OpenCV classical baseline pipeline
- Fine-tune MobileNetV2 on collected dataset (transfer learning from ImageNet weights)
- Build real-time inference UI with pass/fail verdict and confidence score
- Validate on held-out test set, tune decision threshold

**Tier 2 (weeks 5–6):**
- RealSense SDK setup; point cloud capture pipeline
- STL-to-scan registration using Open3D ICP algorithm
- Integrate depth deviation map into the unified UI
- Document integration challenges regardless of outcome

### Phase 5 — Evaluation (~2 weeks) | AO4

- Compute precision, recall, F1 on held-out test set vs. F1 > 0.85 target
- Classical CV baseline vs MobileNetV2 head-to-head comparison
- Failure mode analysis: which defects were hardest (hypothesis: fine stringing)
- Dataset limitation analysis: single lighting, limited colour variety
- Tier 2 integration outcome and ICP registration challenges
- Reflection on plan changes made during AO3 and why

---

## 7. Success Metrics

| Metric | Target | Notes |
|---|---|---|
| F1 Score (held-out test set) | **> 0.85** | Primary success criterion |
| Precision | > 0.80 | Minimise false passes (bad parts called good) |
| Recall | > 0.85 | Minimise missed defects |
| Inference speed | Real-time at 1080p | Sub-second per frame |
| Tier 2 (aspirational) | Point cloud deviation map generated | Document regardless of success |

---

## 8. Mark Scheme Mapping (AO1–AO4)

| AO | Weighting | How This Project Scores |
|---|---|---|
| **AO1 — Manage** | 20% | Strong. Five natural phases with clear deliverables at each. Plan changes during AO3 are documented explicitly. |
| **AO2 — Use Resources** | 20% | Excellent. Extensive literature (MobileNets paper, MobileNetV2 paper, OpenCV docs, RealSense SDK, Open3D docs, ImageNet). Real industry deployments cited (Keyence, Tesla, Foxconn). |
| **AO3 — Develop & Realise** | **40%** | Outstanding. Physical system to integrate with. Real failure cases. Iteration based on what doesn't work. Visual outputs at every stage. Natural plan deviations with documented reasons (this is literally in the top-band criteria). |
| **AO4 — Review** | 20% | Outstanding. Quantitative F1 metrics, classical vs ML comparison, failure mode analysis, bias acknowledgement, Tier 2 reflection. Meaty, specific, evidenced. |

### Key AO3 Documents to Produce

- Confusion matrices at each training checkpoint
- Sample predictions with defect overlay images
- Point cloud visualisations (Tier 2)
- Written justification for every significant deviation from the original plan

---

## 9. Coursework Evidence Guide

### AO1 Sources to Cite

- OpenCV documentation — `docs.opencv.org`
- Howard et al. (2017) — *MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications*
- Sandler et al. (2018) — *MobileNetV2: Inverted Residuals and Linear Bottlenecks*
- Intel RealSense SDK documentation — `intelrealsense.com`
- Open3D library documentation
- ImageNet dataset — basis of pre-trained weights used in transfer learning

### AO1 Industry Deployments to Reference

- Keyence vision inspection systems
- Tesla Autopilot manufacturing QC pipeline
- Foxconn Automated Optical Inspection (AOI) lines
- Zeiss industrial metrology

### AO3 — What to Document Every Iteration

When the OpenCV baseline underperforms on a defect type → justify switching to / adding the CNN classifier. When dataset imbalance is discovered → document augmentation response. When Tier 2 integration hits obstacles → document analysis, even if Tier 2 is incomplete. **Changes to the original plan with clear written reasons are explicitly rewarded in the top band.**

---

## 10. Project Timeline (Gantt Summary)

```
Phase 1 · Analysis        ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
Phase 2 · Design              ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
Phase 3 · Dataset                 ██████░░░░░░░░░░░░░░░░░░░░░░░░░░
Phase 4 · Implementation              ████████████░░░░░░░░░░░░░░░░
Phase 5 · Evaluation                              ████░░░░░░░░░░░░
                          W1  W2  W3  W4  W5  W6  W7  W8  W9  W10 W11 W12 W13 W14
```

Full Gantt with specific task dates is in the FigJam board (generated via Mermaid syntax in the Applied Computing project file).

---

## 11. Internship Signalling

**Strong for:** Engineering firms, manufacturing companies, robotics startups, automotive (large ML/CV hiring), defence contractors, general tech roles.

**The story:** *"I run a 3D printing business and I built a quality control system for it."* This is not a textbook exercise; it's a problem the builder actually has. The cross-domain narrative (business owner + ML engineer) is rare at GCSE level and genuinely memorable in an interview.

**The technical vocabulary you demonstrate:** Transfer learning, confusion matrix, F1 score, precision/recall tradeoff, ICP registration, point cloud processing, classical vs learned features — all of which a first-year engineering undergraduate would be expected to explain, but most 16-year-olds couldn't.

**Weak for:** Pure finance (though ML competence still registers with fintech).

---

## 12. Key Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Dataset bias (single filament colour, single lighting) | High | Medium | Acknowledge explicitly in AO4 — this is a *strength* for evaluation depth, not just a weakness |
| MobileNetV2 fails to reach F1 > 0.85 | Medium | Medium | Document why; compare against baseline; partial success with good analysis still scores well |
| Tier 2 (RealSense) integration incomplete | Medium | Low | Tier 2 is aspirational. Document outcome regardless — even partial depth integration scores AO3 marks for iteration |
| D405 harder to source used | Low | Low | D435 usable at ≥30cm with reduced accuracy; document the tradeoff |
| Time pressure (exams) | High | High | Tier 1 is a complete, submittable project on its own. Tier 2 is additive. Don't let Tier 2 scope-creep Tier 1 quality |

---

*README compiled from project planning conversations. Last substantive update: May 2026.*