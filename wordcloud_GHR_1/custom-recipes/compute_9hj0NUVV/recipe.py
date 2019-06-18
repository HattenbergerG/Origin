# -*- coding: utf-8 -*-
import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import matplotlib 
import wordcloud
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import dataiku.insights

#############################
# Recipe parameter import
#############################

input_dataset_name = get_input_names_for_role('input_dataset')[0]
df = dataiku.Dataset(input_dataset_name).get_dataframe()

output_folder_name = get_output_names_for_role('output_folder')[0]
folder = dataiku.Folder(output_folder_name)
wordcloud_path = folder.get_path()

static_insight_id = get_recipe_config()['static_insight_id']
text_column = get_recipe_config()['text_column']

#############################
# Code of the recipe
#############################

## wordcloud creation
wc = wordcloud.WordCloud(
        background_color='white',
        max_font_size=40, 
        scale=3
).generate(str(df[text_column]))
plt.figure()
plt.axis('off')
plt.imshow(wc)
plt.show()

## save the wordcloud to the output folder
path_fig = wordcloud_path + '/' + "wordcloud_from_plugin"
plt.savefig(path_fig)

## export the wordcloud as a static insight
id = static_insight_id
dataiku.insights.save_figure(id)


