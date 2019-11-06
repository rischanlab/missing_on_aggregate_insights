import csv
import aggregate_insight as ag
import glob

if __name__ == "__main__":

    k_list = [5, 10, 12]

    for k in k_list:
        percentage_list = [0,10,20,30,40,50,60,70,80,90]
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_readmitted_100/raw_results/db_' +str(percent) + 'rand_missing_attr' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_readmitted_NO_vs_Yes_attr.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_readmitted(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_readmitted_100/raw_results/db_' +str(percent) + 'rand_missing_measure' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_readmitted_NO_vs_Yes_measure.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_readmitted(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        #
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_readmitted_100/raw_results/db_' +str(percent) + 'rand_missing_a_m' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_readmitted_NO_vs_Yes_a_m.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_readmitted(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        #
        #
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_insulin_100/raw_results/db_' +str(percent) + 'rand_missing_attr' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_insulin_Steady_vs_No_attr.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_insulin(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        #
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_insulin_100/raw_results/db_' +str(percent) + 'rand_missing_measure' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_insulin_Steady_vs_No_measure.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_insulin(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        #
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_insulin_100/raw_results/db_' +str(percent) + 'rand_missing_a_m' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_insulin_Steady_vs_No_a_m.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_insulin(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        #
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_gender_100/raw_results/db_' +str(percent) + 'rand_missing_attr' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_gender_Female_vs_Male_attr.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_gender(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_gender_100/raw_results/db_' +str(percent) + 'rand_missing_measure' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_gender_Female_vs_Male_measure.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_gender(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)
        #
        # for percent in percentage_list:
        #     for i in range(100):
        #         file_name = '1_results_gender_100/raw_results/db_' +str(percent) + 'rand_missing_a_m' + str(i+1) + '.xlsx'
        #         #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
        #         for file_view in glob.glob(file_name):
        #             print(percent, file_name, k)                    #print("Missing topk: ", missing)
        #             #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
        #             #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
        #             with open('results/variance_gender_Female_vs_Male_a_m.csv', 'a', newline='') as f:
        #             #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
        #                 fields = [percent, k, ag.get_topk_gap_gender(k, file_name)]
        #                 writer = csv.writer(f)
        #                 writer.writerow(fields)


        for percent in percentage_list:
            for i in range(100):
                file_name = '1_results_age_100/raw_results/db_' +str(percent) + 'rand_missing_attr' + str(i+1) + '.xlsx'
                #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/variance_age_80_90_vs_No_attr.csv', 'a', newline='') as f:
                    #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.get_topk_gap_age(k, file_name)]
                        writer = csv.writer(f)
                        writer.writerow(fields)
        for percent in percentage_list:
            for i in range(100):
                file_name = '1_results_age_100/raw_results/db_' +str(percent) + 'rand_missing_measure' + str(i+1) + '.xlsx'
                #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/variance_age_80_90_vs_No_measure.csv', 'a', newline='') as f:
                    #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.get_topk_gap_age(k, file_name)]
                        writer = csv.writer(f)
                        writer.writerow(fields)

        for percent in percentage_list:
            for i in range(100):
                file_name = '1_results_age_100/raw_results/db_' +str(percent) + 'rand_missing_a_m' + str(i+1) + '.xlsx'
                #file_name = 'raw_results/db_' + str(percent) + 'nodrop_attr' + str(i + 1) + '.xlsx'
                for file_view in glob.glob(file_name):
                    print(percent, file_name, k)                    #print("Missing topk: ", missing)
                    #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                    #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                    with open('results/variance_age_80_90_vs_No_a_m.csv', 'a', newline='') as f:
                    #with open('results/nodrop_attributes_vs_ideal.csv', 'a', newline='') as f:
                        fields = [percent, k, ag.get_topk_gap_age(k, file_name)]
                        writer = csv.writer(f)
                        writer.writerow(fields)