LOVE FORMULA – TECHNICAL SPECIFICATION

Public 30% Release (Educational, Personal & Research Use)

The Love Formula is a modular scoring framework that analyses text for emotional tone, relational intent, and compassion-weighted indicators. This specification documents the public 30% release — a safe, limited, transparent subset of the full system designed for education, research, youth work and personal use.

This version is intentionally simplified to prevent misuse, while allowing learning and exploration.


---

1. Purpose of This Version

This specification describes:

The structure of the public scoring model

The input/output format

The weighting logic

Definitions of positive and negative indicators

Limitations and boundaries

Safe-use constraints


This is not the commercial or enterprise version, and does not include:

Multi-layer intent modelling

Advanced context analysis

Relational pattern detection

Multi-sentence inference

Harm escalation mapping

Real-time behaviour prediction

Love-OS override pathways


These remain restricted to prevent misuse.


---

2. Input Format

The public Love Formula implementation accepts:

text_input: string

Requirements:

UTF-8 compatible

Preferably 3–400 characters for best results

Single-message analysis (short texts suitable)



---

3. Output Format

The function returns a dictionary:

{
  "love_score": float
}

Score range: 0.00 → 1.00

Higher score = more compassionate, calm, connective language

Lower score = more harmful, harsh, or emotionally unsafe language


This version returns only a single scalar, not the multidimensional scores of the professional edition.


---

4. Core Formula Structure (Public Version)

The 30% public algorithm uses a linear combination of:

4.1 Positive Indicators

Weighted keywords and patterns including:

gratitude

kindness

appreciation

supportiveness

calmness

cooperative intent

non-violent tone


Examples include:
“thank you”, “I appreciate”, “I understand”, “sorry”, “let’s fix this”, “I care”


---

4.2 Negative Indicators

Weighted keywords and patterns representing:

verbal aggression

hostility

threats

emotional harm

coercion

insulting language


Examples include:
“shut up”, “stupid”, “idiot”, “I hate you”, “you’re nothing”


---

4.3 Neutrality Factor

A normalisation step reducing score volatility for short messages.

This prevents:

accidental over-scoring

accidental under-scoring

the system being “gamed” by repeated positive words



---

4.4 Final Score Calculation

The simplified equation:

love_score = (positive_weight - negative_weight)

Then normalised to a final range of 0.00 → 1.00:

love_score = max(0.0, min(1.0, (score + 1) / 2))

Full code version is provided in src/love_formula.py.


---

5. Limitations (Important)

The public Love Formula:

Does not understand sarcasm

Does not detect psychological manipulation

Does not evaluate long conversations

Does not make behavioural predictions

Does not judge character or personality

Does not determine truth/falsehood


It is not suitable for:

Policing

Surveillance

Sentencing

Punitative scoring

HR decisions

Law enforcement

Behaviour monitoring

Predictive analysis


This public version is intentionally constrained for ethics and safety.


---

6. Safe Use Cases

This specification supports use for:

Youth communication workshops

Emotional intelligence training

Classroom activities

Reflective journalling

Calm-down and de-escalation tools

Educational prototypes

AI alignment experiments

Ethical research environments


The primary purpose is growth, understanding and discussion.


---

7. Forbidden Use Cases

The Love Formula must never be used for:

Punishing people

Ranking human worth

Denying opportunities

Predicting criminality

Scoring people’s morality

Surveillance or monitoring

Medical diagnosis

Immigration or policing


This is a trauma-aware system, designed for compassion only.


---

8. Public Release Philosophy

This 30% version is released openly because:

People deserve transparent tools

Young people benefit from emotional structure

Researchers need a baseline framework

AI developers need safe models

Communities need tools that uplift rather than punish


The deeper levels remain protected until we know they can be used ethically.


---

9. Versioning

Current version: v0.1.0 – Public Educational Release
Future versions will expand documentation but maintain safety boundaries.
