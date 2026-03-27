# HIPE-OCRepair 2026 – Evaluation Results

- **Date**: 2026-03-27
- **Scorer**: hipe-ocrepair-scorer v0.9.0
- **Benchmark**: hipe-ocrepair-bench v0.9

System names follow the pattern:  
`<teamname>_hipe-ocrepair-bench_<version>_<dataset>_<split>_<language>_run<N>`

**Primary metric**: overall micro-cMER — weighted mean of per-test-set cMER micro (`cmer_micro`) — **lower is better**  
**Secondary metric**: overall macro-preference — weighted mean of per-test-set preference score (`pref_cmer_macro`) — **higher is better**

**Weighting**: each non-DTA test set has weight 1; each of the three DTA test sets (dta19-l0, dta19-l1, dta19-l2) has weight 1/3, so that together they contribute as one dataset to the overall score. These are design weights, not corpus-size weights.

## Team key

| Team ID | Affiliation |
|---------|-------------|
| char-swaps-p05 | Swap 5% char pairs Institute, City, Country |
| char-swaps-p10 | Swap 10% char pairs Institute, City, Country |
| no-correction | Example University, City, Country |
| perfect | Test Institute, City, Country |
| word-swaps-p05 | Swap 5% word pairs Institute, City, Country |
| word-swaps-p10 | Swap 10% word pairs Institute, City, Country |

## Overall rankings

Scores are computed separately for each official test set. Overall benchmark scores are weighted averages over test sets, using the design weights described above.

¹ CIs for overall scores are approximate (weighted average of per-test-set bootstrap CIs).

### Overall — test split

| Rank | System | Overall cMER ↓ | 95% CI¹ | Overall Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|----------------|---------|----------------------|---------|----------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_run1 | 0.0000 | [0.0000, 0.0000] | 0.9760 | [0.9370, 0.9975] | 8/8 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run3 | 0.0111 | [0.0087, 0.0142] | 0.2798 | [-0.1354, 0.6756] | 8/8 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run2 | 0.0113 | [0.0087, 0.0145] | 0.2516 | [-0.1303, 0.6296] | 8/8 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run1 | 0.0115 | [0.0095, 0.0142] | 0.1846 | [-0.2143, 0.6141] | 8/8 |
| 5 | no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0265 | [0.0177, 0.0373] | 0.0000 | [0.0000, 0.0000] | 8/8 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0268 | [0.0234, 0.0303] | -0.1380 | [-0.5409, 0.2986] | 8/8 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0271 | [0.0240, 0.0300] | -0.1204 | [-0.4899, 0.2835] | 8/8 |
| 8 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0282 | [0.0245, 0.0317] | -0.1834 | [-0.5518, 0.2188] | 8/8 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0433 | [0.0420, 0.0446] | -0.4531 | [-0.7772, -0.0614] | 8/8 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0436 | [0.0419, 0.0450] | -0.4884 | [-0.7811, -0.1623] | 8/8 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0439 | [0.0422, 0.0453] | -0.4559 | [-0.7820, -0.0632] | 8/8 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run1 | 0.0844 | [0.0820, 0.0867] | -0.9607 | [-0.9769, -0.9418] | 8/8 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run2 | 0.0849 | [0.0826, 0.0868] | -0.9600 | [-0.9752, -0.9420] | 8/8 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run3 | 0.0851 | [0.0829, 0.0869] | -0.9267 | [-0.9752, -0.8420] | 8/8 |

See [ranking-overall-test-weighted.tsv](results-dummy/system-rankings/ranking-overall-test-weighted.tsv) for full details.

## Per-language rankings

Per-language rankings are computed in the same way as the overall ranking, but restricted to the official test sets of the respective language.

¹ CIs for language scores are approximate (weighted average of per-test-set bootstrap CIs).

### Language: de (German) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_run1 | 0.0000 | [0.0000, 0.0000] | 0.9833 | [0.9742, 0.9924] | 4/4 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run2 | 0.0118 | [0.0092, 0.0154] | 0.0924 | [-0.2606, 0.4394] | 4/4 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run3 | 0.0128 | [0.0099, 0.0165] | 0.0273 | [-0.2758, 0.3773] | 4/4 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run1 | 0.0138 | [0.0111, 0.0169] | 0.0576 | [-0.2939, 0.4061] | 4/4 |
| 5 | no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0236 | [0.0170, 0.0330] | 0.0000 | [0.0000, 0.0000] | 4/4 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0269 | [0.0239, 0.0296] | -0.3303 | [-0.6697, 0.0121] | 4/4 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0270 | [0.0241, 0.0297] | -0.3045 | [-0.6440, 0.0364] | 4/4 |
| 8 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0273 | [0.0238, 0.0308] | -0.3167 | [-0.6500, 0.0182] | 4/4 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0439 | [0.0428, 0.0450] | -0.4667 | [-0.6757, -0.1576] | 4/4 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0443 | [0.0432, 0.0452] | -0.4636 | [-0.6667, -0.1576] | 4/4 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0445 | [0.0433, 0.0456] | -0.4667 | [-0.6757, -0.1576] | 4/4 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run1 | 0.0857 | [0.0844, 0.0871] | -0.9939 | [-1.0000, -0.9849] | 4/4 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run3 | 0.0859 | [0.0842, 0.0876] | -0.9970 | [-1.0000, -0.9909] | 4/4 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run2 | 0.0861 | [0.0846, 0.0875] | -0.9970 | [-1.0000, -0.9909] | 4/4 |

See [ranking-language-de-test-weighted.tsv](results-dummy/system-rankings/ranking-language-de-test-weighted.tsv) for full details.

### Language: en (English) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_run1 | 0.0000 | [0.0000, 0.0000] | 0.9447 | [0.8367, 1.0000] | 2/2 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run1 | 0.0100 | [0.0089, 0.0114] | 0.5963 | [0.2510, 0.9362] | 2/2 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run2 | 0.0110 | [0.0092, 0.0129] | 0.6122 | [0.2697, 0.9495] | 2/2 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run3 | 0.0115 | [0.0094, 0.0138] | 0.6122 | [0.2697, 0.9495] | 2/2 |
| 5 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0272 | [0.0244, 0.0294] | 0.1665 | [-0.2053, 0.5383] | 2/2 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0275 | [0.0243, 0.0304] | 0.1905 | [-0.1787, 0.5595] | 2/2 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0281 | [0.0251, 0.0315] | 0.2692 | [-0.1000, 0.6383] | 2/2 |
| 8 | no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0343 | [0.0232, 0.0459] | 0.0000 | [0.0000, 0.0000] | 2/2 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0431 | [0.0414, 0.0445] | -0.2984 | [-0.6675, 0.0708] | 2/2 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0437 | [0.0422, 0.0451] | -0.3011 | [-0.6702, 0.0681] | 2/2 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0442 | [0.0430, 0.0454] | -0.2958 | [-0.6649, 0.0734] | 2/2 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run2 | 0.0852 | [0.0829, 0.0872] | -0.8830 | [-0.9255, -0.8351] | 2/2 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run1 | 0.0857 | [0.0839, 0.0877] | -0.8883 | [-0.9308, -0.8404] | 2/2 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run3 | 0.0861 | [0.0844, 0.0873] | -0.7830 | [-0.9255, -0.5351] | 2/2 |

See [ranking-language-en-test-weighted.tsv](results-dummy/system-rankings/ranking-language-en-test-weighted.tsv) for full details.

### Language: fr (French) — test split

| Rank | System | Language cMER ↓ | 95% CI¹ | Language Pref Macro ↑ | 95% CI¹ | Test sets |
|------|--------|-----------------|---------|----------------------|---------|----------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_run1 | 0.0000 | [0.0000, 0.0000] | 1.0000 | [1.0000, 1.0000] | 2/2 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run3 | 0.0092 | [0.0070, 0.0122] | 0.2000 | [-0.4000, 0.7000] | 2/2 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run1 | 0.0107 | [0.0085, 0.0141] | -0.1000 | [-0.6000, 0.5000] | 2/2 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_run2 | 0.0111 | [0.0078, 0.0151] | 0.0500 | [-0.4000, 0.5000] | 2/2 |
| 5 | no-correction_hipe-ocrepair-bench_v0.9_run1 | 0.0215 | [0.0127, 0.0330] | 0.0000 | [0.0000, 0.0000] | 2/2 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0261 | [0.0216, 0.0307] | -0.3000 | [-0.8000, 0.3000] | 2/2 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0264 | [0.0230, 0.0290] | -0.3000 | [-0.7000, 0.2000] | 2/2 |
| 8 | word-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0300 | [0.0252, 0.0348] | -0.4000 | [-0.8000, 0.1000] | 2/2 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run1 | 0.0415 | [0.0397, 0.0433] | -0.6000 | [-1.0000, -0.1000] | 2/2 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run3 | 0.0433 | [0.0411, 0.0452] | -0.6000 | [-1.0000, -0.1000] | 2/2 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_run2 | 0.0437 | [0.0413, 0.0456] | -0.7000 | [-1.0000, -0.4000] | 2/2 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run1 | 0.0818 | [0.0778, 0.0855] | -1.0000 | [-1.0000, -1.0000] | 2/2 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run3 | 0.0833 | [0.0803, 0.0859] | -1.0000 | [-1.0000, -1.0000] | 2/2 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_run2 | 0.0834 | [0.0804, 0.0857] | -1.0000 | [-1.0000, -1.0000] | 2/2 |

See [ranking-language-fr-test-weighted.tsv](results-dummy/system-rankings/ranking-language-fr-test-weighted.tsv) for full details.

## Results by dataset

### Dataset: dta19-l0_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run1 | 0.0000 | [0.0000, 0.0000] | 0.9000 | [0.8455, 0.9545] | 0.0000 | 0.0000 |
| 2 | no-correction_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run1 | 0.0035 | [0.0030, 0.0040] | 0.0000 | [0.0000, 0.0000] | 0.0038 | 0.0211 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run2 | 0.0070 | [0.0064, 0.0077] | -0.6545 | [-0.8000, -0.5091] | 0.0118 | 0.0179 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run1 | 0.0075 | [0.0067, 0.0084] | -0.7636 | [-0.8727, -0.6364] | 0.0129 | 0.0179 |
| 5 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run3 | 0.0076 | [0.0069, 0.0084] | -0.6909 | [-0.8182, -0.5455] | 0.0125 | 0.0179 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run1 | 0.0297 | [0.0287, 0.0307] | -0.9818 | [-1.0000, -0.9455] | 0.0328 | 0.0443 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run2 | 0.0304 | [0.0294, 0.0314] | -0.9818 | [-1.0000, -0.9455] | 0.0318 | 0.0446 |
| 8 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run3 | 0.0318 | [0.0307, 0.0330] | -0.9818 | [-1.0000, -0.9455] | 0.0341 | 0.0453 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run1 | 0.0444 | [0.0440, 0.0448] | -1.0000 | [-1.0000, -1.0000] | 0.0441 | 0.1762 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run3 | 0.0447 | [0.0442, 0.0451] | -1.0000 | [-1.0000, -1.0000] | 0.0438 | 0.1764 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run2 | 0.0449 | [0.0444, 0.0452] | -1.0000 | [-1.0000, -1.0000] | 0.0442 | 0.1801 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run1 | 0.0857 | [0.0851, 0.0863] | -1.0000 | [-1.0000, -1.0000] | 0.0849 | 0.3336 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run3 | 0.0857 | [0.0851, 0.0862] | -1.0000 | [-1.0000, -1.0000] | 0.0856 | 0.3329 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l0_v0.1_test_de_run2 | 0.0859 | [0.0853, 0.0864] | -1.0000 | [-1.0000, -1.0000] | 0.0853 | 0.3331 |

See [ranking-dta19-l0_v0.1-test-de-cmer-micro.tsv](results-dummy/system-rankings/ranking-dta19-l0_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: dta19-l1_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run1 | 0.0000 | [0.0000, 0.0000] | 1.0000 | [1.0000, 1.0000] | 0.0000 | 0.0000 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run2 | 0.0070 | [0.0064, 0.0077] | 0.8636 | [0.7636, 0.9455] | 0.0118 | 0.0179 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run1 | 0.0075 | [0.0067, 0.0084] | 0.7636 | [0.6364, 0.8727] | 0.0129 | 0.0179 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run3 | 0.0076 | [0.0069, 0.0084] | 0.8091 | [0.6909, 0.9091] | 0.0125 | 0.0179 |
| 5 | no-correction_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run1 | 0.0227 | [0.0220, 0.0234] | 0.0000 | [0.0000, 0.0000] | 0.0227 | 0.1405 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run1 | 0.0297 | [0.0287, 0.0307] | -0.5909 | [-0.7364, -0.4364] | 0.0328 | 0.0443 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run2 | 0.0304 | [0.0294, 0.0314] | -0.7091 | [-0.8364, -0.5636] | 0.0318 | 0.0446 |
| 8 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run3 | 0.0318 | [0.0307, 0.0329] | -0.6818 | [-0.8091, -0.5455] | 0.0341 | 0.0453 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run1 | 0.0444 | [0.0440, 0.0448] | -0.9818 | [-1.0000, -0.9455] | 0.0441 | 0.1762 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run3 | 0.0447 | [0.0442, 0.0451] | -0.9818 | [-1.0000, -0.9455] | 0.0438 | 0.1764 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run2 | 0.0449 | [0.0444, 0.0453] | -0.9818 | [-1.0000, -0.9455] | 0.0442 | 0.1801 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run1 | 0.0857 | [0.0851, 0.0863] | -1.0000 | [-1.0000, -1.0000] | 0.0849 | 0.3336 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run3 | 0.0857 | [0.0851, 0.0862] | -1.0000 | [-1.0000, -1.0000] | 0.0856 | 0.3329 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l1_v0.1_test_de_run2 | 0.0859 | [0.0853, 0.0864] | -1.0000 | [-1.0000, -1.0000] | 0.0853 | 0.3331 |

See [ranking-dta19-l1_v0.1-test-de-cmer-micro.tsv](results-dummy/system-rankings/ranking-dta19-l1_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: dta19-l2_v0.1

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run1 | 0.0000 | [0.0000, 0.0000] | 1.0000 | [1.0000, 1.0000] | 0.0000 | 0.0000 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run2 | 0.0070 | [0.0064, 0.0077] | 0.9455 | [0.8727, 1.0000] | 0.0118 | 0.0179 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run1 | 0.0075 | [0.0067, 0.0084] | 0.9455 | [0.8727, 1.0000] | 0.0129 | 0.0179 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run3 | 0.0076 | [0.0069, 0.0084] | 0.9455 | [0.8727, 1.0000] | 0.0125 | 0.0179 |
| 5 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run1 | 0.0297 | [0.0287, 0.0307] | 0.9455 | [0.8727, 1.0000] | 0.0328 | 0.0443 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run2 | 0.0304 | [0.0294, 0.0314] | 0.9091 | [0.8182, 0.9818] | 0.0318 | 0.0446 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run3 | 0.0318 | [0.0307, 0.0330] | 0.9636 | [0.9091, 1.0000] | 0.0341 | 0.0453 |
| 8 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run1 | 0.0444 | [0.0440, 0.0448] | 1.0000 | [1.0000, 1.0000] | 0.0441 | 0.1762 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run3 | 0.0447 | [0.0442, 0.0451] | 0.9818 | [0.9455, 1.0000] | 0.0438 | 0.1764 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run2 | 0.0449 | [0.0444, 0.0452] | 0.9818 | [0.9455, 1.0000] | 0.0442 | 0.1801 |
| 11 | no-correction_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run1 | 0.0580 | [0.0571, 0.0591] | 0.0000 | [0.0000, 0.0000] | 0.0591 | 0.2906 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run1 | 0.0857 | [0.0851, 0.0863] | -0.9636 | [-1.0000, -0.9091] | 0.0849 | 0.3336 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run3 | 0.0857 | [0.0851, 0.0862] | -0.9818 | [-1.0000, -0.9455] | 0.0856 | 0.3329 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_dta19-l2_v0.1_test_de_run2 | 0.0859 | [0.0853, 0.0864] | -0.9818 | [-1.0000, -0.9455] | 0.0853 | 0.3331 |

See [ranking-dta19-l2_v0.1-test-de-cmer-micro.tsv](results-dummy/system-rankings/ranking-dta19-l2_v0.1-test-de-cmer-micro.tsv) for full details.

### Dataset: icdar2017_v1.1

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.0000 | [0.0000, 0.0000] | 0.9894 | [0.9734, 1.0000] | 0.0000 | 0.0000 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run3 | 0.0064 | [0.0060, 0.0069] | 0.8245 | [0.7394, 0.8989] | 0.0111 | 0.0161 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run2 | 0.0067 | [0.0063, 0.0072] | 0.8245 | [0.7394, 0.8989] | 0.0112 | 0.0159 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.0068 | [0.0063, 0.0073] | 0.7926 | [0.7021, 0.8723] | 0.0121 | 0.0160 |
| 5 | word-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run3 | 0.0307 | [0.0299, 0.0314] | 0.1330 | [-0.0106, 0.2766] | 0.0297 | 0.0420 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.0309 | [0.0302, 0.0316] | 0.1809 | [0.0426, 0.3191] | 0.0300 | 0.0423 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run2 | 0.0310 | [0.0303, 0.0317] | 0.1383 | [0.0000, 0.2766] | 0.0307 | 0.0420 |
| 8 | no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.0343 | [0.0298, 0.0392] | 0.0000 | [0.0000, 0.0000] | 0.0418 | 0.1694 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.0443 | [0.0439, 0.0446] | -0.1915 | [-0.3298, -0.0532] | 0.0434 | 0.1687 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run2 | 0.0444 | [0.0441, 0.0447] | -0.1968 | [-0.3351, -0.0585] | 0.0437 | 0.1668 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run3 | 0.0444 | [0.0441, 0.0448] | -0.2021 | [-0.3404, -0.0638] | 0.0437 | 0.1687 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run1 | 0.0850 | [0.0845, 0.0855] | -0.7766 | [-0.8617, -0.6809] | 0.0838 | 0.3153 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run3 | 0.0853 | [0.0848, 0.0857] | -0.7660 | [-0.8511, -0.6702] | 0.0840 | 0.3143 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_en_run2 | 0.0856 | [0.0851, 0.0860] | -0.7660 | [-0.8511, -0.6702] | 0.0842 | 0.3157 |

See [ranking-icdar2017_v1.1-test-en-cmer-micro.tsv](results-dummy/system-rankings/ranking-icdar2017_v1.1-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run1 | 0.0000 | [0.0000, 0.0000] | 1.0000 | [1.0000, 1.0000] | 0.0000 | 0.0000 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run2 | 0.0060 | [0.0041, 0.0090] | 0.7000 | [0.2000, 1.0000] | 0.0122 | 0.0168 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run3 | 0.0063 | [0.0048, 0.0090] | 0.6000 | [0.0000, 1.0000] | 0.0091 | 0.0102 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run1 | 0.0066 | [0.0045, 0.0105] | 0.4000 | [-0.2000, 1.0000] | 0.0158 | 0.0168 |
| 5 | word-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run2 | 0.0288 | [0.0256, 0.0311] | 0.2000 | [-0.4000, 0.8000] | 0.0272 | 0.0415 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run1 | 0.0311 | [0.0260, 0.0366] | 0.0000 | [-0.6000, 0.6000] | 0.0304 | 0.0411 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run3 | 0.0316 | [0.0282, 0.0351] | 0.0000 | [-0.6000, 0.6000] | 0.0348 | 0.0418 |
| 8 | no-correction_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run1 | 0.0327 | [0.0197, 0.0474] | 0.0000 | [0.0000, 0.0000] | 0.0329 | 0.1210 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run1 | 0.0425 | [0.0409, 0.0440] | -0.4000 | [-1.0000, 0.2000] | 0.0412 | 0.1652 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run2 | 0.0425 | [0.0409, 0.0439] | -0.4000 | [-1.0000, 0.2000] | 0.0425 | 0.1512 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run3 | 0.0426 | [0.0406, 0.0439] | -0.4000 | [-1.0000, 0.2000] | 0.0411 | 0.1578 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run1 | 0.0814 | [0.0779, 0.0841] | -1.0000 | [-1.0000, -1.0000] | 0.0815 | 0.2798 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run3 | 0.0825 | [0.0790, 0.0852] | -1.0000 | [-1.0000, -1.0000] | 0.0803 | 0.2842 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_icdar2017_v1.1_test_fr_run2 | 0.0827 | [0.0805, 0.0848] | -1.0000 | [-1.0000, -1.0000] | 0.0828 | 0.2904 |

See [ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv](results-dummy/system-rankings/ranking-icdar2017_v1.1-test-fr-cmer-micro.tsv) for full details.

### Dataset: impresso-snippets_v1.0

#### Language: de (German) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run1 | 0.0000 | [0.0000, 0.0000] | 1.0000 | [1.0000, 1.0000] | 0.0000 | 0.0000 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run2 | 0.0167 | [0.0120, 0.0231] | -0.2000 | [-0.8000, 0.4000] | 0.0182 | 0.0258 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run3 | 0.0180 | [0.0128, 0.0246] | -0.3000 | [-0.8000, 0.3000] | 0.0196 | 0.0258 |
| 4 | no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run1 | 0.0192 | [0.0067, 0.0371] | 0.0000 | [0.0000, 0.0000] | 0.0216 | 0.0944 |
| 5 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run1 | 0.0202 | [0.0155, 0.0254] | -0.2000 | [-0.8000, 0.4000] | 0.0214 | 0.0258 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run3 | 0.0229 | [0.0169, 0.0286] | -0.4000 | [-1.0000, 0.2000] | 0.0221 | 0.0326 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run2 | 0.0234 | [0.0184, 0.0278] | -0.4000 | [-1.0000, 0.2000] | 0.0223 | 0.0326 |
| 8 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run1 | 0.0243 | [0.0196, 0.0288] | -0.4000 | [-1.0000, 0.2000] | 0.0238 | 0.0326 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run2 | 0.0430 | [0.0413, 0.0448] | -0.6000 | [-1.0000, 0.0000] | 0.0429 | 0.1936 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run1 | 0.0442 | [0.0425, 0.0456] | -0.6000 | [-1.0000, 0.0000] | 0.0440 | 0.1910 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run3 | 0.0443 | [0.0424, 0.0461] | -0.6000 | [-1.0000, 0.0000] | 0.0444 | 0.2102 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run1 | 0.0857 | [0.0837, 0.0878] | -1.0000 | [-1.0000, -1.0000] | 0.0855 | 0.3364 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run2 | 0.0862 | [0.0838, 0.0886] | -1.0000 | [-1.0000, -1.0000] | 0.0860 | 0.3590 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_de_run3 | 0.0862 | [0.0832, 0.0889] | -1.0000 | [-1.0000, -1.0000] | 0.0861 | 0.3528 |

See [ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv](results-dummy/system-rankings/ranking-impresso-snippets_v1.0-test-de-cmer-micro.tsv) for full details.

#### Language: en (English) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.0000 | [0.0000, 0.0000] | 0.9000 | [0.7000, 1.0000] | 0.0000 | 0.0000 |
| 2 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.0133 | [0.0114, 0.0155] | 0.4000 | [-0.2000, 1.0000] | 0.0136 | 0.0231 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run2 | 0.0153 | [0.0120, 0.0186] | 0.4000 | [-0.2000, 1.0000] | 0.0157 | 0.0231 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run3 | 0.0165 | [0.0127, 0.0208] | 0.4000 | [-0.2000, 1.0000] | 0.0174 | 0.0231 |
| 5 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run3 | 0.0236 | [0.0189, 0.0275] | 0.2000 | [-0.4000, 0.8000] | 0.0232 | 0.0365 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.0240 | [0.0184, 0.0292] | 0.2000 | [-0.4000, 0.8000] | 0.0231 | 0.0365 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run2 | 0.0252 | [0.0199, 0.0313] | 0.4000 | [-0.2000, 1.0000] | 0.0250 | 0.0365 |
| 8 | no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.0344 | [0.0167, 0.0525] | 0.0000 | [0.0000, 0.0000] | 0.0331 | 0.1146 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run2 | 0.0418 | [0.0387, 0.0442] | -0.4000 | [-1.0000, 0.2000] | 0.0418 | 0.1707 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run3 | 0.0430 | [0.0404, 0.0455] | -0.4000 | [-1.0000, 0.2000] | 0.0428 | 0.1754 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.0441 | [0.0420, 0.0462] | -0.4000 | [-1.0000, 0.2000] | 0.0441 | 0.1631 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run2 | 0.0849 | [0.0806, 0.0884] | -1.0000 | [-1.0000, -1.0000] | 0.0843 | 0.3150 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run1 | 0.0863 | [0.0834, 0.0898] | -1.0000 | [-1.0000, -1.0000] | 0.0869 | 0.3188 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_en_run3 | 0.0869 | [0.0839, 0.0889] | -0.8000 | [-1.0000, -0.4000] | 0.0864 | 0.3058 |

See [ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv](results-dummy/system-rankings/ranking-impresso-snippets_v1.0-test-en-cmer-micro.tsv) for full details.

#### Language: fr (French) — test split

cMER micro [`cmer_micro`] — ordered ascending (lower is better)

| Rank | System | cMER micro ↓ | 95% CI | Pref cMER Macro ↑ | 95% CI | cMER macro | wMER macro |
|------|--------|--------------|--------|--------------|--------|------------|------------|
| 1 | perfect_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.0000 | [0.0000, 0.0000] | 1.0000 | [1.0000, 1.0000] | 0.0000 | 0.0000 |
| 2 | no-correction_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.0104 | [0.0058, 0.0185] | 0.0000 | [0.0000, 0.0000] | 0.0117 | 0.0568 |
| 3 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run3 | 0.0120 | [0.0093, 0.0154] | -0.2000 | [-0.8000, 0.4000] | 0.0136 | 0.0249 |
| 4 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.0149 | [0.0125, 0.0178] | -0.6000 | [-1.0000, 0.0000] | 0.0158 | 0.0249 |
| 5 | word-swaps-p01_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run2 | 0.0162 | [0.0116, 0.0212] | -0.6000 | [-1.0000, 0.0000] | 0.0177 | 0.0224 |
| 6 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.0211 | [0.0173, 0.0248] | -0.6000 | [-1.0000, 0.0000] | 0.0204 | 0.0363 |
| 7 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run2 | 0.0240 | [0.0204, 0.0270] | -0.8000 | [-1.0000, -0.4000] | 0.0232 | 0.0356 |
| 8 | word-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run3 | 0.0284 | [0.0222, 0.0346] | -0.8000 | [-1.0000, -0.4000] | 0.0280 | 0.0363 |
| 9 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.0405 | [0.0385, 0.0426] | -0.8000 | [-1.0000, -0.4000] | 0.0402 | 0.1627 |
| 10 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run3 | 0.0441 | [0.0417, 0.0466] | -0.8000 | [-1.0000, -0.4000] | 0.0441 | 0.1619 |
| 11 | char-swaps-p05_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run2 | 0.0449 | [0.0418, 0.0472] | -1.0000 | [-1.0000, -1.0000] | 0.0441 | 0.1577 |
| 12 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run1 | 0.0822 | [0.0777, 0.0870] | -1.0000 | [-1.0000, -1.0000] | 0.0822 | 0.2969 |
| 13 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run2 | 0.0840 | [0.0802, 0.0866] | -1.0000 | [-1.0000, -1.0000] | 0.0822 | 0.3030 |
| 14 | char-swaps-p10_hipe-ocrepair-bench_v0.9_impresso-snippets_v1.0_test_fr_run3 | 0.0841 | [0.0815, 0.0866] | -1.0000 | [-1.0000, -1.0000] | 0.0839 | 0.2999 |

See [ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv](results-dummy/system-rankings/ranking-impresso-snippets_v1.0-test-fr-cmer-micro.tsv) for full details.
