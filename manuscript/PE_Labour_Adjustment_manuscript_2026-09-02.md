Private Equity and Labour Adjustment

across Pre-Deal Hiring States

Daewoong Kang (Draft Version)

ABSTRACT

Most evidence on heterogeneous real outcomes after private equity investment turns to the deal, the financing environment, or the sponsor. We ask whether recent target-level hiring also predicts subsequent labour adjustment. We link private equity investments to monthly Korean National Pension records and match each target to untreated firms in the same industry, size, prior employment-growth, age, and pre-deal hiring-state cells. A one-interquartile shift towards lower prior hiring is associated with a 0.20-log-point larger treated-minus-control increase in worker inflows. Comparable untreated firms also rebound from low-hiring states, but their gradients are far smaller. The control design is material: under conventional matching, assigned control outcomes covary with the target's hiring state; matching within state terciles nearly eliminates this control-side slope. The result remains in worker-entry counts, which remove employment from the denominator. Low-hiring targets also show more churn but smaller net-employment gains, and the separation response is too imprecise to isolate an exit margin. The heterogeneity is thus concentrated in worker inflows rather than net job growth. The design absorbs observable state-dependent rebound, but it cannot exclude sponsor selection on private information about future demand, financing, or organisational change.

Keywords: Private equity; Employment; Worker flows; Heterogeneous responses; Administrative data

JEL classification: G34, G24, J23, J63

## 1. Introduction

Employment after private equity investment varies widely across target firms. Prior work relates this variation to transaction form, financing conditions, and sponsor characteristics (Davis et al. 2014, 2025). We examine a less studied source of heterogeneity: the target's own operating condition before the deal. In particular, does recent hiring history predict how the workforce adjusts after investment? A firm that has hired little for a year enters a transaction from a different position than an otherwise similar firm that has been adding workers steadily. Weak demand, financing constraints, recruiting capacity, organisational delay, or the timing of labour demand could all produce the same history. We do not attempt to recover that latent condition. The narrower question is whether recent hiring provides a useful ordering of subsequent worker inflows.

That ordering creates its own counterfactual problem. Low-hiring firms may rebound without private equity. If the rebound varies with the state used to classify target responses, matching only on industry, size, employment growth, and age can assign systematically different untreated paths to low- and high-hiring targets. The resulting treated-minus-control gradient would then mix variation in target outcomes with variation in the constructed counterfactual.

We address this problem in two steps. The primary design matches targets to untreated firms within a coarse pre-deal hiring-state stratum as well as industry, size, prior employment growth, and age. We then compare the target gradient with an empirical distribution obtained from untreated pseudo-events that undergo the same state construction, matching, outcome transformation, adjustment, and estimation. The first step limits observable state dependence in assigned controls; the second measures the rebound that remains among untreated firms. The data link private equity investments in Korea to monthly National Pension records of insured employment, worker entries, and worker exits. The baseline matched universe contains 379 investment events. Requiring a complete earlier state, complete outcome windows, and controls from the same hiring-state stratum leaves 286 events for the primary gradient analysis. Higher state values denote lower pre-deal hiring intensity, and the outcome is the treated-minus-control change in the log hiring rate over the twelve months after investment relative to the preceding twelve months.

The gradient is 0.7101, with a 95 percent treated-event bootstrap interval of [0.3187, 1.1254]. Moving one interquartile range towards lower prior hiring corresponds to a 0.2005-log-point larger matched response [0.0900, 0.3177], or about 22 percent on a multiplicative scale. This is cross-target variation in the matched response, not an estimate of the average effect of private equity investment. Low-hiring untreated firms also rebound, but by much less. Across the 1,205 pseudo-events used by the primary procedure, the reference distribution has a mean gradient of 0.1010 and a standard deviation of 0.1538. The target estimate is 0.6091 above that mean, or 3.96 reference-distribution standard deviations; the centred, two-sided empirical p-value is 0.0005. What distinguishes the targets is the size of the relationship relative to untreated firms processed in the same way.

The matching design is consequential. On the same 286 events, conventional matching produces a gradient of 0.4698 and state-balanced matching a gradient of 0.7101. In the unwinsorised decomposition, the treated-side slope is fixed at 0.8425. The control-side slope with respect to the target's state falls from 0.2950 to 0.0056 once the state tercile enters the exact-matching cell. Conventional controls thus supply different untreated paths along the very dimension used to measure heterogeneity. This pattern gives empirical content to a familiar concern in observational heterogeneity analysis: overall covariate balance need not deliver balance within strata of an effect modifier (Dong et al. 2020; Yang et al. 2021). Direct matching on every moderator is neither necessary nor always feasible. But when a proposed moderator also predicts untreated outcomes, its relation to the assigned counterfactual should be reported and, where support permits, reduced by design.

The result is specific to worker inflows rather than an artefact of scaling flows by employment. The state gradient is 0.6315 when the outcome is the log number of worker entries, and 0.6957 in a diagnostic that also includes the change in log employment. Net employment moves differently: it rises relative to matched controls on average, yet its cross-state gradient is -0.0580. Low-hiring targets therefore record larger inflow responses without larger net-employment gains. Churn follows the inflow pattern, whereas the separation gradient is too imprecise to identify a distinct exit or replacement margin.

These margins connect the paper to two strands of private equity research. Davis et al. (2014) show that gross job creation and destruction can be substantial even when net employment changes are modest, while Davis et al. (2025) document heterogeneity by transaction type, market conditions, and sponsor characteristics. Our worker flows are not establishment-level job flows, but they reveal a related limitation of net employment: it can hide where labour adjustment occurs. We add recent target hiring as a pre-deal dimension along which that adjustment is sharply concentrated.

Recent low hiring is an empirical state, not a structural diagnosis. Financing constraints, governance or managerial changes, recruiting capacity, product-market opportunities, and non-convex adjustment costs all give plausible accounts of the pattern (Boucly et al. 2011; Kaplan and Strömberg 2009; Gompers et al. 2016; Cooper et al. 2015). The observed state does not distinguish among them, and the analysis does not treat it as a persistent firm type or an identified inaction regime. Forward-looking sponsor selection remains the principal threat to causal attribution. A sponsor may choose a low-hiring target after learning about demand, a customer contract, financing, or a management change that is not yet visible in administrative outcomes. Untreated pseudo-events absorb ordinary state-dependent rebound, and the pre-deal diagnostics show no positive divergence of comparable magnitude. Neither exercise can reproduce private information that becomes visible only after investment.

The matched population also bounds the result. It consists mainly of smaller Korean private firms and includes minority growth investments as well as control transactions. The estimates need not extend to large public-to-private buyouts or to settings with different labour markets, pension reporting, and private equity institutions.

The paper's contribution is twofold. Substantively, it shows that recent target hiring identifies where post-investment worker inflows are concentrated, and that this ordering differs from the ordering of net employment. Methodologically, it shows that the moderator also belongs in the counterfactual diagnostic when it predicts untreated paths. The claim is about the location and benchmarking of realised heterogeneity, not a unique organisational mechanism or an unconditional causal effect of private equity ownership. Section 2 develops the link to private equity and labour-adjustment research. Sections 3 and 4 describe the data and design. Section 5 presents the main evidence, Section 6 examines pre-deal dynamics and remaining selection, and Section 7 reports timing and transaction-form checks. Section 8 concludes.

## 2. Related literature and empirical motivation

## 2.1 Private equity, employment, and heterogeneous adjustment

Private equity employment effects vary across both transactions and outcomes. Davis et al. (2014) report modest net employment changes alongside much larger gross job creation and destruction around U.S. buyouts. Davis et al. (2025) further show that real responses differ with transaction type, market conditions, and sponsor characteristics. A single average change in employment therefore misses economically important variation in who adjusts and on which margin. Evidence outside the United States reaches a similar conclusion from different settings and measures. French targets grow after some leveraged buyouts, Swedish buyouts alter employment composition, and German transactions carry worker-level consequences (Boucly et al. 2011; Olsson and Tåg 2017; Antoni et al. 2019). Studies of Japanese buyouts and Korean restructuring transactions add evidence from Asia (Blind and Lottanti von Mandach 2021; Koo 2016). Differences in coverage, institutions, and measurement make these estimates complements rather than direct replications.

Korean pension records add a measurement margin that transaction databases and annual accounts rarely provide. They report monthly insured-worker entries, exits, and employment for predominantly private firms. We can thus measure recent hiring before the outcome window and distinguish worker movement from the employment stock. Worker flows and job flows are not interchangeable: the former track people entering and leaving an employer, whereas the latter track positions created or destroyed. A firm may turn over many workers with little net change in employment. Related work studies career paths, workplace safety, pay dispersion, labour-market power, and implicit contracts after private equity investment (Agrawal and Tambe 2016; Cohn et al. 2021; Fang et al. 2026; Herkenhoff et al. 2025). We instead ask which pre-treatment target condition orders the realised labour response.

Most heterogeneity research starts with the transaction or the investor. Control rights, financing conditions, strategy, and sponsor experience are natural candidates. Targets receiving similar investments, however, can arrive with very different recent operating histories. We use hiring before the deal as a target-side ordering variable and ask both whether it predicts subsequent worker inflows and whether it also predicts the untreated path used for comparison.

## 2.2 Why pre-deal hiring may matter

Low hiring before a deal is observationally compatible with several conditions: weak demand, limited finance, little need to expand, recruiting difficulty, or delayed organisational adjustment. Private equity may coincide with changes on any of these margins. The state is therefore useful as an empirical summary of recent activity, not as a label for one latent mechanism.

Financing capacity is one possible mechanism. Boucly et al. (2011) find stronger growth after French leveraged buyouts among firms more likely to have been financially constrained. More generally, private equity can change access to capital and the ability to finance investment or expansion (Kaplan and Strömberg 2009). A low-hiring target could respond strongly if investment relaxes a binding constraint. Our accounting data cannot isolate that channel. Cash, leverage, interest coverage, and profitability do not order the hiring response as clearly as the hiring state in the audited subsample (Section 6.2). Those measures are imperfect proxies, and audited firms are a selected, generally larger group. Their weak coefficients do not rule out financial constraints.

Operational change offers another account. Sponsors can alter incentives, monitoring, management, recruiting, and growth strategy (Kaplan and Strömberg 2009; Gompers et al. 2016). A firm that has hired little may have more scope for recruitment or reorganisation, whereas a firm already expanding rapidly may have less scope for a further proportional increase. The worker-flow data cannot identify which intervention, if any, generates the response. Non-convex adjustment costs provide a third motivation. Fixed or organisational costs can make employment adjust in episodes rather than continuously (Cooper et al. 2015). A low-hiring period may precede a larger adjustment once its benefits exceed those costs. We use this idea only as motivation; the empirical state is not an estimated inaction band.

No private equity mechanism is needed for the most immediate alternative. A temporary hiring pause or unusually weak year may be followed by a return towards normal activity. Because the outcome compares post-deal hiring with the preceding year, such rebound creates a positive state gradient even for untreated firms. The relevant benchmark is therefore not zero. It is the distribution of gradients among untreated firms that enter comparable observed states and are processed under the same design. The pseudo-event analysis estimates that background state dependence directly. Rebound also affects matching. If controls are selected without regard to hiring state, their later outcomes may vary with the state of the targets to which they are assigned. A treated-minus-control gradient would then embed both target heterogeneity and a control-side slope. Matching within state terciles and reporting the control-side component address this observable source of contamination.

Alternative state definitions help distinguish a broad recent condition from a short pause at closing. The duration of the no-entry spell already under way should be most informative under the latter account; hiring over the preceding year should dominate if the state reflects a broader history. A state measured two to three years earlier should also weaken if the relevant condition is recent rather than persistent. Section 6 and Online Appendix B report these comparisons. Employment growth provides a related but distinct comparison: low entries may accompany contraction or a pause in expansion. We therefore condition on pre-deal employment growth and separately residualise the state on size, industry, growth, age, and seasonality. These exercises clarify what the state summarises without claiming to purge every observed or unobserved firm condition.

Forward-looking sponsor selection is harder to address. A sponsor may know about future demand, a contract, financing, or a management change before that information appears in worker flows. Matching cannot remove such information, and untreated pseudo-events cannot reproduce it. Nor must it generate a visible pre-deal trend. Accordingly, we treat the hiring state as an ordering variable for realised post-investment heterogeneity. The empirical tests ask whether low-hiring targets have unusually large inflow responses relative to observably comparable untreated firms, whether a short pause explains the ordering, and whether net employment moves in the same way. They do not identify financing constraints, organisational slack, or a permanent firm type.

## 3. Institutional setting and data

## 3.1 National Pension records and employment measurement

We measure insured employment and worker flows with monthly records from Korea's National Pension Scheme (NPS), available from November 2015 through May 2026. For each reporting workplace, the data record entries and exits of insured workers and the number of insured employees. The monthly frequency permits a hiring state well before the deal and separates later worker flows from changes in employment. The state and outcome windows do not overlap. The state uses months -24 through -13, the baseline outcome months -12 through -1, and the post-investment outcome months +1 through +12. Entries used to construct the state therefore do not enter the baseline hiring outcome, and the transaction month is omitted.

NPS reporting is administered at the workplace (saeopjang) level, whereas transactions are linked to firms through business registration numbers. A business can operate more than one registered workplace. We aggregate the pension records to the business-registration-number level and use that identifier as the empirical firm unit. We also track changes in the number of registered workplaces around the transaction because consolidation, re-registration, or another administrative reorganisation could otherwise appear as worker movement in the pension records. Online Appendix C examines this issue directly. We interpret an NPS entry as an administrative inflow of an insured worker and use 'hire' or 'hiring' as shorthand after this qualification. The record does not identify the recruiting decision behind an entry: re-registration, payroll consolidation, or another reporting change can occasionally produce the same observation. Online Appendix C checks the accounting relation among entries, exits, and employment; excludes large discrepancies and changes in workplace counts; and reconstructs inflows from employment changes and separations.

Coverage is limited to NPS-insured workers. The data omit workers outside the scheme, informal labour, hours, occupations, vacancies, recruiting expenditure, and the managerial decision behind an entry or exit. The outcomes should be read as insured-worker flows and insured employment, not complete measures of labour input. The records also report the contribution base used for pension contributions. Statutory caps and floors make it a measure of pensionable earnings rather than total compensation; we use it only in Online Appendix F.

## 3.2 Private equity investments, sample construction, and supplementary data

We identify investments in Korean firms from PitchBook and link them to NPS records. Of the 379 matched events, 283 link by business registration number and 96 through manually reviewed firm-name matches. Ambiguous candidates are excluded. The treatment follows the private equity classification used to build the transaction sample and includes minority growth investments as well as control transactions; 'buyout' is reserved for the relevant subset. The transaction file begins with 752 private equity investment events. We exclude 168 that cannot be linked to NPS records, 120 without sufficient pre-investment history, 75 with fewer than five insured employees at the deal, and 10 without an eligible baseline control cell. The baseline matched universe contains 379 events.

The average-effect and heterogeneity samples branch separately from this universe. The average-effect analysis contains 367 events that meet its outcome-availability rule. Conventional heterogeneity matching yields 301 events; adding the hiring-state restriction yields the 286-event primary gradient sample. The latter is not obtained by successively removing observations from the 367- or 301-event samples. The 93 events lost between the 379-event universe and the primary gradient sample have four sources: 53 lack a complete state window, one falls below five insured employees during that window, 17 lack an eligible control once the state restriction is imposed, and 22 lack a usable complete-window log-hiring outcome.

Each of the 379 treated events has a distinct business registration number, so the target sample does not contain repeat transactions for the same empirical firm. Sponsors can recur across targets; Online Appendix E examines that dimension. The primary state-gradient sample contains transactions from November 2017 through May 2025. Its timing is constrained by the requirement that both the earlier state window and the complete twelve-month post-investment window be observed. The baseline matched universe is less restrictive because construction of a match does not itself require a complete post-investment outcome window.

The matched sample is tilted towards smaller firms. Baseline targets have median insured employment of 79.8 and mean employment of 218.2, compared with a median of 135.6 among identified targets outside the matched design. The median deal year is 2021, and the targets span 44 two-digit industries. Table 1 reports sample construction and covariate balance. In the 286-event gradient sample, treated firms and controls are close in size, employment growth, hiring state, prior hiring, and prior separations. Firm age has the largest absolute normalised difference, at -0.1676. These statistics cover observed matching variables and nearby measures; they say nothing about unobserved determinants of investment or hiring.

Audited annual accounts supply cash, assets, liabilities, interest expense, revenue, and operating income. Because statutory audit coverage selects a smaller, generally larger-firm subsample, financial data are not required for the worker-flow analysis. The one-year audited analysis contains 147 events. Annual shareholder records identify large owners and stakes. We use them to measure acquired ownership, classify majority and minority investments where possible, and check the year in which a sponsor first appears. Their annual frequency cannot replace transaction-month dating in a monthly design.

### Table 1. Sample construction and characteristics of the matched population

Panel A. Sample construction

| Private equity investment events identified | 752 |
|---|---|
| Unable to link to NPS records | -168 |
| Insufficient pre-investment history | -120 |
| Fewer than five insured employees at transaction | -75 |
| No eligible baseline control cell | -10 |
| Baseline matched universe | 379 |
| Average-effect sample (≥6 observed months per window, target and a control) | 367 |
| Conventional heterogeneity sample | 301 |
| Primary gradient sample | 286 |
| State window, months -24 to -13, not fully observed | -53 |
| Employment below five within the state window | -1 |
| No eligible control cell under the additional hiring-state restriction | -17 |
| No usable primary log-hiring outcome | -22 |
| Complete transaction-characteristic sample | 180 |
| Audited financial-statement sample used in the one-year analysis | 147 |

Notes. The primary gradient sample additionally requires the treated target and its controls to belong to the same pre-deal hiring-state tercile; Section 4.1 describes this matching restriction.

Panel B. Target characteristics and sample scope

| Characteristic | Matched targets | Identified targets not enteringthe matched design |
|---|---|---|
| Median insured employment | 79.8 | 135.6 |
| Mean insured employment | 218.2 | - |
| Median deal year | 2021 | - |
| Two-digit industries represented | 44 | - |

Panel C. Covariate and state balance in the primary 286-event sample

| Variable | Treated | Primary matched controls | Normaliseddifference |
|---|---|---|---|
| Log insured employment | 4.442 | 4.380 | +0.0538 |
| Pre-deal employment growth | +0.095 | +0.080 | +0.0651 |
| Firm age, years | 16.524 | 18.099 | -0.1676 |
| Pre-deal hiring state S | -0.352 | -0.343 | -0.0390 |
| Prior hiring rate, 12 months | 0.436 | 0.415 | +0.0624 |
| Prior separation rate, 12 months | 0.352 | 0.350 | +0.0075 |

Notes. The 367-event average-effect sample and the 286-event primary gradient sample are parallel branches of the 379-event baseline universe rather than successive restrictions. The indented rows below the primary gradient sample account for the 93 events excluded from that branch. The primary matching procedure imposes an additional restriction on the target’s pre-deal hiring state, as described in Section 4.1. The 301-event conventional heterogeneity sample is constructed without that additional restriction. Panel C compares the 286 treated events in the primary sample with their primary matched controls. The normalised difference is . Prior hiring and separation rates refer to the twelve-month pre-investment outcome window.

## 4. Research design

## 4.1 Matching and the pre-deal hiring state

For the baseline comparison, each target is matched to five firms never observed as private equity targets. A control must be present in the same event month and in the same exact cell for two-digit industry, size, pre-deal employment growth, and age. All 752 identified targets are excluded from the control pool, including those that do not enter the final matched samples.

Firm size is measured as mean insured employment over months  through  and divided at 5, 10, 20, 50, 100, and 250 employees. Pre-deal employment growth compares employment over months  through  with employment over months  through  and is grouped using cutoffs at  and  percent. Firm age is measured from first observed NPS enrolment and grouped at five and fifteen years. Within an eligible exact cell, the five nearest controls are selected using log pre-deal employment and pre-deal employment growth. The neighbour distance is

where pre-deal employment growth is clipped to  before differencing.

We exclude a target if its exact cell contains no eligible untreated firm rather than extrapolate beyond common support. The resulting estimates apply only where observably similar controls exist. This restriction improves comparability but does not make investment conditionally random.

The primary heterogeneity analysis adds the target's recent hiring condition to this matching structure. Let  denote worker entries over months  through , and let  denote mean insured employment over the same twelve state-window months. We define

Higher values of  indicate lower pre-deal hiring intensity. The negative transformation is used so that a positive state gradient corresponds to a larger subsequent hiring response among targets that had been hiring less actively. The state window is deliberately separated from the baseline outcome window.  uses months  through , while the pre-investment hiring outcome uses months  through . This separation prevents the same worker entries from mechanically determining both the moderator and the pre-period component of the outcome.

The primary design divides the state into terciles and adds the tercile to the exact-matching cell. Five nearest controls are then selected within that cell. We call this state-balanced matching. Only the coarse tercile is exact-matched; the continuous state remains the regressor in the gradient specification. The restriction therefore changes the comparison group without discretising the estimand (Stuart 2010; Iacus, King, and Porro 2012; Dong et al. 2020; Yang et al. 2021). The restriction follows from the estimand. Overall covariate balance does not guarantee balance within strata of an effect modifier. Here, untreated outcomes may vary with the same hiring state used to order target responses. Regressing the treated-minus-control response on that state would then combine the target-side slope with a slope in the counterfactual assigned to targets at different state values. Section 5.2 reports both components under conventional and state-balanced matching.

State balance removes an observable dependence of assigned controls on the moderator. It does not equalise unobserved growth opportunities, financing, managerial plans, or information. Selection on target-specific information held by the sponsor remains possible.

## 4.2 Outcomes and the state-gradient estimand

For a firm  and twelve-month window , define the hiring rate as

where  is the total number of NPS worker entries during the window and  is mean insured employment over the same months. The measure is not annualised. The primary pre-investment window covers months  through , and the post-investment window covers months  through . For target , let  denote its matched control firms. The event-level matched response is

A positive  means that the target's hiring rate increased more, or declined less, than the mean change among its matched controls. The primary heterogeneity estimand is the gradient of  with respect to the target's continuous pre-deal state. We partial out log pre-deal size, pre-deal employment growth, firm age, and one-digit industry from both  and . Let  and  denote the corresponding residuals. We estimate

Because higher  indicates lower pre-deal hiring intensity, a positive  means that targets entering from lower-hiring states exhibit larger post-investment changes in hiring relative to their state-balanced controls. The coefficient is a cross-target gradient in a matched response. It is distinct from the average post-investment change in Section 5.1 and is neither a structural labour-adjustment parameter nor a forecasting coefficient for future deals.

The primary gradient requires complete twelve-month pre- and post-investment windows and positive worker entries in both, as required by the logarithm. This last restriction removes three otherwise eligible events. Online Appendix B.3 reports inverse-hyperbolic-sine and log(1 + HR) specifications that retain zero-entry windows. The average-effect sample uses a different availability rule: at least six observed months in each required window for the target and an eligible control, yielding 367 events. The 286-event gradient sample requires complete state and outcome windows. Estimates from the two samples answer different questions and need not describe a common population.

We winsorise the treated event-level response at its 5th and 95th percentiles and apply the same absolute cutoffs to pseudo-event outcomes. Online Appendix B reports unwinsorised results, alternative cutoffs and transformations, and other matching and weighting procedures. Because employment enters the denominator of HR, we also estimate gradients for the log number of worker entries. A further diagnostic adds the post-investment change in log employment. Employment is itself an outcome, so this is not a causal control; it asks only whether denominator movements drive the rate result. Net employment is measured directly from the employment stock.

## 4.3 Untreated reference distribution and statistical inference

Zero is not the relevant null for the state gradient. Mean reversion, temporary hiring pauses, and other untreated dynamics can produce a positive relation between low prior hiring and subsequent hiring even without private equity. We estimate this background relation with untreated pseudo-events. Eligible firms receive pseudo-event dates and undergo the same state construction, matching, transformation, covariate adjustment, and winsorisation as the targets. The primary pool contains 1,205 pseudo-events. In each of 2,000 draws, we randomly order eligible events within the matching structure, accumulate observations until 286 are retained, and re-estimate the gradient. The distribution therefore incorporates the rebound observed among untreated low-hiring firms.

This is an empirical reference distribution, not a randomisation distribution: investment is not randomly assigned, and the pseudo-events do not reproduce an experimental assignment mechanism. The comparison asks whether the target gradient is unusual relative to untreated state-dependent movements generated by the same procedure. It cannot reproduce sponsor information absent from the data.

The 2,000 primary draws have mean 0.1010 and standard deviation 0.1538. The target gradient of 0.7101 is 3.96 reference-distribution standard deviations above that mean. We calculate the centred two-sided empirical p-value as

Because the observed gradient lies farther from the reference mean than every simulated gradient, no draw enters the numerator apart from the add-one correction. With 2,000 draws, the reported 0.0005 (= 1/2,001) is therefore the smallest attainable empirical p-value, not an interpolated tail estimate. Here, b indexes the reference draws, the bar over g denotes their mean, and the superscript obs identifies the target estimate. Ties enter the numerator. The reference-distribution p-value measures how unusual the target gradient is relative to untreated gradients; the treated-event bootstrap interval instead quantifies uncertainty in the target estimate.

For the target interval, we resample treated events together with their matched sets. Two thousand bootstrap draws give [0.3187, 1.1254]. The 286 targets are distinct firms and use 1,144 distinct controls; 95.02 percent of controls appear in one event and none in more than three. Online Appendix D.5 reports checks for this limited reuse.

A causal reading still requires matched controls to approximate the state-specific path each target would have followed without investment, conditional on observed matching variables and hiring state. That condition is not testable. Section 6 examines its observable implications, while treating forward-looking sponsor information as the main remaining threat.

## 5. Main results

## 5.1 Average post-investment responses

We first report average matched changes to establish the scale of labour adjustment before analysing how it varies with pre-deal hiring. Relative to controls, target employment rises by 0.0878 log points [0.0462, 0.1300] twelve months after the deal, roughly 9 percent. The matched pre-to-post change in the hiring rate is 0.0485 [0.0163, 0.0814], or 4.85 percentage points. Both estimates use the 367-event average-effect sample.

The average separation-rate change is 0.0007 [−0.0353, 0.0398]. The interval spans economically relevant changes in both directions and does not establish that separations were unchanged. Targets thus add employment and worker inflows on average. These averages do not reveal whether the same pre-deal states account for the largest movements in each outcome.

### Table 2. Average post-investment changes relative to matched controls

| Outcome | Matched change | 95% CI | Events |
|---|---|---|---|
| Log employment at +12 months | 0.0878 | [0.0462, 0.1300] | 367 |
| Hiring rate, post 12 months − pre 12 months | 0.0485 | [0.0163, 0.0814] | 367 |
| Separation rate, post 12 months − pre 12 months | 0.0007 | [−0.0353, 0.0398] | 367 |

Notes. Employment is measured at month  relative to mean employment over months  through , and then differenced against matched controls. Hiring and separation rates are twelve-month sums of worker flows divided by mean insured employment over the corresponding window; reported coefficients are treated-minus-control changes from the pre- to the post-investment window. The average-effect sample requires at least six observed months in each required window for the target and an eligible control and is distinct from the 286-event primary state-gradient sample.

## 5.2 Hiring responses across pre-deal hiring states

The average hiring increase conceals a steep cross-target gradient. Targets with lower pre-deal hiring show larger post-investment increases relative to controls matched within the same state tercile. The primary gradient is 0.7101 [0.3187, 1.1254] (Table 3, Panel A). A one-interquartile-range move towards lower pre-deal hiring corresponds to a 0.2005-log-point larger matched response [0.0900, 0.3177], about 22 percent on a multiplicative scale. This magnitude describes variation across target states, not the average effect of investment.

The 1,205-event untreated pool produces a reference mean of 0.1010 and a standard deviation of 0.1538. The target gradient is 0.6091 above that mean, or 3.96 standard deviations, with a centred two-sided empirical p-value of 0.0005. Low-hiring firms commonly rebound; what distinguishes the targets is the size of the gradient. Figure 1(a) plots event-level matched responses against the pre-deal state. Figure 1(b) shows the 2,000 empirical reference gradients rather than a parametric approximation; the target estimate lies at the far right of the distribution.

Control selection changes the estimate. On the common 286 events, conventional matching yields 0.4698; adding the state tercile to the exact cell raises the gradient to 0.7101 (Table 3, Panel B). Panel C locates the difference with an unwinsorised decomposition. Because the target events are identical, the treated-side slope remains 0.8425. The assigned-control slope falls from 0.2950 under conventional matching to 0.0056 under state-balanced matching. Conventional matching therefore assigns different untreated paths to targets in different states. State balance removes most of that observed dependence; it does not establish balance on unobserved information. Panel C is unwinsorised, whereas Panel B reports 5/95-winsorised gradients. Its component slopes are diagnostic and do not subtract to the Panel B coefficients.

Alternative specifications preserve a positive slope but not a fixed magnitude. The gradient is 0.678 with twenty controls, 0.640 when continuous state distance enters neighbour selection, 0.678 with deal-year fixed effects, and 0.346 under inverse-variance weights. Online Appendix B reports the full set.

The cross-target pattern also appears without collapsing each event to a single twelve-month response. A stacked panel built from the 286 state-balanced matched sets gives a Treated  Post  State coefficient of 0.0179 [0.0035, 0.0323] for the monthly hiring rate. Joint Wald tests do not reject zero pre-deal quarter coefficients for either the level path (p = 0.9078) or the state interaction (p = 0.9904); the interaction becomes positive later in the post-deal year. Because this specification estimates a different monthly panel parameter and does not address selection on unobserved sponsor information, we treat it as cross-estimator robustness rather than a replacement for the primary matched-response gradient (Online Appendix D.7, Figure D1 and Table D6).

### Figure 1. Hiring responses across pre-deal hiring states

(a) Matched hiring response and pre-deal hiring state

(b) Target state gradient and untreated reference distribution

Notes. Panel (a) plots the event-level treated-minus-control change in the log hiring rate against the target’s pre-deal hiring state for the 286-event primary sample. Higher state values indicate lower pre-deal hiring intensity. Panel (b) plots the actual 2,000 gradients drawn from the 1,205-event primary untreated pseudo-event pool and estimated using the primary procedure. The vertical line marks the target gradient of 0.7101. The untreated reference distribution has mean 0.1010 and standard deviation 0.1538.

### Table 3. Hiring responses across pre-deal hiring states

Panel A. Primary state gradient

| Quantity | Estimate |
|---|---|
| State gradient | 0.7101 [0.3187, 1.1254] |
| Effect of an interquartile move | 0.2005 [0.0900, 0.3177] |
| Untreated reference mean (SD) | 0.1010 (0.1538) |
| Excess over untreated mean | 0.6091 |
| Standardized distance | 3.96 |
| Empirical two-sided p | 0.0005 |

Panel B. Effect of balancing the pre-deal hiring statePreferred 5/95-winsorised specification, common 286-event sample

| Matching design | Matched gradient |
|---|---|
| Conventional matching, state not balanced | 0.4698 |
| State-balanced matching | 0.7101 |

Panel C. Control-path diagnosticUnwinsorised decomposition, common 286-event sample

| Component slope | Conventional | State-balanced |
|---|---|---|
| Treated-side slope | 0.8425 | 0.8425 |
| Control-side slope with respect to treated state | 0.2950 | 0.0056 |

Notes. Panel A reports the primary 5/95-winsorised specification. The confidence interval is obtained from 2,000 treated-event bootstrap draws. The untreated reference distribution is based on 2,000 gradients constructed from the 1,205 untreated pseudo-events in the primary pool. The empirical two-sided -value follows the centred rule described in Section 4.3. Panel B compares matching procedures on the same 286 treated events. Panel C uses an unwinsorised outcome and is a control-path diagnostic; its component slopes therefore do not subtract numerically to the winsorised gradients reported in Panel B.

## 5.3 Worker inflows and net employment

We next remove employment from the denominator and compare worker inflows with changes in the employment stock. Holding the state-balanced sample fixed, the log worker-entry count has a gradient of 0.6315, an untreated mean of 0.1858, and a two-sided empirical p-value of 0.0110 (Table 4, Panel A). The corresponding figures for the primary log hiring rate are 0.7101, 0.1006, and 0.0005. Adding the change in log employment to the worker-entry-count specification gives a gradient of 0.6957 against an untreated mean of 0.0377 (p = 0.0005). Since employment is post-treatment, this is a denominator diagnostic rather than a causal adjustment.

Net employment has the opposite cross-state pattern. Its gradient is -0.0580, 2.60 reference-distribution standard deviations below its untreated mean (two-sided p = 0.005). This does not conflict with the positive average in Table 2: employment can rise across targets while rising less among those that entered with lower hiring. Churn also rises more from low-hiring states: its gradient is 0.3816, 3.08 standard deviations above the untreated mean (p = 0.002). Because churn includes entries, it is not independent evidence of a stronger exit response.

The separation gradient is 0.1788, with a standardised distance of 1.17 and p = 0.2384. The interval is too wide to isolate a state-dependent separation margin, so we do not infer worker replacement or two-sided reallocation. Within-event contrasts make the difference in margins explicit. The hiring-minus-employment gradient is 0.7536 on 286 common events, 4.56 standard deviations above its reference mean of 0.0232 (p = 0.001). The churn-minus-employment contrast is 0.4539 on 288 events, compared with a reference mean of -0.0750 and a standardised distance of 4.19 (p = 0.001). The robust distinction is between worker inflows and net employment. Low-hiring targets record unusually large inflows but smaller relative employment gains. The available separation evidence does not support a stronger claim about exits or replacement.

### Table 4. Worker-flow and employment gradients across pre-deal hiring states

Panel A. Worker-inflow measures

| Outcome | Gradient | Untreated reference mean | Empirical two-sided p | Events |
|---|---|---|---|---|
| Log hiring rate | 0.7101 | 0.1006 | 0.0005 | 286 |
| Log worker-entry count | 0.6315 | 0.1858 | 0.0110 | 286 |
| Log worker-entry count, controlling for Δ log employment | 0.6957 | 0.0377 | 0.0005 | 286 |

Panel B. Worker flows and employment

| Outcome | Gradient | Standardized distance | Empirical two-sided p | Events |
|---|---|---|---|---|
| Log churn rate | 0.3816 | 3.08 | 0.0020 | 288 |
| Log separation rate | 0.1788 | 1.17 | 0.2384 | 281 |
| Log employment | −0.0580 | −2.60 | 0.0050 | 289 |

Panel C. Within-event outcome contrasts

| Contrast | Estimate | Reference mean / standardized distance | Empirical two-sided p | Events |
|---|---|---|---|---|
| Hiring − employment | 0.7536 | 0.0232 / 4.56 | 0.0010 | 286 |
| Churn − employment | 0.4539 | −0.0750 / 4.19 | 0.0010 | 288 |

Notes. Panel A fixes the primary 286-event state-balanced design while changing the worker-inflow outcome; the untreated reference mean is recomputed for each outcome. The employment-change control in the third row is post-treatment and is used only as a denominator diagnostic. Panel B uses outcome-specific eligible samples. Churn contains worker entries as well as separations and is therefore not independent evidence of an exit response. Panel C constructs contrasts within events. The reference distributions in this table come from an outcome-specific run whose pseudo-event pool contains 1,246 observations, whereas Section 4.3, Figure 1, and Table 3 use the 1,205-event primary pool. The outcome-specific run retains pseudo-events that are available for other outcomes but do not have a defined primary log-hiring response; this accounts for both the difference in pool size and the small difference between the hiring-rate reference means of 0.1006 and 0.1010.

## 6. Validity, interpretation, and remaining selection

## 6.1 Untreated rebound and pre-deal hiring dynamics

State-balanced controls remove an observed source of counterfactual heterogeneity, but they do not by themselves establish causality. We examine two observable alternatives: rebound among low-hiring firms generally and a different hiring path among eventual targets before investment. The untreated distribution addresses the first. Its mean gradient is about 0.101, compared with 0.7101 for the targets. Ordinary rebound is present but too small to account for the target gradient on its own; the comparison does not capture forces specific to firms selected for investment.

Pre-deal diagnostics involve a trade-off. Moving the state window earlier avoids mechanical overlap with the earlier outcome but changes the moderator. Retaining the primary state preserves comparability while allowing the state and earlier outcome to share observations. The non-overlapping specification moves the state to months -36 through -25. Relative to its untreated reference, the pre-deal excess gradient is -0.1770 [−0.4394, 0.0854] across 250 events (Table 5). Its interval excludes a positive divergence close to the post-investment gradient, although the moderator is no longer the primary state.

Keeping the primary state gives a pre-deal gradient of 0.1068 [−0.1955, 0.4351] for 283 events. The post-deal gradient on the same events is 0.7250 [0.3259, 1.1081]. The earlier estimate is much smaller but remains compatible with a meaningful positive relationship. Neither diagnostic dominates: one cleanly separates the windows, while the other holds the moderator fixed. We treat them as complementary evidence rather than tests of the identifying assumption.

Quarterly estimates in Online Appendix D show no persistent positive ordering before investment. The four gradients are +0.087, -0.042, -0.038, and -0.056; their mean is -0.012 [−0.163, 0.131], and a fitted linear drift is -0.038 [−0.600, 0.473]. The estimates are nevertheless too imprecise to exclude moderate differential dynamics. Relative-magnitude calculations following Rambachan and Roth (2023) give a breakdown value of 3.126 at the twelve-month resolution. The quarterly calculation is uninformative because pre-period gradients are too noisy to yield a stable bound. We use both as sensitivity calibrations, not as validation of the design.

### Table 5. Pre-deal dynamics of the hiring-state gradient

| Diagnostic | Value | 95% Interval | Events |
|---|---|---|---|
| Pre-deal excess gradient, non-overlapping earlier state | −0.1770 | [−0.4394, 0.0854] | 250 |
| Pre-deal gradient, primary-state specification | 0.1068 | [−0.1955, 0.4351] | 283 |
| Post-deal gradient, same events | 0.7250 | [0.3259, 1.1081] | 283 |

Notes. The first row avoids overlap between the state and the earlier outcome by moving the state window from months -24 through -13 to months -36 through -25. This produces a mechanically cleaner comparison but changes the moderator relative to the primary specification. The second row retains the primary state definition but shares observations between the state and the earlier outcome. The third row reports the post-investment gradient on the same 283 events as the second row. These specifications are complementary diagnostics rather than formal tests of the identifying assumption. Relative-magnitude sensitivity calculations are reported in Online Appendix D.

## 6.2 What does the pre-deal hiring state capture?

Online Appendix B asks whether the state records a broad period of low hiring or merely a pause already under way at the deal date. Controlling for employment growth leaves a state coefficient of 0.410 [0.078, 0.753]. The historical share of months with no entries predicts the response (0.559 [0.241, 0.885]), whereas the length of the current no-entry spell is estimated at 0.040 [−0.016, 0.107]. Entered jointly, the two coefficients are 0.536 and 0.032. Broader recent history is thus more informative than the duration of the pause at closing.

The state is not a distinct structural trait. Size, industry, employment growth, age, and seasonality explain 63.9 percent of its variation. Residualising on those variables leaves a positive but imprecise coefficient of 0.243 [−0.221, 0.723]. Distance from the deal also matters. A state measured over months -36 through -25 produces a post-deal gradient of 0.268, against an untreated mean of 0.141 and a standardised distance of 0.92. Together with the pause results, this attenuation points to a recent condition rather than a time-invariant firm type.

Accounting variables offer a separate comparison in the audited subsample. Measured in the fiscal year before the deal, clipped at the 1st and 99th percentiles, and standardised, the response coefficients are 0.0255 [−0.0650, 0.1152] for cash to assets, -0.0045 [−0.1027, 0.0875] for leverage, 0.0489 [−0.0420, 0.0891] for interest coverage, and -0.0055 [−0.0911, 0.1018] for profitability. In the same audited setting, the hiring-state coefficient is 0.1087 [0.0229, 0.1964] across 169 events. All coefficients are per standard deviation and use the unwinsorised event-level hiring response. These comparisons do not reject a financing channel. Accounting ratios are noisy proxies for constraints, and audited firms are a selected, generally larger subset. They show only that the available financial measures do not reproduce the same cross-sectional ordering.

## 6.3 Forward-looking sponsor selection and the causal boundary

The diagnostics have less power against sponsor information about future target prospects. A sponsor may invest after learning about demand, a customer contract, financing, or management changes that observably similar untreated firms do not share. Such selection need not appear as a pre-deal trend. Section 6.1 constrains information already reflected in worker flows or employment, but information that remains latent until investment can evade those tests.

Online Appendix D uses fund age as a proxy for deployment pressure. The estimate runs opposite to the prediction that sponsors with greater timing discretion generate larger responses. Fund age is neither random nor a direct measure of target-specific information, so the exercise cannot remove forward-looking selection. Other comparisons have similar limits. Shareholder records check the transaction year but not the month; not-yet-treated firms offer weaker support and may anticipate their own future deals; sponsor exits and non-private-equity ownership changes are sparse or economically different. We report them as scope checks rather than substitute identification strategies.

The evidence makes ordinary mean reversion and continuation of a comparably large visible trend less plausible as complete explanations. It does not eliminate selection on information missing from the pension, transaction, shareholder, and financial data. We therefore interpret the estimate as an unusually large post-investment hiring response among low-hiring targets relative to observably comparable untreated firms. A stronger causal claim depends on the absence of sufficiently large forward-looking sponsor selection.

## 7. Additional evidence and scope checks

## 7.1 Post-investment hiring dynamics

The average hiring difference appears soon after the deal. The first quarterly estimate is positive, with a 95 percent interval of [0.0032, 0.0250], and point estimates remain positive through quarter ten. The first four sum to about 0.048, close to the twelve-month change of 0.0485 in Table 2. Figure 2 traces this average matched path. It is not a quarterly version of the state-gradient analysis, and later quarters draw on fewer events as recent cohorts run out of follow-up.

Worker entries also occur in more months after investment. Higher total entry volume can generate this pattern mechanically: with a fixed number of months, more entries generally leave fewer zero-entry months even if their allocation process is unchanged. Online Appendix A compares the observed incidence with a volume-preserving benchmark that fixes each firm-window's entry total and monthly employment exposure, then reallocates entries across months in proportion to that exposure.

The observed zero-entry share falls by 0.0466. The employment-weighted benchmark predicts -0.0508, leaving an excess change of 0.0042 [−0.0088, 0.0180]. An equal-month benchmark predicts -0.0518 and leaves 0.0052 [−0.0082, 0.0189]. Increased entry volume therefore accounts for most of the broader monthly incidence under these benchmarks. This does not establish unchanged recruiting timing: neither benchmark models firm seasonality, monthly demand shocks, or other allocation determinants.

### Figure 2. Quarterly hiring differences relative to matched controls

Notes. The figure plots quarterly treated-minus-control differences in the hiring rate around the private equity transaction. Estimates are shown with 95 percent event-level confidence intervals. The quarterly specification describes the average matched hiring path rather than the state-gradient estimand. The number of contributing events declines at longer post-investment horizons as the available follow-up period shortens

## 7.2 Transaction form and target composition

Because the sample includes minority growth investments and control transactions, we compare event-level hiring responses across these broad forms. The unadjusted control-minus-growth contrast is 0.1218 log points [−0.0494, 0.2776]. Control targets also enter with lower recent hiring. Adjusting for hiring state, size, employment growth, age, industry, and deal year reduces the contrast to 0.0475 [−0.1062, 0.1958]. Target composition explains part of the raw contrast, but the adjusted interval still permits moderate deal-type heterogeneity. It establishes neither equality nor a distinct control-transaction effect.

Online Appendix E reports ownership-stake and sponsor comparisons. Sponsor experience counts only transactions observed before the focal deal, avoiding look-ahead. We use these estimates to define scope rather than to dismiss transaction- or sponsor-level heterogeneity.

## 8. Conclusion

Recent target hiring sharply orders labour adjustment after private equity investment. In monthly Korean pension records, a one-interquartile shift towards lower pre-deal hiring predicts a 0.2005-log-point larger treated-minus-control increase in the hiring rate. Rebound among untreated low-hiring firms is real but much smaller. Applying the same state definition, matching, transformation, and estimation to untreated pseudo-events yields a mean gradient of 0.1010, compared with 0.7101 for the targets. The empirical benchmark therefore separates the target pattern from the positive state dependence that arises without a private equity event.

The counterfactual is part of the finding. Under conventional matching, assigned control outcomes vary with the target's state. Matching within state terciles nearly eliminates this control-side slope. More generally, a variable used to organise heterogeneous responses should also be examined as a predictor of the untreated path. The heterogeneity lies in worker inflows, not net job growth. It remains in entry counts that remove employment from the denominator, while the net-employment gradient is negative. Churn follows the inflow pattern, but imprecise separation estimates do not identify an exit or replacement mechanism.

The hiring state is a recent empirical condition, not a structural latent state. Conventional characteristics explain much of it; a more distant state and a current hiring pause are less informative than the preceding year's history. The data do not distinguish financing, demand, recruiting, or organisational mechanisms. Forward-looking sponsor selection also remains. Private information may become visible only after investment. The result is therefore an unusually large matched response among low-hiring targets, not an unconditional causal effect of private equity ownership.

The matched support consists mainly of smaller Korean private firms and covers growth and control transactions. Large public-to-private buyouts and other institutional settings require separate evidence. Within that population, recent hiring history reveals a dimension of post-investment adjustment that net employment alone would miss. It also shows why the study of heterogeneous outcomes cannot be separated from the design of the state-specific counterfactual.

References

Abadie, Alberto, and Guido W. Imbens. 2006. "Large Sample Properties of Matching Estimators for Average Treatment Effects." Econometrica 74 (1): 235–67. https://doi.org/10.1111/j.1468-0262.2006.00655.x.

Agrawal, Ashwini, and Prasanna Tambe. 2016. "Private Equity and Workers' Career Paths: The Role of Technological Change." Review of Financial Studies 29 (9): 2455–89. https://doi.org/10.1093/rfs/hhw025.

Antoni, Manfred, Ernst Maug, and Stefan Obernberger. 2019. "Private Equity and Human Capital Risk." Journal of Financial Economics 133 (3): 634–57. https://doi.org/10.1016/j.jfineco.2019.04.010.

Bernstein, Shai, and Albert Sheen. 2016. "The Operational Consequences of Private Equity Buyouts: Evidence from the Restaurant Industry." Review of Financial Studies 29 (9): 2387–418. https://doi.org/10.1093/rfs/hhw037.

Blind, Georg D., and Stefania Lottanti von Mandach. 2021. "Private Equity Buyouts in Japan: Effects on Employment Numbers." Journal of the Japanese and International Economies 59: 101121. https://doi.org/10.1016/j.jjie.2020.101121.

Boucly, Quentin, David Sraer, and David Thesmar. 2011. "Growth LBOs." Journal of Financial Economics 102 (2): 432–53. https://doi.org/10.1016/j.jfineco.2011.05.014.

Braun, Reiner, Tim Jenkinson, and Ingo Stoff. 2017. "How Persistent Is Private Equity Performance? Evidence from Deal-Level Data." Journal of Financial Economics 123 (2): 273–91. https://doi.org/10.1016/j.jfineco.2016.01.033.

Cohn, Jonathan B, Edith S Hotchkiss, and Erin M Towery. 2022. "Sources of Value Creation in Private Equity Buyouts of Private Firms." Review of Finance 26 (2): 257–85. https://doi.org/10.1093/rof/rfac005.

Cohn, Jonathan B., Lillian F. Mills, and Erin M. Towery. 2014. "The Evolution of Capital Structure and Operating Performance after Leveraged Buyouts: Evidence from U.S. Corporate Tax Returns." Journal of Financial Economics 111 (2): 469–94. https://doi.org/10.1016/j.jfineco.2013.11.007.

Cohn, Jonathan, Nicole Nestoriak, and Malcolm Wardlaw. 2021. "Private Equity Buyouts and Workplace Safety." The Review of Financial Studies 34 (10): 4832–75. https://doi.org/10.1093/rfs/hhab001.

Cooper, Russell, John Haltiwanger, and Jonathan L. Willis. 2015. "Dynamics of Labor Demand: Evidence from Plant-Level Observations and Aggregate Implications." Research in Economics 69 (1): 37–50. https://doi.org/10.1016/j.rie.2015.01.002.

Davis, Steven J., and John Haltiwanger. 1992. "Gross Job Creation, Gross Job Destruction, and Employment Reallocation." Quarterly Journal of Economics 107 (3): 819–63. https://doi.org/10.2307/2118365.

Davis, Steven J., John Haltiwanger, Kyle Handley, Ron Jarmin, Josh Lerner, and Javier Miranda. 2014. "Private Equity, Jobs, and Productivity." American Economic Review 104 (12): 3956–90. https://doi.org/10.1257/aer.104.12.3956.

Davis, Steven J., John Haltiwanger, Kyle Handley, Ben Lipsius, Josh Lerner, and Javier Miranda. 2025. "The (Heterogeneous) Economic Effects of Private Equity Buyouts." Management Science 71 (11): 9569–87. https://doi.org/10.1287/mnsc.2021.03890.

Dong, Jing, Junni L. Zhang, Shuxi Zeng, and Fan Li. 2020. "Subgroup Balancing Propensity Score." Statistical Methods in Medical Research 29(3): 659–676. doi:10.1177/0962280219870836.

Dunne, Timothy, Mark J. Roberts, and Larry Samuelson. 1989. "Plant Turnover and Gross Employment Flows in the U.S. Manufacturing Sector." Journal of Labor Economics 7 (1): 48–71. https://doi.org/10.1086/298198.

Fang, Lily, Jim Goldman, and Alexandra Roulet. 2026. "Private Equity and Pay Gaps Inside the Firm." The Journal of Finance 81 (4): 1805–40. https://doi.org/10.1111/jofi.70043.

Gompers, Paul, Steven N. Kaplan, and Vladimir Mukharlyamov. 2016. "What Do Private Equity Firms Say They Do?" Journal of Financial Economics 121 (3): 449–76. https://doi.org/10.1016/j.jfineco.2016.06.003.

Herkenhoff, Kyle, Josh Lerner, Gordon Phillips, Francisca Rebelo, and Benjamin Sampson. 2025. Private Equity and Workers: Modeling and Measuring Monopsony, Implicit Contracts, and Efficient Reallocation. Working Paper No. 33942. National Bureau of Economic Research. https://doi.org/10.3386/w33942.

Iacus, Stefano M., Gary King, and Giuseppe Porro. 2012. "Causal Inference without Balance Checking: Coarsened Exact Matching." Political Analysis 20 (1): 1–24. https://doi.org/10.1093/pan/mpr013.

Kaplan, Steven N., and Antoinette Schoar. 2005. "Private Equity Performance: Returns, Persistence, and Capital Flows." Journal of Finance 60 (4): 1791–1823. https://doi.org/10.1111/j.1540-6261.2005.00780.x.

Kaplan, Steven N., and Per Strömberg. 2009. "Leveraged Buyouts and Private Equity." Journal of Economic Perspectives 23 (1): 121–46. https://doi.org/10.1257/jep.23.1.121.

Koo, Jahyun. 2016. "Private Equity as an Alternative Corporate Restructuring Scheme: Does Private Equity Increase the Operating Performance of PE-Backed Firms?" KDI Journal of Economic Policy 38 (2): 21–44. https://doi.org/10.23895/kdijep.2016.38.2.21.

Olsson, Martin, and Joacim Tåg. 2017. "Private Equity, Layoffs, and Job Polarization." Journal of Labor Economics 35 (3): 697–754. https://doi.org/10.1086/690712.

Rambachan, Ashesh, and Jonathan Roth. 2023. "A More Credible Approach to Parallel Trends." Review of Economic Studies 90 (5): 2555–91. https://doi.org/10.1093/restud/rdad018.

Stuart, Elizabeth A. 2010. "Matching Methods for Causal Inference: A Review and a Look Forward." Statistical Science 25 (1): 1–21. https://doi.org/10.1214/09-STS313.

Yang, Siyun, Elizabeth Lorenzi, Georgia Papadogeorgou, Daniel M. Wojdyla, Fan Li, and Laine E. Thomas. 2021. "Propensity Score Weighting for Causal Subgroup Analysis." Statistics in Medicine 40(19): 4294–4309. doi:10.1002/sim.9029.


# Online Appendix

Online Appendix.

Private Equity and Labour Adjustment across Pre-Deal Hiring States

Unless otherwise stated, confidence intervals follow the procedures described in the main text. State-gradient analyses are evaluated against specification-specific untreated reference distributions generated using the same matching, outcome transformation, adjustment, and estimation procedure as the focal specification. Empirical -values for the primary gradient and other non-directional comparisons are two-sided and follow the centred empirical rule described in Section 4.3. Where a directional upper-tail probability from an earlier specification is retained for comparison, it is identified explicitly as supplementary. We read secondary analyses from the estimates and their uncertainty, not only from conventional significance thresholds. The monthly-allocation ranges are descriptive scale benchmarks, not externally established equivalence thresholds. State-balanced matching denotes the primary design defined in Section 4.1: the pre-deal hiring-state tercile is added to the baseline exact-matching cell.

## Appendix A. Monthly hiring allocation and the volume benchmark

Private equity targets record worker entries in more months after investment. Some of that widening is mechanical: over a fixed horizon, more entries generally imply fewer no-entry months even if their timing is otherwise unchanged. We compare the observed monthly pattern with benchmarks that hold realised entry volume fixed. The primary benchmark also preserves monthly employment exposure, separating the allocation change implied by higher volume from the residual change across months.

## A.1 Construction of the volume benchmark

For each firm-window, let  denote the realised number of worker entries and let  denote insured employment in month . Define

so that  is month ’s share of total insured-employment exposure over the window. The employment-weighted benchmark holds , the set of observed months, and monthly employment exposure fixed and reallocates the  entries with probabilities . The expected number of no-entry months is therefore

For a complete twelve-month window, the equal-month comparison has expected no-entry months

Because employment varies by month, we report both rules. The employment-weighted calculation is primary; the equal-month rule is a transparent sensitivity check. For measures without a closed-form expectation—the longest no-entry spell, the Herfindahl index of entries across months, and the share of entries occurring in the two busiest months—we use 100 multinomial reallocations per firm-window with fixed random seed 42. All such simulations use the employment-exposure probabilities . The fixed seed makes the reported benchmark values exactly reproducible.

For any monthly-allocation measure , define the excess change as

The excess is the treated-minus-control change beyond the component implied by the volume-preserving allocation. It is not a regression coefficient that conditions on realised volume. Even before investment, entries are more concentrated than the volume-preserving benchmark. Treated firms average 91.9 entries, 3.23 no-entry months rather than the benchmark's 2.58, and a longest no-entry spell of 1.97 months rather than 1.53. The observed and benchmark Herfindahl indices are 0.203 and 0.163; the corresponding shares of entries in the two busiest months are 0.468 and 0.378.

## A.2 Monthly allocation relative to realised volume

### Table A1. Monthly worker-entry measures and the volume benchmark

Panel A. Twelve-month window

| Measure | Observed change | Benchmark change | Excess | 95% CI for excess | Comparison range |
|---|---|---|---|---|---|
| Share of no-entry months, employment-weighted benchmark | −0.0466 | −0.0508 | +0.0042 | [−0.0088, +0.0180] | ±0.046 |
| Share of no-entry months, equal-month benchmark | −0.0466 | −0.0518 | +0.0052 | [−0.0082, +0.0189] | ±0.046 |
| Number of no-entry months | −0.5594 | −0.6182 | +0.0587 | [−0.1097, +0.2086] | ±0.55 |
| Longest no-entry spell, months | −0.3566 | −0.3688 | +0.0122 | [−0.1330, +0.1608] | ±0.36 |
| Herfindahl index of worker entries across months | −0.0248 | −0.0309 | +0.0061 | [−0.0064, +0.0190] | ±0.025 |
| Share of worker entries in the two busiest months | −0.0249 | −0.0335 | +0.0086 | [−0.0082, +0.0250] | ±0.025 |

Panel B. Thirty-six-month window

| Measure | Observed change | 95% CI | Excess | 95% CI for excess | Comparison range |
|---|---|---|---|---|---|
| Share of no-entry months | −0.055 | [−0.086, −0.025] | +0.0088 | [−0.0058, +0.0220] | ±0.046 |
| Longest no-entry spell, months | −0.756 | [−1.335, −0.161] | +0.2970 | [−0.117, +0.727] | ±1.0 |

Notes. Changes are treated-minus-control. The first two Panel A rows report the employment-weighted and equal-month rules; the other simulated rows use the employment-weighted rule. Excess is observed minus benchmark. Comparison ranges are descriptive and scaled to the observed movement. Panel B contains 180 events.

The no-entry share falls by 0.0466. The employment-weighted benchmark predicts −0.0508, leaving 0.0042 [−0.0088, 0.0180]; the equal-month rule predicts −0.0518, leaving 0.0052 [−0.0082, 0.0189]. Under either allocation rule, most of the rise in monthly participation is accounted for by the increase in realised entry volume. The remaining twelve-month measures show a similar pattern. The observed number of no-entry months falls by 0.5594, compared with a benchmark change of , leaving an excess of 0.0587 [−0.1097, 0.2086]. The longest no-entry spell falls by 0.3566 months, with an excess of 0.0122 [−0.1330, 0.1608]. The Herfindahl index falls by 0.0248, compared with a benchmark decline of 0.0309, leaving an excess of 0.0061 [−0.0064, 0.0190].

The concentration of worker entries in the two busiest months provides a less precise comparison. The observed share falls by 0.0249 and the benchmark by 0.0335, yielding an excess of 0.0086 [−0.0082, 0.0250]. The upper endpoint coincides with the stated  comparison boundary at the reported precision. We report the interval directly rather than assign a binary classification based on an unreported decimal place. At thirty-six months, the no-entry share falls by 0.055 and the excess is 0.0088 [−0.0058, 0.0220]. The longest spell falls by 0.756 months, with an excess of 0.297 [−0.117, 0.727]. Because only 180 events remain, these estimates are not a balanced extension of the twelve-month analysis.

A.2.1 State-specific comparisons

The raw decline in the no-entry share is larger among targets entering from lower-hiring states: −0.1076 [−0.1551, −0.0613], compared with −0.0182 [−0.0452, 0.0131] among more active targets. Under the equal-month allocation, the corresponding excess changes are 0.0058 [−0.0249, 0.0350] and 0.0027 [−0.0159, 0.0203], with a between-state difference of 0.0032 [−0.0321, 0.0365]. Under the employment-exposure-weighted benchmark used as the primary allocation rule, the excess changes are 0.0047 [−0.0245, 0.0298] and 0.0013 [−0.0171, 0.0198], with a difference of 0.0034 [−0.0308, 0.0347].  Realised entry volume accounts for most of the much larger raw participation change among lower-hiring targets; the residual allocation differences are small. This calculation does not show that recruiting dates are unchanged. It shows that the broader set of entry months does not require a comparably large timing response once entry volume is fixed.

## A.3 Decomposition of the average hiring increase

The primary twelve-month hiring rate satisfies

When employment varies across months, the simple share of active months and the unweighted mean of monthly hiring intensity do not yield an exact decomposition. We instead define the active component using employment exposure. Let  denote the set of months with positive worker entries, and define

Then

and therefore

This identity remains exact with time-varying employment. It separates the change in employment exposure during positive-entry months from the change in entry intensity within those months.

### Table A2. Exposure-based decomposition of the average increase in hiring

| Component | Estimate | 95% CI |
|---|---|---|
| Change in active-month employment-exposure share, Δq | 0.0457 | [0.0263, 0.0665] (n=346) |
| Change in active-month worker-entry intensity, ΔiE | 0.0028 | [−0.0004, 0.0064] (n=342) |
| Change in log active-month employment-exposure share, Δlogq | 0.1044 | [0.0536, 0.1515] (n=342) |
| Change in log active-month worker-entry intensity, ΔlogiE | 0.0586 | [0.0080, 0.1146] (n=342) |

Notes. The pre-deal means are  and . For observations for which both log components are defined, their changes sum exactly to the change in the log hiring rate. The log exposure-share component accounts for 64.0 percent [0.4454, 0.9525] of the summed log change. This decomposition is descriptive: the probability that a month contains a worker entry itself increases mechanically with realised entry volume, so  should not be interpreted as an independently identified behavioural extensive margin.

## Appendix B. State measurement and specification sensitivity

The primary analysis summarises pre-deal hiring using worker-entry activity over months  through . Higher values of the state correspond to lower prior hiring intensity. This appendix examines alternative measures of that history, distinguishes a broader recent hiring condition from a short pause at closing, evaluates sensitivity to the outcome transformation and matching procedure, and compares the hiring state with observable pre-deal financial condition. Some exercises compare state measures on a common sample; others rebuild the state-balanced design under a modified specification. Each subsection states which comparison it uses.

## B.1 Alternative measures of pre-deal hiring activity

### Table B1. Alternative measures of pre-deal hiring activity in the conventional matched sample

| State measure | Unadjusted slope | Adjusted slope, 95% CI |
|---|---|---|
| Hiring rate | 0.4964 | 0.5650 [0.210, 0.968] |
| Worker-entry volume | 0.1275 | 0.1578 [0.020, 0.291] |
| Share of months with no worker entry | 0.5259 | 0.3522 [−0.079, 0.829] |

Notes. All measures use months  through  and are oriented so that a positive coefficient corresponds to a larger subsequent response among targets with lower pre-deal activity. The adjusted specifications partial out log pre-deal employment, pre-deal employment growth, firm age, and one-digit industry from both the state measure and the outcome. Coefficient magnitudes should not be compared directly across state measures because their scales differ. These regressions use the 301-event conventional matched sample and an unwinsorised outcome; the preferred estimator instead uses 286 state-balanced events and 5/95 winsorisation.

The adjusted hiring-rate slope is 0.5650 [0.210, 0.968]. Discrete definitions give similar orderings: the low-minus-high activity contrast is 0.215 [0.026, 0.392] for terciles, 0.215 [0.030, 0.425] for quartiles, and 0.188 [0.031, 0.332] for a median split. The frequency of no-entry months is closely related to total pre-deal worker-entry volume. Over the same state window, the correlation between the no-entry share and log worker-entry volume is . Subtracting the no-entry share implied by the volume benchmark in Appendix A reduces that correlation to .

Once this volume component is removed, no-entry frequency carries little separate information about the post-investment response. The low-versus-high tercile contrast in the volume-adjusted frequency measure is 0.0031 [−0.176, 0.190]. The pooled frequency slope estimated within quintiles of pre-deal worker-entry volume is , while residualising frequency on volume and size gives a slope of 0.063. Mechanical sparsity is less important when the state window contains more entries. Among firms with at least twelve pre-deal entries, however, the coefficient on no-entry frequency is still only 0.010 after conditioning on entry volume. This is a partial coefficient, not the unconditional frequency slope in the restricted sample. These comparisons favour the hiring rate as the summary of recent pre-deal hiring. No-entry frequency is tightly linked to total entry volume and adds little ordering of the subsequent response after volume is accounted for.

## B.2 Recent hiring history and the firm’s position at closing

The primary state may capture a broad spell of low hiring, a pause already under way at closing, or observable firm characteristics correlated with both. Table B2 separates these possibilities.

### Table B2. Alternative interpretations of the pre-deal hiring state

| Specification | Estimate | 95% CI | N |
|---|---|---|---|
| Hiring state, controlling for pre-deal employment growth | 0.4099 | [0.0778, 0.7534] | 256 |
| Historical share of no-entry months | 0.5590 | [0.2408, 0.8853] | 301 |
| Length of hiring pause in progress at closing | 0.0403 | [−0.0156, 0.1073] | 301 |
| Residualised hiring state | 0.2433 | [−0.2213, 0.7226] | 301 |
| Earlier hiring state, months -36 to -25 | 0.2675 | [−0.0819, 0.6127] | 238 |
| Joint specification: historical no-entry share | 0.5363 | [0.2123, 0.8815] | 301 |
| Joint specification: pause duration | 0.0317 | [−0.0228, 0.0895] | 301 |

Notes. The residualised state removes size, industry, pre-deal employment growth, firm age, and seasonality, which jointly account for 63.9 percent of state variation. The earlier-state specification reconstructs the state-balanced design using months −36 through −25. Its untreated reference mean is 0.141; the excess is 0.127, the standardised distance is 0.92, and the corresponding empirical two-sided -value is 0.3638.

Controlling for pre-deal employment growth leaves a state coefficient of 0.410 [0.078, 0.753]. The historical no-entry share has an estimate of 0.559 [0.241, 0.885], whereas the length of the pause under way at closing has an estimate of 0.040 [−0.016, 0.107]. When the two pause measures enter jointly, their estimates are 0.536 and 0.032. The state also overlaps with conventional firm characteristics. Size, industry, pre-deal employment growth, age, and seasonality explain 63.9 percent of its variance. After removing that component, the residualised-state estimate is 0.243 [−0.221, 0.723], too imprecise to isolate a relationship independent of those observables.

Moving the state further into the past also weakens the relationship. Using months  through  produces a gradient of 0.268 against an untreated reference mean of 0.141, giving a standardised distance of 0.92. The result is less pronounced than for the primary recent state. Combined with the pause comparison, this pattern is more consistent with the state summarising a relatively recent hiring condition than a time-invariant firm type.

## B.3 Outcome transformations and winsorisation

The primary outcome is the change in the log hiring rate and therefore requires positive entries in both twelve-month windows. Table B3 varies the tail treatment and transformation; each Panel A estimate is compared with an untreated distribution built under the same rule.

### Table B3. Alternative outcome transformations and count-model check

Panel A. Outcome transformation and winsorisation

| Specification | Grad. | Untreated reference mean (SD) | Std. distance | Empirical two-sided p | Events |
|---|---|---|---|---|---|
| Winsorised 5/95, primary | 0.7101 | 0.1010 (0.1538) | 3.96 | 0.0005 | 286 |
| Unwinsorised | 0.8370 | 0.1216 (0.1808) | 3.96 | 0.0005 | 286 |
| Winsorised 1/99 | 0.8157 | 0.1141 (0.1712) | 4.10 | 0.0010 | 286 |
| Winsorised 10/90 | 0.6339 | 0.0959 (0.1359) | 3.96 | 0.0005 | 286 |
| Inverse hyperbolic sine of hiring rate | 0.2062 | 0.0259 (0.0586) | 3.08 | 0.0015 | 289 |
| log(1+hiring rate)​ | 0.1623 | 0.0167 (0.0449) | 3.24 | 0.0020 | 289 |

Panel B. Count-model check

| Specification | Coefficient | 95% CI |
|---|---|---|
| PPML worker-entry count with log employment offset | 0.1038 | [−0.3185, 0.5261] |

Notes. The inverse-hyperbolic-sine and  specifications retain zero-entry windows and are on different scales from the primary coefficient. The PPML model is estimated at the firm-window level using 1,611 pooled treated and matched-control post windows, including 19 zero-entry windows. It relates the post-window worker-entry count to the treated indicator and its interaction with the pre-deal state, uses log window employment exposure as the offset, absorbs matching-cell fixed effects, and clusters standard errors by matching cell. The PPML interval is wide, so the count model is treated as a functional-form diagnostic rather than evidence of an estimator-invariant state coefficient.

The gradient remains positive across the reported tail treatments: 0.837 without winsorisation, 0.710 at 5/95, 0.816 at 1/99, and 0.634 at 10/90. Transformations that retain zero-entry windows yield the same directional ordering. The inverse-hyperbolic-sine specification gives 0.206, while  gives 0.162. Because these transformations change the scale of the outcome, their numerical coefficients are not measures of the same magnitude as the primary log-rate gradient. The PPML coefficient is 0.104 [−0.319, 0.526]. The wide interval makes this a functional-form diagnostic, not evidence that the state coefficient is invariant to the estimator.

## B.4 Selected matching and estimation alternatives

Table B4 varies the number of controls, the role of the state in neighbour selection, state-window completeness, matching cells, state horizon, event weights, and deal-year adjustment. Each row rebuilds its own untreated reference distribution.

### Table B4. Selected alternatives to the primary matching and estimation design

| Specification | N | Grad. | Std. distance | Empirical two-sided p |
|---|---|---|---|---|
| Primary: exact state tercile, 5 controls | 286 | 0.7101 | 3.96 | 0.0005 |
| Exact state tercile, 20 controls | 286 | 0.6778 | 4.12 | 0.0010 |
| State included in neighbour distance, 5 controls | 299 | 0.6400 | 3.54 | 0.0015 |
| At least 6 of 12 state months observed | 310 | 0.6545 | 4.57 | 0.0005 |
| Two state bins rather than three | 292 | 0.6101 | 3.65 | 0.0005 |
| One-digit rather than two-digit industry cell | 299 | 0.6361 | 3.69 | 0.0010 |
| State measured over months −36 to −13 | 244 | 0.3883 | 2.33 | 0.0185 |
| Inverse-variance weighting | 286 | 0.3458 | 2.28 | 0.0185 |
| Add deal-year fixed effects | 286 | 0.6779 | 3.50 | 0.0010 |

Notes. Each row is evaluated against its own untreated reference distribution. The inverse-variance specification uses weights proportional to the inverse of , with the entry counts floored at one before calculating the variance proxy; the resulting weights are normalised to have mean one. The alternatives support a positive state relationship across several matching choices while also showing that its magnitude is sensitive to weighting and to the horizon over which the state is measured.

The gradient is 0.678 with twenty rather than five controls and 0.640 when the state enters neighbour distance rather than the exact cell. Two state bins give 0.610; one-digit rather than two-digit industry matching gives 0.636. Allowing as few as six observed state months raises the sample to 310 events and yields a gradient of 0.655. The primary specification retains complete windows so that the moderator has the same measurement horizon across events.

Using a longer state window from months  through  reduces the sample to 244 events and the gradient to 0.388. The result is consistent with the separate earlier-state analysis in Section B.2: hiring history measured further from the transaction provides a weaker ordering of subsequent responses. Event weighting matters more. Inverse-variance weighting lowers the gradient to 0.346, 2.28 standard deviations above its specification-specific reference mean. Deal-year fixed effects give 0.678 and a standardised distance of 3.50. The coefficient is positive across these designs, but its magnitude and precision are not invariant. The inverse-variance and longer-window estimates are substantive sensitivity results, not exceptions to be set aside.

## B.5 Pre-deal financial condition and hiring-response heterogeneity

To assess whether observable financial condition orders the response, we compare the hiring state with pre-deal cash relative to assets, leverage, interest coverage, and return on assets. Each measure comes from the audited statement for the fiscal year before the deal, is clipped at the within-sample 1st and 99th percentiles, and is standardised. Coefficients are changes in the event-level matched response per one-standard-deviation difference in the measure.

### Table B5. Pre-deal financial condition and hiring-response heterogeneity

| Pre-deal measure, standardised | Coefficient per SD | 95% CI | N |
|---|---|---|---|
| Cash / assets | +0.0255 | [−0.0650, 0.1152] | 186 |
| Leverage, liabilities / assets | −0.0045 | [−0.1027, 0.0875] | 186 |
| Interest coverage, operating income / interest expense | +0.0489 | [−0.0420, 0.0891] | 170 |
| Profitability, ROA | −0.0055 | [−0.0911, 0.1018] | 184 |
| Pre-deal hiring state, audited subsample | +0.1087 | [0.0229, 0.1964] | 169 |
| Memo: pre-deal hiring state, conventional full sample | +0.1095 | [0.0221, 0.1949] | 301 |

Notes. The outcome is the unwinsorised event-level treated-minus-control change in the log hiring rate. Financial variables come from the fiscal year preceding the deal year, are clipped at the within-sample 1st and 99th percentiles, and are standardised before estimation. Confidence intervals are obtained by resampling treated firms. The audited-subsample state row reports the hiring-state coefficient where the corresponding audited observations are available. The memo row reports the same form of state coefficient in the 301-event conventional full sample and is included to distinguish sample restriction from the choice of financial variable.

None of the four accounting variables provides a comparably clear ordering of the realised hiring response in its available audited sample. Cash relative to assets has a coefficient of 0.0255 [−0.0650, 0.1152], leverage  [−0.1027, 0.0875], interest coverage 0.0489 [−0.0420, 0.0891], and profitability  [−0.0911, 0.1018]. The hiring-state coefficient remains 0.1087 [0.0229, 0.1964] in the smaller audited sample, close to 0.1095 [0.0221, 0.1949] in the 301-event conventional sample. The weaker financial-variable gradients are thus not simply a generic consequence of restricting the sample to firms with audited accounts. These accounting variables are imperfect measures of access to finance, and the audited sample is larger and more selected than the pension-based population. Their weak gradients do not test a financing-constraint mechanism or rule out financing capacity, governance, product demand, managerial capacity, or recruiting access.

## Appendix C. Validation of administrative worker inflows and flow outcomes

NPS entries measure administrative worker inflows, not necessarily one-for-one external recruitment: re-registration, payroll consolidation, and other administrative changes can also generate entries. In addition, hiring and separation rates use employment as a denominator. This appendix checks flow-stock accounting, applies measurement filters, reconstructs inflows without the reported entry field, and compares flow measures with the employment stock.

## C.1 Accounting consistency of worker entries and exits

Let  denote the month-end insured-employment stock,  reported worker entries during month , and  reported worker exits. Define

Perfect reconciliation under a common timing convention would imply 0. In practice, the stock is measured at month end whereas entries and exits are monthly acquisition and loss records; late filings and administrative corrections can therefore make the two series differ. We scale the absolute discrepancy by lagged insured employment:

excluding observations for which . Among 227,339 firm-months, the median absolute discrepancy is one worker and 24.3 percent reconcile exactly. The median discrepancy is 1.4 percent of employment; the 90th percentile is 7.1 percent.

### Table C1. Accounting consistency of pension worker flows

| Measure | Value |
|---|---|
| Firm-month observations | 227,339 |
| Median absolute discrepancy | 1 worker |
| Share reconciling exactly | 24.3% |
| Median discrepancy relative to employment | 1.4% |
| 90th percentile, relative discrepancy | 7.1% |
| Treated firms, year before transaction | 2.8% |
| Treated firms, transaction month | 3.6% |
| Treated firms, post-transaction period | 3.1% |

Notes. The last three rows report mean relative discrepancies for treated firms over the indicated periods. Employment is the month-end NPS insured-employment stock. Only three of the 379 baseline treated firms change their registered-workplace count around the transaction. The accounting checks support interpreting NPS entries as administrative worker inflows while preserving the distinction between a recorded pension entry and an independently observed recruiting decision.

The mean relative discrepancy rises from 2.8 percent in the year before the transaction to 3.6 percent in the transaction month, then falls to 3.1 percent. The movement is modest but rules out assuming perfect reconciliation precisely at the ownership change. Section C.2 therefore tests sensitivity to large discrepancies and administrative restructuring. Only three of the 379 treated firms change their number of registered NPS workplaces around the transaction. Observable workplace restructuring is rare, although that fact cannot show that every recorded entry is an external recruit.

## C.2 Measurement filters and reconstructed worker inflows

We re-estimate the state gradient after removing firm-months with large flow-stock discrepancies, months with exceptionally high turnover, and treated firms whose registered-workplace count changes around investment.

The final specification reconstructs worker inflows without using the reported entry variable. From the employment-flow identity,

the implied inflow absent the discrepancy term is

The implemented reconstructed measure follows

Negative implied inflows are set to zero, and missing or non-consecutive observations invalidate the window. We exclude the transaction month, aggregate reconstructed entries over months −12 to −1 and +1 to +12, and scale by mean insured employment in each window.

### Table C2. Hiring-state gradient under worker-flow measurement checks

| Specification | N | Grad. | 95% CI | Empirical two-sided p |
|---|---|---|---|---|
| Primary worker-entry measure | 286 | 0.7101 | [0.3187, 1.1254] | 0.0005 |
| Exclude relative discrepancy >10% | 288 | 0.3118 | [−0.0784, 0.7155] | — |
| Exclude relative discrepancy >5% | 231 | 0.5441 | [−0.1059, 1.1829] | — |
| Exclude total turnover >50% of employment | 300 | 0.4883 | [0.1017, 0.8502] | — |
| Exclude treated firms with workplace-count changes | 299 | 0.5571 | [0.1596, 0.9299] | — |
| Reconstructed worker inflows | 288 | 0.3650 | — | 0.0230 |

Notes. The turnover restriction excludes months in which reported entries plus exits exceed 50 percent of same-month insured employment. The workplace-count restriction removes treated firms whose number of registered NPS workplaces changes at any point in the observed panel. The discrepancy and workplace rows use the conventional matched sample with regression adjustment and bootstrap intervals. The reconstructed-flow row uses the state-balanced design and its own untreated reference distribution. Its coefficient remains positive but is materially smaller than the primary reported-entry coefficient, so the two worker-flow measures should not be treated as numerically interchangeable.

The gradient remains positive but varies across filters. It is 0.312 after removing relative discrepancies above 10 percent, 0.544 at the 5-percent threshold, and 0.488 [0.102, 0.850] after removing months in which entries plus exits exceed half of employment. Excluding treated firms with workplace-count changes gives 0.557 [0.160, 0.930]. The result is not confined to targets with an observable change in pension-reporting structure.

Reconstructed inflows produce a gradient of 0.3650 and an empirical two-sided p-value of 0.0230. The estimate is positive but materially below the 0.7101 gradient based on reported entries, so the measures are not numerically interchangeable. The comparison is diagnostic: the ordering remains when inflows are inferred from employment changes and recorded exits. The stricter discrepancy filters also remove information, so their intervals must be read with the event counts in Table C2. The direction is not confined to observations with the clearest accounting or registration concerns, although administrative measurement can affect the magnitude.

## C.3 Worker-entry counts, employment denominators, and level-flow accounting

Because the primary hiring rate divides entries by mean insured employment, post-investment employment changes could affect the gradient mechanically. We therefore examine entry counts directly. On the same 286-event design used in Table 4, the gradient in the log worker-entry count is 0.6315. The corresponding untreated reference mean is 0.1858, and the empirical two-sided -value is 0.0110. The positive state relationship therefore remains when employment is removed from the outcome denominator. A diagnostic specification additionally controls for the change in log employment. The worker-entry-count gradient is then 0.6957, against an outcome-specific untreated reference mean of 0.0377; the two-sided empirical -value is 0.0005. Because the change in employment is itself a post-investment outcome, this coefficient is not interpreted as a controlled causal effect. It is reported solely as a denominator check. For comparison, the primary log hiring-rate gradient is 0.7101 and its reference mean is 0.1006. Each reference mean is re-estimated for its outcome while the event design remains fixed.

Level worker-flow measures provide a separate accounting diagnostic. The state gradients in the worker-entry rate, separation rate, and net-inflow rate are , , and , respectively. The entry-minus-separation relation therefore reconciles with the net-inflow gradient to within approximately 0.003.

### Table C3. Worker-flow accounting and employment

| Outcome | State gradient |
|---|---|
| Level worker-entry rate | +0.263 |
| Level separation rate | +0.094 |
| Level net-inflow rate | +0.172 |
| Log employment | −0.058 |

Notes. The first three rows are level worker-flow rates and use employment in their denominators. Their estimated gradients satisfy the corresponding worker-flow accounting identity to within approximately 0.003. The log-employment row measures the employment stock directly and is not an algebraic component of this rate identity.

A positive net-inflow-rate gradient can coexist with a negative log-employment gradient. The former scales contemporaneous flows by employment; the latter measures the matched change in the stock. Denominators, timing, and cumulation can therefore produce different gradients. We use the level-flow identity as an accounting check and log employment for differential net-employment growth.

## C.4 Employment at longer horizons and an additional worker-flow contrast

We examine whether the negative employment-state relationship is confined to the primary horizon. Table C4 reports log employment at 12, 24, and 36 months relative to mean employment over months  through . This outcome construction differs from the main Table 4 employment specification and should not be read as a replication of its  coefficient. At twelve months, the horizon-specific gradient is , with a standardised distance of  relative to its untreated reference distribution. At 24 months the gradient is , and at 36 months it is . The corresponding standardised distances are  and .

### Table C4. Additional employment horizons and worker-flow contrast

Panel A. Relative employment at longer horizons

| Horizon | Grad. | Std. distance | N |
|---|---|---|---|
| +12 months | −0.0316 | −1.92 | 291 |
| +24 months | −0.1616 | −1.63 | 245 |
| +36 months | −0.2092 | −2.29 | 203 |

Panel B. Additional within-event worker-flow contrast

| Contrast | Estimate | Empirical two-sided p | N |
|---|---|---|---|
| Worker-entry gradient − separation gradient | 0.5746 | 0.0415 | 279 |

Notes. Panel A measures log employment at the stated horizon relative to mean employment over months −6 through −1, followed by the treated-minus-control comparison and state-gradient estimation. This differs from the primary Table 4 employment outcome, which is constructed from the primary twelve-month pre- and post-investment windows rather than a single horizon-specific employment stock. The standardised distance is calculated from the horizon-specific untreated reference distribution. Panel B constructs the worker-entry-minus-separation contrast within the same events and compares it with its own untreated reference distribution.

Employment gradients are negative at all three horizons and become more negative with the horizon. But the event count falls from 291 at twelve months to 245 at twenty-four months and 203 at thirty-six months, so the sequence is not a balanced-panel path; both horizon and composition can change the estimates. The within-event entry-minus-separation gradient is 0.5746, with an empirical two-sided p-value of 0.0415 across 279 events. This supplementary contrast does not turn the imprecise separation gradient into an identified replacement mechanism. The state relationship is more clearly detected in inflows than in exits.

## Appendix D. Pre-deal dynamics, timing, and inference sensitivity

This appendix moves the rebound and pre-deal-dynamics checks to quarterly frequency, reports the relative-magnitude calculations, and examines sponsor timing, transaction-date measurement, and repeated control firms. It then treats the separate average-effect estimand and re-estimates the state relationship in a stacked matched panel. Each exercise diagnoses a particular threat; none supplies independent identification.

## D.1 Quarterly state-gradient dynamics

Table D1 reports quarterly state gradients. They reveal the timing of the pre-investment pattern but are much less precise than the twelve-month analysis.

### Table D1. State gradients at quarterly frequency

| Period | Quarter 1 | Quarter 2 | Quarter 3 | Quarter 4 |
|---|---|---|---|---|
| Treated, pre-deal | +0.087 | −0.042 | −0.038 | −0.056 |
| Treated, post-deal | +0.147 | +0.240 | +0.108 | +0.010 |
| Untreated pseudo-events, pre-deal | −0.073 | −0.031 | −0.003 | +0.045 |
| Untreated pseudo-events, post-deal | −0.024 | +0.088 | −0.040 | −0.000 |

Notes. Entries are state gradients estimated separately by quarter and ordered from earliest to latest within the pre- and post-deal periods. The mean of the four treated pre-deal gradients is  [−0.163, 0.131]. A linear drift fitted across those four pre-deal estimates is  [−0.600, 0.473]. The mean of the four treated post-deal gradients is 0.126.

The treated pre-deal coefficients alternate in sign: , , , and . Their mean is  [−0.163, 0.131]. The sequence does not display a persistent positive ordering before investment. Precision is limited. A single linear drift across the four treated pre-deal quarters is  [−0.600, 0.473]. The interval accommodates moderate differential dynamics in either direction. The quarterly results show no clear positive divergence; they do not establish flat or parallel pre-investment paths.

## D.2 Relative-magnitude sensitivity of the state gradient

We apply the relative-magnitude framework of Rambachan and Roth (2023) to differential trends that may remain after matching. Let  denote the differential trend component at event time . Under the relative-magnitude restriction,

The parameter  therefore limits the largest post-treatment change in the differential trend relative to the largest corresponding change observed before treatment. Larger values permit larger departures from the pre-period pattern. On the 283-event common sample, the twelve-month calculation uses a pre-period benchmark of 0.1068 and a post-period gradient of 0.7250 (standard error 0.1995). The 95 percent sensitivity interval first contains zero at M̄ = 3.126. At quarterly frequency, the mean post-deal gradient is 0.1259 (standard error 0.0711) and the largest pre-period movement is 0.0871; sampling uncertainty leaves a breakdown value of zero.

### Table D2. Relative-magnitude sensitivity of the state gradient

| Temporal resolution | Breakdown value | Interpretation |
|---|---|---|
| Twelve-month state-gradient calculation | 3.126 | Confidence set first contains zero at M=3.126 |
| Quarterly state-gradient calculation | 0 | Pre-period estimates are too noisy to yield an informative positive breakdown value |

Notes. The twelve-month calculation uses the 283-event common sample, a pre-period benchmark of 0.1068 in absolute value, and the post-period state-gradient estimate of 0.7250 (standard error 0.1995). The quarterly calculation uses the mean post-deal gradient of 0.1259 (approximate standard error 0.0711) and a maximum pre-period movement of 0.0871. A breakdown value is conditional on the specified class of differential trends and is not a test of whether the identifying restriction is true.

Sensitivity is resolution-dependent here. The twelve-month calculation matches the primary estimand's horizon; the quarterly calculation is uninformative because precision is limited. Neither result validates the identifying assumption.

## D.3 Sponsor deployment pressure

Forward-looking sponsor selection remains the central causal limitation. A narrower version predicts larger hiring responses when sponsors have more discretion to wait for favourable target-specific conditions. We proxy deployment pressure with the age of the sponsor's most recent fund at the transaction. Fund age is measured from the latest closing month; when only a vintage year is known, we assign its midpoint. High pressure is the top tercile, beginning at 2.42 years.

### Table D3. Sponsor deployment pressure and monthly positive-entry incidence

| Specification | Hazard ratio | 95% CI | N |
|---|---|---|---|
| Treated × post × high deployment pressure | 1.2881 | [1.0535, 1.5750] | 379 |

Notes. High deployment pressure is defined as the upper tercile of the age of the sponsor’s most recent fund at the focal transaction, with a cutoff of 2.42 years. The complementary log-log model contains event fixed effects and duration-category fixed effects and clusters standard errors by event. The estimation sample contains 4,686 grouped cells and 48,853 firm-month observations. Duration since the previous positive-entry month evolves after investment and is therefore a post-treatment conditioning variable.

The larger conditional response among transactions associated with older funds runs opposite to the narrow prediction that greater timing discretion should produce the larger response. Fund age is not an instrument for timing. It can covary with sponsor strategy, target composition, fundraising conditions, and transaction type, and it does not reveal target-specific information. The hazard model also conditions on duration since the previous entry, which changes with post-investment entries. This is a conditional descriptive comparison. It does not materially narrow the possibility that sponsors select low-hiring targets using private information about future growth.

## D.4 Independent confirmation of transaction timing

PitchBook supplies the monthly event date. Annual shareholder records provide an independent, coarser check by recording the first year in which the sponsor appears among reported shareholders. The transaction year can be corroborated using the shareholder records for 62 events. In this subsample, the treated-minus-control change in the share of months with no worker entry is  [−0.1145, −0.0163], compared with approximately  in the full corresponding sample. The common direction makes large transaction-year miscoding less plausible as the main source of the average no-entry pattern. The check is limited: annual records cannot validate the month, only 62 events qualify, and the outcome is the no-entry share rather than the log-hiring-rate state gradient. We treat this as a transaction-year measurement check, not an independently dated replication.

## D.5 Shared control firms and uncertainty

A control firm can enter more than one matched set, creating dependence across event-level outcomes. Reuse is limited: the 286 state-balanced events contain 1,144 distinct controls, 95.02 percent of which appear in one event; none appears in more than three. We address the dependence with control-firm-cluster resampling and with a deterministic design that assigns each control to at most one treated event.

### Table D4. Sensitivity to shared control firms

| Specification | Grad. | 95% CI |
|---|---|---|
| Primary matched-event bootstrap | 0.7101 | [0.3187, 1.1254] |
| Alternative bootstrap clustered on control firms | 0.7101 | [0.4595, 0.8771] |
| Each control assigned to at most one event | 0.7036 | — |

Notes. The primary bootstrap resamples the 286 matched target-control sets with replacement for 2,000 draws, so each target moves together with its assigned controls; the primary winsorisation cutoffs are held fixed. The alternative procedure resamples the 1,144 distinct control firms with replacement. For each replication, an event’s control mean is reconstructed using the multiplicity with which its controls were sampled, and an event is omitted if none of its original controls appears in that draw. In the deterministic one-event-per-control specification, a control appearing in more than one matched set is retained only for the event with the earliest transaction month. A separate interval is not reported for that deterministic reassignment.

Control-cluster resampling leaves the point estimate at 0.7101 and gives an interval of [0.4595, 0.8771]. Assigning each control to one event gives 0.7036. Repeated controls do not account for the gradient in these checks. We retain matched-event resampling because the target and its comparison set define the event-level response; the control-cluster result is an inference sensitivity exercise, not a preferred interval.

## D.6 Relative-magnitude sensitivity of the average post-investment effect

The average hiring effect and the hiring-state gradient are different estimands, so we report their relative-magnitude calculations separately. For the average effect, the largest pre-period first difference in the quarterly treated-minus-control path is 0.0154. The twelve-month effect is 0.0460 with a standard error of 0.0105. Bounding quarterly post-period movement relative to that pre-period difference, the 95 percent normal-approximation interval first includes zero at M̄ = 0.658.

### Table D5. Relative-magnitude sensitivity of the average hiring effect

| Estimand | Breakdown value |
|---|---|
| Average post-investment hiring effect | 0.658 |
| Primary state gradient, twelve-month calculation | 3.126 |

Notes. The two rows involve different estimands, outcome constructions, and event-time sequences. The numbers are reported together only to document the corresponding sensitivity calculations; they should not be used to rank the credibility of the average-effect and heterogeneity analyses.

Interpretation is estimand-specific. The average-effect estimate is sensitive to its own assumed differential-trend bound at . The state-gradient calculation yields 3.126 under its twelve-month implementation, while the quarterly state-gradient calculation in Section D.2 is uninformative. These sensitivity results delimit the conclusions supported by each design rather than validate the corresponding identifying assumptions.

## D.7 Stacked matched panel difference-in-differences

To check whether the state gradient depends on collapsing each event to a twelve-month response, we re-estimate the primary state-balanced matched sets as a stacked firm-month panel. The stack contains 286 events, 1,545 event-by-firm units, and 36,913 observations spanning 115 calendar months. Controls are never treated, so the stack contains no treated-versus-treated comparisons. The outcome is the untransformed monthly worker-entry rate. The target's continuous state is assigned to every firm in its matched set and centred at the event mean (-0.3517). The interaction model includes Post, Treated x Post, Post x State, and Treated x Post x State, along with event-by-firm and calendar-month fixed effects. Intervals cluster by event. Because the state rises as pre-deal hiring weakens, a positive triple interaction denotes a larger post-investment target-control response among lower-hiring targets.

### Figure D1. Stacked matched event-study coefficients

Notes. Coefficients are relative to quarter -1. Panel (a) reports Treated x Quarter; Panel (b) reports Treated x Quarter x State. Bars are event-clustered 95 percent intervals. Both models absorb event-by-firm and calendar-month fixed effects. Joint Wald tests for the three pre-deal coefficients give chi-squared(3) = 0.55 (p = 0.9078) for the level path and chi-squared(3) = 0.112 (p = 0.9904) for the state interaction.

### Table D6. Stacked matched panel difference-in-differences

| Specification | Estimate | 95% CI | t |
|---|---|---|---|
| Level model: Treated x Post | +0.0054 | [0.0028, 0.0081] | 3.98 |
| Interaction model: Treated x Post at mean State | +0.0055 | [0.0029, 0.0081] | 4.11 |
| Interaction model: Treated x Post x State | +0.0179 | [0.0035, 0.0323] | 2.44 |
| log(1 + rate): Treated x Post x State | +0.0161 | [0.0032, 0.0289] | 2.45 |
| Unit and event-time FE: Treated x Post x State | +0.0177 | [0.0034, 0.0321] | 2.43 |
| Conventional matching: Treated x Post x State | +0.0161 | [0.0029, 0.0294] | 2.39 |
| Event-equal weighting: Treated x Post x State | +0.0228 | [0.0045, 0.0411] | 2.44 |

Notes. Baseline rows use the 286 state-balanced matched sets, the untransformed monthly worker-entry rate, event-by-firm and calendar-month fixed effects, and event-clustered intervals. The log specification changes only the outcome. The event-time row replaces calendar-month fixed effects with event-time fixed effects. The conventional-matching row uses 301 events. Event-equal weighting assigns equal total weight to each matched event after fixed-effect residualisation.

The level model gives a monthly target-control difference of 0.0054 [0.0028, 0.0081]. In the interaction model, the difference at the mean state is 0.0055 [0.0029, 0.0081], and the Treated x Post x State coefficient is 0.0179 [0.0035, 0.0323]. The interaction remains positive with the log outcome, event-time fixed effects, conventional matching, and event-equal weighting. The pre-deal state-interaction estimates for quarters -4, -3, and -2 are -0.0018, -0.0038, and -0.0019; the joint test gives p = 0.9904. The post-deal estimates are 0.0038, 0.0102, 0.0260, and 0.0245 in quarters 1 through 4. The positive interaction is therefore concentrated in the latter half of the post-deal year rather than appearing as a discrete break in the first quarter.

This exercise is a cross-estimator check, not a new identification strategy. Failure to reject the joint pre-period restrictions does not establish parallel paths or rule out sponsor information that is not expressed in observed pre-deal hiring. Nor is 0.0179 numerically comparable with the primary gradient of 0.7101: the former is a monthly rate interaction in a firm-month panel, whereas the latter is a gradient in a twelve-month matched log-hiring-rate response after the primary transformation and adjustment.

## Appendix E. Transaction form and sponsor characteristics

This appendix asks whether the realised worker-inflow response also varies with transaction and sponsor characteristics. The estimates are scope checks, not competing explanations for the state gradient. Coverage differs by characteristic, so estimates across panels do not form a common-sample ranking. Sponsor activity counts only investments observed before the focal transaction month; later deals never add experience to an earlier event.

## E.1 Transaction form, ownership, and prior sponsor activity

We begin with transaction form and acquired ownership. Adjusted specifications include the hiring state, log size, pre-deal employment growth, age, industry, and deal year. The unadjusted control-minus-growth contrast is 0.1218 log points [−0.0494, 0.2776]. Control targets also have a 0.0948 higher pre-deal no-entry share. Adjustment for the hiring state and other pre-deal characteristics reduces the contrast to 0.0475 [−0.1062, 0.1958], consistent with target composition explaining part of the raw difference. Ownership contrasts are less precise. Each percentage point of acquired ownership is associated with 0.0007 log points [−0.0015, 0.0027]; the adjusted majority-minus-minority contrast is 0.0397 [−0.1761, 0.2674].

### Table E1. Transaction form, ownership, and prior sponsor activity

Panel A. Transaction and ownership characteristics

| Characteristic | Estimate | 95% CI | N |
|---|---|---|---|
| Control transaction − growth investment, unadjusted | 0.1218 | [−0.0494, 0.2776] | 301 |
| Control transaction − growth investment, adjusted | 0.0475 | [−0.1062, 0.1958] | 301 |
| Acquired ownership stake, per percentage point, adjusted | 0.0007 | [−0.0015, 0.0027] | 181 |
| Majority (≥50%) − minority investment, adjusted | 0.0397 | [−0.1761, 0.2674] | 181 |

Panel B. Prior sponsor deal activity at the focal transaction

| Prior sponsor deal count | Mean response | 95% CI | N |
|---|---|---|---|
| First observed deal, 0 prior | +0.1240 | [0.0219, 0.2276] | 158 |
| 1–3 prior deals | +0.2749 | [0.1369, 0.4128] | 96 |
| 4 or more prior deals | +0.1122 | [−0.0643, 0.3025] | 45 |
| ≥4 − first observed deal | −0.0118 | [−0.2193, 0.2195] | — |
| Repeat (≥1) − first observed deal | +0.0990 | [−0.0565, 0.2498] | — |

Notes. The Panel A outcome is the event-level change in the log hiring rate. Adjusted specifications condition on the pre-deal hiring state, log firm size, pre-deal employment growth, firm age, industry, and deal year. Acquired ownership stake is the sum of private equity holders’ common-share stakes reported in the shareholder register for the entry year. The transaction-level percentage-acquired field is not used because it is heavily concentrated at 100 percent.

Panel B defines sponsor experience as the number of private equity investment events by the same sponsor observed strictly before the focal transaction month within the 379-event treated universe. No later transaction contributes to the experience assigned to an earlier focal event. Fifty-three percent of the events with this measure are the sponsor’s first observed transaction in the treated universe. The correlation between the prior-deal measure and the former full-sample sponsor deal count is 0.74. Because terciles of prior activity are degenerate at zero, the table uses fixed groups of 0, 1–3, and at least 4 prior deals.

The response is not monotonic in prior sponsor activity. Mean responses are 0.1240 [0.0219, 0.2276] for first-observed deals, 0.2749 [0.1369, 0.4128] for one to three prior deals, and 0.1122 [−0.0643, 0.3025] for at least four. The high-activity-minus-first contrast is −0.0118 [−0.2193, 0.2195]; pooling repeat sponsors gives 0.0990 [−0.0565, 0.2498]. The observed deals show no monotonic experience gradient. Because the measure covers only transactions in our data, we use it as an ex ante activity measure, not a complete investment history or a proxy for sponsor skill.

## E.2 Common-sample descriptive fit and held-out-event comparison

We next compare observable transaction characteristics and the pre-deal hiring state on the same 180 events for which the relevant transaction variables are jointly observed. The transaction-characteristic set consists of the control-transaction indicator, acquired ownership stake, and . The sponsor variable uses only deals observed before the focal transaction. The comparison is descriptive. In-sample  measures the fraction of realised cross-event response variation captured by each specification in this common sample. It does not measure causal importance. We also report five-fold held-out-event , assigning folds at the event level. This exercise asks whether fit estimated on one subset carries to omitted events in the same observed sample; it is not a temporal forecast of future private equity transactions.

### Table E2. Transaction characteristics and pre-deal hiring state on a common sample

Panel A. In-sample fit

| Model | R2​ | Permutation p |
|---|---|---|
| Transaction characteristics | 0.0054 | 0.814 |
| Pre-deal hiring state | 0.0286 | 0.0220 |
| Transaction characteristics and state | 0.0311 | — |

Panel B. Five-fold held-out-event fit

| Model | Held-out-event R2 |
|---|---|
| Transaction characteristics | −0.0454 |
| Pre-deal hiring state | −0.0168 |
| Transaction characteristics and state | −0.0534 |
| State − transaction-characteristic R2 | +0.0287 [−0.0280, 0.1148] |

Notes. The common sample contains 180 events. Transaction characteristics are the control-transaction indicator, acquired ownership stake, and log(1 + prior sponsor deal count), where prior sponsor activity uses only transactions preceding the focal event. The permutation probabilities in Panel A use 2,000 random permutations of the transaction-characteristic vectors across events while the state is held fixed. Panel B uses five event-level folds. Negative held-out-event R² indicates worse squared-error performance than the corresponding benchmark prediction for omitted observations. The interval for the state-minus-transaction difference is [−0.0280, 0.1148].

Within the 180-event common sample, transaction characteristics explain 0.54 percent of event-level response variation, with a permutation -value of 0.814. The pre-deal hiring state alone explains 2.86 percent, with a permutation -value of 0.0220. Including both produces an  of 0.0311. These quantities describe realised in-sample association and do not rank the causal importance of target condition and transaction characteristics. None of the specifications performs well on held-out events. The transaction-characteristic model has an  of −0.0454, the state model −0.0168, and the combined model −0.0534. The state-minus-transaction difference is 0.0287 [−0.0280, 0.1148]. The interval does not establish a held-out advantage for either specification. We use the state to organise realised heterogeneity, not as a validated prediction rule. Its role rests on the within-sample ordering of responses and the untreated counterfactual dynamics, not on forecasting performance for omitted or future transactions.

## E.3 Repeat-deal associations within sponsors

Sponsor counts depend on the sample. The 379-event treated universe contains 206 sponsor identifiers; the 301-event conventional heterogeneity sample contains 164. For each eligible event, we relate its response to the mean among the same sponsor's other eligible transactions. The leave-one-out coefficient is −0.2675 across 189 events belonging to 54 repeat sponsors. This is a within-sponsor association, not a prediction exercise: the other transactions used in the mean may occur before or after the focal deal.

### Table E3. Repeat-deal associations within sponsors

Panel A. Leave-one-out within-sponsor association

| Specification | Leave-one-out coefficient |
|---|---|
| Baseline sponsor leave-one-out | −0.2675 |
| Outcome winsorised at 1/99 | −0.2659 |
| Outcome winsorised at 5/95 | −0.2387 |
| Drop five most influential events | −0.1751 |
| Covariate-adjusted response | −0.2496 |

Panel B. Sponsor fixed-effect variance share

| Statistic | Value |
|---|---|
| Observed sponsor fixed-effect share | 0.2875 |
| Permutation median | 0.2571 |
| Permutation p | 0.2605 |

Notes. The 379-event baseline treated universe contains 206 distinct sponsor identifiers. The 301-event conventional heterogeneity sample used for the response-level sponsor analysis contains 164 sponsor identifiers. Panel A is further restricted to 189 event observations for which the leave-one-out same-sponsor response can be constructed. These observations represent 54 distinct repeat-sponsor identifiers. Other transactions used to form the same-sponsor mean can occur either before or after the focal event, so the coefficient is a within-sponsor association rather than an ex ante forecast.

The influence specification removes the five events with the largest effect on the baseline coefficient. The covariate-adjusted response partials out the pre-deal hiring state, log firm size, pre-deal employment growth, firm age, one-digit industry, and deal year. Business registration numbers are unique across the 379 treated events, so repeated observation of the same target does not generate the sponsor-level association. Panel B is estimated on 213 events associated with 56 sponsors. Its permutation benchmark is generated by 2,000 random reassignments of sponsor labels that preserve the observed sponsor-group sizes.

The leave-one-out coefficient remains negative across specifications: −0.2659 with 1/99 winsorisation, −0.2387 at 5/95, −0.1751 after removing the five most influential events, and −0.2496 after covariate adjustment. Limited repeat-deal support precludes an economic interpretation of the sign. The observed sponsor fixed-effect variance share is 0.2875, compared with a permutation median of 0.2571. The corresponding permutation -value is 0.2605. The observed sponsor-level variation is not unusual relative to this benchmark. The exercise does not imply that sponsor identity is economically irrelevant. It shows only that the eligible repeat deals do not reveal a stable positive same-sponsor association. The 206 sponsors in the broader universe are not 206 independent repeat-sponsor groups; the useful repeat-deal sample is much narrower.

## Appendix F. Supplementary worker earnings and firm outcomes

This appendix adds earnings and firm outcomes to the average worker-inflow and employment comparisons. Coverage differs sharply: pension earnings are relatively broad, while audited statements select a smaller set of larger firms. We treat the estimates as supplementary matched comparisons, not mechanism tests or results that automatically extend to the 286-event gradient sample.

## F.1 Pensionable earnings

The National Pension contribution base is bounded by statute, so it measures pensionable earnings rather than total compensation. Across 346 events, pensionable earnings per insured worker rise by 0.0096 log points relative to matched controls [0.0039, 0.0154], a small increase alongside the average gains in employment and worker inflows.

We also construct a payroll-based earnings measure associated with added employment. The measure is defined as

Here,  is total NPS contribution-base payroll over months −12 through −1,  is total contribution-base payroll over months +1 through +12,  is the change in window-mean insured employment between those periods, and  provides the pre-window earnings-per-worker normalisation. We retain observations only when insured employment rises by at least two workers and truncate the resulting ratio to [−3, 5]. Because incumbent earnings also enter the construction, the measure is not the wage of an identified marginal or newly hired worker. We interpret only its treated-minus-control difference.

### Table F1. Supplementary worker-earnings measures

| Outcome | Estimate | 95% CI | N |
|---|---|---|---|
| Pensionable earnings per insured worker, log | 0.0096 | [0.0039, 0.0154] | 346 |
| Payroll-based added-employment earnings measure | 0.0086 | [−0.1383, 0.1585] | 182 |

Notes. Pensionable earnings are measured using the National Pension contribution base and are subject to the statutory contribution bounds. The payroll-based added-employment measure is defined as . Because changes in incumbent earnings also affect the construction, the second row is not interpreted as the wage of a marginal hire.

The payroll-based added-employment measure differs by 0.0086 [−0.1383, 0.1585] between treated firms and controls. The interval spans economically meaningful values in both directions and provides little information about earnings attached specifically to added employment.

## F.2 Audited firm outcomes

Audited financial statements provide a broader set of firm outcomes over the first three post-investment years. We construct value added as operating income plus payroll observed in the National Pension records. We use value added below as shorthand for this constructed accounting measure; it is not asserted to be identical to a national-accounts measure of firm value added.

### Table F2. Audited firm outcomes over three post-investment years

| Outcome | +1 year | +2 years | +3 years |
|---|---|---|---|
| Log value added | 0.0778 [0.0296, 0.1294] (n=147) | 0.0795 [0.0022, 0.1491] (n=117) | 0.0519 [−0.0323, 0.1385](n=90) |
| Log value added per worker | −0.0052 [−0.0333, 0.0261] (n=147) | −0.0030 [−0.0409, 0.0308] (n=117) | 0.0060 [−0.0448, 0.0483](n=90) |
| Log assets | 0.2265 [0.1241, 0.3522] (n=155) | 0.1796 [0.0643, 0.3032] (n=123) | 0.2396 [0.0974, 0.3811] (n=95) |
| Log revenue | −0.0191 [−0.1169, 0.0707] (n=152) | 0.0009 [−0.1153, 0.1174] (n=121) | 0.0622 [−0.0761, 0.2034] (n=93) |
| Return on assets | −0.0079 [−0.0373, 0.0236] (n=155) | −0.0131 [−0.0482, 0.0217] (n=122) | 0.0265 [−0.0107, 0.0684] (n=93) |
| Log value added / assets | −0.0990 [−0.1774, −0.0203](n=146) | −0.0811 [−0.1990, 0.0357] (n=116) | −0.2046 [−0.3299, −0.0713](n=89) |

Notes. Entries are treated-minus-control estimates at the indicated post-investment horizons. Value added is constructed as operating income plus payroll observed in the National Pension records. Samples vary across outcomes and horizons with financial-statement availability and the required post-investment observations. The ±0.10-log-point range used for value added per worker and the ±0.15-log-point range used for revenue are descriptive comparison ranges rather than externally established equivalence thresholds.

Constructed value added is 0.0778 log points above controls after one year [0.0296, 0.1294] and 0.0795 after two years [0.0022, 0.1491]; at three years it is 0.0519 [−0.0323, 0.1385]. Value added per worker changes little: −0.0052, −0.0030, and 0.0060, with intervals inside the stated ±0.10-log-point range. Assets rise more: 0.2265 log points after one year [0.1241, 0.3522], 0.1796 after two [0.0643, 0.3032], and 0.2396 after three [0.0974, 0.3811].

Revenue and profitability do not share that pattern. Revenue is −0.0191 after one year [−0.1169, 0.0707] and remains imprecise later; return on assets is −0.0079 [−0.0373, 0.0236] after one year and −0.0131 [−0.0482, 0.0217] after two. Value added relative to assets falls by 0.0990 [−0.1774, −0.0203] after one year and 0.2046 [−0.3299, −0.0713] after three. The audited sample shows expansion in some measures of scale, not a uniform improvement in operating performance. Assets and constructed value added rise, revenue and return on assets do not rise clearly, and value added relative to assets falls. Given sample selection and the mixed outcomes, the estimates do not establish productivity gains or an organisational mechanism.

## F.3 Sample coverage and continued NPS observation

The audited sample is more selected than the worker-flow sample: the one-year value-added analysis contains 147 events rather than 286, and its targets are generally larger. Without reweighting, Section F.2 describes only targets with the required statements. Long-horizon observability is also ambiguous. A firm can leave the NPS panel after closure, acquisition, restructuring, sale, or administrative re-registration; panel presence is not the same as survival.

### Table F3. Pre-deal hiring state and continued observation in the NPS panel

| Horizon | State contrast in continued NPS observation | 95% CI | Multiplicity-adjusted p | N |
|---|---|---|---|---|
| +12 months | −0.0072 | [−0.0598, 0.0468] | 0.9972 | 224 |
| +24 months | −0.0480 | [−0.1275, 0.0292] | 0.6069 | 194 |
| +36 months | −0.0505 | [−0.1391, 0.0358] | 0.6805 | 167 |
| +48 months | −0.1360 | [−0.2563, −0.0289] | 0.0394 | 133 |

Notes. The contrast compares the top tercile of the state distribution, corresponding to the lowest pre-deal hiring activity, with the bottom tercile in treated-minus-control continued-observation rates. The four horizon-specific two-sided bootstrap probabilities are adjusted using the Šidák correction. Approximately one-third of otherwise usable events cannot contribute to the forty-eight-month estimate because the corresponding transactions occur too close to the end of the NPS panel.

The adjusted contrasts at 12, 24, and 36 months are −0.0072 [−0.0598, 0.0468] (p = 0.9972; n = 224), −0.0480 [−0.1275, 0.0292] (p = 0.6069; n = 194), and −0.0505 [−0.1391, 0.0358] (p = 0.6805; n = 167). At 48 months the contrast is −0.1360 [−0.2563, −0.0289] (p = 0.0394; n = 133) after adjustment across the four horizons. The four-year estimate occurs where follow-up loss is greatest: about one-third of otherwise usable events fall beyond the panel. The data also do not reveal why a firm leaves its NPS reporting unit. We interpret the estimate as a state-dependent difference in longer-run panel presence, not as evidence of failure among low-hiring targets. Separating closure from acquisition, restructuring, sponsor exit, or administrative change requires other data.

## Appendix G. Alternative comparison designs and descriptive checks

This appendix studies four alternatives to the primary design: sponsor exits, not-yet-treated controls, non-private-equity ownership changes, and the association between hiring and realised post-deal cash changes. None supplies a stronger counterfactual. Sponsor exits are sparse; future-treated controls may anticipate their own deals; other ownership changes need not be comparable interventions; and post-deal cash is treatment-affected. The exercises delineate these alternatives rather than serve as independent replications.

## G.1 Sponsor exits and reversibility

We use annual shareholder records to ask whether the worker-inflow response weakens or reverses when the sponsor exits. Sponsor names are normalised and identifiable variants grouped within firms. Only thirteen exits have an identifiable sponsor departure, an assignable period, and twelve months of post-exit NPS data. We rematch each firm at exit using the applicable exact cell and five-nearest-neighbour rule, then measure the twelve-month treated-minus-control change in the no-entry share.

### Table G1. Sponsor exits and reversibility

| Estimate | Value | 95% CI |
|---|---|---|
| Entry-period change in no-entry share | −0.0715 | [−0.1328, −0.0093] |
| Exit-period change in no-entry share | −0.0077 | [−0.1192, 0.0859] |
| Entry + exit | −0.0792 | [−0.2122, 0.0338] |
| Usable sponsor exits | 13 | — |

Notes. The entry-period estimate measures the matched change around the original private equity investment for the thirteen firms later observed to exit. The exit-period estimate measures the corresponding change around sponsor departure after rematching at the exit event. A positive exit-period estimate would offset the negative entry-period change. Their sum is therefore reported as a descriptive measure of how much of the original no-entry-share change remains after incorporating the exit-period estimate. The analysis does not impose that the two event windows represent exact inverse treatments.

For these firms, the no-entry share falls by 0.0715 around entry [−0.1328, −0.0093] and by 0.0077 around exit [−0.1192, 0.0859]. Their sum is −0.0792 [−0.2122, 0.0338]. The combined interval accommodates persistence, partial reversal, and little remaining difference. Thirteen exits do not distinguish these paths with useful precision.

## G.2 Not-yet-treated firms as controls

As an alternative to never-treated controls, we use firms that receive private equity investment sufficiently far in the future. Future-treated firms may share unobserved determinants of eventual private equity selection. But those approaching their own transaction may already be adjusting or responding to related information. Controls must be at least twenty-four months from their own transaction, satisfy the size restriction, and rank among the five nearest neighbours. The gap keeps their deal outside the focal post-event window but cannot exclude anticipation beginning earlier. We report continuous outcomes before the earlier binary comparison. Panel A uses the treated-minus-control change in the share of months with no worker entry. Panel B uses , which retains windows with zero worker entries. Panel C reports the original  statistic, defined as the treated-minus-control difference in the probability that the no-entry share declines between the pre- and post-event windows.

### Table G2. Not-yet-treated private equity targets as controls

Panel A. Continuous change in the no-entry share

| Specification | Estimate | 95% CI | N |
|---|---|---|---|
| Original treated sample and future-treated controls | +0.0411 | [−0.0113, 0.0921] | 186 |
| Expanded treated sample and future-treated controls | +0.0342 | [−0.0074, 0.0722] | 256 |
| Difference | +0.0069 | [−0.0573, 0.0772] | — |

Panel B. Continuous change in

| Specification | Estimate | 95% CI | N |
|---|---|---|---|
| Original treated sample and future-treated controls | +0.0453 | [−0.0062, 0.0946] | 186 |
| Expanded treated sample and future-treated controls | +0.0207 | [−0.0245, 0.0651] | 256 |
| Difference | +0.0246 | Not separately bootstrapped | — |

Panel C. Probability that the no-entry share declines

| Specification | P1​ | 95% CI | N |
|---|---|---|---|
| Original treated sample and future-treated controls | −0.0863 | [−0.1653, −0.0069] | 186 |
| Expanded treated sample and future-treated controls | −0.0577 | [−0.1257, 0.0081] | 256 |
| Difference | −0.0287 | [−0.1295, 0.0713] | — |

Notes. Future-treated controls receive private equity investment at least twenty-four months after the focal event and are selected using a size restriction and five-nearest-neighbour procedure. Panel A reports the continuous change in the no-entry share. Panel B reports the corresponding fixed-window comparison in log(1 + worker-entry rate). Panel C reports the earlier binary P1 statistic. The original sample uses targets linked directly by business registration number; the expanded sample also includes reviewed name-based recoveries. For the expanded P1 sample, changing the minimum gap gives −0.0631 [−0.1254, −0.0003] at eighteen months (n = 272), −0.0577 [−0.1257, 0.0081] at twenty-four months (n = 256), and −0.0660 [−0.1416, 0.0106] at thirty-six months (n = 200).

The continuous outcomes are closer to the paper's fixed-window measures. The original- and expanded-sample no-entry-share estimates are 0.0411 [−0.0113, 0.0921] and 0.0342 [−0.0074, 0.0722], a difference of 0.0069 [−0.0573, 0.0772]. For log(1 + worker-entry rate), the estimates are 0.0453 [−0.0062, 0.0946] and 0.0207 [−0.0245, 0.0651]; their unbootstrapped difference is 0.0246. For the binary P1 statistic, the original-sample estimate is −0.0863 [−0.1653, −0.0069] and the expanded-sample estimate is −0.0577 [−0.1257, 0.0081]. Their difference is −0.0287 [−0.1295, 0.0713]. Not-yet-treated controls do not solve selection. They may better match eventual selection but offer a smaller pool and can anticipate their own transactions. We use them as a stress test, not a replacement for never-treated firms.

## G.3 Non-private-equity ownership changes

Among firms never observed as private equity targets, we identify changes in the largest shareholder and exclude incoming holders identified as financial sponsors. Private equity and other ownership events use annual timing and a common control pool excluding any identified ownership change.

### Table G3. Labour outcomes around non-private-equity ownership changes

| Outcome | Estimate | 95% CI | N |
|---|---|---|---|
| No-entry outcome | 0.0050 | [−0.0066, 0.0176] | 1,191 |
| Employment level | +0.0054 | [−0.0069, 0.0184] | 1,188 |
| Slope with transferred ownership stake | −0.000008 per %p | [−0.0006, 0.0006] | 798 |

Notes. Ownership changes are identified from annual shareholder records among firms never observed as private equity targets. Incoming holders identified as financial sponsors are excluded. The transferred-stake slope uses the recorded percentage of common shares transferred. These comparisons do not establish that the labour response is unique to private equity because non-private-equity ownership transitions need not involve comparable financing, governance, or operating changes.

The no-entry and employment estimates are close to zero. The slope with transferred ownership stake is −0.000008 per percentage point [−0.0006, 0.0006]. The comparison has limited identifying leverage. Other recorded ownership changes need not involve the financing, governance, operating involvement, or effective control associated with private equity, and the shareholder data may miss economically relevant changes.

Supplementary panel. Exploratory ownership-transfer subgroups

| Subgroup | Estimate | Unadjusted p | Šidák-adjusted p |
|---|---|---|---|
| Overall | −0.0052 | 0.4259 | 0.9642 |
| Majority acquisition, <50% → ≥50% | −0.0178 | 0.0361 | 0.1982 |
| Corporate acquirer | −0.0109 | 0.1202 | 0.5364 |
| Individual acquirer, different surname | +0.0059 | 0.3606 | 0.9317 |
| Individual acquirer, same surname | −0.0018 | 0.7820 | 0.9999 |
| Top tercile of transferred stake | −0.0167 | 0.0109 | 0.0634 |

Notes. None of the subgroup comparisons is detected after the Šidák adjustment. Surname similarity is a coarse administrative classification and does not establish a family relationship; it should not be labelled as a family-succession measure in the table or text.

Thus the observed labour response is not shown to be unique to private equity. The ownership changes visible in these records simply lack a comparably clear average movement in the two reported labour outcomes.

## G.4 Post-deal cash changes and hiring: a descriptive comparison

Because cash is measured after the event, the comparison is descriptive, not a mechanism test.

### Table G4. Post-deal cash changes and the no-entry response

Panel A. Cash relative to assets

| Horizon | Treated-minus-control change | 95% CI | N |
|---|---|---|---|
| Transaction year | 0.0327 | [0.0104, 0.0562] | 194 |
| +1 year | 0.0215 | [−0.0024, 0.0483] | 154 |
| +2 years | 0.0179 | [−0.0108, 0.0494] | 122 |

Panel B. No-entry-share change by realised post-deal cash change

| Group | Estimate | 95% CI | N |
|---|---|---|---|
| Bottom cash-change tercile | −0.0631 | [−0.1038, −0.0194] | 61 |
| Top cash-change tercile | −0.0553 | [−0.1019, −0.0092] | 60 |
| Top − bottom | 0.0079 | [−0.0551, 0.0671] | — |

Notes. Panel A reports treated-minus-control changes in cash relative to assets. Panel B defines realised cash change as the treated-minus-control change in cash relative to assets between the fiscal year preceding the deal and the deal year. Tercile cutoffs are calculated among treated firms with the required audited statements. Because this grouping variable is realised after private equity investment, Panel B conditions on a post-treatment variable and is not used to identify a financing mechanism.

Cash relative to assets rises by 0.0327 [0.0104, 0.0562] in the transaction year across 194 events. The estimates are 0.0215 [−0.0024, 0.0483] one year later and 0.0179 [−0.0108, 0.0494] after two years. The no-entry share falls by 0.0631 [−0.1038, −0.0194] in the bottom cash-change tercile and by 0.0553 [−0.1019, −0.0092] in the top tercile. The difference is 0.0079 [−0.0551, 0.0671].

Similar tercile estimates do not show that financial slack is irrelevant. Cash can respond to the transaction, and conditioning on its realised change can select on treatment-affected outcomes or determinants. The comparison cannot determine whether financial conditions cause, follow, or merely covary with the inflow response. Appendix B.5 instead uses pre-investment financial characteristics. The timing differs, but neither exercise identifies a financing mechanism.

## Appendix H. Conditional monthly positive-entry hazard

The fixed-window analysis aggregates worker inflows over twelve months. Here we instead model, month by month, whether a firm records any NPS worker entry. The hazard conditions on time since the previous positive-entry month, which evolves with post-investment entries and may itself be affected by treatment. It therefore describes conditional monthly incidence, not the causal average response or the event-level state gradient.

## H.1 Post-investment positive-entry hazard

The sample contains 48,853 firm-months from 379 matched events. We estimate a grouped-binomial complementary log-log model with event and duration fixed effects and event-clustered standard errors. Duration counts consecutive no-entry months immediately before the current month and is grouped as 1, 2, 3, 4–5, 6–11, and at least 12, capped at 24. An entry resets the next month's count to one. After the panel begins or an observation gap occurs, six consecutive observed months are required. We exclude the transaction month and use months −12 to −1 and +1 to +12.

### Table H1. Conditional monthly positive-entry hazard

| Specification | Hazard ratio | 95% CI |
|---|---|---|
| Post-investment positive worker entry, treated relative to matched controls | 1.1593 | [1.0834, 1.2409] |

Notes. The complementary log-log model includes event fixed effects and fixed effects for duration categories 1, 2, 3, 4–5, 6–11, and ≥12 months, with standard errors clustered by event. The sample contains 379 matched events and 48,853 firm-month observations. Because duration evolves with post-investment worker entries, the hazard ratio is a conditional descriptive estimand rather than a direct analogue of the fixed-window hiring-rate response.

The treated-post hazard ratio is 1.1593 [1.0834, 1.2409], or 15.9 percent higher conditional incidence of a positive-entry month. The hazard discards the number of entries within such a month and conditions on evolving duration, so it is not a second estimate of the twelve-month hiring-rate effect. The estimate shows that positive-entry months become more common after investment; it does not measure the magnitude of the fixed-window worker-inflow response.

## H.2 Pre-deal hiring state and the monthly positive-entry hazard

The state interaction in the hazard model draws on different variation from the primary event-level gradient. The primary estimator relates a twelve-month treated-minus-control response to the continuous target state; the hazard estimates conditional monthly incidence with event and duration fixed effects. The continuous state used in this analysis is the treated target’s , measured over months −24 through −13. It enters without rescaling and is assigned to every firm-month in the corresponding matched event; a matched control therefore carries the treated target’s state rather than its own state value.

### Table H2. Pre-deal hiring-state interaction in the monthly positive-entry hazard

| Matching design | State interaction, hazard ratio | 95% CI |
|---|---|---|
| Conventional matching, state not exact-matched | 1.204 | [1.0205, 1.4205] |
| State-balanced matching, continuous state | 1.5074 | [0.8710, 2.6087] |
| State-balanced matching, state tercile | — | — |

Notes. The conventional specification uses 308 events, 3,919 grouped cells, and 41,303 firm-month observations. The state-balanced continuous specification uses 308 events, 1,199 grouped cells, and 38,652 firm-month observations. Both models contain event fixed effects and duration-category fixed effects, with standard errors clustered by event. The continuous state is the treated target’s unrescaled −log(1 + worker-entry rate) over months −24 through −13 and is assigned to every firm-month in the corresponding matched event. The state-tercile interaction is not separately estimable in the state-balanced event-fixed-effect model because the tercile indicator defining the exact matching cell is constant within event and therefore collinear with the event fixed effects.

The hazard interaction and the event-level gradient are different parameters. The latter first balances controls on the target state and constructs a fixed-window response; the former conditions monthly incidence on duration and event fixed effects. The conventional-matching interaction is positive and more precise. Under state-balanced matching, the point estimate remains above one but is imprecise; it neither replicates nor falsifies the primary gradient. State-dependent adjustment is identified by the fixed-window matched gradient, not this hazard model.
