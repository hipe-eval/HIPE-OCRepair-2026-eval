# HIPE-OCRepair 2026 – Evaluation Results

- **Generated**: 2026-04-10 08:40:49
- **Scorer**: hipe-ocrepair-scorer v0.9.0
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

## Overall rankings

Scores are computed separately for each official test set. Overall benchmark scores are weighted averages over test sets, using the design weights described above.

¹ CIs for overall scores are approximate (weighted average of per-test-set bootstrap CIs).

### Overall — test split

| Rank | System | Overall cMER ↓ | 95% CI¹ | Overall Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0075 | [0.0058, 0.0095] | 0.8342 | [0.7562, 0.8964] | 8/8 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0096 | [0.0073, 0.0123] | 0.8092 | [0.7221, 0.8832] | 8/8 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0103 | [0.0080, 0.0130] | 0.8276 | [0.7265, 0.9127] | 8/8 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0160 | [0.0115, 0.0217] | 0.5914 | [0.4676, 0.7068] | 8/8 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0188 | [0.0152, 0.0231] | 0.3300 | [0.2063, 0.4471] | 8/8 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0231 | [0.0198, 0.0268] | 0.0000 | [0.0000, 0.0000] | 8/8 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Overall cMER ↓ | 95% CI¹ | Overall Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0228 | [0.0194, 0.0267] | -0.1067 | [-0.2167, 0.0033] | 3/8 |
| — | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0241 | [0.0170, 0.0336] | 0.3271 | [0.1799, 0.4704] | 7/8 |

See [ranking-overall-test-weighted.tsv](results/system-rankings/ranking-overall-test-weighted.tsv) for full details.

## Per-language rankings

Per-language rankings are computed in the same way as the overall ranking, but restricted to the official test sets of the respective language.

¹ CIs for language scores are approximate (weighted average of per-test-set bootstrap CIs).

### Language: de (German) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0116 | [0.0091, 0.0143] | 0.6675 | [0.5787, 0.7492] | 4/4 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0123 | [0.0098, 0.0152] | 0.8279 | [0.7296, 0.9129] | 4/4 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0147 | [0.0115, 0.0182] | 0.5875 | [0.4613, 0.6996] | 4/4 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0226 | [0.0196, 0.0258] | 0.3450 | [0.2238, 0.4612] | 4/4 |
| 5 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0294 | [0.0206, 0.0408] | 0.2292 | [0.0779, 0.3804] | 4/4 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0296 | [0.0270, 0.0324] | 0.0000 | [0.0000, 0.0000] | 4/4 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0298 | [0.0256, 0.0345] | 0.0200 | [-0.0900, 0.1300] | 1/4 |
| — | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0366 | [0.0286, 0.0469] | -0.2680 | [-0.4145, -0.1165] | 3/4 |

See [ranking-language-de-test-weighted.tsv](results/system-rankings/ranking-language-de-test-weighted.tsv) for full details.

### Language: en (English) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0054 | [0.0040, 0.0070] | 0.9150 | [0.8350, 0.9750] | 2/2 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0063 | [0.0046, 0.0081] | 0.9000 | [0.8200, 0.9650] | 2/2 |
| 3 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0077 | [0.0052, 0.0109] | 0.8600 | [0.7650, 0.9400] | 2/2 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0088 | [0.0064, 0.0117] | 0.8500 | [0.7600, 0.9250] | 2/2 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0181 | [0.0119, 0.0270] | 0.5750 | [0.4250, 0.7150] | 2/2 |
| 6 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0182 | [0.0142, 0.0236] | 0.3200 | [0.2000, 0.4350] | 2/2 |
| 8 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0215 | [0.0175, 0.0258] | 0.0000 | [0.0000, 0.0000] | 2/2 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0186 | [0.0159, 0.0215] | -0.1700 | [-0.2800, -0.0600] | 1/2 |

See [ranking-language-en-test-weighted.tsv](results/system-rankings/ranking-language-en-test-weighted.tsv) for full details.

### Language: fr (French) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_run1 | 0.0055 | [0.0041, 0.0073] | 0.9200 | [0.8550, 0.9650] | 2/2 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_run3 | 0.0080 | [0.0059, 0.0106] | 0.9400 | [0.8850, 0.9850] | 2/2 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_run2 | 0.0099 | [0.0078, 0.0123] | 0.8050 | [0.6900, 0.9001] | 2/2 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_run1 | 0.0109 | [0.0086, 0.0135] | 0.6850 | [0.5600, 0.8000] | 2/2 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_run1 | 0.0155 | [0.0118, 0.0200] | 0.3250 | [0.1950, 0.4450] | 2/2 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0183 | [0.0149, 0.0221] | 0.0000 | [0.0000, 0.0000] | 2/2 |
| 7 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_run1 | 0.0197 | [0.0126, 0.0292] | 0.5750 | [0.4300, 0.7150] | 2/2 |

#### Systems with incomplete test set coverage

_Systems that have not processed all test sets are shown separately and not included in the official ranking._

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| — | l3i_hipe-ocrepair-bench_v0.9_run2 | 0.0201 | [0.0167, 0.0240] | -0.1700 | [-0.2800, -0.0600] | 1/2 |

See [ranking-language-fr-test-weighted.tsv](results/system-rankings/ranking-language-fr-test-weighted.tsv) for full details.

## Results by dataset

### Dataset: dta19-l0_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run2 | 0.0026 | [0.0021, 0.0032] | 0.4250 | [0.2625, 0.5750] | 0.0025 | 0.0172 |
| 2 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0030 | [0.0026, 0.0035] | 0.0000 | [0.0000, 0.0000] | 0.0031 | 0.0199 |
| 3 | l3i_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0050 | [0.0042, 0.0060] | -0.3250 | [-0.4250, -0.2250] | 0.0062 | 0.0348 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run3 | 0.0096 | [0.0069, 0.0124] | -0.2125 | [-0.3750, -0.0375] | 0.0105 | 0.0654 |
| 5 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0105 | [0.0078, 0.0136] | -0.3125 | [-0.5000, -0.1250] | 0.0112 | 0.0698 |
| 6 | blocr_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0245 | [0.0196, 0.0294] | -0.8625 | [-0.9500, -0.7625] | 0.0252 | 0.1335 |
| 7 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_masked-test_de_run1 | 0.0363 | [0.0253, 0.0535] | -0.9500 | [-0.9875, -0.9000] | 0.0288 | 0.1444 |

See [ranking-dta19-l0_v0.1-test-de-cmer-micro.tsv](results/system-rankings/ranking-dta19-l0_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: dta19-l1_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run2 | 0.0085 | [0.0064, 0.0114] | 0.8625 | [0.7500, 0.9625] | 0.0097 | 0.0559 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0139 | [0.0108, 0.0172] | 0.4500 | [0.2500, 0.6500] | 0.0153 | 0.0971 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run3 | 0.0174 | [0.0138, 0.0213] | 0.1375 | [-0.0875, 0.3500] | 0.0189 | 0.1145 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0212 | [0.0188, 0.0232] | -0.0250 | [-0.1500, 0.1000] | 0.0238 | 0.1355 |
| 5 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0227 | [0.0217, 0.0235] | 0.0000 | [0.0000, 0.0000] | 0.0223 | 0.1402 |
| 6 | blocr_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0289 | [0.0251, 0.0329] | -0.3375 | [-0.5375, -0.1250] | 0.0310 | 0.1508 |
| 7 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_masked-test_de_run1 | 0.0397 | [0.0353, 0.0442] | -0.7500 | [-0.8750, -0.6125] | 0.0412 | 0.1853 |

See [ranking-dta19-l1_v0.1-test-de-cmer-micro.tsv](results/system-rankings/ranking-dta19-l1_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: dta19-l2_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0228 | [0.0190, 0.0269] | 0.9875 | [0.9625, 1.0000] | 0.0259 | 0.1445 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run2 | 0.0234 | [0.0201, 0.0272] | 0.9500 | [0.8750, 1.0000] | 0.0264 | 0.1264 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run3 | 0.0282 | [0.0237, 0.0330] | 0.9000 | [0.8000, 0.9750] | 0.0322 | 0.1622 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0549 | [0.0506, 0.0587] | 0.2000 | [0.0875, 0.3125] | 0.0596 | 0.2828 |
| 5 | baseline-no-correction_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0611 | [0.0602, 0.0621] | 0.0000 | [0.0000, 0.0000] | 0.0616 | 0.3086 |
| 6 | blocr_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_masked-test_de_run1 | 0.0844 | [0.0479, 0.1345] | 0.4750 | [0.2750, 0.6500] | 0.0680 | 0.2219 |

See [ranking-dta19-l2_v0.1-test-de-cmer-micro.tsv](results/system-rankings/ranking-dta19-l2_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: icdar2017_v1.1

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0051 | [0.0040, 0.0066] | 0.9500 | [0.8800, 1.0000] | 0.0073 | 0.0257 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run3 | 0.0065 | [0.0050, 0.0081] | 0.9400 | [0.8700, 0.9900] | 0.0092 | 0.0314 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run2 | 0.0096 | [0.0069, 0.0129] | 0.9600 | [0.9100, 1.0000] | 0.0124 | 0.0418 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0097 | [0.0063, 0.0145] | 0.9100 | [0.8300, 0.9800] | 0.0122 | 0.0343 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0175 | [0.0132, 0.0226] | 0.7300 | [0.6000, 0.8500] | 0.0213 | 0.0582 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0263 | [0.0212, 0.0321] | 0.0000 | [0.0000, 0.0000] | 0.0305 | 0.1302 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_en_run1 | 0.0264 | [0.0204, 0.0345] | 0.0700 | [-0.0400, 0.1800] | 0.0377 | 0.1310 |

See [ranking-icdar2017_v1.1-test-en-cmer-micro.tsv](results/system-rankings/ranking-icdar2017_v1.1-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0053 | [0.0041, 0.0066] | 0.9800 | [0.9400, 1.0000] | 0.0052 | 0.0205 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run2 | 0.0094 | [0.0079, 0.0111] | 0.9000 | [0.8000, 0.9800] | 0.0095 | 0.0514 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run3 | 0.0098 | [0.0074, 0.0129] | 0.9700 | [0.9300, 1.0000] | 0.0096 | 0.0523 |
| 4 | blocr_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0098 | [0.0077, 0.0120] | 0.9000 | [0.8100, 0.9700] | 0.0098 | 0.0324 |
| 5 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0150 | [0.0103, 0.0212] | 0.8100 | [0.6900, 0.9200] | 0.0148 | 0.0370 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0188 | [0.0156, 0.0224] | 0.0000 | [0.0000, 0.0000] | 0.0190 | 0.1079 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_masked-test_fr_run1 | 0.0205 | [0.0163, 0.0257] | -0.0300 | [-0.1400, 0.0800] | 0.0268 | 0.1115 |

See [ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv](results/system-rankings/ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv) for full details.

### Dataset: impresso-snippets_v1.0

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0074 | [0.0057, 0.0094] | 0.9600 | [0.9200, 0.9900] | 0.0083 | 0.0517 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run3 | 0.0110 | [0.0083, 0.0141] | 0.9000 | [0.8100, 0.9700] | 0.0121 | 0.0600 |
| 3 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0129 | [0.0103, 0.0160] | 0.7000 | [0.5600, 0.8400] | 0.0137 | 0.0545 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 | 0.0131 | [0.0100, 0.0164] | 0.9100 | [0.8300, 0.9800] | 0.0146 | 0.0616 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0182 | [0.0146, 0.0224] | 0.7400 | [0.6100, 0.8600] | 0.0204 | 0.0817 |
| 6 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run2 | 0.0298 | [0.0256, 0.0345] | 0.0200 | [-0.0900, 0.1300] | 0.0322 | 0.1737 |
| 7 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0303 | [0.0258, 0.0352] | 0.0000 | [0.0000, 0.0000] | 0.0325 | 0.1823 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_de_run1 | 0.0356 | [0.0274, 0.0456] | 0.1200 | [-0.0700, 0.3100] | 0.0401 | 0.1074 |

See [ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv) for full details.

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0056 | [0.0041, 0.0074] | 0.8800 | [0.7900, 0.9500] | 0.0056 | 0.0233 |
| 2 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0056 | [0.0041, 0.0072] | 0.8100 | [0.7000, 0.9000] | 0.0058 | 0.0190 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run3 | 0.0060 | [0.0041, 0.0081] | 0.8600 | [0.7700, 0.9400] | 0.0060 | 0.0180 |
| 4 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 | 0.0080 | [0.0059, 0.0104] | 0.7400 | [0.6100, 0.8500] | 0.0084 | 0.0242 |
| 5 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0101 | [0.0079, 0.0126] | 0.5700 | [0.4400, 0.6900] | 0.0104 | 0.0325 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0166 | [0.0138, 0.0196] | 0.0000 | [0.0000, 0.0000] | 0.0169 | 0.0699 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run2 | 0.0186 | [0.0159, 0.0215] | -0.1700 | [-0.2800, -0.0600] | 0.0192 | 0.0801 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_en_run1 | 0.0188 | [0.0107, 0.0313] | 0.4200 | [0.2500, 0.5800] | 0.0194 | 0.0415 |

See [ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0058 | [0.0041, 0.0079] | 0.8600 | [0.7700, 0.9300] | 0.0067 | 0.0318 |
| 2 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run3 | 0.0062 | [0.0043, 0.0083] | 0.9100 | [0.8400, 0.9700] | 0.0072 | 0.0290 |
| 3 | bnf-mistral_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 | 0.0104 | [0.0077, 0.0135] | 0.7100 | [0.5800, 0.8202] | 0.0117 | 0.0529 |
| 4 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0104 | [0.0072, 0.0143] | 0.6800 | [0.5300, 0.8100] | 0.0122 | 0.0417 |
| 5 | blocr_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0121 | [0.0096, 0.0151] | 0.4700 | [0.3100, 0.6300] | 0.0137 | 0.0688 |
| 6 | baseline-no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0179 | [0.0143, 0.0219] | 0.0000 | [0.0000, 0.0000] | 0.0194 | 0.1048 |
| 7 | l3i_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run2 | 0.0201 | [0.0167, 0.0240] | -0.1700 | [-0.2800, -0.0600] | 0.0219 | 0.1115 |
| 8 | Zakaria-ENSIAS_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_masked-test_fr_run1 | 0.0244 | [0.0148, 0.0372] | 0.3400 | [0.1700, 0.5100] | 0.0270 | 0.0606 |

See [ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv](results/system-rankings/ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv) for full details.
