
## Climate Risk Modelling

### General-Purpose Climate Risk Model

Climate risk can generally be measured as a combination of three components:

| Component | Definition |
|---|---|
| **Hazard** (physical risk) / **Driver** (transition risk) | The factors that can cause damage — hazard for physical risk; driver for the source of risk in transition risk |
| **Exposure** | The extent to which a counterparty is exposed to a hazard |
| **Vulnerability** | Any adaptation the counterparty has implemented to reduce the impact of a hazard |

### Data

There are four useful categories of climate risk data:

| Category | Description |
|---|---|
| **Climate data** | Weather data such as temperature and rainfall |
| **Climate hazard data** | Data relating to hazards resulting from weather, such as fire or floods |
| **Climate-related data** | Data on factors that can affect climate, such as emissions |
| **Exposure data** | Data on exposures which are sensitive to climate risk |

Note: these categories are not mutually exclusive (e.g. temperature can be both climate data and used to determine heat stress as a hazard).

#### Physical Risk Data

Physical risk requires climate data such as rainfall and temperature. There are three main sources:

| Source | Strengths | Weaknesses |
|---|---|---|
| **Weather station data** | Most accurate — relies on actual measurements | Incomplete (instrument failure); limited number of stations means it is ultimately a sample; gaps require infilling at cost |
| **Satellite data** | Better geographic coverage | Lower temporal granularity (max ~2 readings per day); accuracy limited by cloud cover; algorithms apply estimation to imagery |
| **Interpolated data** | More granular than station data; useful for regional modelling | Interpolation itself is a modelling assumption, introducing additional inaccuracy; quality depends on source data quality |

Given the variance of climate data by location, it is important to **geolocate exposure data** so that models do not need to summarise climate across several regions.

#### Transition Risk Data

Transition risk makes use of **climate-related data**, such as carbon emissions, focusing on sectoral rather than geographic granularity:

- **Firm emissions data**: The primary data point of interest for transition risk, but a particularly difficult data item to source. Some firms voluntarily post emissions, but this represents a minority of wholesale exposures. For smaller firms, proxies or estimates are required — noting that even firms' own emissions estimates are inherently uncertain.
- **Sector as proxy**: Sector is commonly used as a proxy for transition risk (different sectors have different carbon intensity), but this is imperfect — e.g. two utilities firms may have very different carbon profiles (coal vs. renewables), yet both are classified as utilities.
- **Expert-based data sources**: Credit [[04-ratings_agencies|ratings agencies]] and other data providers are increasingly offering views on climate risk by sector or for key individual exposures.

#### Stranded Assets

A **stranded asset** is one that has suffered from an unanticipated or premature write-down. Relevant causes include:

- Technological change making current technology obsolete before it generates economic value
- Changing climate patterns making property values unsustainable (e.g. coastal homes as sea levels rise)
- At a macroeconomic level: entire industries or countries heavily reliant on a single high-emission industry (e.g. fossil fuel generation) may face significant transition risk

Assessing stranded assets requires a view of a firm's balance sheet and expert judgement on which assets may become stranded — this is a non-trivial exercise and may form part of a model development process itself.

### General Considerations

As it stands, there is **no 'best way'** to go about climate risk modelling. Several climate risk stress tests have been run by [[05-central_banks|central banks]] around the world (e.g. [[bank_of_england|Bank of England]]'s 2021 Biennial Exploratory Scenario for climate-related financial risks), and there is currently **no single benchmark model** being used. Regardless, there are common considerations when choosing the best approach for a specific institution.

## References and Further Reading

- NGFS. (June 2020). *Climate Scenarios Database*. <https://www.ngfs.net/en>
- NGFS. (April 2019). *A call for action: Climate change as a source of financial risk*.
- NGFS. (June 2020). *NGFS Climate Scenarios for [[05-central_banks|central banks]] and supervisors*.
- IPCC. (October 2018). *Global Warming of 1.5°C*.
- IPCC. (October 2014). *AR5 Synthesis Report*.
- IAA. (February 2021). *Introduction to Climate-Related Scenarios*.
- TCFD. (June 2017). *Recommendations of the Task Force on Climate-related Financial Disclosures*.
- [[bank_of_england|Bank of England]]. (2021). *Key elements of the 2021 Biennial Exploratory Scenario: Financial risks from climate change*. <https://www.bankofengland.co.uk/stress-testing/2021/key-elements-2021-biennialexploratory-scenario-financial-risks-climate-change>
