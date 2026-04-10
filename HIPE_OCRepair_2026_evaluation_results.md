# HIPE-OCRepair 2026 – Evaluation Results

- **Generated**: 2026-04-10 11:21:04
- **Scorer**: hipe-ocrepair-scorer v0.9.3
- **Benchmark**: hipe-ocrepair-bench v0.9

System names follow the pattern:  
`<teamname>_hipe-ocrepair-bench_<version>_<dataset>_<split>_<language>_run<N>`

For official submissions, `<split>` in system filenames is usually `masked-test`;
the unmatched DTA variant uses `masked-test-unmatched`, while matching
reference files in `data/reference/` use `test` or `test-unmatched`.

**Primary metric**: overall micro-cMER — weighted mean of per-test-set cMER micro (`cmer_micro`) — **lower is better**  
**Secondary metric**: overall macro-preference — weighted mean of per-test-set preference score (`pref_cmer_macro`) — **higher is better**

**Weighting**: each non-DTA test set has weight 1; each of the three DTA test sets (dta19-l0, dta19-l1, dta19-l2) has weight 1/3, so that together they contribute as one dataset to the overall score. These are design weights, not corpus-size weights.

## Team key

| Team ID | Affiliation |
|---------|-------------|
| Zakaria-ENSIAS | Zakaria-ENSIAS team |
| baseline-no-correction | Automatic Baseline that preserves text as is |
| blocr | blocr team |
| bnf-mistral | bnf-mistral team |
| l3i | l3i team |

## Submission overview

| Team | Dataset | Run | System |
|------|---------|-----|--------|
| baseline-no-correction | dta19-l0_v0.1_masked-test_de | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 |
| baseline-no-correction | dta19-l1_v0.1_masked-test_de | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 |
| baseline-no-correction | dta19-l2_v0.1_masked-test_de | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 |
| baseline-no-correction | icdar2017_v1.1_masked-test_en | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 |
| baseline-no-correction | icdar2017_v1.1_masked-test_fr | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 |
| baseline-no-correction | impresso-snippets_v1.0_masked-test_de | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 |
| baseline-no-correction | impresso-snippets_v1.0_masked-test_en | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 |
| baseline-no-correction | impresso-snippets_v1.0_masked-test_fr | 1 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 |
| blocr | dta19-l0_v0.1_masked-test_de | 1 | blocr_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 |
| blocr | dta19-l1_v0.1_masked-test_de | 1 | blocr_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 |
| blocr | dta19-l2_v0.1_masked-test_de | 1 | blocr_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 |
| blocr | icdar2017_v1.1_masked-test_en | 1 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 |
| blocr | icdar2017_v1.1_masked-test_fr | 1 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 |
| blocr | impresso-snippets_v1.0_masked-test_de | 1 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 |
| blocr | impresso-snippets_v1.0_masked-test_en | 1 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 |
| blocr | impresso-snippets_v1.0_masked-test_fr | 1 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 |
| bnf-mistral | dta19-l0_v0.1_masked-test_de | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 |
| bnf-mistral | dta19-l0_v0.1_masked-test_de | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run2 |
| bnf-mistral | dta19-l0_v0.1_masked-test_de | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run3 |
| bnf-mistral | dta19-l1_v0.1_masked-test_de | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 |
| bnf-mistral | dta19-l1_v0.1_masked-test_de | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run2 |
| bnf-mistral | dta19-l1_v0.1_masked-test_de | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run3 |
| bnf-mistral | dta19-l2_v0.1_masked-test_de | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 |
| bnf-mistral | dta19-l2_v0.1_masked-test_de | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run2 |
| bnf-mistral | dta19-l2_v0.1_masked-test_de | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run3 |
| bnf-mistral | icdar2017_v1.1_masked-test_en | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 |
| bnf-mistral | icdar2017_v1.1_masked-test_en | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run2 |
| bnf-mistral | icdar2017_v1.1_masked-test_en | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run3 |
| bnf-mistral | icdar2017_v1.1_masked-test_fr | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 |
| bnf-mistral | icdar2017_v1.1_masked-test_fr | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run2 |
| bnf-mistral | icdar2017_v1.1_masked-test_fr | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run3 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_de | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_de | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_de | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run3 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_en | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_en | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_en | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run3 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_fr | 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_fr | 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 |
| bnf-mistral | impresso-snippets_v1.0_masked-test_fr | 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run3 |
| l3i | dta19-l0_v0.1_masked-test_de | 1 | l3i_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 |
| l3i | dta19-l1_v0.1_masked-test_de | 1 | l3i_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 |
| l3i | dta19-l2_v0.1_masked-test_de | 1 | l3i_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 |
| l3i | icdar2017_v1.1_masked-test_en | 1 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 |
| l3i | icdar2017_v1.1_masked-test_fr | 1 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 |
| l3i | impresso-snippets_v1.0_masked-test_de | 1 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 |
| l3i | impresso-snippets_v1.0_masked-test_de | 2 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 |
| l3i | impresso-snippets_v1.0_masked-test_en | 1 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 |
| l3i | impresso-snippets_v1.0_masked-test_en | 2 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 |
| l3i | impresso-snippets_v1.0_masked-test_fr | 1 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 |
| l3i | impresso-snippets_v1.0_masked-test_fr | 2 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 |
| Zakaria-ENSIAS | dta19-l0_v0.1_masked-test_de | 1 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 |
| Zakaria-ENSIAS | dta19-l1_v0.1_masked-test_de | 1 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 |
| Zakaria-ENSIAS | icdar2017_v1.1_masked-test_en | 1 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 |
| Zakaria-ENSIAS | icdar2017_v1.1_masked-test_fr | 1 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 |
| Zakaria-ENSIAS | impresso-snippets_v1.0_masked-test_de | 1 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 |
| Zakaria-ENSIAS | impresso-snippets_v1.0_masked-test_en | 1 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 |
| Zakaria-ENSIAS | impresso-snippets_v1.0_masked-test_fr | 1 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 |

## Submission counts by team and dataset

_Number of runs submitted per team for each dataset._

| Dataset | baseline-no-correction | blocr | bnf-mistral | l3i | Zakaria-ENSIAS |
|---------|-----|-----|-----|-----|-----|
| dta19-l0_v0.1_masked-test_de | 1 | 1 | 3 | 1 | 1 |
| dta19-l1_v0.1_masked-test_de | 1 | 1 | 3 | 1 | 1 |
| dta19-l2_v0.1_masked-test_de | 1 | 1 | 3 | 1 | 0 |
| icdar2017_v1.1_masked-test_en | 1 | 1 | 3 | 1 | 1 |
| icdar2017_v1.1_masked-test_fr | 1 | 1 | 3 | 1 | 1 |
| impresso-snippets_v1.0_masked-test_de | 1 | 1 | 3 | 2 | 1 |
| impresso-snippets_v1.0_masked-test_en | 1 | 1 | 3 | 2 | 1 |
| impresso-snippets_v1.0_masked-test_fr | 1 | 1 | 3 | 2 | 1 |

## Overall rankings

Scores are computed separately for each official test set. Overall benchmark scores are weighted averages over test sets, using the design weights described above.

¹ CIs for overall scores are approximate (weighted average of per-test-set bootstrap CIs).

### Overall — test split

| Rank | System | Overall cMER ↓ | 95% CI¹ | Overall Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0074 | [0.006, 0.009] | 0.8349 | [0.761, 0.897] | 8/8 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0096 | [0.007, 0.012] | 0.8092 | [0.723, 0.882] | 8/8 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0103 | [0.008, 0.013] | 0.8276 | [0.727, 0.914] | 8/8 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0157 | [0.011, 0.021] | 0.6053 | [0.482, 0.716] | 8/8 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0186 | [0.015, 0.023] | 0.3333 | [0.213, 0.449] | 8/8 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0231 | [0.020, 0.027] | 0.0000 | [0.000, 0.000] | 8/8 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Overall cMER ↓ | 95% CI¹ | Overall Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0228 | [0.019, 0.026] | -0.1067 | [-0.217, 0.000] | 3/8 |
| — | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0239 | [0.017, 0.033] | 0.3356 | [0.183, 0.480] | 7/8 |

See [ranking-overall-test-weighted.tsv](results/system-rankings/ranking-overall-test-weighted.tsv) for full details.

## Per-language rankings

Per-language rankings are computed in the same way as the overall ranking, but restricted to the official test sets of the respective language.

¹ CIs for language scores are approximate (weighted average of per-test-set bootstrap CIs).

### Language: de (German) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0114 | [0.009, 0.014] | 0.6696 | [0.587, 0.745] | 4/4 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0122 | [0.010, 0.015] | 0.8279 | [0.730, 0.913] | 4/4 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0145 | [0.011, 0.018] | 0.5875 | [0.463, 0.695] | 4/4 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0222 | [0.019, 0.025] | 0.3550 | [0.239, 0.468] | 4/4 |
| 5 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0285 | [0.020, 0.040] | 0.2708 | [0.122, 0.412] | 4/4 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0296 | [0.027, 0.032] | 0.0000 | [0.000, 0.000] | 4/4 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0296 | [0.025, 0.034] | 0.0200 | [-0.090, 0.130] | 1/4 |
| — | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0357 | [0.028, 0.046] | -0.2390 | [-0.391, -0.083] | 3/4 |

See [ranking-language-de-test-weighted.tsv](results/system-rankings/ranking-language-de-test-weighted.tsv) for full details.

### Language: en (English) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0054 | [0.004, 0.007] | 0.9150 | [0.840, 0.975] | 2/2 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0063 | [0.005, 0.008] | 0.9000 | [0.820, 0.965] | 2/2 |
| 3 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0077 | [0.005, 0.011] | 0.8600 | [0.765, 0.940] | 2/2 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0088 | [0.006, 0.012] | 0.8500 | [0.760, 0.925] | 2/2 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0181 | [0.012, 0.027] | 0.5750 | [0.420, 0.715] | 2/2 |
| 6 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0182 | [0.014, 0.024] | 0.3200 | [0.200, 0.435] | 2/2 |
| 8 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0215 | [0.018, 0.026] | 0.0000 | [0.000, 0.000] | 2/2 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0186 | [0.016, 0.021] | -0.1700 | [-0.280, -0.060] | 1/2 |

See [ranking-language-en-test-weighted.tsv](results/system-rankings/ranking-language-en-test-weighted.tsv) for full details.

### Language: fr (French) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0055 | [0.004, 0.007] | 0.9200 | [0.855, 0.970] | 2/2 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0080 | [0.006, 0.011] | 0.9400 | [0.885, 0.985] | 2/2 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0099 | [0.008, 0.012] | 0.8050 | [0.690, 0.905] | 2/2 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0109 | [0.009, 0.013] | 0.6850 | [0.560, 0.795] | 2/2 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0155 | [0.012, 0.020] | 0.3250 | [0.200, 0.445] | 2/2 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0183 | [0.015, 0.022] | 0.0000 | [0.000, 0.000] | 2/2 |
| 7 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0197 | [0.013, 0.029] | 0.5750 | [0.425, 0.715] | 2/2 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0201 | [0.017, 0.024] | -0.1700 | [-0.280, -0.070] | 1/2 |

See [ranking-language-fr-test-weighted.tsv](results/system-rankings/ranking-language-fr-test-weighted.tsv) for full details.

## Results by dataset

### Dataset: dta19-l0_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run2 | 0.0026 | [0.002, 0.003] | 0.4250 | [0.263, 0.575] | 0.0025 | 0.0172 |
| 2 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0030 | [0.003, 0.004] | 0.0000 | [0.000, 0.000] | 0.0031 | 0.0199 |
| 3 | l3i_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0050 | [0.004, 0.006] | -0.3250 | [-0.425, -0.225] | 0.0062 | 0.0348 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run3 | 0.0096 | [0.007, 0.013] | -0.2125 | [-0.375, -0.050] | 0.0105 | 0.0654 |
| 5 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0105 | [0.008, 0.014] | -0.3125 | [-0.487, -0.125] | 0.0112 | 0.0698 |
| 6 | blocr_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0237 | [0.019, 0.029] | -0.8625 | [-0.950, -0.762] | 0.0244 | 0.1318 |
| 7 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0350 | [0.024, 0.052] | -0.9250 | [-0.988, -0.850] | 0.0274 | 0.1416 |

See [ranking-dta19-l0_v0.1-test-de-cmer-micro.tsv](results/system-rankings/ranking-dta19-l0_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: dta19-l1_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run2 | 0.0084 | [0.006, 0.011] | 0.8625 | [0.750, 0.963] | 0.0097 | 0.0558 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0138 | [0.011, 0.017] | 0.4500 | [0.250, 0.625] | 0.0152 | 0.0969 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run3 | 0.0172 | [0.014, 0.021] | 0.1375 | [-0.075, 0.338] | 0.0187 | 0.1144 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0212 | [0.019, 0.023] | -0.0250 | [-0.150, 0.100] | 0.0238 | 0.1355 |
| 5 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0227 | [0.022, 0.024] | 0.0000 | [0.000, 0.000] | 0.0223 | 0.1402 |
| 6 | blocr_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0275 | [0.024, 0.031] | -0.3125 | [-0.525, -0.100] | 0.0299 | 0.1482 |
| 7 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0384 | [0.034, 0.043] | -0.7500 | [-0.875, -0.613] | 0.0399 | 0.1831 |

See [ranking-dta19-l1_v0.1-test-de-cmer-micro.tsv](results/system-rankings/ranking-dta19-l1_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: dta19-l2_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0225 | [0.019, 0.027] | 1.0000 | [1.000, 1.000] | 0.0255 | 0.1434 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run2 | 0.0233 | [0.020, 0.027] | 0.9500 | [0.875, 1.000] | 0.0262 | 0.1262 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run3 | 0.0279 | [0.024, 0.033] | 0.9000 | [0.800, 0.975] | 0.0318 | 0.1614 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0549 | [0.051, 0.059] | 0.2000 | [0.087, 0.325] | 0.0596 | 0.2828 |
| 5 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0611 | [0.060, 0.062] | 0.0000 | [0.000, 0.000] | 0.0616 | 0.3086 |
| 6 | blocr_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0833 | [0.047, 0.133] | 0.5500 | [0.350, 0.725] | 0.0670 | 0.2195 |

See [ranking-dta19-l2_v0.1-test-de-cmer-micro.tsv](results/system-rankings/ranking-dta19-l2_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: icdar2017_v1.1

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0051 | [0.004, 0.007] | 0.9500 | [0.880, 1.000] | 0.0073 | 0.0257 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run3 | 0.0065 | [0.005, 0.008] | 0.9400 | [0.870, 0.990] | 0.0092 | 0.0314 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run2 | 0.0096 | [0.007, 0.013] | 0.9600 | [0.910, 1.000] | 0.0124 | 0.0418 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0097 | [0.006, 0.015] | 0.9100 | [0.830, 0.980] | 0.0122 | 0.0343 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0175 | [0.013, 0.023] | 0.7300 | [0.590, 0.850] | 0.0213 | 0.0582 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0263 | [0.021, 0.032] | 0.0000 | [0.000, 0.000] | 0.0305 | 0.1302 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0264 | [0.020, 0.035] | 0.0700 | [-0.050, 0.180] | 0.0377 | 0.1310 |

See [ranking-icdar2017_v1.1-test-en-cmer-micro.tsv](results/system-rankings/ranking-icdar2017_v1.1-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0053 | [0.004, 0.007] | 0.9800 | [0.940, 1.000] | 0.0052 | 0.0205 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run2 | 0.0094 | [0.008, 0.011] | 0.9000 | [0.800, 0.980] | 0.0095 | 0.0514 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run3 | 0.0098 | [0.007, 0.013] | 0.9700 | [0.930, 1.000] | 0.0096 | 0.0523 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0098 | [0.008, 0.012] | 0.9000 | [0.810, 0.970] | 0.0098 | 0.0324 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0150 | [0.010, 0.021] | 0.8100 | [0.690, 0.920] | 0.0148 | 0.0370 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0188 | [0.016, 0.022] | 0.0000 | [0.000, 0.000] | 0.0190 | 0.1079 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0205 | [0.016, 0.026] | -0.0300 | [-0.140, 0.080] | 0.0268 | 0.1115 |

See [ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv](results/system-rankings/ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv) for full details.

### Dataset: impresso-snippets_v1.0

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0072 | [0.005, 0.009] | 0.9600 | [0.920, 0.990] | 0.0080 | 0.0506 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run3 | 0.0108 | [0.008, 0.014] | 0.9000 | [0.810, 0.970] | 0.0119 | 0.0594 |
| 3 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0122 | [0.010, 0.015] | 0.7500 | [0.620, 0.870] | 0.0131 | 0.0521 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 | 0.0129 | [0.010, 0.016] | 0.9100 | [0.830, 0.980] | 0.0144 | 0.0607 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0173 | [0.014, 0.021] | 0.7600 | [0.640, 0.870] | 0.0197 | 0.0794 |
| 6 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 | 0.0296 | [0.025, 0.034] | 0.0200 | [-0.090, 0.130] | 0.0321 | 0.1725 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0303 | [0.026, 0.035] | 0.0000 | [0.000, 0.000] | 0.0325 | 0.1816 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0351 | [0.027, 0.045] | 0.1600 | [-0.030, 0.350] | 0.0396 | 0.1056 |

See [ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv) for full details.

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0056 | [0.004, 0.007] | 0.8800 | [0.800, 0.950] | 0.0056 | 0.0233 |
| 2 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0056 | [0.004, 0.007] | 0.8100 | [0.700, 0.900] | 0.0058 | 0.0190 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run3 | 0.0060 | [0.004, 0.008] | 0.8600 | [0.770, 0.940] | 0.0060 | 0.0180 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 | 0.0080 | [0.006, 0.010] | 0.7400 | [0.610, 0.850] | 0.0084 | 0.0242 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0101 | [0.008, 0.013] | 0.5700 | [0.450, 0.690] | 0.0104 | 0.0325 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0166 | [0.014, 0.019] | 0.0000 | [0.000, 0.000] | 0.0169 | 0.0699 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 | 0.0186 | [0.016, 0.021] | -0.1700 | [-0.280, -0.060] | 0.0192 | 0.0801 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0188 | [0.011, 0.031] | 0.4200 | [0.250, 0.580] | 0.0194 | 0.0415 |

See [ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0058 | [0.004, 0.008] | 0.8600 | [0.770, 0.940] | 0.0067 | 0.0318 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run3 | 0.0062 | [0.004, 0.008] | 0.9100 | [0.840, 0.970] | 0.0072 | 0.0290 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 | 0.0104 | [0.008, 0.013] | 0.7100 | [0.580, 0.830] | 0.0117 | 0.0529 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0104 | [0.007, 0.014] | 0.6800 | [0.540, 0.810] | 0.0122 | 0.0417 |
| 5 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0121 | [0.009, 0.015] | 0.4700 | [0.310, 0.620] | 0.0137 | 0.0688 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0179 | [0.014, 0.022] | 0.0000 | [0.000, 0.000] | 0.0194 | 0.1048 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 | 0.0201 | [0.017, 0.024] | -0.1700 | [-0.280, -0.070] | 0.0219 | 0.1115 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0244 | [0.015, 0.036] | 0.3400 | [0.160, 0.510] | 0.0270 | 0.0606 |

See [ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv) for full details.
