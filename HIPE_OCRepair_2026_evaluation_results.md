# HIPE-OCRepair 2026 – Evaluation Results

- **Generated**: 2026-04-10 17:22:40
- **Scorer**: hipe-ocrepair-scorer v0.9.4
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
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0094 | [0.005, 0.017] | 0.8433 | [0.773, 0.902] | 8/8 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0116 | [0.007, 0.020] | 0.8260 | [0.748, 0.890] | 8/8 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0124 | [0.007, 0.021] | 0.8494 | [0.753, 0.928] | 8/8 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0177 | [0.011, 0.029] | 0.6138 | [0.493, 0.722] | 8/8 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0207 | [0.015, 0.030] | 0.3416 | [0.223, 0.456] | 8/8 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0255 | [0.020, 0.034] | -0.0017 | [-0.005, 0.000] | 8/8 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Overall cMER ↓ | 95% CI¹ | Overall Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0221 | [0.019, 0.026] | -0.0933 | [-0.203, 0.017] | 3/8 |
| — | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0261 | [0.016, 0.041] | 0.3537 | [0.207, 0.497] | 7/8 |

See [ranking-overall-test-weighted.tsv](results/system-rankings/ranking-overall-test-weighted.tsv) for full details.

## Per-language rankings

Per-language rankings are computed in the same way as the overall ranking, but restricted to the official test sets of the respective language.

¹ CIs for language scores are approximate (weighted average of per-test-set bootstrap CIs).

### Language: de (German) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0107 | [0.008, 0.013] | 0.6696 | [0.587, 0.745] | 4/4 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0116 | [0.009, 0.014] | 0.8479 | [0.760, 0.918] | 4/4 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0139 | [0.011, 0.017] | 0.6075 | [0.493, 0.705] | 4/4 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0216 | [0.019, 0.025] | 0.3750 | [0.259, 0.483] | 4/4 |
| 5 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0279 | [0.019, 0.039] | 0.2808 | [0.133, 0.422] | 4/4 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0293 | [0.027, 0.032] | 0.0000 | [0.000, 0.000] | 4/4 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0287 | [0.024, 0.033] | 0.0200 | [-0.090, 0.130] | 1/4 |
| — | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0352 | [0.027, 0.045] | -0.2390 | [-0.391, -0.083] | 3/4 |

See [ranking-language-de-test-weighted.tsv](results/system-rankings/ranking-language-de-test-weighted.tsv) for full details.

### Language: en (English) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0127 | [0.003, 0.032] | 0.9304 | [0.861, 0.985] | 2/2 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0135 | [0.004, 0.033] | 0.9204 | [0.851, 0.975] | 2/2 |
| 3 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0150 | [0.005, 0.034] | 0.8805 | [0.791, 0.955] | 2/2 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0163 | [0.006, 0.036] | 0.8753 | [0.786, 0.945] | 2/2 |
| 6 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0256 | [0.012, 0.050] | 0.6163 | [0.477, 0.751] | 2/2 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0258 | [0.014, 0.046] | 0.3147 | [0.200, 0.429] | 2/2 |
| 8 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0293 | [0.018, 0.049] | -0.0050 | [-0.015, 0.000] | 2/2 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0187 | [0.016, 0.022] | -0.1500 | [-0.260, -0.040] | 1/2 |

See [ranking-language-en-test-weighted.tsv](results/system-rankings/ranking-language-en-test-weighted.tsv) for full details.

### Language: fr (French) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0049 | [0.004, 0.006] | 0.9300 | [0.870, 0.975] | 2/2 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0073 | [0.005, 0.010] | 0.9500 | [0.900, 0.990] | 2/2 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0093 | [0.007, 0.012] | 0.8250 | [0.715, 0.920] | 2/2 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0102 | [0.008, 0.013] | 0.6800 | [0.555, 0.790] | 2/2 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0148 | [0.011, 0.019] | 0.3350 | [0.210, 0.455] | 2/2 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0178 | [0.015, 0.022] | 0.0000 | [0.000, 0.000] | 2/2 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0191 | [0.012, 0.028] | 0.5850 | [0.435, 0.725] | 2/2 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0190 | [0.016, 0.023] | -0.1500 | [-0.260, -0.040] | 1/2 |

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
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0204 | [0.004, 0.057] | 0.9307 | [0.852, 0.990] | 0.0160 | 0.0288 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run3 | 0.0219 | [0.005, 0.059] | 0.9208 | [0.842, 0.980] | 0.0181 | 0.0361 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run2 | 0.0251 | [0.007, 0.062] | 0.9406 | [0.871, 0.990] | 0.0215 | 0.0472 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0251 | [0.006, 0.062] | 0.8911 | [0.802, 0.960] | 0.0212 | 0.0399 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0328 | [0.013, 0.069] | 0.7327 | [0.604, 0.852] | 0.0302 | 0.0633 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0416 | [0.022, 0.078] | -0.0099 | [-0.030, 0.000] | 0.0396 | 0.1362 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0417 | [0.021, 0.079] | 0.0594 | [-0.050, 0.168] | 0.0467 | 0.1369 |

See [ranking-icdar2017_v1.1-test-en-cmer-micro.tsv](results/system-rankings/ranking-icdar2017_v1.1-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0053 | [0.004, 0.007] | 0.9800 | [0.940, 1.000] | 0.0052 | 0.0204 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run2 | 0.0094 | [0.008, 0.011] | 0.9000 | [0.800, 0.980] | 0.0095 | 0.0514 |
| 3 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0096 | [0.008, 0.012] | 0.9000 | [0.810, 0.970] | 0.0096 | 0.0319 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run3 | 0.0098 | [0.007, 0.013] | 0.9700 | [0.930, 1.000] | 0.0096 | 0.0523 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0148 | [0.010, 0.021] | 0.8100 | [0.690, 0.920] | 0.0146 | 0.0366 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0188 | [0.016, 0.022] | 0.0000 | [0.000, 0.000] | 0.0190 | 0.1079 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0205 | [0.016, 0.026] | -0.0300 | [-0.140, 0.080] | 0.0268 | 0.1115 |

See [ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv](results/system-rankings/ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv) for full details.

### Dataset: impresso-snippets_v1.0

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0058 | [0.004, 0.007] | 0.9600 | [0.920, 0.990] | 0.0067 | 0.0418 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run3 | 0.0096 | [0.007, 0.012] | 0.9400 | [0.870, 0.990] | 0.0108 | 0.0526 |
| 3 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0109 | [0.009, 0.013] | 0.7700 | [0.640, 0.890] | 0.0118 | 0.0438 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 | 0.0117 | [0.009, 0.015] | 0.9500 | [0.890, 0.990] | 0.0132 | 0.0537 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0161 | [0.013, 0.020] | 0.8000 | [0.680, 0.900] | 0.0185 | 0.0730 |
| 6 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 | 0.0287 | [0.024, 0.033] | 0.0200 | [-0.090, 0.130] | 0.0313 | 0.1679 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0296 | [0.025, 0.034] | 0.0000 | [0.000, 0.000] | 0.0319 | 0.1773 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0342 | [0.026, 0.044] | 0.1600 | [-0.030, 0.350] | 0.0388 | 0.0995 |

See [ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv) for full details.

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0049 | [0.003, 0.007] | 0.9300 | [0.870, 0.980] | 0.0048 | 0.0187 |
| 2 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0049 | [0.004, 0.006] | 0.8700 | [0.780, 0.950] | 0.0052 | 0.0150 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run3 | 0.0052 | [0.003, 0.007] | 0.9200 | [0.860, 0.970] | 0.0052 | 0.0134 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 | 0.0074 | [0.005, 0.010] | 0.8100 | [0.700, 0.900] | 0.0077 | 0.0205 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0099 | [0.008, 0.012] | 0.5700 | [0.450, 0.690] | 0.0102 | 0.0316 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0170 | [0.014, 0.020] | 0.0000 | [0.000, 0.000] | 0.0174 | 0.0723 |
| 7 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0183 | [0.010, 0.031] | 0.5000 | [0.350, 0.650] | 0.0190 | 0.0389 |
| 8 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 | 0.0187 | [0.016, 0.022] | -0.1500 | [-0.260, -0.040] | 0.0194 | 0.0812 |

See [ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0044 | [0.003, 0.006] | 0.8800 | [0.800, 0.950] | 0.0051 | 0.0249 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run3 | 0.0048 | [0.003, 0.007] | 0.9300 | [0.870, 0.980] | 0.0056 | 0.0216 |
| 3 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0091 | [0.006, 0.013] | 0.7000 | [0.560, 0.830] | 0.0106 | 0.0345 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 | 0.0092 | [0.007, 0.012] | 0.7500 | [0.630, 0.860] | 0.0103 | 0.0464 |
| 5 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0108 | [0.008, 0.014] | 0.4600 | [0.300, 0.610] | 0.0121 | 0.0626 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0169 | [0.013, 0.021] | 0.0000 | [0.000, 0.000] | 0.0182 | 0.1008 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 | 0.0190 | [0.016, 0.023] | -0.1500 | [-0.260, -0.040] | 0.0206 | 0.1065 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0233 | [0.014, 0.035] | 0.3600 | [0.180, 0.530] | 0.0258 | 0.0553 |

See [ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv) for full details.
