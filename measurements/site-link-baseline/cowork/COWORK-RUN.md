# The ResStock questions in Claude Cowork — by hand

Cowork cannot be started by a script, so each question is pasted into a new Cowork task by a
person. This sheet keeps those runs as close as possible to the scripted ones.

Scope: 13 questions, once each (13 tasks). Q01 to Q05 are the upgrade and measure-report
questions, where other agents found the most differences; if time is short, stop after Q05.

## Before the first question

Set these once and write down what you could not switch off. The names in the app may differ
slightly; the point of each line is what matters.

1. **Model**: Claude Sonnet, the same model as the Claude Code run. Leave the thinking or
   effort setting at its default and note what it is.
2. **Connectors off**: every connector (GitHub, Google Drive and so on) disabled for the task.
   A GitHub connector in particular changes what the agent can find.
3. **Memory off**: any memory or "reference past chats" setting disabled.
4. **No personal instructions**: clear or disable custom instructions and preferences.
5. **No project and no folder**: start each task outside any project. If Cowork insists on a
   working folder, give it a new empty one.
6. **Web search on.**
7. **Skills**: leave as they are if they cannot be switched off, and note that they were on.

## For each question

1. Start a **new task**. Never continue an earlier one.
2. Paste the question exactly as written below. Add nothing.
3. If it asks for permission to search or open a page, allow it. If it asks you a question,
   answer "use your judgment" and note it.
4. Let it finish. Do not reply to the answer.
5. Fill in that question's row in `runs_cowork.csv`, or leave the task open and untouched:
   after the first one we check whether the record can be read from the app directly, which
   would save the copying.

What to record per row:

- `urls_opened`: every link it opened or cited, in order, separated by spaces.
- `answer_text`: the full answer.
- `files_created`: names of any files it made or downloaded (a PDF, a spreadsheet).
- `tools_seen`: anything it used besides search and opening pages, such as running code.
- `notes`: anything odd, and how long it took.

Do not grade the answers.

## The questions

**Q01** In ResStock 2025 Release 1, which upgrade number is the cold climate air-source heat pump, and which report documents it?

**Q02** Which upgrades in ResStock 2025 Release 1 are HVAC demand flexibility measures, and how do they differ from each other?

**Q03** In the ResStock 2025 Release 1 dual fuel heat pump upgrade, at what outdoor temperature does the system switch from the heat pump to the furnace?

**Q04** What efficiency and first hour rating does the ResStock 2025 Release 1 heat pump water heater upgrade assume, and does it include 120V units?

**Q05** Which homes are eligible for the advanced air sealing upgrade in ResStock 2025 Release 1, what leakage level are they sealed to, and what share of dwelling units does it apply to?

**Q06** In ResStock 2025 Release 1, what range of heating setpoints is modeled, what data source is the distribution built from, and what does a 55 F setpoint indicate?

**Q07** In ResStock 2025 Release 1, what share of housing units are in one-story buildings according to the Geometry Stories characteristic, what is its data source, and are basements counted as stories?

**Q08** How does ResStock 2025 Release 1 assign AMY weather files to housing units, and roughly how many weather stations are used?

**Q09** ResStock 2025 Release 1 models periods when HVAC is unavailable. How is the start date of a partial-year period chosen, and what seasons are assumed where there are no Building America heating or cooling months?

**Q10** How many ResStock samples does the ResStock team recommend using for an analysis when nothing more specific is known?

**Q11** Is there a known problem with wall type data for Maine in ResStock, and what should I do if I need wall type results for Maine?

**Q12** Does ResStock include dormitories, assisted care facilities or high-rise apartment buildings?

**Q13** ResStock's how-to guide for accessing timeseries data programmatically is a Jupyter notebook. In its worked example, which upgrade is compared against the baseline, which building type is used, and which single week does it zoom in on?
