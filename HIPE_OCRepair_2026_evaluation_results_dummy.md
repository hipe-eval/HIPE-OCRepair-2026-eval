# HIPE-OCRepair 2026 – Evaluation Results

- **Date**: 2026-03-26
- **Scorer**: hipe-ocrepair-scorer v0.9.0
- **Benchmark**: hipe-ocrepair-bench v0.9

System names follow the pattern:  
`<teamname>_hipe-ocrepair-bench_<version>_<dataset>_<split>_<language>_run<N>`

**Primary metric**: overall micro-cMER — weighted mean of per-test-set cMER micro (`cmer_micro`) — **lower is better**  
**Secondary metric**: overall macro-preference — weighted mean of per-test-set preference score (`pref_score_cmer_macro`) — **higher is better**

**Weighting**: each non-DTA test set has weight 1; each of the three DTA test sets (dta19-l0, dta19-l1, dta19-l2) has weight 1/3, so that together they contribute as one dataset to the overall score. These are design weights, not corpus-size weights.

## Team key

| Team ID | Affiliation |
|---------|-------------|
| random | Test Institute, City, Country |
| same | Example University, City, Country |

## Overall rankings

Scores are computed separately for each official test set. Overall benchmark scores are weighted averages over test sets, using the design weights described above.

¹ CIs for overall scores are approximate (weighted average of per-test-set bootstrap CIs).

### Overall — test split

| Rank | System | Overall cMER ↓ | 95% CI¹ | Overall Pref. ↑ | 95% CI¹ | Test sets |
|------|--------|----------------|---------|-----------------|---------|----------|
| 1 | same_hipe-ocrepair-bench_v0.9_run1 | 0.0268 | [0.0146, 0.0431] | 0.0000 | [0.0000, 0.0000] | 4/4 |
| 2 | random_hipe-ocrepair-bench_v0.9_run1 | 0.6435 | [0.6191, 0.6673] | -1.0000 | [-1.0000, -1.0000] | 4/4 |

See [ranking-overall-test-weighted.tsv](results-dummy/system-rankings/ranking-overall-test-weighted.tsv) for full details.

## Per-language rankings

Per-language rankings are computed in the same way as the overall ranking, but restricted to the official test sets of the respective language.

¹ CIs for language scores are approximate (weighted average of per-test-set bootstrap CIs).

### Language: de (German) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref. ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|------------------|---------|----------|
| 1 | same_hipe-ocrepair-bench_v0.9_run1 | 0.0282 | [0.0059, 0.0625] | 0.0000 | [0.0000, 0.0000] | 1/1 |
| 2 | random_hipe-ocrepair-bench_v0.9_run1 | 0.5829 | [0.5037, 0.6610] | -1.0000 | [-1.0000, -1.0000] | 1/1 |

See [ranking-language-de-test-weighted.tsv](results-dummy/system-rankings/ranking-language-de-test-weighted.tsv) for full details.

### Language: en (English) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref. ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|------------------|---------|----------|
| 1 | same_hipe-ocrepair-bench_v0.9_run1 | 0.0343 | [0.0233, 0.0457] | 0.0000 | [0.0000, 0.0000] | 2/2 |
| 2 | random_hipe-ocrepair-bench_v0.9_run1 | 0.6646 | [0.6583, 0.6704] | -1.0000 | [-1.0000, -1.0000] | 2/2 |

See [ranking-language-en-test-weighted.tsv](results-dummy/system-rankings/ranking-language-en-test-weighted.tsv) for full details.

### Language: fr (French) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref. ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|------------------|---------|----------|
| 1 | same_hipe-ocrepair-bench_v0.9_run1 | 0.0104 | [0.0058, 0.0185] | 0.0000 | [0.0000, 0.0000] | 1/1 |
| 2 | random_hipe-ocrepair-bench_v0.9_run1 | 0.6618 | [0.6563, 0.6672] | -1.0000 | [-1.0000, -1.0000] | 1/1 |

See [ranking-language-fr-test-weighted.tsv](results-dummy/system-rankings/ranking-language-fr-test-weighted.tsv) for full details.

## Results by dataset

### Dataset: icdar2017_v1.1

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref. score ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|---------------|--------|------------|------------|
| 1 | same_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.0343 | [0.0298, 0.0391] | 0.0000 | [0.0000, 0.0000] | 0.0418 | 0.1694 |
| 2 | random_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.6740 | [0.6720, 0.6760] | -1.0000 | [-1.0000, -1.0000] | 0.6703 | 0.9287 |

See [ranking-icdar2017_v1.1-test-en-cmer-micro.tsv](results-dummy/system-rankings/ranking-icdar2017_v1.1-test-en-cmer-micro.tsv) for full details.

### Dataset: impresso-nzz_v1.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref. score ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|---------------|--------|------------|------------|
| 1 | same_hipe-ocrepair-bench_v0.9_impresso-nzz_v1.1_test_de_run1 | 0.0396 | [0.0318, 0.0499] | 0.0000 | [0.0000, 0.0000] | 0.0892 | 0.2076 |
| 2 | random_hipe-ocrepair-bench_v0.9_impresso-nzz_v1.1_test_de_run1 | 0.6781 | [0.6741, 0.6825] | -0.9412 | [-1.0000, -0.8235] | 0.6853 | 0.9687 |

See [ranking-impresso-nzz_v1.1-test-de-cmer-micro.tsv](results-dummy/system-rankings/ranking-impresso-nzz_v1.1-test-de-cmer-micro.tsv) for full details.

### Dataset: impresso-snippets

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref. score ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|---------------|--------|------------|------------|
| 1 | same_hipe-ocrepair-bench_v0.9_impresso-snippets_test_de_run1 | 0.0282 | [0.0059, 0.0625] | 0.0000 | [0.0000, 0.0000] | 0.0273 | 0.1331 |
| 2 | random_hipe-ocrepair-bench_v0.9_impresso-snippets_test_de_run1 | 0.5829 | [0.5037, 0.6610] | -1.0000 | [-1.0000, -1.0000] | 0.5789 | 0.8263 |

See [ranking-impresso-snippets-test-de-cmer-micro.tsv](results-dummy/system-rankings/ranking-impresso-snippets-test-de-cmer-micro.tsv) for full details.

### Dataset: impresso-snippets_v1.0

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref. score ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|---------------|--------|------------|------------|
| 1 | same_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.0344 | [0.0168, 0.0522] | 0.0000 | [0.0000, 0.0000] | 0.0331 | 0.1146 |
| 2 | random_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.6553 | [0.6446, 0.6649] | -1.0000 | [-1.0000, -1.0000] | 0.6534 | 0.8914 |

See [ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv](results-dummy/system-rankings/ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref. score ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|---------------|--------|------------|------------|
| 1 | same_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.0104 | [0.0058, 0.0185] | 0.0000 | [0.0000, 0.0000] | 0.0117 | 0.0568 |
| 2 | random_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.6618 | [0.6563, 0.6672] | -1.0000 | [-1.0000, -1.0000] | 0.6616 | 0.8875 |

See [ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv](results-dummy/system-rankings/ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv) for full details.

### Dataset: overproof-combined_v1.0

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref. score ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|---------------|--------|------------|------------|
| 1 | same_hipe-ocrepair-bench_v0.9_overproof-combined_v1.0_test_en_run1 | 0.0655 | [0.0451, 0.0900] | 0.0000 | [0.0000, 0.0000] | 0.0668 | 0.1986 |
| 2 | random_hipe-ocrepair-bench_v0.9_overproof-combined_v1.0_test_en_run1 | 0.6711 | [0.6664, 0.6757] | -1.0000 | [-1.0000, -1.0000] | 0.6681 | 0.9284 |

See [ranking-overproof-combined_v1.0-test-en-cmer-micro.tsv](results-dummy/system-rankings/ranking-overproof-combined_v1.0-test-en-cmer-micro.tsv) for full details.
