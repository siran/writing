---
title: 'Algo Trading: backtesting an intraday scalping strategy'
date: '2020-01-28T01:17:37.719Z'
excerpt: >-
  This is the third article of a series I’ve been writing. If interested you can
  start here....
thumb_img_path: null
comments_count: 0
positive_reactions_count: 4
tags:
  - scalping
  - stocks
  - investment
  - backtesting
canonical_url: >-
  https://medium.com/my-new-knowledge/algo-trading-backtesting-an-intraday-scalping-strategy-with-a-simple-custom-script-fcd15642555
layout: post
---
This is the third article of a series I’ve been writing. If interested you can start here.

## What is scalping?

In the trading world, “scalping” refers to taking many small profits as quickly as possible instead of using a “buy and hold’ strategy and wait a longer period of time to make a — hopefully — bigger profit.

![Alt Notice the green and red dots during trading day (purchases and sells, respectively). The title of $1031 refers to a 9.6% profit over a $1000 initial simulated investment, after about 70 days (3 1/2 trading months).](https://miro.medium.com/max/1310/1*NYUKp8IdV01zW0TOTyet_A.png)

Investopedia defines a scalper as someone that
> intends to take as many small profits as possible, without letting them evaporate. This is the opposite of the “let your profits run” mindset, which attempts to optimize positive trading results by increasing the size of winning

As mentioned in my [first article](https://medium.com/@mrodz/algo-trading-algorithms-to-beat-the-market-ccad674258b0), the use of margin might be useful to further increase the profits (or losses) made with a scalping strategy.

Doing manual scalping might be a time-intensive and stressful activity, since you have to keep track of all the charts for the stocks you care. And buy/sell many times at the right moments.

Imagine doing all submitting all those BUY and SELL orders as seen in the figure above. Doing that manually, with many stocks, is virtually impossible.

A computer can do this hard work for you. Faster and better.

# Let a computer do the hard work for you
Algo Trading is a very handy and simple way to exploit the scalping strategy.

With Algo Trading, you can do a simple script that buy or sells a stock when certain condition are met. This happens as frequently as you want: many times a day, a minute or whatever.

The idea is to build a script that buys and sell as many times as possible, making a small profit as often as possible.

Scalping is just a general mindset of what we want to do. But we still need some indicator or signal of when to buy or sell.

# The concept of “mean reversion”

![Alt The price fluctuates around the average.](https://miro.medium.com/max/1400/0*wmcHG94evf4hK7Fj.jpg)

In case it’s not already clear by the image above, Investopedia defines “mean reversion” as:

> Mean reversion is a theory used in finance that suggests that asset prices and historical returns eventually will revert to the long-run mean or average level of the entire dataset.

This means that the price of a stock will in general tend to “revert” to its average price.

That is, if a price suddenly hikes we would expect it to return to a lower value. Also, if a price suddenly drops we would expect it to return to a higher value.

We can use this idea to have buy signals. If the price of a stocks crosses the average from a lower to a higher price, we might decide to Buy.

The scalping strategy suggests to sell as soon as price of the stock is higher than the purchase price.

# Backtesting a scalping strategy

In my last article, [Algo Trading: backtesting your algorithm](https://medium.com/@mrodz/algo-trading-backtesting-your-algorithm-bd6d7385c89c), I posted some sample code on how to download one year of data.

Also how we could backtest a simple “buy and hold” strategy over that year of data.

Now, I’m going to share a script that allows you to backtest a scalping algo trading algorithm.

The idea of the script is to:

- Loop over all days of a given year.
- Calculate a n-point moving average of the close price.
- For every day, loop over the minute-by-minute data.
- If the open price for a given minute changes from being below the average to above the average we simulate a Buy.
- We sell as soon as the open price is greater than the buy_price.

If you already downloaded the data as shown in my previous article, the script copied below should work out of the box.

With 2016 data, using AAPL it performs almost 3x over a Buy and Hold strategy! From 9.9% to 30.2%.


```
AAPL - market change: 1.099
AAPL - wallet change: 1.302
```


If you also download the data for FTEC and V and run the script using


```
SYMBOLS = ["AAPL", "V", "FTEC"]
```


you would also obtain good profits over a Buy and Hold strategy:


```
AAPL - market change %: 1.099
AAPL - wallet change %: 1.302
AAPL - num_transactions: 454
...
V - market change %: 1.032
V - wallet change %: 1.049
V - num_transactions: 290
...
FTEC - market change %: 1.145
FTEC - wallet change %: 1.298
FTEC - num_transactions: 390
```


Check out [the script](https://gist.github.com/siran/5f06c569e83579c5849ec55b32e38326# file-backtest_scalping-py)

But again, as said in my first article, this same algorith underperforms using data from 2019! : /

Also, I haven’t tested for a wider range of symbols.

I’ll do that for a next article.

I also want to do a rolling profit analysis over this strategy with more stocks. My goal will be to determine if there’s a moment common to most stocks were the market started growing so much in 2019.

Any ideas? Would be glad to read your comments on ways to improve this.

[Full article here](https://medium.com/my-new-knowledge/algo-trading-backtesting-an-intraday-scalping-strategy-with-a-simple-custom-script-fcd15642555)


*[This post is also available on DEV.](https://dev.to/michrodz/algo-trading-backtesting-an-intraday-scalping-strategy-3337)*


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
