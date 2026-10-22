# Lab 15 Implementation

```mermaid
flowchart TD
    A[Manual Meridian inputs:<br/>expected returns, volatilities, correlations] --> C[Validate correlation table]
    B[Monthly adjusted-price CSV] --> B1[Validate Date-first, oldest-first,<br/>and numeric price data]
    B1 --> B2[Calculate monthly returns;<br/>annualize mean returns and volatility;<br/>calculate correlations]
    B2 --> C
    C --> D[Build covariance matrix]
    D --> E[Grid search all long-only mixes<br/>in 5-percentage-point steps]
    E --> F[For each mix, calculate expected return,<br/>reserve-eligible weight, and portfolio volatility]
    F --> G{Expected return meets objective<br/>and reserve-eligible weight meets minimum?}
    G -- Yes --> H[Compare volatility with qualifying mixes]
    H --> I[Lowest-volatility qualifying mix]
    G -- No --> J{More grid mixes?}
    H --> J
    J -- Yes --> E
    J -- No, none qualified --> K[No mix meets objective]
    J -- No, qualifier found --> I
```

The manual Meridian-input path uses the editable annual expected returns, volatilities, and correlations directly. The monthly-price CSV path instead validates monthly adjusted prices and estimates annual returns, volatility, and correlations from monthly returns before using the same covariance and grid-search steps. Every 5-percentage-point long-only mix must meet both the objective and reserve rule; among the qualifying mixes, the one with the lowest volatility is returned.
