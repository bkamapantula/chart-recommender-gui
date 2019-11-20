import gramex
import pandas as pd

type_recognizer = {
    'numerical': {
        'categorical': 'num_and_cat',
        'time_series': 'several_series'
    },
    'categorical': {
        'numerical': 'num_and_cat',
    },
    'num_and_cat': {
        'time_series': 'time_series',
    },
    'time_series': {
        'time_series': 'several_series'
    }
}

chart_possible: {
    'num_and_cat': {
        'one_num_one_cat': {
            'one_obs_per_group': ['lollipop', 'bar_plot', 'circular_bar_plot', 'treemap', 'circlepack'],
            'several_obs_per_group': ['box_plot', 'violin_plot', 'circular_bar_plot', 'treemap', 'circlepack']
        },
        'one_cat_several_num': {
            'one_value_per_group': ['multi_line', 'parallel_plot', 'stacked_bar_plot', 'grouped_bar_plot'],
            'multiple_values_per_group': ['grouped_scatterplot']
        },
        'several_cat_one_num': {
            'subgroup': {

            },
            'nested': {

            },
            'adjacency': {

            }
        },
    },
    'numerical': {
        'one_num': ['histogram', 'density_plot'],
        'two_num': {
            'not_ordered': {
                'few_points': ['facet_box_plot', 'scatterplot'],
                'many_points': ['facet_violin_plot', 'facet_densityplot', ]
            },
            'ordered': ['line_chart', 'area_chart', 'connected_scatterplot']
        },
        'three_num': {
            'not_ordered': [],
            'ordered': []
        },
        'several_num': {
            'not_ordered': [],
            'ordered': []
        }
    },
    'categorical': {
      'one_cat': ['barplot', 'lollipop', 'donut', 'treemap', 'circlepack'],
      'several_cat': {

      }
    }
}


def is_one_obs_per_group(df, one_cat):
    return df[one_cat].unique().count() == df[one_cat].count()


group_type_recognizer = {
    'one_obs_per_group': is_one_obs_per_group

}


def initiate(handler):
    df = gramex.cache.open('flags.xlsx')
    print(df.head())


def type_combination(fields_names, type_map):
    """returns combination for column types

    Arguments:
        fields_names {list} -- Field names selected by the user
        type_map {dict} -- dictionary of field names and its corresponding dtypes
    """
    type_recognized = fields_names[0]
    for field in fields_names[1:]:
        type_recognized = type_recognizer[type_recognized][type_map[field]]

    return type_recognized


def group_type(categorical_cols):
    """if multiple categorical cols chosen, this function is called. 

    Arguments:
        categorical_cols {[type]} -- [description]
    """
    return "t1"


def group_item_type(categorical_col):
    """[summary]

    Arguments:
        categorical_col {[type]} -- [description]

    Returns:
        [type] -- [description]
    """

    return "h11"
