from name import *
from utils import *
import os
import time

def load_spider_data():
    spider_train_path = os.path.join(Spiderpath, Spidertrain)
    spider_others_path = os.path.join(Spiderpath, Spiderothers)
    spider_dev_path = os.path.join(Spiderpath, Spiderdev)
    spider_table_path = os.path.join(Spiderpath, Spidertable)

    spider_train_data = read_json(spider_train_path)
    spider_others_data = read_json(spider_others_path)
    spider_dev_data = read_json(spider_dev_path)
    spider_table_data = read_json(spider_table_path)

    total_data = []
    total_data += spider_train_data
    total_data += spider_dev_data

    questions, dbschema = preprocess_data(total_data, spider_table_data, Spider)
    otherquestions, dbschema = preprocess_data(spider_others_data, spider_table_data, Spiderother)

    return questions, dbschema, otherquestions

def load_hybridQA_data():
    hybridQA_train_path = os.path.join(HybridQApath, HybridQAtrain)
    hybridQA_test_path = os.path.join(HybridQApath, HybridQAtest)
    hybridQA_dev_path = os.path.join(HybridQApath, HybridQAdev)

    hybridQA_train_data = read_json(hybridQA_train_path)
    hybridQA_test_data = read_json(hybridQA_test_path)
    hybridQA_dev_data = read_json(hybridQA_dev_path)
    hybridQA_table_data = get_hybridQA_table_data()

    total_data = []
    total_data += hybridQA_train_data
    total_data += hybridQA_test_data
    total_data += hybridQA_dev_data

    questions, dbschema = preprocess_data(total_data, hybridQA_table_data, HybridQA)

    return questions, dbschema

def load_wikiSQL_data():
    wikiSQL_train_path = os.path.join(WikiSQLpath, WikiSQLtrain)
    wikiSQL_test_path = os.path.join(WikiSQLpath, WikiSQLtest)
    wikiSQL_dev_path = os.path.join(WikiSQLpath, WikiSQLdev)
    wikiSQL_train_table_path = os.path.join(WikiSQLpath, WikiSQLtraintable)
    wikiSQL_test_table_path = os.path.join(WikiSQLpath, WikiSQLtesttable)
    wikiSQL_dev_table_path = os.path.join(WikiSQLpath, WikiSQLdevtable)

    wikiSQL_train_data = read_jsonl(wikiSQL_train_path)
    wikiSQL_test_data = read_jsonl(wikiSQL_test_path)
    wikiSQL_dev_data = read_jsonl(wikiSQL_dev_path)
    wikiSQL_train_table_data = read_jsonl(wikiSQL_train_table_path)
    wikiSQL_test_table_data = read_jsonl(wikiSQL_test_table_path)
    wikiSQL_dev_table_data = read_jsonl(wikiSQL_dev_table_path)

    total_data = []
    total_data += wikiSQL_train_data
    total_data += wikiSQL_test_data
    total_data += wikiSQL_dev_data

    total_table = []
    total_table += wikiSQL_train_table_data
    total_table += wikiSQL_test_table_data
    total_table += wikiSQL_dev_table_data

    questions, dbschema = preprocess_data(total_data, total_table, WikiSQL)

    return questions, dbschema

def load_wikitable_data():
    wikitable_train_path = os.path.join(Wikitablepath, Wikitabletrain)

    wikitable_train_data = get_wikitable_question(wikitable_train_path)
    wikitable_table_data = get_wikitable_table_data()

    questions, dbschema = preprocess_data(wikitable_train_data, wikitable_table_data, Wikitable)

    return questions, dbschema

def load_kvret_data():
    kvret_train_path = os.path.join(Kvretpath, Kvrettrain)
    kvret_dev_path = os.path.join(Kvretpath, Kvretdev)

    kvret_train_data = read_json(kvret_train_path)
    kvret_dev_data = read_json(kvret_dev_path)

    total_data = []
    total_data += kvret_train_data
    total_data += kvret_dev_data

    questions, dbschema = preprocess_data(total_data, [], Kvret)

    return questions, dbschema

def load_tablefact_data():
    tablefact_train1_path = os.path.join(Tablefactquestionpath, Tablefacttrain1)
    tablefact_train2_path = os.path.join(Tablefactquestionpath, Tablefacttrain2)

    tablefact_train1_data = read_json(tablefact_train1_path)
    tablefact_train2_data = read_json(tablefact_train2_path)
    tablefact_table_data = get_tablefact_table_data()

    total_data = {}
    total_data.update(tablefact_train1_data)
    total_data.update(tablefact_train2_data)

    questions, dbschema = preprocess_data(total_data, tablefact_table_data, Tablefact)

    return questions, dbschema

def load_msmarco_data():
    #msmarcousefulnesspath = os.path.join(Msmarcopath, Msmarcousefulness)
    msmarcomsmarcopath = os.path.join(Msmarcopath, Msmarcomsmarco)
    #questions = get_msmarco_usefulness(msmarcousefulnesspath)
    questions = read_json(msmarcomsmarcopath)

    questions, dbschema = preprocess_data(questions, [], Msmarco)

    return questions, dbschema

def load_wikiQA_data():
    wikiqapath = os.path.join(WikiQApath, WikiQAtsv)

    questions = get_wikiQAtsv(wikiqapath)

    questions, dbschema = preprocess_data(questions, [], WikiQA)

    return questions, dbschema

def load_coqa_data():
    coqapath = os.path.join(Coqapath, Coqatrain)

    content = read_json(coqapath)

    questions, dbschema = preprocess_data(content, [], Coqa)

    return questions, dbschema

def load_quac_data():
    quacpath = os.path.join(Quacpath, Quactrain)

    content = read_json(quacpath)

    questions, dbschema = preprocess_data(content, [], Quac)

    return questions, dbschema

def load_dbdomain_data():
    dbdomainsqlitepath = os.path.join(Dbdomainpath, Dbdomainsqlite)
    dbdomainrevisedpath = os.path.join(Dbdomainpath, Dbdomainrevised)

    db2tables = get_domainsqlite(dbdomainsqlitepath, dbdomainrevisedpath)
    db2questionsambiguous, db2questionsnotambiguous = get_domainrevised(dbdomainrevisedpath)

    ambiguousquestions, dbschema = preprocess_data(db2questionsambiguous, db2tables, Dbdomainambiguous)
    notambiguousquestions, dbschema = preprocess_data(db2questionsnotambiguous, db2tables, Dbdomainnotambiguous)

    return ambiguousquestions, notambiguousquestions, dbschema

def load_alex_data():
    alexpath = os.path.join(Alexpath, Alexdataset)

    alexquestions = read_json(alexpath)

    questions, dbschema = preprocess_data(alexquestions, [], Alex)

    return questions, dbschema

def load_googlenq_data():
    """googlenqpath = os.path.join(Googlenqpath, Googlenqdev)

    googlenqquestions = read_jsonl(googlenqpath)"""
    googlenqpath = os.path.join(Googlenqpath, Googlenqdata)

    googlenqquestions = read_json(googlenqpath)

    questions, dbschema = preprocess_data(googlenqquestions, [], Googlenq)

    return questions, dbschema

def load_totto_data():
    tottotrainpath = os.path.join(Tottopath, Tottotrain)
    tottodevpath = os.path.join(Tottopath, Tottodev)

    #tottotrainquestions = read_jsonl(tottotrainpath)
    tottodevquestions = read_jsonl(tottodevpath)

    total_data = []
    #total_data += tottotrainquestions
    total_data += tottodevquestions

    questions, dbschema = preprocess_data(total_data, [], Totto)

    return questions, dbschema

def load_logicnlg_data():
    logicnlgtrainpath = os.path.join(Logicnlgpath, Logicnlgtrain)
    #logicnlgtestpath = os.path.join(Logicnlgpath, Logicnlgtest)
    #logicnlgvalpath = os.path.join(Logicnlgpath, Logicnlgval)

    logicnlgtrainquestions = read_json(logicnlgtrainpath)

    questions, dbschema = preprocess_data(logicnlgtrainquestions, [], Logicnlg)

    return questions, dbschema

def load_sparc_data():
    sparctrainpath = os.path.join(Sparcpath, Sparctrain)
    sparcdevpath = os.path.join(Sparcpath, Sparcdev)
    sparctablespath = os.path.join(Sparcpath, Sparctables)

    sparctraindata = read_json(sparctrainpath)
    sparcdevdata = read_json(sparcdevpath)
    sparctables = read_json(sparctablespath)

    total_data = []
    total_data += sparctraindata
    total_data += sparcdevdata

    questions, dbschema = preprocess_data(total_data, sparctables, Sparc)

    return questions, dbschema

def load_cosql_data():
    cosqldatapath = os.path.join(Cosqlpath, Cosqldialogs)
    cosqltrainpath = os.path.join(Cosqluserintentpath, Cosqltrain)
    cosqldevpath = os.path.join(Cosqluserintentpath, Cosqldev)
    cosqltablepath = os.path.join(Cosqlpath, Cosqltables)

    cosqldata = read_json(cosqldatapath)
    cosqltraindata = read_json(cosqltrainpath)
    cosqldevdata = read_json(cosqldevpath)
    cosqltables = read_json(cosqltablepath)

    total_data = []
    total_data += cosqltraindata
    total_data += cosqldevdata

    questions, dbschema = preprocess_data(total_data, cosqltables, Cosql)
    questionsnotambiguous, dbschema = preprocess_data(cosqldata, cosqltables, Cosqlnotambiguous)

    return questions, dbschema, questionsnotambiguous

def load_alexa_data():
    alexatrainpath = os.path.join(Alexapath, Alexatrain)
    alexavalidfreqpath = os.path.join(Alexapath, Alexavalidfreq)
    alexavalidrarepath = os.path.join(Alexapath, Alexavalidrare)
    alexatestfreqpath = os.path.join(Alexapath, Alexatestfreq)
    alexatestrarepath = os.path.join(Alexapath, Alexatestrare)

    alexatraindata = read_json(alexatrainpath)
    alexavalidfreq = read_json(alexavalidfreqpath)
    alexavalidrare = read_json(alexavalidrarepath)
    alexatestfreq = read_json(alexatestfreqpath)
    alexatestrare = read_json(alexatestrarepath)

    total_data = {}
    total_data.update(alexatraindata)
    total_data.update(alexavalidfreq)
    total_data.update(alexavalidrare)
    total_data.update(alexatestfreq)
    total_data.update(alexatestrare)

    questions, dbschema = preprocess_data(total_data, [], Alexa)

    return questions, dbschema

if __name__ == "__main__":
    start = time.time()

    spiderquestions, spiderdbschema, spiderotherquestions = load_spider_data()
    hybridQAquestions, hybridQAschema = load_hybridQA_data()
    wikiSQLquestions, wikiSQLschema = load_wikiSQL_data()
    wikitablequestions, wikitableschema = load_wikitable_data()
    #kvretquestions, kvretschema, kvretquestions2dataset = load_kvret_data()
    tablefactquestions, tablefactschema = load_tablefact_data()
    msmarcoquestions, msmarcoschema = load_msmarco_data()
    wikiqaquestions, wikiqaschema = load_wikiQA_data()
    coqaquestions, coqaschema = load_coqa_data()
    quacquestions, quacschema = load_quac_data()
    dbdomainambiguousquestions, dbdomainnotambiguousquestions, dbdomainschema = load_dbdomain_data()
    #alexquestions, alexschema = load_alex_data()
    googlenqquestions, googlenqschema = load_googlenq_data()
    tottoquestions, tottoschema = load_totto_data()
    logicnlgquestions, logicnlgschema = load_logicnlg_data()
    sparcquestions, sparcschema = load_sparc_data()
    cosqlquestions, cosqlschema, cosqlnotambiguousquestions = load_cosql_data()
    alexaquestions, alexaschema = load_alexa_data()

    total_schema = {Spider: spiderdbschema,
                    Spiderother: spiderdbschema,
                    HybridQA: hybridQAschema,
                    WikiSQL: wikiSQLschema,
                    Wikitable: wikitableschema,
                    Tablefact: tablefactschema,
                    Dbdomainambiguous: dbdomainschema,
                    Dbdomainnotambiguous: dbdomainschema,
                    Totto: tottoschema,
                    Logicnlg: wikiSQLschema,
                    Sparc: sparcschema,
                    Cosql: cosqlschema,
                    Cosqlnotambiguous: cosqlschema}

    train_schema, dev_schema, test_schema = splitdataschema(total_schema)

    """out = WikiSQL

    newschema = {}
    for key in train_schema[out]:
        newschema[key] = train_schema[out][key]['table']
    mkdir(out)
    write_json(
        newschema, out + "/train.json"
    )
    newschema = {}
    for key in test_schema[out]:
        newschema[key] = test_schema[out][key]['table']
    mkdir(out)
    write_json(
        newschema, out + "/test.json"
    )

    newschema = {}
    for key in dev_schema[out]:
        newschema[key] = dev_schema[out][key]['table']
    mkdir(out)
    write_json(
        newschema, out + "/dev.json"
    )"""

    total_questions = {Spider: spiderquestions,
                       Spiderother: spiderotherquestions,
                       WikiSQL: wikiSQLquestions,
                       Tablefact: tablefactquestions,
                       Msmarco: msmarcoquestions,
                       WikiQA: wikiqaquestions,
                       Coqa: coqaquestions,
                       Quac: quacquestions,
                       Dbdomainambiguous: dbdomainambiguousquestions,
                       Dbdomainnotambiguous: dbdomainnotambiguousquestions,
                       #Alex: alexquestions,
                       Googlenq: googlenqquestions,
                       Totto: tottoquestions,
                       Wikitable: wikitablequestions,
                       HybridQA: hybridQAquestions,
                       Logicnlg: logicnlgquestions,
                       Sparc: sparcquestions,
                       Cosql: cosqlquestions,
                       Alexa: alexaquestions,
                       Cosqlnotambiguous: cosqlnotambiguousquestions
                       }


    question_count = defaultdict(int)
    for datasetid in total_questions:
        dataset = total_questions[datasetid]
        for dbid in dataset:
            db = dataset[dbid]
            question_count[datasetid] += len(db)


    print("question_num:")
    for datasetid in question_count:
        print(datasetid + ": " + str(question_count[datasetid]))
    print("------------------")

    #total_questions = filterquestion(totalq)

    trainq, devq, testq = splittype1question(total_questions)

    train_dataset = defaultdict(lambda : defaultdict(int))
    dev_dataset = defaultdict(lambda : defaultdict(int))
    test_dataset = defaultdict(lambda : defaultdict(int))

    train_question = defaultdict(lambda: defaultdict(int))
    dev_question = defaultdict(lambda: defaultdict(int))
    test_question = defaultdict(lambda: defaultdict(int))

    print("trainset:")
    train_type1 = gen_type1(trainq, train_schema, train_dataset, train_question)
    print("type1 dataset: " + str(dict(train_dataset[Type1])))
    print("type1 question: " + str(dict(train_question[Type1])))
    train_type2 = gen_type2(total_questions, train_schema, train_dataset, train_question)
    print("type2 dataset: " + str(dict(train_dataset[Type2])))
    print("type2 question: " + str(dict(train_question[Type2])))
    train_type3 = gen_type3(total_questions, train_schema, train_dataset, train_question)
    print("type3 dataset: " + str(dict(train_dataset[Type3])))
    print("type3 question: " + str(dict(train_question[Type3])))
    train_type4 = gen_type4(total_questions, train_schema, train_dataset, train_question)
    print("type4 dataset: " + str(dict(train_dataset[Type4])))
    print("type4 question: " + str(dict(train_question[Type4])))
    train_type5 = gen_type5(total_questions, train_schema, train_dataset, train_question)
    print("type5 dataset: " + str(dict(train_dataset[Type5])))
    print("type5 question: " + str(dict(train_question[Type5])))
    mkdir(Train)
    write_json(train_type1, os.path.join(Train, Type1json))
    write_json(train_type2, os.path.join(Train, Type2json))
    write_json(train_type3, os.path.join(Train, Type3json))
    write_json(train_type4, os.path.join(Train, Type4json))
    write_json(train_type5, os.path.join(Train, Type5json))
    print("------------------")

    print("devset:")
    dev_type1 = gen_type1(devq, dev_schema, dev_dataset, dev_question)
    print("type1 dataset: " + str(dict(dev_dataset[Type1])))
    print("type1 question: " + str(dict(dev_question[Type1])))
    dev_type2 = gen_type2(total_questions, dev_schema, dev_dataset, dev_question)
    print("type2 dataset: " + str(dict(dev_dataset[Type2])))
    print("type2 question: " + str(dict(dev_question[Type2])))
    dev_type3 = gen_type3(total_questions, dev_schema, dev_dataset, dev_question)
    print("type3 dataset: " + str(dict(dev_dataset[Type3])))
    print("type3 question: " + str(dict(dev_question[Type3])))
    dev_type4 = gen_type4(total_questions, dev_schema, dev_dataset, dev_question)
    print("type4 dataset: " + str(dict(dev_dataset[Type4])))
    print("type4 question: " + str(dict(dev_question[Type4])))
    dev_type5 = gen_type5(total_questions, dev_schema, dev_dataset, dev_question)
    print("type5 dataset: " + str(dict(dev_dataset[Type5])))
    print("type5 question: " + str(dict(dev_question[Type5])))
    mkdir(Dev)
    write_json(dev_type1, os.path.join(Dev, Type1json))
    write_json(dev_type2, os.path.join(Dev, Type2json))
    write_json(dev_type3, os.path.join(Dev, Type3json))
    write_json(dev_type4, os.path.join(Dev, Type4json))
    write_json(dev_type5, os.path.join(Dev, Type5json))
    print("------------------")

    print("testset:")
    test_type1 = gen_type1(testq, test_schema, test_dataset, test_question)
    print("type1 dataset: " + str(dict(test_dataset[Type1])))
    print("type1 question: " + str(dict(test_question[Type1])))
    test_type2 = gen_type2(total_questions, test_schema, test_dataset, test_question)
    print("type2 dataset: " + str(dict(test_dataset[Type2])))
    print("type2 question: " + str(dict(test_question[Type2])))
    test_type3 = gen_type3(total_questions, test_schema, test_dataset, test_question)
    print("type3 dataset: " + str(dict(test_dataset[Type3])))
    print("type3 question: " + str(dict(test_question[Type3])))
    test_type4 = gen_type4(total_questions, test_schema, test_dataset, test_question)
    print("type4 dataset: " + str(dict(test_dataset[Type4])))
    print("type4 question: " + str(dict(test_question[Type4])))
    test_type5 = gen_type5(total_questions, test_schema, test_dataset, test_question)
    print("type5 dataset: " + str(dict(test_dataset[Type5])))
    print("type5 question: " + str(dict(test_question[Type5])))
    mkdir(Test)
    write_json(test_type1, os.path.join(Test, Type1json))
    write_json(test_type2, os.path.join(Test, Type2json))
    write_json(test_type3, os.path.join(Test, Type3json))
    write_json(test_type4, os.path.join(Test, Type4json))
    write_json(test_type5, os.path.join(Test, Type5json))
    print("------------------")

    #get_stat(train_question, test_question, dev_question)

    end = time.time()
    print(end - start)

