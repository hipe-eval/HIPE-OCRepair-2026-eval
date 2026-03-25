PYTHON        := venv/bin/python
REFERENCE_DIR := data/reference
SUBMISSIONS_DIR        := evaluation/system-responses/submitted
SUBMISSIONS_DUMMY_DIR  := evaluation/system-responses-dummy/submitted
PER_RUN_DIR   := results/per-run
RANKINGS_DIR  := results/system-rankings
RESULTS_MD    := HIPE_OCRepair_2026_evaluation_results.md
TEAMS_JSON    := lib/teams.json
SCORER_VERSION := 0.9.0
DATA_VERSION   := v0.9

SUBMISSIONS      := $(wildcard $(SUBMISSIONS_DIR)/*.jsonl)
PER_RUN_JSONS    := $(patsubst $(SUBMISSIONS_DIR)/%.jsonl,$(PER_RUN_DIR)/%.json,$(SUBMISSIONS))

$(PER_RUN_DIR):
	mkdir -p $@
$(RANKINGS_DIR):
	mkdir -p $@

$(PER_RUN_DIR)/%.json: $(SUBMISSIONS_DIR)/%.jsonl | $(PER_RUN_DIR)
	$(PYTHON) lib/score_one.py --hypothesis $< --reference-dir $(REFERENCE_DIR) --output $@

.PHONY: score
score: $(PER_RUN_JSONS)

.PHONY: score-dummy
score-dummy: | $(PER_RUN_DIR)
	for f in $(SUBMISSIONS_DUMMY_DIR)/*.jsonl; do \
		stem=$$(basename $$f .jsonl); \
		$(PYTHON) lib/score_one.py --hypothesis $$f --reference-dir $(REFERENCE_DIR) --output $(PER_RUN_DIR)/$$stem.json; \
	done

.PHONY: rankings
rankings: $(PER_RUN_JSONS) | $(RANKINGS_DIR)
	$(PYTHON) lib/build_rankings.py --per-run-dir $(PER_RUN_DIR) --output-dir $(RANKINGS_DIR)

.PHONY: rankings-dummy
rankings-dummy: | $(RANKINGS_DIR)
	$(PYTHON) lib/build_rankings.py --per-run-dir $(PER_RUN_DIR) --output-dir $(RANKINGS_DIR)

.PHONY: results-md
results-md: | $(RANKINGS_DIR)
	$(PYTHON) lib/build_results_md.py --rankings-dir $(RANKINGS_DIR) --teams-json $(TEAMS_JSON) --output $(RESULTS_MD) --scorer-version $(SCORER_VERSION) --data-version $(DATA_VERSION)

.PHONY: eval-full
eval-full: score rankings results-md

.PHONY: eval-full-dummy
eval-full-dummy:
	$(MAKE) score-dummy
	$(MAKE) rankings-dummy results-md

.PHONY: eval-full-refresh
eval-full-refresh:
	rm -rf $(PER_RUN_DIR) $(RANKINGS_DIR)
	$(MAKE) eval-full

.PHONY: clean
clean:
	rm -rf $(PER_RUN_DIR) $(RANKINGS_DIR) $(RESULTS_MD)
