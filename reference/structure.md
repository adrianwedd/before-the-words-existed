# Research Structure & Technical Documentation

This document contains the technical details, workflow architecture, and evidence standards for the *Neuromancer Cognitive Mismatch* research project.

---

## Project Status

**Phase 1: COMPLETE** ✓ (Second pass complete)  
**Phase 2: COMPLETE** ✓ (Second pass complete)  
**Phase 3: COMPLETE** ✓ (Track C draft complete + hardened)

**Track B draft complete. Track C draft complete and hardened.**

---

## Second Pass: Coverage Summary (Complete)

All tasks exceeded targets. Evidence base now suitable for Track C peer review.

| Task | First Pass | Second Pass | Target | Status |
|------|------------|-------------|--------|--------|
| 1.1 Deprivation | 18 entries | 25 entries + 4 counter | 25-30 | ✓ Done |
| 1.2 Sharp Memory | 8 entries | 15 entries + domain counter | 15-20 | ✓ Done |
| 2.1 Time | 15 entries | 28 entries (TRN gap filled) | 25-35 | ✓ Done |
| 2.2 Addiction | 9 entries | 20 entries (substances added) | 12-15 | ✓ Done |
| 2.3 Environment | 9 entries | 18 entries + 14 environments | 18-25 | ✓ Done |

See `reference/second-pass-trawl-protocol.md` for keyword lists, chapter audits, and methodology.

---

## Task Index

### Phase 1: Validation — COMPLETE ✓

| Task | Title | Status | Key Finding |
|------|-------|--------|-------------|
| **1.1** | Verify Deprivation State | ✓ COMPLETE | Validated with qualifications; two-layer model holds |
| **1.2** | Verify Sharp Memory | ✓ COMPLETE | Phantom-limb structure validated; precision discriminant satisfied |

### Phase 2: Evidence Gathering — COMPLETE ✓

| Task | Title | Purpose | Key Tests | Status |
|------|-------|---------|-----------|--------|
| **2.1** | Time Phenomenology | Map temporal experience shifts across states | Time distortion patterns + ADHD resonance points | ✓ COMPLETE |
| **2.2** | Addiction Framing | Test "institutional misdescription" thesis | Speaker attribution + Experience vs. label mismatch | ✓ COMPLETE |
| **2.3** | Environmental Markers | Test oscillation between medical/interactional framings | Attribution inventory + Functional logic assessment | ✓ COMPLETE |

### Phase 3: Track C Preparation — COMPLETE ✓

| Task | Title | Purpose | Status |
|------|-------|---------|--------|
| **3.1** | The Body Problem | Determine if meat-disdain is ideology or phenomenology | ✓ COMPLETE |
| **3.2** | Case vs. Molly | Compare phenomenologies, test for cognitive diversity | ✓ COMPLETE |
| **3.3** | Historical Context | Document what language didn't exist in 1984 | ✓ COMPLETE |

---

## Directory Structure

```
neuromancer-mismatch/
├── README.md                    # Public-facing introduction (poetic/accessible)
├── Before-the-Words-Existed.md  # Release-ready thesis (source)
│
├── docs/                        # GitHub Pages site + PDF output
│   ├── index.html
│   ├── thesis.html
│   └── Before-the-Words-Existed.pdf
│
├── analysis/                    # Research corpus (tasks, reviews, deep dives)
│   ├── tasks/                   # 8 research task files with evidence tables
│   ├── task-1.1-verify-deprivation-state.md
│   ├── task-1.2-verify-sharp-memory.md
│   ├── task-2.1-time-phenomenology.md
│   ├── task-2.2-addiction-framing.md
│   ├── task-2.3-environmental-markers.md
│   ├── task-3.1-body-problem.md
│   ├── task-3.2-case-vs-molly.md
│   └── task-3.3-historical-context.md
│
├── drafts/                      # Essay drafts
│   ├── track-b-draft.md         # Standalone essay version
│   └── track-c-draft.md         # Academic paper version
│
│   ├── research/                # 5 historiographic deep-dives
│   │   ├── The_Phenomenology_of_the_Glitch.md  # ADHD history 1960-1990
│   │   ├── Paradigms_of_Pluralism.md           # Neurodiversity timeline
│   │   ├── The_Texture_of_the_Present.md       # Gibson's creative process
│   │   ├── The_Exegesis_of_the_Idios_Kosmos.md # Philip K. Dick parallel
│   │   └── Terminal_Psychologies.md            # Early criticism 1984-1995
│   └── reviews/                 # Adversarial peer review simulations
│       └── [review files and analyses]
│
├── reference/                   # Supporting documentation
│   ├── dsm-history-1980.md
│   ├── methodology.md
│   ├── second-pass-trawl-protocol.md
│   └── structure.md
│
├── source/                      # Full Neuromancer text
│   └── Neuromancer.md
│
├── prompts/                     # Archived research prompts
│   └── [various .md files]
│
└── scripts/                     # Utility scripts
    ├── render_thesis.py
    └── verify_openlibrary.py
```

---

## Evidence Logging System

**Use consistently across all tasks:**

### Evidence IDs
Format: `[Task]-E[Number]` (e.g., `1.1-E01`, `1.2-E03`, `2.2-E12`)
- Counterexamples use `X` instead of `E` (e.g., `1.1-X01`)
- This enables cross-task synthesis and citation

### Voice Channel
Tag every piece of evidence:
- **N** = Narrator (direct description)
- **FI** = Free indirect discourse (inhabiting Case's perspective)
- **D** = Dialogue (other characters speaking)

**Weight:** N and FI are strong evidence. D is weaker (reflects speaker's framework, not necessarily Case's experience). Patterns across multiple N/FI passages are strongest.

---

## The Noir Problem (Critical Context)

A competent SF/noir critic will object: "This is just genre-conventional alienation. You're redescribing what cyberpunk does."

This objection is serious. The research must not only verify phenomenological claims but also **test whether they exceed generic noir/cyberpunk alienation**.

**Two-layer model:**
- **Noir** names the atmosphere (political economy, genre affect, existential mood)
- **Mismatch** names the mechanism of subjectivity within that atmosphere

These can coexist. The claim is not "Neuromancer depicts alienation." The claim is: it depicts a *reversible, interface-dependent reconfiguration of cognition* with features that exceed generic genre mood.

**Three discriminants distinguish mismatch from noir:**

| Discriminant | Noir Pattern | Mismatch Pattern | Phase 1 Result |
|--------------|--------------|------------------|----------------|
| **Reversibility** | Competence spikes are aesthetic flashes inside persistent futility | Interface-state produces qualitatively different cognition | ✓ Mismatch |
| **Precision** | Longing is nostalgic, mythic, symbolic | Relation to access is procedurally exact (phantom-limb structure) | ✓ Mismatch |
| **Relationality** | Alienation is existential, persists across contexts | Mismatch is relational: appears when environment denies conditions for competence | ✓ Mixed/Mismatch |

---

## Methodological Posture

This analysis does not claim perceptual neutrality. It begins from recognition: the experience of reading *Neuromancer* and finding something that resonates with contemporary accounts of cognitive-environment mismatch. This recognition names a point of entry, not a governing explanation.

The lens is not "ADHD as diagnostic category" but "mismatch as experiential structure": a pattern that must be rendered in the text itself to hold. The structure is testable. If the deprivation state shows engagement rather than flatness, if memory degrades rather than sharpens, if restoration reads as intoxication rather than homecoming, the reading fails.

The discipline lies in testing, not in pretending to see from nowhere.

**Full methodological statement:** See `methodological-posture.md`

---

## Defensive Positions (Pre-Established)

The research framework has been stress-tested against three hostile reviewer positions:

### Reviewer #1: SF Formalist ("This is just noir")
**Established defense:** The two-layer model. Noir is atmosphere; mismatch is mechanism. Phase 1 validated this distinction.

### Reviewer #2: Disability Studies Skeptic ("You're romanticising impairment")
**Established defense:** Acknowledge oscillation. The text uses damage language *and* access language. Task 2.3 gathers evidence for both framings. The claim is that *functional logic* resolves toward access.

### Reviewer #3: Phenomenology Purist ("Your bracketing fails")
**Established defense:** Recognition initiates inquiry but doesn't adjudicate findings. The lens is "mismatch as structure," not "ADHD as diagnosis." Discipline lies in testing. All tasks include explicit falsification criteria.

---

## Current Workflow

```
Phase 1: COMPLETE ✓
         │
         ▼
┌─────────────────────────────────────────────────────────────┐
│                   PHASE 2: EVIDENCE GATHERING                │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │ Task 2.1 │    │ Task 2.2 │    │ Task 2.3 │              │
│  │ Time     │    │ Addiction│    │ Environ  │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│        (these three can run in parallel)                    │
│                                                             │
│  BUILD ON PHASE 1 FINDINGS                                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
                   TRACK B COMPLETE
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   PHASE 3: TRACK C PREP                      │
│  ┌──────────┐        ┌──────────┐        ┌──────────┐      │
│  │ Task 3.1 │───────→│ Task 3.2 │        │ Task 3.3 │      │
│  │ Body     │        │ Molly    │        │ History  │      │
│  └──────────┘        └──────────┘        └──────────┘      │
│                                          (runs parallel)    │
└─────────────────────────────────────────────────────────────┘
```

---

## Common Standards Across All Tasks

### Evidence Requirements
- Quote accurately or paraphrase closely
- Note page/chapter locations
- Distinguish explicit text from inference
- Include counter-evidence

### Counter-Reading Requirement
Each task requires engaging the strongest objection to the reading.

### Deliverables
Each task specifies concrete outputs:
- Evidence tables
- Pattern summaries (word counts specified)
- Implications for draft (specific, actionable)

### Quality Threshold
Tasks are complete only when completion criteria checklist is satisfied.

---

## Key Research Findings Summary

### Task 1.1: Deprivation State — VERIFIED WITH QUALIFICATIONS (25 entries + 4 counter)

**Core claims validated:**
- Body-as-luggage: STRONG
- Purposeless alertness: STRONG
- Tractionlessness: STRONG
- Temporal accumulation: STRONG
- World-as-noise: SUPPORTED
- Affective flatness: QUALIFIED — "attritional flattening punctuated by spikes," not total numbness

**Counterexamples documented (must acknowledge in essay):**
- Tactical calculation, sharp observation, decisive action, future-pull anticipation

**Noir discriminants:**
- Reversibility: Leans mismatch (deprivation framed as contingent/curable)
- Relationality: Mixed but mismatch-leaning (failure framed as fit, not essence)

**Two-layer model validated:** Noir is atmosphere; mismatch is mechanism.

---

### Task 1.2: Sharp Memory — VERIFIED WITH QUALIFICATIONS (15 entries)

**Core claims validated:**
- Memory is procedurally precise: STRONG
- Prose texture tightens for Matrix passages: VERIFIED
- Phantom-limb structure: DEFENSIBLE
- Loss framed as severance, not decay: SUPPORTED

**Critical refinement — domain-specific precision:**
Counter-evidence: "I don't have this good a memory" — Case can't recall the lines on his palms. Memory precision is **domain-specific** (matrix/interface), not globally sharp.

**Precision discriminant:** Strong mismatch signal — procedural specificity exceeds noir mood alone.

---

### Task 2.1: Time Phenomenology — VERIFIED WITH QUALIFICATIONS (28 entries)

**Core pattern validated:**
- Deprivation time: Accumulating and erosive
- Active/Matrix time: Compressing, absorbed, task-structured
- Memory/anticipation: Future-pull present, countdown structure
- Transition (TRN): Fragmented, discontinuous — **gap filled**
- Outside post-restoration (OUT): Externally structured, access-flattened

**ADHD resonance assessment:**
- Time blindness: SUPPORTED
- Hyperfocus collapse: SUPPORTED
- External structure dependence: SUPPORTED
- Future as unreal: MIXED (fading hope, but countdown shows future-pull returns)
- Transition discontinuity: SUPPORTED — **new**

**Pacing analysis confirmed:** Narrative form encodes temporal phenomenology.

---

### Task 2.2: Addiction Framing — SUPPORTED WITH QUALIFICATIONS (20 entries)

**Core thesis tested:** "Addiction operates as institutional misdescription — a label that explains Case to systems that cannot represent functional mismatch."

**Experience vs. label:**
- Matrix longing: persistent, functional, phantom-limb structure (deprivation pattern)
- Stimulant use: cyclical, hedonic, with documented comedown — **addiction pattern confirmed**
- **The text distinguishes these two dependencies**

**Restoration scene:**
- Euphoria present, homecoming present, function present
- **Verdict: Mixed** — not purely intoxication, not purely technical return

---

### Task 2.3: Environmental Markers — VALIDATED WITH OSCILLATION (18 entries + 14 environments)

**Core thesis tested:** "The novel oscillates between medical and interactional framings—but its functional logic resolves in favour of access, not cure."

**Model assessment:**
- Medical model: Has support (real damage acknowledged)
- Social model: Partial (punishment is punitive denial)
- Interactional model: **Functional logic resolves here** — problem is fit/access, restoration is reconnection

**Counter-reading absorbed:** Internal-deficit reading has merit (damage is real), but fails because text defines loss as *specific interface*, not *global function*, and restoration reads as return-to-self.

---

## Files in Tasks Folder

| Filename | Status | Description |
|----------|--------|-------------|
| `task-1.1-verify-deprivation-state.md` | ✓ COMPLETE (2nd pass) | Deprivation phenomenology verified |
| `task-1.2-verify-sharp-memory.md` | ✓ COMPLETE (2nd pass) | Sharp memory/phantom-limb verified |
| `task-2.1-time-phenomenology.md` | ✓ COMPLETE (2nd pass) | Time distortion patterns verified |
| `task-2.2-addiction-framing.md` | ✓ COMPLETE (2nd pass) | Institutional misdescription thesis tested |
| `task-2.3-environmental-markers.md` | ✓ COMPLETE (2nd pass) | Medical vs. interactional framing tested |
| `task-3.1-body-problem.md` | ✓ COMPLETE | Ideology vs. phenomenology (dissociation dominant) |
| `task-3.2-case-vs-molly.md` | ✓ COMPLETE | Contrasting phenomenologies (simstim as test) |
| `task-3.3-historical-context.md` | ✓ COMPLETE | 1984 absence + parallel cases documented |

---

## Related Documents

- **Main Essay:** `drafts/Before the Words Existed - Neuromancer and the Experience of Cognitive Mismatch.md`
- **Track B (Standalone):** `drafts/track-b-draft.md`
- **Track C (Academic):** `drafts/track-c-draft.md`
- **Methods Statement:** `methodological-posture.md`
- **Research Corpus:** `analysis/research/` folder (5 deep-dive reports)

---

*Framework version: 1.1*
*Project: Experience of Cognitive Mismatch in Neuromancer*
*All phases completed: January 2026*
