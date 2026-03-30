.DEFAULT_GOAL := help

PYTHON        := venv/bin/python

# --- Real pipeline paths ---
REFERENCE_DIR          ?= data/reference
SUBMISSIONS_DIR        ?= data/systems
PER_RUN_DIR            := results/per-run
RANKINGS_DIR           := results/system-rankings
RESULTS_MD             := HIPE_OCRepair_2026_evaluation_results.md

# --- Dummy pipeline paths (isolated from real pipeline) ---
REFERENCE_DIR_DUMMY    ?= data/reference-dummy
SUBMISSIONS_DUMMY_DIR  ?= data/systems-dummy
PER_RUN_DIR_DUMMY      := results-dummy/per-run
RANKINGS_DIR_DUMMY     := results-dummy/system-rankings
RESULTS_MD_DUMMY       := HIPE_OCRepair_2026_evaluation_results_dummy.md
DUMMY_BASELINE_SWAP_CHARS ?= 0.05 0.1
DUMMY_BASELINE_SWAP_WORDS ?= 0.01 0.05
DUMMY_BASELINE_RUN_SEEDS  ?= --run-seeds
SCHEMA_PATH         ?=

TEAMS_JSON         := lib/teams.json
COMPETITION_CONFIG := lib/competition_config.json
SCORER_VERSION     := 0.9.0
DATA_VERSION       := v0.9

SUBMISSIONS           := $(wildcard $(SUBMISSIONS_DIR)/*.jsonl)
PER_RUN_JSONS         := $(patsubst $(SUBMISSIONS_DIR)/%.jsonl,$(PER_RUN_DIR)/%.json,$(SUBMISSIONS))
REFERENCE_FILES       := $(wildcard $(REFERENCE_DIR)/*.jsonl)
REFERENCE_FILES_DUMMY := $(wildcard $(REFERENCE_DIR_DUMMY)/*.jsonl)

$(PER_RUN_DIR):
	mkdir -p $@
$(RANKINGS_DIR):
	mkdir -p $@
$(PER_RUN_DIR_DUMMY):
	mkdir -p $@
$(RANKINGS_DIR_DUMMY):
	mkdir -p $@
$(SUBMISSIONS_DUMMY_DIR):
	mkdir -p $@

$(PER_RUN_DIR)/%.json: $(SUBMISSIONS_DIR)/%.jsonl | $(PER_RUN_DIR)
	$(PYTHON) lib/score_one.py --hypothesis $< --reference-dir $(REFERENCE_DIR) --output $@

.PHONY: baselines-dummy
baselines-dummy: | $(SUBMISSIONS_DUMMY_DIR)
	$(PYTHON) lib/create_dummy_baselines.py \
		--output-dir $(SUBMISSIONS_DUMMY_DIR) \
		--swap-chars $(DUMMY_BASELINE_SWAP_CHARS) \
		--swap-words $(DUMMY_BASELINE_SWAP_WORDS) \
		$(DUMMY_BASELINE_RUN_SEEDS) \
		$(REFERENCE_FILES_DUMMY)

.PHONY: score
score: $(PER_RUN_JSONS)

.PHONY: validate-submissions
validate-submissions:
	$(PYTHON) lib/validate_submissions.py --input-dir $(SUBMISSIONS_DIR) $(if $(SCHEMA_PATH),--schema $(SCHEMA_PATH),)

.PHONY: validate-submissions-dummy
validate-submissions-dummy:
	$(PYTHON) lib/validate_submissions.py --input-dir $(SUBMISSIONS_DUMMY_DIR) $(if $(SCHEMA_PATH),--schema $(SCHEMA_PATH),)

.PHONY: score-dummy
score-dummy: | $(PER_RUN_DIR_DUMMY)
	for f in $(SUBMISSIONS_DUMMY_DIR)/*.jsonl; do \
		stem=$$(basename $$f .jsonl); \
		$(PYTHON) lib/score_one.py --hypothesis $$f --reference-dir $(REFERENCE_DIR_DUMMY) --output $(PER_RUN_DIR_DUMMY)/$$stem.json; \
	done

.PHONY: rankings
rankings: $(PER_RUN_JSONS) | $(RANKINGS_DIR)
	$(PYTHON) lib/build_rankings.py --per-run-dir $(PER_RUN_DIR) --output-dir $(RANKINGS_DIR) --competition-config $(COMPETITION_CONFIG)

.PHONY: rankings-dummy
rankings-dummy: | $(RANKINGS_DIR_DUMMY)
	$(PYTHON) lib/build_rankings.py --per-run-dir $(PER_RUN_DIR_DUMMY) --output-dir $(RANKINGS_DIR_DUMMY) --competition-config $(COMPETITION_CONFIG)

.PHONY: results-md-dummy
results-md-dummy: | $(RANKINGS_DIR_DUMMY)
	$(PYTHON) lib/build_results_md.py --rankings-dir $(RANKINGS_DIR_DUMMY) --teams-json $(TEAMS_JSON) --output $(RESULTS_MD_DUMMY) --scorer-version $(SCORER_VERSION) --data-version $(DATA_VERSION)

.PHONY: results-md
results-md: | $(RANKINGS_DIR)
	$(PYTHON) lib/build_results_md.py --rankings-dir $(RANKINGS_DIR) --teams-json $(TEAMS_JSON) --output $(RESULTS_MD) --scorer-version $(SCORER_VERSION) --data-version $(DATA_VERSION)

.PHONY: eval-full
eval-full: score rankings results-md

.PHONY: eval-full-dummy
eval-full-dummy:
	$(MAKE) clean-dummy
	$(MAKE) baselines-dummy
	$(MAKE) score-dummy
	$(MAKE) rankings-dummy results-md-dummy

.PHONY: eval-full-refresh
eval-full-refresh:
	rm -rf $(PER_RUN_DIR) $(RANKINGS_DIR)
	$(MAKE) eval-full

.PHONY: clean-dummy
clean-dummy:
	find $(SUBMISSIONS_DUMMY_DIR) -maxdepth 1 \( -name 'perfect_*.jsonl' -o -name 'no-correction_*.jsonl' -o -name 'char-swaps-*.jsonl' -o -name 'word-swaps-*.jsonl' -o -name 'same_*.jsonl' -o -name 'random_*.jsonl' \) -delete
	rm -rf $(PER_RUN_DIR_DUMMY) $(RANKINGS_DIR_DUMMY) $(RESULTS_MD_DUMMY)

.PHONY: clean
clean:
	rm -rf $(PER_RUN_DIR) $(RANKINGS_DIR) $(RESULTS_MD)

.PHONY: help
help:
	@echo ""
	@echo "HIPE-OCRepair-2026 evaluation pipeline"
	@echo ""
	@echo "End-to-end targets:"
	@echo "  eval-full-dummy    Generate dummy baselines, score them, build rankings and MD (uses results-dummy/)"
	@echo "  eval-full          Score real submissions, build rankings and MD (uses results/)"
	@echo "  eval-full-refresh  Remove all derived real files and re-run eval-full from scratch"
	@echo ""
	@echo "Dummy pipeline step-by-step (all output under results-dummy/):"
	@echo "  baselines-dummy    Generate dummy baselines from $(REFERENCE_DIR_DUMMY) into $(SUBMISSIONS_DUMMY_DIR)"
	@echo "  validate-submissions-dummy  Validate dummy submissions against the JSON schema"
	@echo "  score-dummy        Score all files in $(SUBMISSIONS_DUMMY_DIR)"
	@echo "  rankings-dummy     Build per-test-set and overall ranking TSVs"
	@echo "  results-md-dummy   Render $(RESULTS_MD_DUMMY)"
	@echo ""
	@echo "Real pipeline step-by-step (all output under results/):"
	@echo "  validate-submissions  Validate real submissions in $(SUBMISSIONS_DIR) against the JSON schema"
	@echo "  score              Score real submissions in $(SUBMISSIONS_DIR) (incremental)"
	@echo "  rankings           Build ranking TSVs from scored real submissions"
	@echo "  results-md         Render $(RESULTS_MD)"
	@echo ""
	@echo "Utilities:"
	@echo "  clean              Remove results/, $(RESULTS_MD)"
	@echo "  clean-dummy        Remove results-dummy/, $(RESULTS_MD_DUMMY), and generated baselines"
	@echo ""
	@echo "Override variables:"
	@echo "  REFERENCE_DIR        Real reference JSONL directory     (default: data/reference)"
	@echo "  REFERENCE_DIR_DUMMY  Dummy reference JSONL directory    (default: data/reference-dummy)"
	@echo "  SCHEMA_PATH          Optional JSON schema override      (default: scorer built-in schema)"
	@echo "  SUBMISSIONS_DUMMY_DIR  Dummy hypothesis directory       (default: $(SUBMISSIONS_DUMMY_DIR))"
	@echo "  DUMMY_BASELINE_SWAP_CHARS  Character swap ratios        (default: $(DUMMY_BASELINE_SWAP_CHARS))"
	@echo "  DUMMY_BASELINE_SWAP_WORDS  Word swap ratios             (default: $(DUMMY_BASELINE_SWAP_WORDS))"
	@echo ""
