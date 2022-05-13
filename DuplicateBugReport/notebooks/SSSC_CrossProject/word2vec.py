import gensim
import logging
import pandas as pd

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def extract_questions():
    """
    Extract questions for making word2vec model.
    """
    
    Eclip_Non_Dup = './dataBR/Eclipse/EP_nondup.csv'
    Eclip_Dup = './dataBR/Eclipse/EP_dup.csv'


    #Mozilla BugReports

    Mozilla_Non_Dup = './dataBR/Mozilla/M_NonDuplicate.csv'
    Mozilla_Dup = './dataBR/Mozilla/M_Duplicate.csv'

    #ThunderBird Bug Reports

    ThunderBird_Non_Dup = './dataBR/ThunderBird/Nondup_TB.csv'
    ThunderBird_Dup = './dataBR/ThunderBird/dup_TB.csv'
    
    #Eclipse dataframes

    Eclipse_dups = pd.read_csv(Eclip_Dup,sep=";", engine='python')
    Eclipse_nondups = pd.read_csv(Eclip_Non_Dup,sep=";", engine='python')
    Eclipse_combined = pd.concat([Eclipse_dups, Eclipse_nondups], ignore_index=True, sort=False)
    Eclipse_combined['Report1'] = Eclipse_combined['Title1'] +" "+ Eclipse_combined['Description1']
    Eclipse_combined['Report2'] = Eclipse_combined['Title2'] +" "+ Eclipse_combined['Description2']


    #Mozilla dataframes

    Mozilla_dups = pd.read_csv(Mozilla_Dup,sep=";", engine='python')
    Mozilla_nondups = pd.read_csv(Mozilla_Non_Dup,sep=";", engine='python')
    Mozilla_combined = pd.concat([Mozilla_dups, Mozilla_nondups], ignore_index=True, sort=False)
    Mozilla_combined['Report1'] = Mozilla_combined['Title1'] +" "+ Mozilla_combined['Description1']
    Mozilla_combined['Report2'] = Mozilla_combined['Title2'] +" "+ Mozilla_combined['Description2']


    #ThunderBird dataframes

    ThunderBird_dups = pd.read_csv(ThunderBird_Dup,sep=";", engine='python')
    ThunderBird_nondups = pd.read_csv(ThunderBird_Non_Dup,sep=";", engine='python')
    ThunderBird_combined = pd.concat([ThunderBird_dups, ThunderBird_nondups], ignore_index=True, sort=False)
    ThunderBird_combined['Report1'] = ThunderBird_combined['Title1'] +" "+ ThunderBird_combined['Description1']
    ThunderBird_combined['Report2'] = ThunderBird_combined['Title2'] +" "+ ThunderBird_combined['Description2']




    for dataset in [Eclipse_combined, Mozilla_combined,ThunderBird_combined]:
        for i, row in dataset.iterrows():
            if i != 0 and i % 1000 == 0:
                logging.info("read {0} sentences".format(i))

            if row['Report1']:
                yield gensim.utils.simple_preprocess(row['Report1'])
            if row['Report2']:
                yield gensim.utils.simple_preprocess(row['Report2'])


documents = list(extract_questions())
logging.info("Done reading data file")

model = gensim.models.Word2Vec(documents, vector_size=300)
model.train(documents, total_examples=len(documents), epochs=10)
model.save("./data/Bug_duplicates.w2v")
