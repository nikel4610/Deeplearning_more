import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('./titanic_train.csv')

# sns.distplot(titanic_df['Age'], bins = 10)
# # kde = False: 그래프 선 그리지 않음
# # bins: 그래프 구분하는 칸의 개수
# # sns.distplot(titanic_df['Age'], bins = 10, kde = False)

# hisplot: 크기 조정 가능(axis level)
# plt.figure(figsize = (12, 6))
# sns.histplot(x = 'Age', data = titanic_df, kde = True, bins = 30)

# displot: 사이즈 고정됨(figure level)
# sns.displot(titanic_df['Age'], kde = True, rug = True, height = 4, aspect = 2)

# plt.figure(figsize = (10, 6))
# sns.distplot(titanic_df['Age'], kde = True, rug = True)

# sns.countplot(x = 'Pclass', data = titanic_df)

# # xlabel, ylabel 자동으로 설정
# sns.barplot(x = 'Pclass', y = 'Age', data = titanic_df)
# sns.barplot(x = 'Pclass', y = 'Sex', data = titanic_df)

# # ci = None: 그래프에 그어진 선 제거 '-'
# sns.barplot(x = 'Pclass', y = 'Survived', data = titanic_df, ci = None, estimator = sum)

# # hue: 데이터를 덧붙여서 그래프 그림
# sns.barplot(x = 'Pclass', y = 'Age', hue = 'Sex', data = titanic_df, ci = None)
# sns.barplot(x='Pclass', y='Survived', hue='Sex', data=titanic_df, ci = None)


# def get_category(age):
#     cat = ''
#     if age <= 5: cat = 'Baby'
#     elif age <= 12: cat = 'Child'
#     elif age <= 18: cat = 'Teenager'
#     elif age <= 25: cat = 'Student'
#     elif age <= 35: cat = 'Young Adult'
#     elif age <= 60: cat = 'Adult'
#     else : cat = 'Elderly'
#     return cat

# titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))

# # sns.barplot(x='Age_cat', y='Survived', hue='Sex', data=titanic_df, ci = None)

# plt.figure(figsize=(10, 4))
# order_columns = ['Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Elderly']
# # sns.barplot(x='Age_cat', y='Survived', hue='Sex', data=titanic_df, order=order_columns, ci = None)
# sns.barplot(x='Sex', y='Survived', hue='Age_cat', data=titanic_df, ci = None)
# # sns.barplot(x='Survived', y='Pclass', data=titanic_df, orient='h')

# # Age 컬럼에 대한 연속 확률 분포 시각화
# sns.violinplot(y = 'Age', data = titanic_df)
# sns.violinplot(x='Pclass', y='Age', data=titanic_df)
# sns.violinplot(x='Sex', y='Age', data=titanic_df)

# cat_columns = ['Survived', 'Pclass', 'Sex', 'Age_cat']
# # nrows는 1이고 ncols는 컬럼의 갯수만큼인 subplots을 설정.
# for index, column in enumerate(cat_columns):
#     print(index, column)

# fig, axs = plt.subplots(nrows=1, ncols=len(cat_columns), figsize=(16, 4))

# for index, column in enumerate(cat_columns):
#     # print('index:', index)
#     # seaborn의 Axes 레벨 function들은 ax인자로 subplots의 어느 Axes에 위치할지 설정.
#     sns.countplot(x=column, data=titanic_df, ax=axs[index])
#     if index == 3:
#         # plt.xticks(rotation=90)으로 간단하게 할수 있지만 Axes 객체를 직접 이용할 경우 API가 상대적으로 복잡.
#         axs[index].set_xticklabels(axs[index].get_xticklabels(), rotation=45)

# def show_hist_by_target(df, columns):
#     cond_1 = (df['Survived'] == 1)
#     cond_0 = (df['Survived'] == 0)
        
#     for column in columns:
#         fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
#         sns.violinplot(x='Survived', y=column, data=df, ax=axs[0] )
#         sns.histplot(df[cond_0][column], ax=axs[1], kde=True, label='Survived 0', color='blue')
#         sns.histplot(df[cond_1][column], ax=axs[1], kde=True, label='Survived 1', color='red')
#         axs[1].legend()

# cont_columns = ['Age', 'Fare', 'SibSp', 'Parch']
# show_hist_by_target(titanic_df, cont_columns)

# sns.boxplot(x='Pclass', y='Age', data=titanic_df)
# sns.scatterplot(x='Age', y='Fare', data=titanic_df, hue='Pclass',style='Survived')

# titanic_df.corr()
# plt.figure(figsize=(8, 8))

# corr = titanic_df.corr()
# sns.heatmap(corr)
# sns.heatmap(corr, annot=True, fmt='.1f', linewidths=0.5, cmap='YlGnBu')
# sns.heatmap(corr, annot=True, fmt='.2g', cbar=True, linewidths=0.5, cmap='YlGnBu')

sns.set_theme(style='whitegrid')
penguins = sns.load_dataset("penguins")

# sns.histplot(data=penguins, x="flipper_length_mm", hue="species", multiple='stack')
# sns.displot(data=penguins, x="flipper_length_mm", hue="species", col="species")

# sns.barplot(data=penguins, x="flipper_length_mm", y="species", hue='species')
# sns.barplot(data=penguins, y="flipper_length_mm", x="species", hue='species')
# sns.barplot(data=penguins, y="body_mass_g", x="species", hue='species')

# sns.countplot(data=penguins, x='species', hue='sex')

# sns.boxplot(data=penguins, x="flipper_length_mm", y="species", hue="species")
# sns.boxplot(data=penguins, x="body_mass_g", y="species", hue="species")
# sns.boxplot(data=penguins, x="body_mass_g", y="species", hue="sex")
# sns.boxplot(data=penguins, y="body_mass_g", x="species", hue="sex")

# sns.pairplot(data=penguins, hue="island")
# sns.pairplot(data=penguins, hue="species")
# sns.pairplot(data=penguins, hue="sex")

# sns.violinplot(data=penguins, y="flipper_length_mm", x="species", hue="species")
# sns.violinplot(data=penguins, y="body_mass_g", x="species", hue="sex")

# sns.lineplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="species")
# sns.lineplot(data=penguins, y="body_mass_g", x="flipper_length_mm", hue="sex")
# sns.lineplot(data=penguins, y="bill_length_mm", x="bill_depth_mm", hue="species")

# sns.pointplot(data=penguins, y="flipper_length_mm", x="sex", hue="species")
# sns.pointplot(data=penguins, y="bill_length_mm", x="sex", hue="species")

# sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="species")
# sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="sex")

corr = penguins.corr()
sns.heatmap(corr)

plt.show()

