# M100 — first-session memecoin research report

**Research window:** 2026-08-23T23:34:05Z–2026-08-23T23:38:30Z

**Bankroll:** exactly **$100.00**

**Execution status:** no wallet connected, no order constructed, no real-money trade placed.

**Decision at the end of this session:** **NO TRADE — CAPITAL PRESERVED.**

> **Executive verdict.** Risking any of the $100 is **not currently justified**. Solana is the highest-activity environment for a future small-account study, but the available evidence does not establish a point-in-time, post-friction, out-of-sample positive-expectancy trade state. The attractive-looking fresh launches failed either the information, on-chain, execution, or risk committee. The default allocation remains cash.

This is a research record, not a solicitation or a claim that a token is safe. All dollar values and market data are timestamped snapshots. A value can be stale minutes later.

---

## 1. Current market state

### 1.1 Chain comparison and venue choice

| Chain | DEX volume, 24h | DEX volume, 7d | DEX volume, 30d | Current transaction-cost snapshot | Launch / meme conclusion |
|---|---:|---:|---:|---|---|
| **Solana** | **$3.732bn** | $17.479bn | $52.945bn | SOL base fee is 5,000 lamports/signature; current Raydium suggested CU prices: 10k / 15k / 20k micro-lamports per CU | **Selected for research only.** Largest observed DEX turnover, the deepest public launchpad cluster, public discovery APIs, and low unit cost. This is not evidence of a tradable edge. |
| BNB Smart Chain | $1.562bn | $8.884bn | $32.091bn | BscScan 23:37:42Z: standard swap ~$0.007 | Meaningful secondary meme lane: Four.meme / PancakeSwap. Less accessible current launch-history and wallet-graph evidence in this session. |
| Ethereum mainnet | $1.477bn | $9.693bn | $28.412bn | Etherscan 23:38:26Z: standard swap ~$0.037 | Current gas is unusually cheap, so gas is not the exclusion. New-pool latency, MEV and contract complexity remain less suitable than Solana for this $100 research mandate. |
| Base | $1.275bn | $7.003bn | $20.625bn | BaseScan 23:37:47Z: standard swap ~$0.002, rapid ~$0.003 | Meaningful social/AI-token lane (Clanker; creator-token tooling), but not selected: less demonstrated current launch-flow advantage for this account and lower directly observable launchpad activity than the Solana reference point. |
| Arbitrum | $0.367bn | $1.739bn | $4.372bn | Not selected | No current evidence here of a superior meme-launch opportunity. |

**Definition warning:** these are DefiLlama *all-DEX* volumes, not memecoin-only volumes, and therefore cannot be used to claim a memecoin market share. The source definitions and raw values are preserved in [`m100/data/live_snapshot_2026-08-23T2334Z.json`](m100/data/live_snapshot_2026-08-23T2334Z.json).

Solana volume was +3.65% day/day, +219.26% on DefiLlama's 7-day comparison field, and +152.8% on its 1-month comparison field at collection. The current 30-day total was still 7.68% below the preceding 30-day total. That is a **high-turnover, recently re-accelerating but regime-unstable** environment, not a stable trend declaration.

### 1.2 Solana launch, DEX, migration, and fee environment

| Layer | Current evidence | Interpretation for M100 |
|---|---|---|
| Primary launchpad | Pump's public fee API recorded $4.819m of parent-product fees over 24h and $32.896m over 7d. Pump.fun uses an on-chain constant-product bonding curve and atomically migrates graduated liquidity to PumpSwap. | Pump.fun remains the primary standardized lifecycle to study. It is not the only launchpad: LetsBonk/BONK.fun, Raydium LaunchLab, Meteora DBC, Bags, Jupiter Studio and social launch products are competing lanes. |
| DEX / post-graduation | PumpSwap's filtered DEX volume was $570.006m over 24h, $3.984bn over 7d and $17.770bn over 30d. Its stated volume filter requires at least $5k TVL and 50 unique traders; it is not bonding-curve volume. Raydium showed $275.916m 24h and Meteora $395.864m 24h on their parent DEX records. | There is real secondary trading liquidity, but a token's own exit depth must be quoted. Network-level volume is not exit liquidity for a $10 order. |
| Pump bonding curve | Official Pump documentation says it is a deterministic constant-product AMM; every buy changes price and graduation closes the curve and migrates liquidity atomically. | A manual participant does not possess an informational speed advantage at launch. The curve's visible momentum is also visible to bots. |
| Pump fees | Official Pump schedule (updated 2026-05-20): **1.25% per bonding-curve trade** = 0.30% creator + 0.95% protocol; **0.015 SOL** taken from liquidity on graduation. Canonical PumpSwap pools start at **1.25%** total at 0–420 SOL market cap and step down to 0.30%; non-canonical pools are 0.30%. | A naïve fresh-curve round trip carries roughly 2.5% in published swap fees before price movement. This alone eliminates many small, short-horizon ideas. |
| Raydium / Meteora | Raydium CPMM typical fee is 0.25%, CLMM tiers include 0.01/0.05/0.25/1%, while LaunchLab fees can stack protocol, platform, creator, and referral components. Meteora DBC fees and migration fees are configuration-specific. | Never use a generic DEX fee in a backtest. Read the pool/configuration and get an immediate quote. |
| Jupiter routing | Jupiter's Metis Swap API has zero default protocol fee, but an integrator can add a platform fee; a live SOL→USDC Ultra preview at collection showed 2 bps. | This exact 2-bp observation is **not** a universal Jupiter or meme-token fee. Route, aggregator, AMM fees, priority fee, and any third-party terminal fee need to be captured at decision time. |
| Priority / MEV | Raydium's live auto-fee API returned 10k/15k/20k micro-lamports/CU (m/h/vh). Jito's live tip floor at **2026-08-23T23:35:42Z** was 0.000010 SOL p75, 0.0007994766 SOL p95, 0.00217848118 SOL p99. SOL was $95.41099756. | Normal priority cost is small in dollars; p95/p99 bundle tips can become material on a $10 position. A tip is an auction bid, not an alpha source. |

### 1.3 Definitions reconciled rather than averaged

A material data disagreement was found and resolved:

* The current DefiLlama PumpSwap fee adapter describes 0.20% LP + 0.05% protocol + 0.05% creator = 0.30%.
* Pump's own current fee schedule says **canonical** pools have a market-cap tiered fee, **1.25%** at 0–420 SOL market cap, with 0.30% reserved for non-canonical pools and the highest canonical tier.

These are not two estimates of one universal number. The official Pump schedule is the execution assumption for a small canonical Pump token; the DefiLlama adapter is useful for its metric methodology but not sufficient to price every specific pool. Every prospective trade must use the actual pool class and quote.

### 1.4 Narratives, social state, bot intensity, and liquidity condition

The current discovery sample was dominated by animal/PEPE-derivative branding, influencer-adjacent names, and TikTok/social claims. This is **not** a measured ecosystem-wide narrative ranking. It is only what appeared in the sampled DexScreener profile/boost feeds.

The same feed showed a 500-unit paid boost on OCTO. Paid boosts and paid profiles are discovery signals only; they are not organic social attention. The GeckoTerminal new-pool page also showed several pools created seconds apart at about $2.1k reserve, including near-identical names. That is direct evidence of a very high-noise launch stream, not an estimate of all launch volume.

Bot/sniper intensity is demonstrably non-zero and structurally important:

* Pump launches expose deterministic curve state and the current Jito auction infrastructure permits atomic bundles.
* The current public Jito floor has a 1,000-lamport minimum, while the p95/p99 tail was 0.000799/0.002178 SOL.
* The published Jito sandwich measurement examined four months in early 2025 and found 521,903 detected sandwiches with at least $7.7m in victim loss. Its data period is not current, but it is strong reason not to assume benign execution.

**Regime conclusion:** there is active speculative capacity, but the observed current regime is better described as **fast, noisy, promotional, and adversarial** than as an independently confirmed organic-demand regime.

---

## 2. Public data actually used

| Dataset / API | Collected or data period | Resolution / fields actually used | Strength | Material limitation / survivor risk |
|---|---|---|---|---|
| DefiLlama DEX and fee APIs | fetched 2026-08-23T23:34–23:38Z | 24h/7d/30d aggregate protocol and chain values; methodology text | Current public benchmark; methodology displayed | DEX volume is not token-level organic volume; protocol definitions differ; not a trade tape. |
| Jupiter price, quote and Ultra order APIs | fetched 2026-08-23T23:35Z | SOL price, route preview, fee fields, current block id | Current executable reference route for SOL/USDC | Not a quote for a candidate token; no wallet/taker supplied; no swap sent. |
| Raydium auto-fee + Jito tip floor | fetched 2026-08-23T23:35Z | CU-price tiers; tip percentiles and timestamp | Current fee-market snapshot | Not account-specific Pump/PumpSwap priority estimation; tip floor only applies to Jito bundles. |
| DexScreener token profiles/boosts/pairs | fetched 2026-08-23T23:34–23:38Z | fresh profile candidates, paid boosts, pool price/liquidity, tx counts | Independent discovery and market snapshot | Pair figures are not wallet-level independence, creator graph, or proof of organic volume. |
| RugCheck reports | fetched 2026-08-23T23:34–23:38Z | mint/freeze authority, Token-2022 extension fields, top holders, reported risk | Useful technical first-pass gate | No safety certification; vendor labels and unlinked holders are not a wallet graph. |
| Zenodo RED-PUMP-2026-v1 | metadata verified 2026-08-23; **2026-05-08–2026-06-10** collection | 860,213 launch records / 832,941 observed terminal outcomes; launch metadata | Rare all-launch rather than winner-only public benchmark | Its v1.4 corrigendum says the 0.198% rate is only a lower bound within an approximately six-minute observer window, **not** a verified 24h graduation rate. |
| GitHub January-2025 Pump.fun study | dataset and notebook audited this session; **January 2025** | 32,000 launches, 583 graduation labels; first-30-minute aggregates | Includes failed launches and has reproducible Parquet data | Exact creation ordering absent; random split; first 30 minutes can contain the graduation event; graduation is not a tradeable net-return label. |
| Published Pump.fun paper | published/submitted 2026; **2025-09-01–2025-10-01** data | 655,770 new tokens, 4,338 graduates; decoded trades | Full-chain reconstruction and failed launches | One 2025 month; label is graduation, not net PnL. |
| MemeTrans | 2026 paper; **2024-12-01–2025-03-01** data | Pump lifecycle / high-risk research | Useful transaction/graph feature ideas | It starts from migrated tokens, so it is not a base-rate universe. |
| Solidus Labs report | published 2026; underlying period starts 2024 and is not a current sample | Pump and Raydium risk classifications | Broad risk reference | Vendor taxonomy calls patterns rugs/pump-and-dumps; not legal findings and not an observed probability for this strategy. |

**Closest usable point-in-time launch universe:** the January-2025 32,000-launch Parquet was downloaded and audited with code because it includes both graduates and failures. The more recent RED-PUMP 2026 record-level universe is larger, but its own v1.4 metadata says the observed outcomes are visibility-window lower bounds rather than valid 24-hour labels. Neither is a legitimate current executable-return training set. The current 2026-08-23 data is therefore a timestamped live *discovery snapshot*, not falsely presented as a complete launch universe.

**Accessible but not substituted with fake data:** Solana RPC, Dune, Helius, Birdeye, GMGN, Bubblemaps, X/Twitter, Telegram, and indexed transaction vendors would be needed to compute exact wallet graphs, historical PnL, funded-cluster links, social author diversity, true unique buyers, and candidate-specific executable quotes at scale. No authentication was available for those paid/authenticated surfaces in this session, and no substitute was invented.

---

## 3. Empirical evidence and what it does—and does not—prove

| Work | Publication date | Actual data period | Useful finding | Correct use here |
|---|---|---|---|---|
| Marino, Naviglio, Tarantelli & Lillo, *Predicting the success of new crypto-tokens: the Pump.fun case* | submitted 2026-02-16 | 2025-09-01 to 2025-10-01 | 655,770 launches; 4,338 graduations (0.63%). Conditional graduation rises with curve state; rapid capital accumulation in fewer trades performed better than bot-heavy turnover; median time-to-graduation ≈4.4 minutes among graduates. | Supports the premise that flow composition matters. It strongly argues **against** waiting thirty minutes to predict a state that often occurs in minutes. It does not validate buying. |
| Kamat, *Pump.fun Graduation Regime Windows* + v1.4 Zenodo corrigendum | paper July 2026; v1.4 dataset 2026-08-13 | 2026-05-08 to 2026-06-10 | 832,941 unique mints, 1,651 observed graduations; advertised Telegram and above-default initial mcap associated with observed outcome. | Use as a data-source and coverage-bias lesson. Do **not** call its 0.198% lower bound a current true 24h graduation rate. The author explicitly retracts that interpretation. |
| Naviglio, Tarantelli & Lillo, *Price manipulation schemes of new crypto-tokens in decentralized exchanges* | record version 2026-01-30 | 17,194 Uniswap-V2 launches, 2024-10-02 to 2024-12-02 | At ten swaps, 94% of measured new-token NTV was in honeypots; sandwiches are especially profitable in low-liquidity pools. | Different chain and era, but supports adversarial treatment of displayed volume/liquidity and no fresh-pool extrapolation. |
| Gerzon et al., *Quantifying the Threat of Sandwiching MEV on Jito* | IMC 2025 | four months in early 2025 | 521,903 detected sandwich instances; ≥$7.7m victim loss; many defensive bundles had tips not meaningful for priority. | Demonstrates cost/adversarial-selection tail, not a current Pump-specific loss probability. |
| Solidus Labs, *2025 Rug Pull Report* | report surfaced 2026 | tokens since 2024, methodology-specific | 98.6% of Pump.fun tokens with ≥5 trades were classified as collapsed below $1k liquidity / pump-and-dump-like; 93% of Raydium pools received related flags. | A harsh prior, not a direct probability of loss after strict gates. It prohibits casual default-on exposure. |

### 3.1 Code-backed January-2025 data audit

I downloaded and read the 3.5 MB public Parquet directly with a zero-dependency Python parquet reader, rather than quoting charts. The reproducible audit is [`m100/scripts/audit_reference_dataset.py`](m100/scripts/audit_reference_dataset.py), and its exact output is [`m100/output/reference_dataset_audit.json`](m100/output/reference_dataset_audit.json).

* Source SHA-256: `ee5412658b8af19d776028d0158963b77f1ab3ca4f476ae4b6cf6080bbfff07c`
* Universe in that public file: 32,000 January-2025 launches; 583 `graduated=1`; base rate **1.8219%** (Wilson 95% CI 1.6810%–1.9743%).
* It contains failed launches, which is essential. It is nevertheless not documented as a complete full-month universe or a complete lifecycle/execution dataset.

Descriptive associations in the file were large:

| First-30-minute field | Non-graduate median | Graduate median | Top-decile graduation rate |
|---|---:|---:|---:|
| volume | $745 | $22,400 | 16.69% (cutoff $7,431) |
| trade count | 24 | 398 | 11.73% (cutoff 213) |
| unique buyers | 6 | 100 | 12.97% (cutoff 41) |
| largest buy | $388 | $2,085 | 13.66% (cutoff $1,182) |
| top-wallet volume share | 55.8% | 9.2% | Not monotone; high concentration is not a quality signal. |

A $10,000 first-30-minute-volume threshold still only had 524 graduates in 2,422 tokens (**21.64%**, Wilson 95% CI 20.04%–23.32%). A single $10k buy had a 41.18% graduation rate in 102 observations, but that is precisely the sort of whale/insider-like condition that cannot be assumed independent or copyable.

### 3.2 Why this is **not** an M100 model

The public notebook reports impressive random-split XGBoost precision. It cannot be adopted:

1. Its formal period is January 2025, not the current regime.
2. It uses `train_test_split`, not a chronological split. The Parquet contains weekday/hour/month, but no exact creation timestamp or slot to reconstruct order.
3. It uses a full **first 30 minutes** to predict “eventual graduation.” The independent September-2025 paper reports a ≈4.4-minute median graduation time among graduates. A substantial share may already have graduated inside the feature window; that is decision-time contamination for a pre-graduation strategy.
4. Graduation is not a barrier label, MFE/MAE, fill, exit quote, or post-cost PnL.
5. It does not identify linked wallets, bundle ownership, creator association, priority fees, failed transactions, Jito costs, price impact, or post-graduation execution.

The observed associations are useful **feature hypotheses** only: real paid-in capital, breadth, low concentration, and non-mechanical flow may matter. They are not calibrated probabilities, trade recommendations, or evidence to deploy the $100.

---

## 4. Information / Opportunity Crossover

**Definition:** the earliest state at which enough independently observable information exists to cut toxic selection while sufficient exit depth and remaining move exist after all friction.

The data does **not** currently establish that this crossover has positive net expectancy. It does establish why the two extremes are unsuitable:

* **Too early:** launch/block-zero/curve sniping is a latency and bundle auction against specialized infrastructure, with 1.25% per-side Pump fees and little time for technical or wallet independence checks.
* **Too late:** a 30-minute screen can be after graduation or after the primary move; it also pays fee/impact to buy an already obvious state.

The best *research hypothesis*, not live strategy, is a **post-graduation first clean pullback** after enough post-migration transactions exist to assess ownership and sell absorption, but before a new independent-demand leg. This earns the most information per unit of remaining opportunity. It is explicitly unproven until it beats cash and simple momentum in chronological, net-of-friction tests.

---

## 5. Strategy tournament

Ranks below are **research priority ranks**, not numerical expected-return ranks. No strategy received an out-of-sample net-expectancy pass, so no rank is a mandate to trade.

| Research rank | Strategy family | Evidence / data reliability | $100 execution & latency | Catastrophic exposure | Current result |
|---:|---|---|---|---|---|
| 0 | **Cash** | Certain | Perfect | None | **Selected benchmark and current holding.** |
| 1 | F. First clean pullback after graduation | Plausible information crossover, but no barrier-labeled backtest | Feasible only in deep, verified pools; not seconds-sensitive | High if ownership is dirty | **Primary research hypothesis; not live.** |
| 2 | E. Post-graduation continuation | Pool/liquidity data can be collected | Better than curve entry but can be chased | High | Secondary research hypothesis; not live. |
| 3 | N. Established-memecoin momentum | Deep venues and quotes are more available | Most feasible for $100 | Lower than fresh launch, still tail risk | Secondary research hypothesis; no M100 test yet. |
| 4 | G. Liquidity expansion | Economically sensible but LP provenance matters | Feasible after verification | Liquidity can be temporary / concentrated | Watch feature, not an entry. |
| 5 | J. Independent smart-wallet consensus | Potentially useful if graph-proven and latency-tested | Needs sub-minute data; unavailable | Insider contamination is severe | No live use. |
| 6 | H. Independent-holder growth | Potentially useful with transfer graph | Slow enough only post-launch | Sybil/bundle distortion | No live use. |
| 7 | I. Smart-wallet following | Labels alone are untrustworthy | Latency can erase edge | Copying insiders is adverse selection | No live use. |
| 8 | K. Social-attention acceleration | Timestamps/author diversity needed | May be late | Bot/paid-promotion contamination | No live use. |
| 9 | L. Narrative rotation | Broad regime indicator | Tradable only with liquid leaders | Reflexive / crowded | No live use. |
| 10 | M. Leader/laggard propagation | Needs defined clusters and non-overlapping tests | Feasible only in liquid names | Correlation breaks sharply | No live use. |
| 11 | O. Catalyst reaction | Event timestamping possible | Often already priced | Headline / fake-news risk | No live use. |
| 12 | A. Early-flow confirmation | Strong association with graduation in old data | Manual latency weak | Volume/bundle manipulation | Screening research only. |
| 13 | C. Pre-graduation acceleration | Curve-state prediction literature exists | Competed away rapidly | Fee plus bot toxicity | Rejected for $100 live use. |
| 14 | D. Graduation event | Mechanical, public, highly observable | Seconds-sensitive | Migration/dislocation / immediate dump | Rejected. |
| 15 | B. Bonding-curve continuation | Curve movement is visible to everyone | Very latency-sensitive; 1.25% each side | Extreme | Rejected. |

**Tournament winner:** **NO LIVE STRATEGY.** A sophisticated classifier is prohibited from replacing the missing execution labels and temporal validation.

### Wallet-copying decision

No wallet is approved for copying. A headline PnL, a terminal tag, or one successful early buy is not replicable alpha. For a future candidate wallet, the log must calculate realized PnL, trade count, median return/loss, maximum loss, holding time, largest-winner contribution, creator relationships, suspicious-token exposure, and classifications (organic / momentum bot / sniper / market maker / creator / insider-associated / unknown). It must then replay copy fills after **1, 3, 5, 10, 30, and 60 seconds** using contemporaneous pool state and actual quotes.

No qualifying wallet tape, graph, or delayed-fill data was accessible in this session. Consequently, the relevant statistic—**Replicable Wallet Alpha**—is unmeasured and treated as zero for allocation purposes.

---

## 6. Pre-registered future strategy and exact gates

The following is an **entry specification to test prospectively**, not a claim that these thresholds are optimal. It cannot become `ENTRY VALID` until the required measurements exist and a chronological study supports net expectancy.

### Primary research lane: post-graduation first clean pullback

1. **Universe:** Pump canonical or major Raydium/Meteora pool, after actual migration; exclude bonding curves and tokens first observed only through paid boosts.
2. **Timing:** Observe 20 minutes to 6 hours after migration. This is a hypothesis window designed to avoid block-zero and allow multiple wallet/flow snapshots. It is not a live buy instruction.
3. **Technical gate:** `mintAuthority=null`; `freezeAuthority=null`; no Token-2022 transfer fee, transfer hook, permanent delegate, default-frozen state, confidential transfer opacity, pausable authority, or mutable unreviewed privilege. A clean report means only **“no obvious technical red flag detected”**, never safe.
4. **Pool / execution gate:** actual total pool liquidity ≥$50k; direct $10 buy **and** sell quotes obtained at the same time; price impact + all fees + priority/bundle cost ≤4% round trip under the base quote and ≤7% under a 1.5× fee / 2× slippage stress. No route with unknown transfer tax or unexplained token-program behavior.
5. **Ownership gate:** creator and linked-wallet adjusted share ≤10%; any connected insider/bundle cluster ≤15%; adjusted top-10 concentration ≤35%; effective independent-holder count must be rising. LP, router, burn, program, CEX and canonical pool addresses must be excluded correctly.
6. **Flow gate:** at least 100 independently classified buyers in the measurement window; independent buy count rises in two successive five-minute windows; no single funder/cluster provides >15% of net buy volume; sell absorption returns price to pre-sell range within the pre-registered time limit.
7. **Smart-wallet gate:** at least two **independent**, historically analyzed wallets have entered after migration and retain exposure; they must pass a delayed-copy study at 5/10/30 seconds. Vendor “smart money” labels do not pass this gate.
8. **Social gate:** timestamped, cross-platform activity with author diversity; paid boosts, copied post templates, unverified follower counts, and creator self-promotion are excluded. If API access is absent, this is a veto—not an invitation to eyeball engagement.
9. **Price gate:** a pullback must hold above the measured post-migration launch range, reclaim on independent buy flow, and remain below a pre-set chase limit. Do not enter after the signal has already moved more than the planned invalidation distance.
10. **Risk gate:** maximum catastrophic loss must fit the position architecture even if a stop does not execute.

**Secondary lanes, only after their own validation:** established-memecoin momentum and independent-wallet consensus. No more than two secondary lanes may be monitored.

### Feature and label plan

At every decision point, record only data available at that exact slot/time:

* **Flow:** buy/sell count and SOL/USD value, unique buyer/seller, acceleration, net inflow, repeat buyers, median size, entropy, inter-arrival time.
* **Liquidity:** actual reserves, pool and LP controls, liquidity/mcap, 1% and 5% exit quote, quote change, liquidity acceleration.
* **Ownership:** adjusted top holders, creator share, linked creator share, Gini, effective independent holder count, concentration trend.
* **Graph:** common funder, direct transfers, same-slot purchases, recurring co-launch behavior, deployer relation, synchrony; produce a documented Wallet Independence Score rather than trusting wallet tags.
* **Deployer:** age, prior launches, prior outcomes, funding source, related-wallet sell pattern, creator inventory.
* **Social:** timestamped mention velocity, unique authors, author age/diversity, repeat-text/bot rate, cross-platform propagation.
* **Non-obvious composite features:**
  * `Independent Demand Acceleration = buyer acceleration × independence × retention × liquidity-growth`.
  * `Toxic Supply Overhang = linked early inventory × unrealized profit × estimated sell propensity`.
  * `Sell Absorption = size-normalized drawdown × recovery time × subsequent independent buyers`.
  * `Quality-Adjusted Volume = raw volume × diversity × independence × non-repetition × liquidity quality`.

**Tradeable labels:** from a realistic executable entry, calculate `+20% before −10%`, `+30% before −15%`, `+40% before −20%`, and `+50% before −25%`; MFE, MAE, time-to-barrier, survival, graduation, post-graduation behavior, actual quoted exit, failed transaction, and net PnL. Graduation alone is an auxiliary label only.

**Validation protocol:** chronological train / validation / untouched test, grouped by launch day to prevent near-duplicate contamination; walk-forward re-fit; calibration; bootstrap CIs; predeclared strategy count; comparisons with cash, SOL, random eligible token, raw volume, buyer growth, holder growth, simple momentum, smart-wallet label, and established-meme momentum. Reject a model unless it materially improves **net** out-of-sample results after stress.

---

## 7. Execution design and stress test

### Venue and routing policy

* Prefer the canonical direct pool only when it is verified and the direct quote is better after all fees; otherwise compare a Jupiter quote with route details.
* Use a dedicated burner wallet with only the exact risk allocation. Never connect a main custody wallet to a fresh launch interface.
* Base Solana fee is 5,000 lamports/signature. Set dynamic CU limits; use account-aware recent priority fees, not a global constant.
* Use Jito/MEV protection only after comparing its current tip to the expected benefit. Jito minimum tips and p95 tail tips are distinct states; do not reflexively pay p95 for a $10 trade.
* Maximum chase: **0% until a model establishes a chase rule**. A missed setup is cheaper than unbounded adverse selection.
* No market order without an immediate exact quote, an explicit max input/price, and an independent exit quote.

### Mechanical friction calculation

[`m100/scripts/execution_stress.py`](m100/scripts/execution_stress.py) was run on the actual $100-account configuration. It calculates a balanced constant-product entry/exit, quoted protocol fee, current network/Jito inputs, 1/3/5/10/30/60-second latency sensitivity, 1×/1.5×/2×/3× slippage overlay, and 1×/1.25×/1.5× fee stress. A compact selected-scenario record is saved in [`m100/output/execution_stress_summary.json`](m100/output/execution_stress_summary.json); the full 1,728-scenario grid is reproducible from the committed script/config and intentionally is not stored as a generated artifact.

It makes **no** claim about return or rug probability. Its latency assumption is deliberately visible: 50 bps adverse price movement per second is a stress sensitivity, not a measured forecast.

Illustrative $10 results:

| Scenario | Net mechanical/stress loss | Required gross move just to break even | Meaning |
|---|---:|---:|---|
| $15k total liquidity, 1.25% pool fee, 1 second / 50 bps adverse latency, no Jito tip | $0.3001 (3.00%) | 3.09% | Published fees dominate at this size; one-leg AMM impact is about $0.0133. |
| $2k total liquidity, same fee/latency | $0.2991 (2.99%) | 3.08% | An immediate reversal partly unwinds own impact, but entry one-leg impact is already $0.099 (0.99%). A later exit after changing flow is much worse than this toy reversal. |
| $50k total liquidity, 0.30% fee, same latency | $0.1117 (1.12%) | 1.13% | This is closer to economical mechanics, but says nothing about organic demand or rug risk. |
| $15k liquidity, 1.5× fees, 3× slippage overlay, 60 seconds at stress rate, final-refresh p99 Jito tip | $3.5829 (35.83%) | 55.83% | Mild-looking displayed liquidity cannot rescue a latency-sensitive setup. |

This fails the robustness requirement for fresh launches: the apparent edge disappears under modest latency/fee pessimism. It supports a high liquidity threshold and a no-trade default.

### Stops, time stops, and exits

Memecoin stops are not treated as guaranteed loss caps. A future validated position would have:

* planned normal loss defined from a **sell quote**, not a chart stop;
* immediate exit if technical authority, liquidity, creator/cluster or transferability conditions change;
* a 30-minute time stop for a momentum/pullback hypothesis unless pre-registered flow conditions improve;
* staged reduction only when the outcome model exists; no averaging down, martingale, leverage, revenge trade, or rescue add;
* a full catastrophic-loss reservation equal to the entire position.

---

## 8. $100 architecture, ruin rules, and Kelly

There is no calibrated trade distribution, so no Kelly fraction, Monte Carlo terminal wealth, or ruin percentage is reported. Inventing those numbers would violate the mandate.

### Deployment architecture if—and only if—a strategy is later validated

| Bucket | Amount | Rule |
|---|---:|---|
| Operational native-gas reserve | **$5.00** (~0.0524 SOL at snapshot) | Counts inside the $100; use only in a burner wallet after explicit authorization. Enough for many normal fees and a limited number of elevated tips, but do not turn it into a bidding war. |
| Untouched cash reserve | **$75.00** | Never used for averaging down or a same-day re-entry. |
| Active risk sleeve | **$20.00** | Maximum capital earmarked for experimentation, not an automatic position. |
| Maximum simultaneous positions | **1** | Correlated memes and shared Solana liquidity do not create diversification. |
| Ordinary future notional | **$5.00** | Only after all four committees approve. |
| Exceptional future notional | **$10.00** | Requires all gates, verified depth, and a validated model. |
| Absolute maximum per position | **$15.00** | The full $15 is catastrophic risk, not a stop-defined risk. |
| Normal planned loss on a $10 exceptional position | **≤$1.50** under its quote/stress plan | This is not a promise. The catastrophic case remains $10. |

### Account-level stop rules

* **Daily loss limit:** $4 realized or conservatively marked loss; no new entries until the next UTC day.
* **Rolling seven-day loss limit:** $8; pause and review all assumptions.
* **Peak-to-trough pause:** 10% ($10) drawdown; stop all new trades pending a written model/data review.
* **One catastrophic/unexitable event:** immediately halt the strategy regardless of dollar amount.
* **Hard ruin:** below $25, capital cannot economically sustain a $5 gas reserve plus a conservative minimum test position. No further speculative trading.
* **Economic ruin:** below **$50**, as required.
* **Strategic ruin:** any failure of the research architecture—e.g., live quote mismatch, two gate-approved trades with an unmodeled execution failure, discovered cluster contamination, or a pre-registered calibration failure. Strategic ruin means stop, not adjust thresholds until a new untouched test exists.

**Kelly comparison:** 0 Kelly is the only defensible current choice. 0.10/0.25/0.50/full Kelly are not computable because win probability, payoff distribution, serial correlation, gap/rug rate, and exitability are uncalibrated. Full Kelly is prohibited even after future validation.

---

## 9. Security and rug gate

The gate is a veto gate, not a scorecard that can be compensated by volume.

1. Read mint and Token-2022 extension state from chain/technical report: mint authority, freeze authority, transfer fee configuration, transfer hook, permanent delegate, default account state, mint close authority, confidential transfer, pausable configuration, and metadata mutability.
2. Verify the venue/program and pool ownership, canonical migration path, LP handling, and actual quote.
3. Compute creator, linked creator, bundled, sniper, and funded-cluster ownership from a graph—not only the publicly listed top holders.
4. Test sellability with a non-broadcast/simulation where technically available and quote the actual exit.
5. Treat unknown critical information as negative evidence.

The official Token-2022 permanent-delegate documentation is particularly important: a permanent delegate can authorize transfers and burns on every account of that mint. Renounced mint/freeze authority is therefore insufficient.

---

## 10. Live discovery scan

### Channels queried

* GeckoTerminal Solana new-pools feed;
* DexScreener latest profile and latest boost feeds;
* DexScreener token-pair endpoints;
* RugCheck token reports;
* current Pump/PumpSwap, Jupiter, Raydium and Jito public data.

### Candidate screen at the collection snapshot

| Token | Chain / venue | Observed state | Hard-gate outcome |
|---|---|---|---|
| **ANSEMLEEK** — `HTU9qkrjohLo4GBzBCzQDt7UPNh8fnZK3otjYH8Wpump` | Solana / Pump.fun + PumpSwap | PumpSwap pair created 2026-08-23T23:34:33Z. DexScreener showed ~$15.1k liquidity, ~$41.8k mcap, 114 buys / 71 sells and $5.45k 5m volume at the snapshot. RugCheck showed null mint/freeze authorities and no listed dangerous Token-2022 extension. | **REJECTED.** Only minutes old; simultaneous curve/AMM observations needed reconciliation; no creator graph, bundler inventory, wallet independence, fresh independent-holder trend, social author diversity, or executable exit simulation. The technical pass is not an on-chain/risk pass. |
| **NALA** — `62seDepNrRkMjXwVyF1UACxcQT8WFBeW7QMUxyCLpump` | Solana / PumpSwap | Pair created 2026-08-23T23:05:12Z. DexScreener showed ~$1,978 liquidity and -95.64% 1h; RugCheck flagged low liquidity. | **REJECTED.** Exit depth and violent post-migration loss fail execution/risk gates. |
| **OCTO** — `9z2x2MaVqhN9AQ65ESA8gAY9Tn5HTq7tGn6CXuppump` | Solana / Pump.fun | Pair created 2026-08-23T22:24:51Z; ~$19.5k mcap; 1 buy / 7 sells in the last 5m. DexScreener recorded an active paid boost of 500. | **REJECTED.** Paid boost is not organic attention; flow deteriorated; linked-wallet and sellability data missing. |
| **DIESEL** — `4gbqirCDG4pJXPMgZMJJNj2u73G9puZwkK3pbPgTpump` | Solana / Pump.fun | About 30 days old; ~$10.2k mcap; only ~$25.57 5m volume; RugCheck showed creator balance ~4.61% before graph adjustment. | **REJECTED.** Insufficient current flow/depth and no validated setup. |

No token reached `WATCH → ARMED → ENTRY VALID`. The rejection state is sticky until material new **measured** evidence arrives; a green candle, paid boost, or name recognition does not count.

### Immediate pre-decision refresh: confirms the veto

A second refresh completed at **2026-08-23T23:43:15Z** and is preserved verbatim in [`m100/data/final_refresh_2026-08-23T2343Z.json`](m100/data/final_refresh_2026-08-23T2343Z.json). It turned the ANSEMLEEK screen from merely information-insufficient into an unambiguous execution/risk rejection: the same PumpSwap pair was $2,809 mcap / $2,679 displayed liquidity, with **−93.41% in 5m**, **−92.74% in 1h**, and 315 sells versus 164 buys in 5m. RugCheck then reported a low-liquidity risk. NALA remained at ~$1,969 liquidity with zero buys and three sells in 5m, after −95.66% in 1h. OCTO still carried its 500 paid boost; DIESEL still had only ~$26 5m volume.

Final refreshed SOL price was $95.0911 (Jupiter block 441268409). The Jito feed's own timestamped update was 23:41:39Z: p75 0.000006 SOL, p95 0.0000591232 SOL, p99 0.00082832 SOL. None of this improves an alpha/on-chain/execution/risk result. It strengthens **NO TRADE**.

### Four-committee decision

| Committee | Required question | Result for every scanned token |
|---|---|---|
| Alpha | Is pessimistic, post-friction net payoff positive? | **VETO.** No calibrated barrier/return model; price movement is already volatile and discovery-feed selection is biased. |
| On-chain | Are technical, creator, holder, bundle and funding risks acceptable? | **VETO.** Some narrow mint checks passed, but creator linkage, wallet independence and bundled inventory were unknown. |
| Execution | Can $10 actually enter and exit at quoted economics? | **VETO.** Low liquidity or no current paired buy/sell simulation; candidate-specific route/exit stress unverified. |
| Risk | Can the $100 survive the full catastrophic case? | **VETO.** A full loss is possible and cannot be justified without demonstrated edge. |

### Final adversarial check

Before any BUY, the answers currently remain adverse or unknown:

1. **What might sellers know?** Early creator/sniper/cluster inventory is unknown.
2. **Who sells into us?** Likely initial curve buyers and paid-promotion attention; not measured as independent.
3. **Are independent wallets connected?** Unknown; graph absent, therefore veto.
4. **Are smart wallets insiders?** Unknown; vendor labels unavailable/untrusted.
5. **Is volume organic?** No evidence; paid boosts and repeated launches cut against the presumption.
6. **Is attention organic?** No timestamped author-level evidence.
7. **Did price front-run the signal?** Fresh candidates already had major hourly moves or collapses.
8. **Is this hindsight?** Yes risk: profile feeds preferentially expose promoted/discovered tokens.
9. **What if liquidity falls 50%?** Current low-liquidity pools become practically untradeable relative to displayed price.
10. **Can the position exit near displayed price?** Not established by a fresh sell quote/simulation.
11. **Would it work without name/ticker/art?** The current candidates do not pass on structure alone.
12. **Why not arbitraged?** The likely answer is latency, private flow,/or insider advantage—not a retail-accessible inefficiency.

Any one of these is sufficient to veto. Multiple vetoes apply.

---

## 11. Missing evidence

The following were deliberately not fabricated:

* complete point-in-time current launch universe and denominator by launchpad;
* exact observed graduation rate for the current regime;
* decoded per-token transaction tape and buyer/seller wallets;
* actual unique buyers, effective independent holders, Gini, graph clusters, common funders, bundlers, sniper inventory, or deployer-link map;
* wallet realized PnL, consistency, trade-stage classification, copy latency, and replicable-wallet alpha;
* candidate-specific social mentions, unique authors, bot rate, account-age distribution and cross-platform propagation;
* current account-aware Solana `getRecentPrioritizationFees` response, transaction simulation, failure rate, Jito inclusion odds, and post-route quote for every candidate;
* tradeable barrier labels, MFE/MAE, real fill history, net expectancy, calibration, or bootstrap/Monte Carlo ruin statistics.

Because these are missing, the correct output is not a lower-confidence BUY. It is no trade.

---

## 12. Highest-value next research step

**Build or obtain a point-in-time, full-universe Solana collector before any live deployment.**

The collector should subscribe directly to Pump/PumpSwap/Raydium/Meteora programs (not poll a top-50 REST feed), record every launch and every trade with slot/time, snapshot reserve and ownership state at fixed decision horizons, resolve wallet funding graphs, store an actual buy/sell quote and fee estimate, and label the executable first-hit barriers after 1/3/5/10/30/60-second delays.

The Zenodo v1.4 corrigendum makes this bottleneck unusually clear: a top-50 polling approach provided only roughly 2.77 minutes of visibility at its observed launch rate and invalidated its advertised 24h interpretation. A complete subscription/backfill plus chronological barrier evaluation would improve the decision more than another chart screen, another token list, or another model variant.

Only after that collector produces a sufficiently large untouched, post-friction test sample should the M100 system reconsider `0 Kelly`.

---

## Source register

Primary and current sources used in this report:

* Solana fees: <https://solana.com/docs/core/fees>
* Pump bonding curve: <https://pump.fun/docs/bonding-curve>
* Pump fees (updated 2026-05-20): <https://pump.fun/docs/fees>
* DefiLlama chain / DEX / fee APIs: <https://api.llama.fi/overview/dexs/Solana?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true>, <https://api.llama.fi/summary/dexs/pumpswap>, <https://api.llama.fi/summary/fees/pump>
* Jupiter current price / quote APIs: <https://api.jup.ag/price/v3?ids=So11111111111111111111111111111111111111112>, <https://lite-api.jup.ag/swap/v1/quote>
* Raydium current priority tiers: <https://api-v3.raydium.io/main/auto-fee>
* Jito current tip floor: <https://bundles.jito.wtf/api/v1/bundles/tip_floor>
* Raydium fee references: <https://docs.raydium.io/raydium/build/tips-and-gotchas/launchlab-and-cpmm-fee-reference>
* Meteora DBC configuration: <https://docs.meteora.ag/developer-guide/guides/dbc/bonding-curve-configs>
* Zenodo RED-PUMP-v1.4 metadata and corrigenda: <https://zenodo.org/api/records/21923106>
* Marino et al. Pump.fun paper: <https://arxiv.org/html/2602.14860v1>
* Kamat et al. companion paper: <https://arxiv.org/html/2607.02823>
* Jito sandwich measurement: <https://dl.acm.org/doi/10.1145/3730567.3764493>
* Token-2022 permanent delegate: <https://solana.com/docs/tokens/extensions/permanent-delegate>

All source URLs and machine-readable snapshot values are also recorded in `m100/data/`.
