---
title: 'Algo Trading: algorithms to beat the market'
date: '2020-02-02T18:36:06.206Z'
excerpt: >-
  TL;DR:    2019 was an outstanding year for the stock market. With such a
  performance it was hard to...
thumb_img_path: null
comments_count: 0
positive_reactions_count: 6
tags:
  - investing
  - trading
  - python
  - strategies
canonical_url: >-
  https://medium.com/my-new-knowledge/algo-trading-algorithms-to-beat-the-market-ccad674258b0
layout: post
---

> TL;DR:
> - 2019 was an outstanding year for the stock market.
> - With such a performance it was hard to come up with an algorithm the could beat the market.
> - Running the same algo with data from 2016 I had a small but consistent average edge of 10% over the market.
> - Define common "mean reversion" strategy and indicators as Bollinger Bands®.
> - There are alternative strategies, like using margin to multiply your earnings (or loses!).

During 2019, the stock market grew. A lot.

Take for example an ETF I like: FTEC (Fidelity MSCI Information Technology Index ETF):

During 2019, FTEC’s price grew from $49.35 to $72.48: a staggering almost 50% growth!

That’s almost double of the standard bearer S&P500 that grew “only” around 30%.

Stocks like APPL (Apple Inc.) grew even more, over 90%!

Put neatly:


```
S&P 500: 30%
FTEC: 50%
V: 41%
AAPL: 90%
```


![Some stocks return during 2019](https://miro.medium.com/max/1062/1*J_KSSzCofolhkFggocVXZA.png)
<figcaption>Some stocks return during 2019</figcaption>

It’s easy to check out using [finance.yahoo.com](https://finance.yahoo.com/chart/MA# eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjMuOTcyMzMyMDE1ODEwMjc3LCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6Ik1BIiwiY2hhcnROYW1lIjoiY2hhcnQiLCJ0b3AiOjB9fSwic2V0U3BhbiI6eyJtdWx0aXBsaWVyIjoxLCJiYXNlIjoieWVhciIsInBlcmlvZGljaXR5Ijp7InBlcmlvZCI6MSwiaW50ZXJ2YWwiOiJkYXkifSwibWFpbnRhaW5QZXJpb2RpY2l0eSI6dHJ1ZSwiZm9yY2VMb2FkIjp0cnVlfSwibGluZVdpZHRoIjoyLCJzdHJpcGVkQmFja2dyb3VkIjp0cnVlLCJldmVudHMiOnRydWUsImNvbG9yIjoiIzAwODFmMiIsImV2ZW50TWFwIjp7ImNvcnBvcmF0ZSI6eyJkaXZzIjp0cnVlLCJzcGxpdHMiOnRydWV9LCJzaWdEZXYiOnt9fSwiY3VzdG9tUmFuZ2UiOm51bGwsInN5bWJvbHMiOlt7InN5bWJvbCI6Ik1BIiwic3ltYm9sT2JqZWN0Ijp7InN5bWJvbCI6Ik1BIn0sInBlcmlvZGljaXR5IjoxLCJpbnRlcnZhbCI6ImRheSIsInRpbWVVbml0IjpudWxsLCJzZXRTcGFuIjp7Im11bHRpcGxpZXIiOjEsImJhc2UiOiJ5ZWFyIiwicGVyaW9kaWNpdHkiOnsicGVyaW9kIjoxLCJpbnRlcnZhbCI6ImRheSJ9LCJtYWludGFpblBlcmlvZGljaXR5Ijp0cnVlLCJmb3JjZUxvYWQiOnRydWV9fSx7InN5bWJvbCI6IkFBUEwiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiQUFQTCJ9LCJwZXJpb2RpY2l0eSI6MSwiaW50ZXJ2YWwiOiJkYXkiLCJ0aW1lVW5pdCI6bnVsbCwic2V0U3BhbiI6eyJtdWx0aXBsaWVyIjoxLCJiYXNlIjoieWVhciIsInBlcmlvZGljaXR5Ijp7InBlcmlvZCI6MSwiaW50ZXJ2YWwiOiJkYXkifSwibWFpbnRhaW5QZXJpb2RpY2l0eSI6dHJ1ZSwiZm9yY2VMb2FkIjp0cnVlfSwiaWQiOiJBQVBMIiwicGFyYW1ldGVycyI6eyJjb2xvciI6IiNhZDZlZmYiLCJ3aWR0aCI6MiwiaXNDb21wYXJpc29uIjp0cnVlLCJjaGFydE5hbWUiOiJjaGFydCIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJBQVBMIn0sInBhbmVsIjoiY2hhcnQiLCJhY3Rpb24iOm51bGwsInNoYXJlWUF4aXMiOnRydWUsInN5bWJvbCI6IkFBUEwiLCJnYXBEaXNwbGF5U3R5bGUiOiJ0cmFuc3BhcmVudCIsIm5hbWUiOiJLNThVTkRNSUFSIiwib3ZlckNoYXJ0Ijp0cnVlLCJ1c2VDaGFydExlZ2VuZCI6dHJ1ZSwiaGVpZ2h0UGVyY2VudGFnZSI6MC43LCJvcGFjaXR5IjoxLCJoaWdobGlnaHRhYmxlIjp0cnVlLCJ0eXBlIjoibGluZSIsInN0eWxlIjoic3R4X2xpbmVfY2hhcnQifX0seyJzeW1ib2wiOiJWIiwic3ltYm9sT2JqZWN0Ijp7InN5bWJvbCI6IlYifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnsibXVsdGlwbGllciI6MSwiYmFzZSI6InllYXIiLCJwZXJpb2RpY2l0eSI6eyJwZXJpb2QiOjEsImludGVydmFsIjoiZGF5In0sIm1haW50YWluUGVyaW9kaWNpdHkiOnRydWUsImZvcmNlTG9hZCI6dHJ1ZX0sImlkIjoiViIsInBhcmFtZXRlcnMiOnsiY29sb3IiOiIjNzJkM2ZmIiwid2lkdGgiOjIsImlzQ29tcGFyaXNvbiI6dHJ1ZSwiY2hhcnROYW1lIjoiY2hhcnQiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiViJ9LCJwYW5lbCI6ImNoYXJ0IiwiYWN0aW9uIjoiYWRkLXNlcmllcyIsInNoYXJlWUF4aXMiOnRydWUsInN5bWJvbCI6IlYiLCJnYXBEaXNwbGF5U3R5bGUiOiJ0cmFuc3BhcmVudCIsIm5hbWUiOiJLNThVWU1KMVgxIiwib3ZlckNoYXJ0Ijp0cnVlLCJ1c2VDaGFydExlZ2VuZCI6dHJ1ZSwiaGVpZ2h0UGVyY2VudGFnZSI6MC43LCJvcGFjaXR5IjoxLCJoaWdobGlnaHRhYmxlIjp0cnVlLCJ0eXBlIjoibGluZSIsInN0eWxlIjoic3R4X2xpbmVfY2hhcnQifX0seyJzeW1ib2wiOiJTUFkiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiU1BZIn0sInBlcmlvZGljaXR5IjoxLCJpbnRlcnZhbCI6ImRheSIsInRpbWVVbml0IjpudWxsLCJzZXRTcGFuIjp7Im11bHRpcGxpZXIiOjEsImJhc2UiOiJ5ZWFyIiwicGVyaW9kaWNpdHkiOnsicGVyaW9kIjoxLCJpbnRlcnZhbCI6ImRheSJ9LCJtYWludGFpblBlcmlvZGljaXR5Ijp0cnVlLCJmb3JjZUxvYWQiOnRydWV9LCJpZCI6IlNQWSIsInBhcmFtZXRlcnMiOnsiY29sb3IiOiIjZmY4MGM1Iiwid2lkdGgiOjIsImlzQ29tcGFyaXNvbiI6dHJ1ZSwiY2hhcnROYW1lIjoiY2hhcnQiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiU1BZIn0sInBhbmVsIjoiY2hhcnQiLCJhY3Rpb24iOiJhZGQtc2VyaWVzIiwic2hhcmVZQXhpcyI6dHJ1ZSwic3ltYm9sIjoiU1BZIiwiZ2FwRGlzcGxheVN0eWxlIjoidHJhbnNwYXJlbnQiLCJuYW1lIjoiSzU4VVlUVTNMQiIsIm92ZXJDaGFydCI6dHJ1ZSwidXNlQ2hhcnRMZWdlbmQiOnRydWUsImhlaWdodFBlcmNlbnRhZ2UiOjAuNywib3BhY2l0eSI6MSwiaGlnaGxpZ2h0YWJsZSI6dHJ1ZSwidHlwZSI6ImxpbmUiLCJzdHlsZSI6InN0eF9saW5lX2NoYXJ0In19LHsic3ltYm9sIjoiRlRFQyIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJGVEVDIn0sInBlcmlvZGljaXR5IjoxLCJpbnRlcnZhbCI6ImRheSIsInRpbWVVbml0IjpudWxsLCJzZXRTcGFuIjp7Im11bHRpcGxpZXIiOjEsImJhc2UiOiJ5ZWFyIiwicGVyaW9kaWNpdHkiOnsicGVyaW9kIjoxLCJpbnRlcnZhbCI6ImRheSJ9LCJtYWludGFpblBlcmlvZGljaXR5Ijp0cnVlLCJmb3JjZUxvYWQiOnRydWV9LCJpZCI6IkZURUMiLCJwYXJhbWV0ZXJzIjp7ImNvbG9yIjoiI2ZmYmQ3NCIsIndpZHRoIjoyLCJpc0NvbXBhcmlzb24iOnRydWUsImNoYXJ0TmFtZSI6ImNoYXJ0Iiwic3ltYm9sT2JqZWN0Ijp7InN5bWJvbCI6IkZURUMifSwicGFuZWwiOiJjaGFydCIsImFjdGlvbiI6ImFkZC1zZXJpZXMiLCJzaGFyZVlBeGlzIjp0cnVlLCJzeW1ib2wiOiJGVEVDIiwiZ2FwRGlzcGxheVN0eWxlIjoidHJhbnNwYXJlbnQiLCJuYW1lIjoiSzU4VVoyTTdHSSIsIm92ZXJDaGFydCI6dHJ1ZSwidXNlQ2hhcnRMZWdlbmQiOnRydWUsImhlaWdodFBlcmNlbnRhZ2UiOjAuNywib3BhY2l0eSI6MSwiaGlnaGxpZ2h0YWJsZSI6dHJ1ZSwidHlwZSI6ImxpbmUiLCJzdHlsZSI6InN0eF9saW5lX2NoYXJ0In19XSwic3R1ZGllcyI6eyJ2b2wgdW5kciI6eyJ0eXBlIjoidm9sIHVuZHIiLCJpbnB1dHMiOnsiaWQiOiJ2b2wgdW5kciIsImRpc3BsYXkiOiJ2b2wgdW5kciJ9LCJvdXRwdXRzIjp7IlVwIFZvbHVtZSI6IiMwMGIwNjEiLCJEb3duIFZvbHVtZSI6IiNGRjMzM0EifSwicGFuZWwiOiJjaGFydCIsInBhcmFtZXRlcnMiOnsid2lkdGhGYWN0b3IiOjAuNDUsImNoYXJ0TmFtZSI6ImNoYXJ0In19fX0%3D).

Compare that with 2016, it’s a completely different picture.


```
S&P 500: 12%
FTEC: 15%
V: 3.1%
AAPL: 10%
```


![Same stocks, but with data during 2015](https://miro.medium.com/max/1060/1*QiqCdLquoxpjcmxkEf_AJg.png)
<figcaption>Same stocks, but with data during 2015</figcaption>

It is evident that 2019 was a very good year for the stock market and for the “buy and hold strategy”.

I was thinking about this today and I decided to compare the performance of my algorithm comparing 2019 with 2016.

I couldn’t beat the market with data from 2019.

But running the same unpolished and very basic algo against data from 2016, my algorith had an edge of about 10% on average over the market.

When I saw this, I could finally understand why my algo trading code never beat the market. It’s hard to beat the 2019 performance of the stock market.

<hr />

People mostly refer to “the market” as the return showed by the S&P 500 (Standard and Poor 500) index. As most of you know, S&P 500 “is a stock market index that measures the stock performance of 500 large companies listed on stock exchanges in the United States”. So it’s a good indicator of how well the stock market is doing as a whole.

Some say that to make money with an Algo Trading algorithm you basically need to come up with a way of «predicting the market».

I would say that this is partially true but at the same time somewhat misleading.

It’s true that in order to make a profit you need to know when to buy and when to sell. But its misleading to call this “predicting the market” as if one were an oracle, or one pretended to read the future with a magic crystal ball.

For example, some would argue that if the price of a stock increases steadily as a straight line, the only way to make money would be to “buy and hold”. This is partially true.

If the price of a stock increase steadily as a straight line, there are no moments where the price can be considered low relative to the mean since the price is always increasing.

So, in this case, it would be imposible to buy at a low price and sell at a higher price.

It would be better to buy at the beginning and sell at the end (whenever you wish to enter or exit the market) and be «exposed» to the stock the longest possible time.

However, one strategy in this case would be to use «margin».

Margin is basically borrowing money from your broker using your securities as a collateral.

In this example, using margin could multiply your winnings simply by buying more. HOWEVER, it could also multiply you loses.

Some brokers offer annual fees as low as 3.75%.

For example, if you borrow $5.000 overnight, you end up paying a $0.52 surplus over the loan.

If your stock ends up making 10%, you pay 3.75% for the loan and pocket the rest 6.25%.

Again, bear in mind that the same way your winnings can be augmented, it’s equally true for your losses. That is, if a your stock loses $1, you actually lose $2 due to margin PLUS the interest (assuming 2x margin).

Although there are countless strategies, many revolve against the concept of mean reversion (“ Mean reversion is a theory used in finance that suggests that asset prices and historical returns eventually will revert to the long-run mean or average level of the entire dataset.”).

There are also many ‘indicators’ that promise to tell you when to buy or sell, or what the market trend is.

A very basic one is to calculate the “standard deviation” of the random price fluctuations, or volatility of the stock.

The indicator named “Bollinger bands®” uses the standard deviation

The standard deviation is easily calculated with, for example, Pandas (“ pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language”).

We’ll be using Pandas in future articles where I’ll share some simple code to get started with algo trading.

I don’t think any are proverbial indicator or strategies («TL;DR Nobody has cracked it. Period.*»). It’s pretty obvious because if these strategies or indicators were magical and openly disclosed, most algotraders would already be rich or making a ton of money.

Also, if these strategies or indicators were so good, it’s hard to think they would be openly available on the internet.

<hr />

If you are looking for a very good Algo Trading platform, I would certainly recommend Alpaca. They are truly a platform dedicated mostly to algorithmic trading. You can also buy/sell stocks in their online platform. They offer margin. Also they have neat integrations, for example with TradingView.

Alpaca also offers a very nice paper account trading. This paper account trading let’s you trade as if you had a live account, but with «fake» money. You can test your algorithms posting buy/sell orders, etc.

But I find more useful doing very simple custom baked “backtesting” scripts. Backtesting is testing your algorithm using historical data. But remember the mantra: «Past Performance Is No Guarantee of Future Results».

<hr />

I recently did a basic backtesting script using Alpaca, downloading data for free from Polygon.io and coded in Python. In fact over time I’ve done a couple. It isn’t hard.

My custom backtesting script basically loops over the data (in days, minutes, or all quotes, transactions, etc). It simulates the decision making on when to buy or sell, and keeps track of the prices. At the end I like to know how much money the algorith would have made or lost.

<hr />

If you find any of this information useful, or have any questions or suggestions or comments, please leave your comments below.

I’ll be writing more articles soon sharing my experience with algo trading, and some code to get started.

[Here’s my next article](https://medium.com/@mrodz/algo-trading-backtesting-your-algorithm-bd6d7385c89c) on how to download historical minute data using Alpaca (the data and code I was mentioning a couple of paragraphs above), and do a simple backtest for the Buy and Hold strategy.

In the third part of this series, we’ll build on our code and work on a scalping script, that even gives good results with 2016 data.

Then I might also want to write about some other strategies I’ve tried, and provide code snippets that some might find useful.

Ideas, comments?

See you next time!

*[This post is also available on DEV.](https://dev.to/michrodz/algo-trading-algorithms-to-beat-the-market-3plm)*


<script>
const parent = document.getElementsByTagName('head')[0];
const script = document.createElement('script');
script.type = 'text/javascript';
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.1.1/iframeResizer.min.js';
script.charset = 'utf-8';
script.onload = function() {
    window.iFrameResize({}, '.liquidTag');
};
parent.appendChild(script);
</script>
