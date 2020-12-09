# # Figure details
# plt.figure(1, figsize=(20,10))
# the_grid = GridSpec(2, 2)
#
# # Color specifications
# cmap = plt.get_cmap('Spectral')
# colors = [cmap(i) for i in np.linspace(0, 1, 8)]
#
# # fontsize = 16, fontweight = 'bold'
# plt.subplot(the_grid[0, 1], aspect=1, title='BESS Cost Composition')
# plt.pie(vis_cost_list, labels=labels_cost_list, autopct='%1.1f%%', shadow=True, colors=colors)
#
# plt.subplot(the_grid[1, 0], aspect=1, title='BESS Cost Composition')
# plt.hist(x = labels_cost_list, y = vis_cost_list , bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)

# pie chart
# plt.title('BESS Cost Composition before operation', fontsize = 16, fontweight = 'bold')
# plt.pie(vis_cost_list, labels = labels_cost_list, autopct='%1.1f%%', shadow=True, colors=colors)

# plt.title('Comparing component costs', fontsize=16, fontweight='bold')
# plt.bar(df_components_labels, df_components_cost, bottom=None, align='center',data=None)
# plt.xticks(rotation=45)
# plt.show()
#
# fig1 = px.bar(df_results, x="Component", y="Cost",
#               labels = {
#                   "Component": " Component name",
#                   "Cost": " Estimated cost (EUR)"
#               },
#               title="Comparing component costs")
# fig1.show()
#
# fig2 = px.pie(df_results, values='Cost', names='Component', title='Populdf')
# fig2.show()
