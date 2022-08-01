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


def get_category(age):
    cat = ''
    if age <= 5: cat = 'Baby'
    elif age <= 12: cat = 'Child'
    elif age <= 18: cat = 'Teenager'
    elif age <= 25: cat = 'Student'
    elif age <= 35: cat = 'Young Adult'
    elif age <= 60: cat = 'Adult'
    else : cat = 'Elderly'
    return cat

titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))

# sns.barplot(x='Age_cat', y='Survived', hue='Sex', data=titanic_df, ci = None)

plt.figure(figsize=(10, 4))
order_columns = ['Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Elderly']
# sns.barplot(x='Age_cat', y='Survived', hue='Sex', data=titanic_df, order=order_columns, ci = None)
sns.barplot(x='Sex', y='Survived', hue='Age_cat', data=titanic_df, ci = None)
# sns.barplot(x='Survived', y='Pclass', data=titanic_df, orient='h')

plt.show()

