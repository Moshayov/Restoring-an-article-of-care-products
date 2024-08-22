import os
import NaiveBase
import KNN
import DecisionTree
import SVM
import DeepLerning
import pandas as pd
import matplotlib.pyplot as plt


def run_algorithm(algo, file_path, product_name, results_df):
    accuracy, f1, error_margin = algo.play(file_path)
    results_df = pd.concat([results_df, pd.DataFrame({
        "Product": [product_name],
        "Algorithm": [algo.__name__],
        "Accuracy": [accuracy],
        "F1 Score": [f1],
        "Error Margin": [error_margin]
    })], ignore_index=True)
    return results_df


def plot_results(results_df):
    products = results_df['Product'].unique()

    for product in products:
        product_df = results_df[results_df['Product'] == product]

        algorithms = product_df['Algorithm']
        accuracy = product_df['Accuracy']
        f1_score = product_df['F1 Score']
        error_margin = product_df['Error Margin']

        fig, ax = plt.subplots()

        index = range(len(algorithms))
        bar_width = 0.25

        ax.bar(index, accuracy, bar_width, label='Accuracy')
        ax.bar([i + bar_width for i in index], error_margin, bar_width, label='Error Margin')
        ax.plot([i + bar_width / 2 for i in index], f1_score, label='F1 Score', color='red', marker='o')

        ax.set_xlabel('Algorithms')
        ax.set_ylabel('Scores')
        ax.set_title(f'Classification Performance for {product}')
        ax.set_xticks([i + bar_width / 2 for i in index])
        ax.set_xticklabels(algorithms)
        ax.legend()

        # יצירת הטבלה עם שמות האלגוריתמים בצד
        table_data = product_df[['Accuracy', 'Error Margin', 'F1 Score']].values
        table = ax.table(cellText=table_data, colLabels=['Accuracy', 'Error Margin', 'F1 Score'],
                         rowLabels=algorithms, cellLoc='center', loc='bottom', bbox=[0, -0.6, 1, 0.5])

        table.auto_set_font_size(False)
        table.set_fontsize(10)  # גודל פונט מתאים
        table.scale(1.2, 1.2)  # גודל הטבלה מתאים

        plt.subplots_adjust(left=0.2, bottom=0.4)  # התאמת השוליים של הגרף
        plt.show()


def main():
    file_paths = [
        r'input_pn/cleaned_belif_polarity.xlsx',
        r'input_pn/cleaned_DRUNK_polarity.xlsx',
        r'input_pn/cleaned_laniege_polarity.xlsx',
        r'input_pn/cleaned_origin_polarity.xlsx'
    ]
    # משום מה כאשר מריצים בבת אחת הוא זורק חריגה אבל כשרהרצנו טבלה טבל בנפרד זה עבד מצוין
    algorithms = [NaiveBase, KNN, SVM, DecisionTree, DeepLerning]
    results_df = pd.DataFrame()

    for file_path in file_paths:
        product_name = file_path.split('/')[-1].split('_')[1].upper()
        for algo in algorithms:
            results_df = run_algorithm(algo, file_path, product_name, results_df)

    plot_results(results_df)


if __name__ == "__main__":
    main()
