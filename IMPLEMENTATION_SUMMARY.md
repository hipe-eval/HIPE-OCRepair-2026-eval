# Implementation Summary: Pairwise Significance Testing

## What Was Implemented

Three new components for statistically rigorous pairwise system comparison:

### 1. `lib/pairwise_significance.py` (Core Testing Script)

**Purpose**: Compare two specific systems using paired bootstrap testing.

**Usage**:

```bash
# Text format (human-readable)
python lib/pairwise_significance.py \
  --system-a data/systems/system1_*test*.jsonl \
  --system-b data/systems/system2_*test*.jsonl \
  --reference-dir data/reference \
  --format text

# TSV format (machine-readable)
python lib/pairwise_significance.py \
  --system-a data/systems/system1_*.jsonl \
  --system-b data/systems/system2_*.jsonl \
  --reference-dir data/reference \
  --format tsv > comparison.tsv

# JSON format (structured data)
python lib/pairwise_significance.py \
  --system-a data/systems/system1_*.jsonl \
  --system-b data/systems/system2_*.jsonl \
  --reference-dir data/reference \
  --format json > comparison.json
```

**Features**:

- Paired bootstrap with 10,000 resamples (configurable with `--n-bootstrap`)
- Tests all 4 metrics: cMER, wMER, char_pref, word_pref
- Handles missing postcorrections (imputes with original OCR)
- Reproducible results with `--random-seed`
- Verbose mode for progress tracking

**Output**:

- Mean difference (A - B)
- 95% confidence interval of difference
- Two-tailed p-value
- Significance determination (α=0.05)
- Winner identification (accounting for "lower is better" vs "higher is better")

### 2. `lib/pairwise_overlaps.py` (Batch Analysis Script)

**Purpose**: Automatically identify and test all consecutive systems with overlapping CIs.

**Usage**:

```bash
# Via Makefile (recommended)
make pairwise-overlaps

# Direct invocation
python lib/pairwise_overlaps.py \
  --rankings-dir results/system-rankings \
  --submissions-dir data/systems \
  --reference-dir data/reference \
  --metric cmer_micro \
  --output results/pairwise-overlaps.tsv \
  --verbose
```

**What It Does**:

1. Reads all ranking TSV files from `--rankings-dir`
2. For each test set, identifies consecutive systems with overlapping CIs on `--metric`
3. Runs paired bootstrap tests for each pair (calls `pairwise_significance.py`)
4. Outputs comprehensive TSV with all results

**Output TSV Columns**:

- `test_set`: Which test set (e.g., dta19-l0_v0.1_test_de)
- `rank_a`, `rank_b`: Rankings from the table
- `system_a`, `system_b`: System names
- `ranking_metric`: Metric used to identify overlap (e.g., cmer_micro)
- `ranking_score_a`, `ranking_ci_lo_a`, `ranking_ci_hi_a`: System A's point estimate and CI
- `ranking_score_b`, `ranking_ci_lo_b`, `ranking_ci_hi_b`: System B's point estimate and CI
- `test_metric`: Which metric is being tested (cMER, wMER, char_pref, word_pref)
- `mean_diff`: Mean difference from paired bootstrap
- `ci_lower`, `ci_upper`: 95% CI of difference
- `p_value`: Two-tailed p-value
- `significant`: yes/no
- `winner`: A, B, or tie

### 3. Makefile Targets

**New targets**:

```makefile
make pairwise-overlaps        # Real data → results/pairwise-overlaps.tsv
make pairwise-overlaps-dummy  # Dummy data → results-dummy/pairwise-overlaps.tsv
```

**Integration**:

- Added to `make help` documentation
- Depends on rankings being generated first
- Runs with verbose output enabled

### 4. Documentation: `PAIRWISE_TESTING.md`

Comprehensive guide covering:

- **The Problem**: Why per-system CIs aren't sufficient
- **The Solution**: How paired bootstrap works
- **Tool Usage**: Examples for both scripts
- **Output Format**: Column-by-column explanation
- **Meaningful Use Cases**: 6 practical applications with examples
- **Statistical Notes**: Multiple testing, effect sizes, assumptions
- **Quick Reference**: Command cheat sheet

## Key Design Decisions

### 1. Winner Determination Logic

For each metric, we determine "better" correctly:

- **cMER, wMER** (lower is better): If diff < 0, then A < B, so A wins
- **char_pref, word_pref** (higher is better): If diff > 0, then A > B, so A wins

Implemented via `lower_is_better` parameter in `paired_bootstrap_test()`.

### 2. Overlapping CI Detection

Function: `has_overlapping_ci()`

- Returns True if CIs overlap (not completely disjoint)
- Used to identify which consecutive systems need testing
- Conservative approach: only tests pairs that _could_ be tied

### 3. Data Processing Pipeline

```
Submission JSONL
  ↓
Load records
  ↓
Impute missing postcorrections (ocr_postcorrection_output.transcription_unit)
  ↓
Align with reference (using hipe_ocrepair_scorer.align_records)
  ↓
Create Evaluation instance
  ↓
Extract per-document scores (using example_level_measures functions)
  ↓
Convert to numpy arrays
  ↓
Paired bootstrap test
```

### 4. Bootstrap Implementation

- **Paired resampling**: Same document indices for both systems
- **Stratification**: None (resamples documents uniformly)
- **Percentile method**: 2.5th and 97.5th percentiles for 95% CI
- **p-value**: Two-tailed (proportion of replicates with opposite sign)
- **Significance**: CI excludes zero

## Testing Results

Verified with real data:

```bash
$ python lib/pairwise_significance.py \
  --system-a data/systems/baseline-no-correction_*_dta19-l0_*_de_*.jsonl \
  --system-b data/systems/blocr_*_dta19-l0_*_de_*.jsonl \
  --reference-dir data/reference \
  --n-bootstrap 1000 \
  --format text

Pairwise Comparison: baseline-no-correction vs blocr
==================================================

cMER:
  Mean difference (A - B): -0.029856
  95% CI: [-0.034069, -0.025530]
  p-value: 0.000000
  *** SIGNIFICANT (α=0.05) - baseline-no-correction is better ***

wMER:
  Mean difference (A - B): -0.139504
  95% CI: [-0.161810, -0.117225]
  p-value: 0.000000
  *** SIGNIFICANT (α=0.05) - baseline-no-correction is better ***

char_pref:
  Mean difference (A - B): +0.950000
  95% CI: [+0.900000, +0.987500]
  p-value: 0.000000
  *** SIGNIFICANT (α=0.05) - baseline-no-correction is better ***

word_pref:
  Mean difference (A - B): +0.925000
  95% CI: [+0.850000, +0.987500]
  p-value: 0.000000
  *** SIGNIFICANT (α=0.05) - baseline-no-correction is better ***
```

**Interpretation**: baseline-no-correction (original OCR) performs better than blocr across all metrics, indicating that blocr's corrections are introducing errors rather than fixing them.

## Meaningful Use Cases

### 1. Validate Ranking Differences

**Question**: "System A is ranked #2 and B is #3, but are they really different?"

**Command**:

```bash
grep "test_set_name" results/pairwise-overlaps.tsv | grep "cMER"
```

**Interpretation**:

- `significant=yes` → Ranking is statistically supported
- `significant=no` → Systems are in statistical tie (ranking may be arbitrary)

### 2. Identify Performance Tiers

**Question**: "Which systems form indistinguishable groups?"

**Command**:

```bash
grep "significant\tno" results/pairwise-overlaps.tsv | \
  cut -f1,2,3,4,5 | sort | uniq
```

**Output Example**:

```
dta19-l0_v0.1_test_de   1   system1   2   system2
dta19-l0_v0.1_test_de   2   system2   3   system3
```

**Interpretation**: Systems 1-3 form a "tier" (statistically indistinguishable)

### 3. Detect Misleading Rankings

**Question**: "Where does the ranking create false impressions?"

**Filter**: Find overlapping CIs that are also not significant

**Use**: Add footnotes to ranking tables like:

```
† Systems at ranks 2-4 are not significantly different (p > 0.05)
```

### 4. Assess System Stability

**Question**: "Are different runs of the same system significantly different?"

**Command**:

```bash
python lib/pairwise_significance.py \
  --system-a data/systems/team_*_run1.jsonl \
  --system-b data/systems/team_*_run2.jsonl \
  --reference-dir data/reference
```

**Interpretation**:

- `significant=yes` → System is unstable (random seed affects results)
- `significant=no` → System is reproducible

### 5. Metric Agreement Analysis

**Question**: "Do cMER and wMER agree on which system is better?"

**Analysis**:

```bash
grep "system1.*system2" results/pairwise-overlaps.tsv | \
  grep -E "cMER|wMER" | awk -F'\t' '{print $8, $18, $19}'
```

**Interpretation**: Different granularities may show different patterns

### 6. Power Analysis

**Question**: "Do we have enough test data to detect differences?"

**Analysis**:

```bash
total=$(grep "cMER" results/pairwise-overlaps.tsv | wc -l)
ties=$(grep "cMER.*\tno\t" results/pairwise-overlaps.tsv | wc -l)
echo "Statistical ties: $ties / $total"
```

**Interpretation**:

- High proportion of ties → May need more test documents
- Low proportion → Ranking is well-supported

## Example Workflow

```bash
# Step 1: Generate rankings
make eval-full

# Step 2: Run pairwise overlap analysis
make pairwise-overlaps

# Step 3: Examine results
wc -l results/pairwise-overlaps.tsv  # How many comparisons?

grep "cMER" results/pairwise-overlaps.tsv | grep "significant\tyes" | wc -l  # How many significant?

# Step 4: Find all statistical ties for a specific test set
grep "dta19-l0_v0.1_test_de" results/pairwise-overlaps.tsv | \
  grep "cMER" | grep "significant\tno" | \
  awk -F'\t' '{print $2" "$3" ~ "$4" "$5" (p="$17")"}'

# Step 5: Find largest non-significant difference (close call)
grep "cMER" results/pairwise-overlaps.tsv | grep "significant\tno" | \
  sort -t$'\t' -k14 -rn | head -1 | \
  awk -F'\t' '{print $3" vs "$5": Δ="$14" (p="$17")"}'

# Step 6: Compare two specific systems in detail
python lib/pairwise_significance.py \
  --system-a data/systems/interesting_system1_*.jsonl \
  --system-b data/systems/interesting_system2_*.jsonl \
  --reference-dir data/reference \
  --format text
```

## Statistical Rigor

### Multiple Testing Correction (Bonferroni)

When comparing N pairs, consider adjusting α:

```
α_adjusted = 0.05 / N
```

Example: 20 comparisons → use α = 0.0025 instead of 0.05

**Filter in analysis**:

```bash
awk -F'\t' '$17 < 0.0025' results/pairwise-overlaps.tsv
```

### Effect Size Interpretation

**For cMER/wMER**:

- Δ < 0.001: Very small practical difference
- Δ > 0.01: Moderate practical difference
- Δ > 0.05: Large practical difference

**For preference scores**:

- Δ < 0.05: Very small practical difference
- Δ > 0.2: Moderate practical difference
- Δ > 0.5: Large practical difference

**Important**: A result can be:

- Statistically significant but practically negligible (large N, tiny effect)
- Statistically non-significant but practically large (small N, large effect)

Always consider both statistical and practical significance!

## Files Created

1. `/lib/pairwise_significance.py` (416 lines)
   - Core paired bootstrap implementation
   - CLI for comparing two systems

2. `/lib/pairwise_overlaps.py` (403 lines)
   - Batch processing script
   - Identifies overlapping CIs and runs tests

3. `/PAIRWISE_TESTING.md` (350+ lines)
   - Comprehensive user documentation
   - Use cases, examples, statistical notes

4. `/Makefile` (updated)
   - Added `pairwise-overlaps` target
   - Added `pairwise-overlaps-dummy` target
   - Updated help text

5. `/IMPLEMENTATION_SUMMARY.md` (this file)
   - Technical documentation for developers

## Next Steps (Optional Enhancements)

### Short Term:

- [ ] Test with real data that has overlapping CIs
- [ ] Verify output TSV opens correctly in Excel/LibreOffice
- [ ] Add example analysis scripts to extract insights from TSV

### Medium Term:

- [ ] Add visualization (heatmap of pairwise significance matrix)
- [ ] Integrate into `build_results_md.py` to auto-generate footnotes
- [ ] Add "all-pairs" mode (not just consecutive overlapping)

### Long Term:

- [ ] Support for stratified bootstrap (by dataset)
- [ ] Support for blocking (by document difficulty)
- [ ] Hierarchical testing (test groups, then within groups)

## References

- Efron & Tibshirani (1993). _An Introduction to the Bootstrap_
- Berg-Kirkpatrick et al. (2012). "An Empirical Investigation of Statistical Significance in NLP"
- Dror et al. (2018). "The Hitchhiker's Guide to Testing Statistical Significance in NLP"
