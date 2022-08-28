<div style="text-align: justify">

<h1>Sticker Album Cost Estimator</h1>

### This script estimates the amount of money you'll need to complete a sticker album

<p1>What if we could not swap stickers to complete the album? How much money we would need to spend to do that? </p1>

<p1>We can answer this question by making a Monte Carlo simulation. In this example I used the world cup sticker album 2022 to run a simulation. The album has 670 stickers and each sticker costs R$ 0,80. The costs are estimated in the brazilian real (BRL), but the only adjustment you have to do to change it to your country's currency it's to set the price of the sticker. </p1>

<p1>The idea behind the simulation is to sort numbers representing the stickers till we get the 670 different ones, count how many stickers we needed to complete the task, do it 1000 times and then analyses the data to see what we got. </p1>

<h3>Analysing the data</h3>

<p1>The program calculate central tendency values and generate histograms and box-plot charts to analyse the data from the simulation. In the example, after 1000 iterations, the result looks like this:<p>

| Number of Iterations | Mean (R$) | Standard Deviation (R$) |
| --- | --- | --- |
| 1,000 | 3,785.91 | 685.86 |

<p1>So the average money spent to complete the album is R$ 3,785.91 and the histogram is showed below.<p1>

<img src=/static/h_1000.png>

<p1>The histogram show us a skew to the right, which is an indicative that the mean may not be the best way to estimate the cost to complete the album. For this reason, it's good to calculate the median, the interquartile range (IQR) and plot a box-plot chart to visualize all this information.<p1>

| Number of Iterations | Median (R$) | IQR (R$) |
| --- | --- | --- |
| 1,000 | 3,688.00 | 810 |

<p1>The difference wasn't so high between the median and the mean, but now the mean is 
supported by a much more robust method. </p1>

<img src=/static/b_1000.png>

<p1>⚠️  This script considers that every sticker has the same chance to be sorted.</p1>

</div>
