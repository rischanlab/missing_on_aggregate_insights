# -*- coding: utf-8 -*-
import csv
import aggregate_insight as ag
import glob




if __name__ == "__main__":

    k_list = [5, 10, 15, 20, 100, 384]
    mlist = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]


    for i in mlist:
        for k in k_list:
            file_ideal_topk = 'raw_results/diabetes.xlsx'
            topk = ag.get_topk_aggregate(k, file_ideal_topk)
            #print("Ideal topk", topk)
            a_list =[1.01, 1.5, 2, 2.5, 3, 3.5, 4]
            for a in a_list:
                for j in range(20):
                    x = int(i * 100)
                    y = int(a * 100)
                    try:
                        file_name = "raw_results/db_" + str(x) + "zipf" + str(y) + "_missing_measure" + str(j+1) + '.xlsx'
                        for file_view in glob.glob(file_name):
                            print(i*100, a, file_name, k)
                            missing = ag.get_topk_aggregate(k, file_view)
                            #print("Missing topk: ", missing)
                            #print("RBO Standard to Ideal = {}".format(ag.rboresult(missing, topk)))
                            #print("Jaccard Standard to Ideal = {}".format(ag.jaccard_similarity(missing, topk)))
                            with open('results/missing_zipf_measures_vs_ideal.csv', 'a', newline='') as f:
                                fields = [i*100, a, k, ag.rboresult(missing, topk), ag.jaccard_similarity(missing, topk)]
                                writer = csv.writer(f)
                                writer.writerow(fields)
                    except:
                        pass
