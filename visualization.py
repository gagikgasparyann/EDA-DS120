import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from analyzer import nyc

class Visualization:

    """
    A class to perform visual representations of our analysis results
    """

    def __init__(self, analyzer):
        """
        Initializing the Visualization class with reference to Analyzer class
        Args used: analyzer(Analizer) that is an instance of Analyzer class which contains data we want to vizualize
        """
        self.analyzer = analyzer

#1.monthly crashes linear plot
    def plot_monthly_crashes(self):
        """
        Generate a bar chart showing the number of crashes per month
        """
        monthly_counts = self.analyzer.crashes_every_month()

        months_order = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November"]

        #make sure the order is correct
        monthly_counts = monthly_counts.reindex(months_order).dropna()
        order = np.arange(11)

        plt.figure(figsize=(7, 6))
        # plt.plot(monthly_counts.index, monthly_counts.values, marker='o', color='blue', linewidth=2)
        plt.stem(monthly_counts.values, markerfmt='#BF0000')
        plt.xticks(order, months_order, rotation=45, fontname="serif", fontsize=10)
        plt.yticks(fontname="serif")
        plt.title("Total Crashes by Month", fontsize=18, fontname="serif", fontweight="bold", color="#BF0000", pad=20)
        plt.xlabel("Month", fontsize=12, fontname="serif", labelpad=20, style="italic")
        plt.ylabel("Number of Incidents", fontsize=12, fontname="serif", labelpad=20, style="italic")
        plt.grid(axis="y", linestyle="--", alpha=0.75)
        plt.tight_layout()
        plt.show()


#2. Bar chart for easy comparison of groups
#looked at the PERSON_TYPE column and count occurrences of Driver, Passenger, Pedestrian and so on
    def plot_person_type_dist(self):
        """
        Creates a pie chart to vizualize the proportion of differfent persons types involved in collisions
        """
        #get the data
        person_type_counts = self.analyzer.crashes_by_person_type()

        #plot-code
        pie_colors = ["#ff6853", "#ffb514", "#51d11a", "#55a9ff"]
        plt.figure(figsize=(8, 8))
        patches, texts, autotexts = plt.pie(person_type_counts.values, colors=pie_colors, labels=person_type_counts.index, autopct='%1.1f%%', startangle=140, textprops={'fontname': 'serif', 'fontsize': 11, 'color': 'blue'}, shadow=True, explode=(0.1, 0.1, 0.1, 0.1))
        plt.title("Distribution of Crashes by Person Type", fontsize=18, fontname="serif", fontweight="bold", color="#FD5800", pad=32)
        for t in texts:
          t.set_color('#ffb514')
          t.set_size(12)
          t.set_weight('bold')
          t.set_style('italic')
        for at in autotexts:
          at.set_color('white')
          at.set_size(11)
          at.set_weight('bold')
        plt.show()
#3mean, median, and mode in genders
    def plot_age_sex_stats(self):
        """
        Creates a bar chart to vizualize the difference of statistics of crashes' mean, median, mode for male and female
        """

        age_stats = self.analyzer.crashes_by_age_sex().T
        age_stats.plot(kind="bar", figsize=(10, 6), color=["#FF007E", "#2431A1"])

        plt.title("Age Statistics by Gender", fontsize=18, fontname="serif", fontweight="bold", pad=25)
        plt.xlabel("Gender (F is Female, M is Male)", fontsize=12, fontname="serif", labelpad=20, style="italic")
        plt.ylabel("Age", fontsize=12, fontname="serif", labelpad=20, style="italic")

        plt.xticks(rotation=0, fontname="serif", fontsize=12)
        plt.yticks(fontname="serif", fontsize=12)

        plt.show()

#4.Correlation between persons role and injury
    def plot_role_injury_corr(self):
        """
        Makes a heatmap representing the correlation between persons role and injury
        """

        #get the data from the analyzer
        role_data = self.analyzer.cor_role_injury()

        #clean the labels
        role_data.index = role_data.index.str.replace("PED_ROLE_", "")
        role_data.columns = role_data.columns.str.replace("PERSON_INJURY_", "")

        df_melted = role_data.reset_index().melt(id_vars=role_data.index.name or 'index')
        df_melted.columns = ['Role', 'Injury', 'Correlation']

        #plot the scatterplot
        plt.figure(figsize=(3, 5))     #SEABORN
        sns.scatterplot(
            data=df_melted,
            x="Injury",
            y="Role",
            size="Correlation",
            hue="Correlation",
            sizes=(20, 500),
            palette="coolwarm"
        )

        plt.title("Correlation - Person Role VS Injury Type", fontsize=15, fontname="serif", fontweight="bold", pad=25)
        plt.xlabel("Injury", fontsize=12, fontname="serif", labelpad=20, style="italic")
        plt.ylabel("Role", fontsize=12, fontname="serif", labelpad=20, style="italic")
        plt.xticks(rotation=0, fontname="serif", fontsize=10)
        plt.yticks(fontname="serif", fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')


#5.Correlation between emotional status and injury
    def plot_emotional_injury_corr(self):
        """
        Generates a heatmap to vizualize the correlation between persons role and injury
        """
        emo_corr = self.analyzer.cor_emotional_status_injury()

        emo_corr.index = emo_corr.index.str.replace("EMOTIONAL_STATUS_", "")
        emo_corr.columns = emo_corr.columns.str.replace("PERSON_INJURY_", "")

        plt.figure(figsize=(5, 6))
        sns.heatmap(emo_corr, annot=True, cmap="Greens", linewidths=0.7, annot_kws={"font": "serif", "size": 10, "style": "italic"})  #SEABORN
        plt.title("Impact of Emotional Status on Injury Type", fontsize=15, color="#14452F" ,fontname="serif", fontweight="bold", pad=25)
        plt.xticks(rotation=0, fontname="serif", fontsize=10)
        plt.yticks(fontname="serif", fontsize=10)
        plt.show()


#6. corredlation between injury and factor
    def plot_top_factors_corr(self):
        """
        Makes a grid chart showing the correlation between contributing factors and injury
        """
        factor_data = self.analyzer.cor_factor_injury()
        factor_data.index = factor_data.index.str.replace("CONTRIBUTING_FACTOR_1_", "")

        #get top-10 factors
        top_10_factors = factor_data.iloc[:, 0].sort_values(ascending=True).tail(10)

        #horizontal bar chart
        plt.figure(figsize=(10, 5))
        top_10_factors.plot(kind="barh", color="red", edgecolor="black")

        plt.title("Top 10 Most Dangerous Contributing Factors", fontsize=15, fontname="serif", fontweight="bold", pad=25)
        plt.xlabel("Correlation Strength", fontname="serif", labelpad=20, style="italic", fontsize=12)
        plt.ylabel("Factor", fontname="serif", labelpad=20, style="italic", fontsize=12)
        plt.xticks(fontname="serif", fontsize=10)
        plt.yticks(fontname="serif", fontsize=10)
        plt.show()



viz = Visualization(nyc)

viz.plot_monthly_crashes()


viz.plot_person_type_dist()

viz.plot_age_sex_stats()

viz.plot_role_injury_corr()

viz.plot_emotional_injury_corr()

viz.plot_top_factors_corr()