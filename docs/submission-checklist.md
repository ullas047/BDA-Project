# Submission checklist

Before pushing to GitHub and tagging `v1.0`, complete these items using real team evidence:

- [ ] Replace the README video placeholder with an accessible 15-20 minute 1080p link and chapter timestamps.
- [ ] Enter group number, names, IDs, repository URL and video link in the final IEEE report PDF.
- [ ] Replace role, contribution, reflection and signature placeholders with the three members' genuine information.
- [ ] Run the full required scale experiments at SF=.25, .5 and 1; fill `docs/performance.md` with measured runtimes/output sizes.
- [ ] Capture genuine Spark UI before/after screenshots for broadcast join and partition/AQE optimisation; insert them into the report (ENG-3).
- [ ] Run threshold sweep, rolling-origin forecast backtest and allocation baseline comparison; report actual results.
- [ ] Set a non-demo `EPISCOPE_HASH_SALT` in a local `.env`, never commit it.
- [ ] Run `pytest -q`, `make all SF=0.01`, then the hidden-drop command and a rerun demonstration.
- [ ] Check dashboard serving export is below 10MB and contains no line-level or 1-4 counts.
- [ ] Create `docs/report.pdf`, commit only permitted artifacts, push to the group private repository, and tag `v1.0` at the deadline.
