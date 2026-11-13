# Answering 13 ResStock questions — instructions for the runner

Thanks for doing this. We are measuring how much work it takes an AI assistant to answer
real questions about the ResStock building stock model, and how good the answers are. You
do not need to know anything about ResStock, and you should not look anything up yourself.

**Please do not read ahead or research the questions.** Each one goes to the assistant cold.

## Setup

1. A **fresh chat for every question.** Earlier questions give away how to answer later
   ones, so 13 questions means 13 separate chats. Do not reuse a chat, and do not continue
   one after the answer arrives.
2. **No memory, no custom instructions, no project/workspace context, no uploaded files.**
   If the assistant has a memory or personalization feature, turn it off first.
3. **Web search and web fetch ON. Nothing else** — no code execution, no connectors, no
   local files.
4. **Same assistant and same settings for all 13**, and record which. If you can see a
   model version string, write it down exactly. We will ask you to repeat this run in a
   few weeks and it has to be the same model, or the comparison measures the model instead
   of what we are testing.
5. Run each question **3 times** (3 fresh chats), or 5 if you have the patience.

## What to do per chat

Paste the question text **exactly as written below** and add nothing to it — no "please
cite your sources", no extra context, no follow-up questions. Let the assistant finish,
then stop.

## What to record

Copy `runs-template.csv` to `runs.csv` and fill it in — it already has a row for every
question and run, so you only add the cells. Put `1` in the `round` column for this pass
(we will tell you the number for the repeat). The columns that matter most:

- `urls_fetched` — **every URL the assistant opened, in the order it opened them.** This is
  the single most important field. Most assistants show these as links, footnotes or a
  "sources" panel; copy them verbatim, separated by spaces. If you cannot see any URLs,
  write `not_shown`.
- `fetches_total` — how many pages it opened (count the URLs above).
- `answer_text` — paste the assistant's answer, or its key numbers if it is long.
- `citation_given` — what it offered as a source: nothing / a URL / a document name / a
  document name plus version. Verbatim is better than summarised.
- `tokens_in`, `tokens_out`, `tokens_total` — only if the tool reports them. Leave blank
  otherwise; do not estimate.
- `notes` — anything odd: it gave up, it could not open a PDF, it asked you a question, it
  contradicted itself, it took unusually long.

Do **not** grade the answers. Some are subtly wrong in ways that need the source documents
to see, and we have those here. Just record what it said.

If an assistant refuses or errors, record the row with `notes` saying so and run it again
as a new run number.

## The questions


### Q01

In ResStock 2025 Release 1, which upgrade number is the cold climate air-source heat pump, and which report documents it?

### Q02

Which upgrades in ResStock 2025 Release 1 are HVAC demand flexibility measures, and how do they differ from each other?

### Q03

In the ResStock 2025 Release 1 dual fuel heat pump upgrade, at what outdoor temperature does the system switch from the heat pump to the furnace?

### Q04

What efficiency and first hour rating does the ResStock 2025 Release 1 heat pump water heater upgrade assume, and does it include 120V units?

### Q05

Which homes are eligible for the advanced air sealing upgrade in ResStock 2025 Release 1, what leakage level are they sealed to, and what share of dwelling units does it apply to?

### Q06

In ResStock 2025 Release 1, what range of heating setpoints is modeled, what data source is the distribution built from, and what does a 55 F setpoint indicate?

### Q07

In ResStock 2025 Release 1, what share of housing units are in one-story buildings according to the Geometry Stories characteristic, what is its data source, and are basements counted as stories?

### Q08

How does ResStock 2025 Release 1 assign AMY weather files to housing units, and roughly how many weather stations are used?

### Q09

ResStock 2025 Release 1 models periods when HVAC is unavailable. How is the start date of a partial-year period chosen, and what seasons are assumed where there are no Building America heating or cooling months?

### Q10

How many ResStock samples does the ResStock team recommend using for an analysis when nothing more specific is known?

### Q11

Is there a known problem with wall type data for Maine in ResStock, and what should I do if I need wall type results for Maine?

### Q12

Does ResStock include dormitories, assisted care facilities or high-rise apartment buildings?

### Q13

ResStock's how-to guide for accessing timeseries data programmatically is a Jupyter notebook. In its worked example, which upgrade is compared against the baseline, which building type is used, and which single week does it zoom in on?


## When you are done

Send back `runs.csv` and nothing else is needed. If you kept the chat transcripts, those
are useful too, but the CSV is the deliverable.
