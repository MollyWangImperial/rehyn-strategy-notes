# Strategy note brief

You write one JSON strategy note per strategy for Rehyn Markets, a geopolitical market-intelligence platform for professional investors.

## Writing rules
- Name a currency pair in the order it is quoted, so the name and the move agree: US dollar against Japanese yen for USD/JPY, Euro against US dollar for EUR/USD.
- Never refer to the prompt, the supplied context, the premise or the instructions; write about the markets.
- Write as a senior analyst explaining a view to a portfolio manager: natural, coherent and easy to follow on first reading, in the standard vocabulary of financial research.
- Open every paragraph, insight and explanation with a topic sentence that states its main point plainly, so the reader knows the conclusion first. The sentences that follow give the mechanism and the figures that support it.
- Explain each point fully: the claim, the mechanism behind it and why it matters for the instrument or market. A vague, compressed or overly brief explanation fails, and so does padding. Be concise without being dense.
- Use only words that are common in financial writing, such as credit spreads, margins, guidance, order backlog, index weight or implied volatility. Avoid rare, literary or invented words, and avoid unusual word pairings: use the collocations an experienced analyst would use, such as weigh on earnings or widen credit spreads.
- Do not stack jargon. Use at most one or two technical terms in a sentence, and never chain nouns into long compounds; unpack them into a clause instead.
- Connect the sentences so the reasoning flows. Each sentence should follow from the one before, with natural links such as because, so, as a result, however or by contrast where they fit, never a list of disconnected statements.
- No metaphors, no dramatic or emotive language such as shock wave, bloodbath or perfect storm, and no cryptic shorthand. Describe effects literally, in financial terms.
- Write with conviction, as a research house does. Express uncertainty only through ranges, likelihoods and conviction. Never write phrases such as not established, unclear, unknown, could not be verified, insufficient evidence, limited data or no data. If a point cannot be supported, leave it out.
- view: judge the user's own view if they gave one, otherwise use none.
- Write as Rehyn. Never use I, me or my. Mark judgement with words like Rehyn estimates or likely.
- This is general research, so describe exposures and risks. Never tell the reader what to buy, sell or hold, and never address their personal circumstances.
- Write in plain professional British English. Be specific. Do not use em dashes.

## Output
One file per strategy at notes/<id>.json, UTF-8 JSON with exactly the same keys and nesting as note_s1.json (the worked example for Variance risk premium harvesting). Follow its structure, tone and length. Use plain apostrophes or typographic ones, never escaped HTML.

## Field rules
- heading: "The Structural Opportunity: " followed by three to five words in title case naming the risk or behaviour the strategy is paid for, as in the example.
- caseLead: exactly two sentences on why the opportunity exists and why it persists, including the geopolitical or policy angle where it applies. caseRest: three sentences on the main risk. Do not describe trading rules here.
- events: six real, well-documented market episodes from 2008 to 2025 that show when this strategy earns and when it loses. Each date is "Month YYYY", theme is one or two words, title at most eight plain words with no colon and never starting with How, What, When, Where or Why, text two sentences of at most 45 words saying what happened and why the strategy gained or lost. effect is up if the strategy gained, down if it lost, mid if mixed. Include at least two geopolitical or policy episodes.
- fig: one large figure per event card, using the same measure for all six cards (for example the peak VIX close, the change in an exchange rate, the oil price move, a credit spread level). Use only figures you are confident are accurate, rounded, with sign and unit where needed, at most seven characters. figNote explains in two sentences what the figure measures, for readers who may not know the measure.
- worstWhen: the month and year of the worst fall, as "Month YYYY". startYear and period: the start of the test window (2010 unless the market did not exist then) and a description in the example's format.
- instrument, rules, costs: short table entries like the example.
- constructionTitle: "Strategy construction, from " ... " to " ..., naming where the return comes from and how the risk is controlled.
- legs: three to five rows with allocations that sum sensibly. entry, size, exit, stop: one short rule each.
- marketWatch: two or three sentences on the indicators and the kind of upcoming events that matter for this strategy now. Do not quote current levels, prices or specific dates. Never recommend a position.
- favourable and adverse: three each, heading at most six words, text two sentences with mechanism and a historical example.
- past: five historical shocks named like "Covid crash, Mar 2020" with the strategy's estimated return in percent during the event (negative for a loss).
- ahead: four numbers, the estimated return in percent over the first month for these scenarios in this order: China blockades Taiwan, OPEC cuts output by 10%, Brazil attacks Colombia, Fed cuts rates by 50bp.
- infoHist and infoForward: one or two sentences each explaining how those figures are calculated, adapted from the example to this strategy's markets.
- altTitle: a question in title case in the style of the example, naming where else investors can find this kind of return.
- related: three other strategies from the library below, chosen because they earn from a different dimension of the same market. why: at most 20 words on how it differs and which risk it is paid to bear. cue: at most seven words on how it relates to this strategy, without undermining it.


## Library (id: name, style, instrument)
v1: Global deep value equity (Value, Equities)
v2: Quality at a reasonable price (Value, Equities)
v3: Value factor investing (Value, ETFs and funds)
v4: Sovereign bond relative value (Value, Government bonds and rates)
v5: Distressed debt investing (Value, Corporate credit)
v6: FX value investing (Value, FX)
v7: REIT discount to NAV investing (Value, Real assets)
v8: Private equity secondaries (Value, Private and structured)
g1: Long-term quality growth equity (Growth, Equities)
g2: AI supply chain thematic equity (Growth, Equities)
g3: Thematic growth ETF allocation (Growth, ETFs and funds)
g4: Core digital asset allocation (Growth, Crypto)
g5: Pre-IPO growth equity (Growth, Private and structured)
i1: Treasury bill laddering (Income, Government bonds and rates)
i2: Barbell bond allocation (Income, Government bonds and rates)
i3: Investment grade bond laddering (Income, Corporate credit)
i4: Dividend quality investing (Income, Equities)
i5: Covered call writing (Income, Options)
i6: Real asset income investing (Income, Real assets)
i7: Direct lending (Income, Private and structured)
i8: Multi-asset income ETF allocation (Income, ETFs and funds)
i9: Stablecoin yield lending (Income, Crypto)
m1: Cross-asset trend following (Momentum, Futures)
m2: Equity momentum investing (Momentum, Equities)
m3: Sector rotation strategy (Momentum, ETFs and funds)
m4: FX trend following (Momentum, FX)
m5: Commodity trend following (Momentum, Commodities)
m6: Crypto trend following (Momentum, Crypto)
m7: Fixed income trend following (Momentum, Government bonds and rates)
s1: Variance risk premium harvesting (Short term volatility, Options)
s2: Earnings long straddle (Short term volatility, Options)
s3: VIX roll yield capture (Short term volatility, Futures)
s4: Long gamma scalping (Short term volatility, Options)
s5: Index dispersion trading (Short term volatility, Options)
s6: FX volatility carry trade (Short term volatility, FX)
s7: Crypto volatility arbitrage (Short term volatility, Crypto)
s8: Oil event volatility trading (Short term volatility, Commodities)
r1: Equity pairs trading (Mean reversion, Equities)
r2: Crypto basis trading (Mean reversion, Crypto)
r3: Convertible bond arbitrage (Mean reversion, Corporate credit)
r4: ETF arbitrage (Mean reversion, ETFs and funds)
r5: Yield curve butterfly trading (Mean reversion, Government bonds and rates)
r6: Commodity spread trading (Mean reversion, Commodities)
r7: Index futures mean reversion (Mean reversion, Futures)
e1: Merger arbitrage (Event driven, Equities)
e2: Post-earnings announcement drift (Event driven, Equities)
e3: Scenario-based hedged allocation (Event driven, ETFs and funds)
e4: Central bank event trading (Event driven, Government bonds and rates)
e5: Special situations credit investing (Event driven, Corporate credit)
e6: Supply shock event trading (Event driven, Commodities)
e7: Catastrophe bond investing (Event driven, Private and structured)
c1: G10 FX carry trade (Macro and carry, FX)
c2: Yield curve steepener trade (Macro and carry, Government bonds and rates)
c3: Commodity roll yield carry (Macro and carry, Commodities)
c4: Gold real yield allocation (Macro and carry, Commodities)
c5: Risk parity allocation (Macro and carry, ETFs and funds)
c6: Short-duration high yield investing (Macro and carry, Corporate credit)
c7: Global macro futures overlay (Macro and carry, Futures)
c8: Autocallable note laddering (Macro and carry, Private and structured)
c9: Inflation-linked infrastructure investing (Macro and carry, Real assets)
d1: Tail risk hedging (Defensive, Options)
d2: Strategic gold allocation (Defensive, Commodities)
d3: Safe haven currency allocation (Defensive, FX)
d4: Long volatility hedging (Defensive, Futures)
d5: Minimum volatility equity (Defensive, ETFs and funds)
d6: Long-duration Treasury hedge (Defensive, Government bonds and rates)
