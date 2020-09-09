# Chart recommender

This project is adapted from [suggest-chart](https://github.com/tejesh0/suggest-chart/) by [@tejesh0](https://github.com/tejesh0).

## How it works

data file -> column type detection -> map against rules -> recommend charts

### Rules

Rules are configured to work for a combination of numeric and categorical columns. `num` and `cat` refer to numeric and categorical columns, respectively.

<br>Below charts are recommended for numeric and categorical columns:

| Combination | Distribution of columns | Uniqueness | Charts |
| --- | --- | --- | --- |
| Numeric and Categorical columns | 1 `num`, 1 `cat` | Unique values in categorical column | ['lollipop', 'bar_plot', 'circular_bar_plot', 'treemap', 'circlepack'] |
| Numeric and Categorical columns | 1 `num`, 1 `cat` | Non-unique values in categorical column | ['boxplot', 'violin_plot'] |
| Numeric and Categorical columns | >1 `num`, 1 `cat` | Unique values in categorical column | ['multi_line', 'parallel_plot', 'stacked_bar_plot', 'grouped_bar_plot'] |
| Numeric and Categorical columns | >1 `num`, 1 `cat` | Non-unique values in categorical column | ['grouped_scatterplot'] |
| Numeric and Categorical columns | 1 `num`, >1 `cat` | Unique values in categorical column | ['multi_line', 'parallel_plot', 'stacked_bar_plot', 'grouped_bar_plot']. <br><br> A variation of this is a nested view with these charts as possibilities: ['lollipop', 'bar_plot', 'circular_bar_plot', 'treemap', 'circlepack'] |
| Numeric and Categorical columns | 1 `num`, >1 `cat` | Non-unique values in categorical column | ['box_plot', 'violin_plot'] |
| Numeric and Categorical columns | 1 `num`, >1 `cat` | Non-unique values in categorical column | Using Adjacency as a principle, these are the chart possibilities: ['network', 'sankey', 'chord', 'arc'] |

<br>Below charts are recommended for numeric columns alone:

| Combination | Distribution of columns | Uniqueness | Charts |
| --- | --- | --- | --- |
| Numeric | 1 `num` | - | ['histogram', 'density_plot'] |
| Numeric | 2 `num` | Unordered, few data points | ['facet_box_plot', 'scatterplot'] |
| Numeric | 2 `num` | Unordered, many data points | ['facet_violin_plot', 'facet_density_plot'] |
| Numeric | 2 `num` | Ordered | ['line_chart', 'area_chart', 'connected_scatterplot'] |
| Numeric | 3 `num` | Unordered | ['box_plot', 'violin_plot', 'bubble_plot'] |
| Numeric | 3 `num` | Ordered | ['stacked_area_plot', 'line_graph'] |
| Numeric | >3 `num` | Unordered | ['box_plot', 'violin_plot', 'heatmap', 'correlogram'] |
| Numeric | >3 `num` | Ordered | ['stacked_area_plot', 'line_graph'] |

<br>Below charts are recommended for numeric columns alone:

| Combination | Distribution of columns | Type | Charts |
| --- | --- | --- | --- |
| Categorical | 1 `cat` | - | ['barplot', 'lollipop', 'donut', 'treemap', 'circlepack'] |
| Categorical | >1 `cat` | Nested | ['sunburst', 'treemap'] |
| Categorical | >1 `cat` | Subgroup | ['grouped_scatterplot', 'parallel_plot', 'stacked_bar_plot', 'grouped_bar_plot'] |
| Categorical | >1 `cat` | Adjacency | ['heatmap', 'network', 'sankey'] |


<br>This work follows a subset of the excellent rule set defined by [from Data to Viz](https://www.data-to-viz.com/).

## Recommended charts

Here is the list of all possible chart recommendations:

- bar chart
- box plot
- bubble sort
- circlepack
- connected scatterplot
- correlogram
- density plot
- donut
- facet box plot
- facet density plot
- grouped scatterplot
- heatmap
- histogram
- line chart
- lollipop
- parallel coordinates
- network
- stacked bar chart
- stacked area chart
- sankey
- scatterplot
- sunburst
- treemap
- violin plot

## Application setup

- [Install Gramex 1.x](https://learn.gramener.com/guide/install/)
- Clone this repository
- From the repo folder, run `gramex setup .`
- From the repo folder, run `gramex`

## Contributions

- Bhanu Kamapantula <bhanu.kamapantula@gramener.com>
- Tejesh <tejesh.p@gramener.com>
- Pragnya Reddy <pragnya.reddy@gramener.com>
