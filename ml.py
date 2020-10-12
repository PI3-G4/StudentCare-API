import pandas as pd
from pandas.api.types import CategoricalDtype
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

class MachineLearning:

    def __init__(self):
        self.data = self.import_cleaning_data()
        self.model = self.model(self.data)

    def import_cleaning_data(self):
        df_mat = pd.read_csv('./data/student-mat2.csv', sep=';')
        df_por = pd.read_csv('./data/student-por2.csv', sep=';')

        df_por_old = pd.read_csv('./data/student-por.csv', sep=';')
        df_por_old = df_por_old.loc[(df_por_old.G1 >= 0) & (df_por_old.G1 <= 6.7)]

        df_mat_old = pd.read_csv('./data/student-mat.csv', sep=';')
        df_mat_old = df_mat_old.loc[(df_mat_old.G1 >= 0) & (df_mat_old.G1 <= 6.7)]

        df = pd.concat([df_mat, df_por,df_por_old, df_mat_old], axis=0)

        df = df.drop(['school', 'paid', 'fatherd'], axis=1)

        sex_category = ['F', 'M']
        address_category = ['U', 'R']
        famsize_category = ['LE3', 'GT3']
        Pstatus_category = ['T', 'A']
        Mjob_category = ['teacher', 'health', 'services', 'at_home', 'other']
        Fjob_category = ['teacher', 'health', 'services', 'at_home', 'other']
        reason_category = ['home', 'reputation', 'course', 'other']
        guardian_category = ['mother', 'father', 'other']
        schoolsup_category = ['yes', 'no']
        famsup_category = ['yes', 'no']
        activities_category = ['yes', 'no']
        nursery_category = ['yes', 'no']
        higher_category = ['yes', 'no']
        internet_category = ['yes', 'no']
        romantic_category = ['yes', 'no']

        def setCategoryColumns(column, categors):
            return column.astype(CategoricalDtype(categories=categors, ordered=True)).cat.codes

        df.sex = setCategoryColumns(df.sex, sex_category)
        df.address = setCategoryColumns(df.address, address_category)
        df.famsize = setCategoryColumns(df.famsize, famsize_category)
        df.Pstatus = setCategoryColumns(df.Pstatus, Pstatus_category)
        df.Mjob = setCategoryColumns(df.Mjob, Mjob_category)
        df.Fjob = setCategoryColumns(df.Fjob, Fjob_category)
        df.reason = setCategoryColumns(df.reason, reason_category)
        df.guardian = setCategoryColumns(df.guardian, guardian_category)
        df.schoolsup = setCategoryColumns(df.schoolsup, schoolsup_category)
        df.famsup = setCategoryColumns(df.famsup, famsup_category)
        df.activities = setCategoryColumns(df.activities, activities_category)
        df.nursery = setCategoryColumns(df.nursery, nursery_category)
        df.higher = setCategoryColumns(df.higher, higher_category)
        df.internet = setCategoryColumns(df.internet, internet_category)
        df.romantic = setCategoryColumns(df.romantic, romantic_category)

        labels = ['G1', 'G2', 'G3']
        for i in labels:
            df.loc[(df[i] >= 0) & (df[i] <= 6.7), i] = 1
            df.loc[(df[i] >= 6.8) & (df[i] <= 13.4), i] = 2
            df.loc[(df[i] >= 13.5) & (df[i] <= 20), i] = 3

        return df

    def model(self, df):

        X = df.iloc[:, 0:28]
        y = df['G1']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

        clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
        clf.fit(X_train, y_train)

        return clf

    def acuracia(self):
        X = self.data.iloc[:, 0:28]
        y = self.data['G1']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

        clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_train)
        accuracy = accuracy_score(y_train, y_pred)

        return accuracy