Spider = "spider"
Spiderother = "spiderother"
Spiderpath = '../dataset/spider'
Spidertrain = "train_spider.json"
Spiderothers = "train_others.json"
Spiderdev = "dev.json"
Spidertable = "tables.json"
Spidertablename = "table_names"
Spidercolumnname = "column_names"
Spiderdbid = "db_id"
Spiderquerytok = "query_toks"


HybridQA = "hybridqa"
HybridQApath = '../dataset/HybridQA/released_data'
HybridQAtrain = 'train.json'
HybridQAtest = 'test.json'
HybridQAdev = 'dev.json'
HybridQAdbid = 'table_id'
HybridQAtablepath = '../dataset/HybridQA/tables'
HybridQAheader = "header"
HybridQAtableid = 'idx'

WikiSQL = "wikisql"
WikiSQLpath = '../dataset/WikiSQL/data'
WikiSQLtrain = 'train.jsonl'
WikiSQLtest = 'test.jsonl'
WikiSQLdev = 'dev.jsonl'
WikiSQLtraintable = 'train.tables.jsonl'
WikiSQLtesttable = 'test.tables.jsonl'
WikiSQLdevtable = 'dev.tables.jsonl'
WikiSQLdbid = 'table_id'
WikiSQLtable = 'id'
WikiSQLheader = 'header'
WikiSQLsql = "sql"
WikiSQLsel = "sel"
WikiSQLconds = "conds"

Wikitable = "wikitable"
Wikitablepath = '../dataset/WikiTableQuestions/data'
Wikitabletrain = 'training.tsv'
Wikitabledir = '../dataset/WikiTableQuestions/'
Wikitabledbid = 'dbid'

Kvret = "kvret"
Kvretpath = '../dataset/dialog_datasets/kvret'
Kvrettrain = 'kvret_train_public.json'
Kvretdev = 'kvret_dev_public.json'
Kvretscenario = "scenario"
Kvretuuid = 'uuid'
Kvretdialogue = 'dialogue'
Kvretdata = 'data'
Kvretutterance = 'utterance'

Tablefact = "tablefact"
Tablefactquestionpath = '../dataset/Table-Fact-Checking/collected_data'
Tablefacttrain1 = 'r1_training_all.json'
Tablefacttrain2 = 'r2_training_all.json'
Tablefacttablepath = '../dataset/Table-Fact-Checking/data/all_csv'

Msmarco = "msmarco"
Msmarcopath = "../dataset/msmarco"
Msmarcousefulness = "Usefulness.tsv"
Msmarcodev = "dev_v2.1.json"
Msmarcomsmarco = "msmarco.json"

WikiQA = "wikiqa"
WikiQApath = '../dataset/WikiQACorpus'
WikiQAtsv = 'WikiQA.tsv'

Coqa = "coqa"
Coqapath = "../dataset/coqa"
Coqatrain = "coqa-train-v1.0.json"
Coqadata = "data"
Coqaquestions = "questions"
Coqainput = "input_text"

Quac = "quac"
Quacpath = "../dataset/quac"
Quactrain = "train_v0.2.json"
Quacdata = "data"
Quacparagraphs = "paragraphs"
Quacqas = "qas"
Quacquestion = "question"

Dbdomainambiguous = "dbdomainambiguous"
Dbdomainnotambiguous = "dbdomainnotambiguous"
Dbdomainpath = "../dataset/db-domain-adaptation"
Dbdomainsqlite = "sqlite_fiiles"
Dbdomainrevised = "annotated-data/manually-labelled-data"
Dbdomainsentences = "sentences"
Dbdomainfulltext = "full-text"
Dbdomainmetafeature = "metafeature"

Alex = "alex"
Alexpath = "../dataset/alex_context_nlg_dataset"
Alexdataset = "dataset.json"
Alexcontextuttl = "context_utt_l"

Googlenq = "googlenq"
Googlenqpath = "../dataset/v1.0-simplified_nq-dev-all"
Googlenqdev = "v1.0-simplified_nq-dev-all.jsonl"
Googlenqquestion = "question_text"
Googlenqdata = "googlenq.json"

Totto = "totto"
Tottopath = "../dataset/totto_data"
Tottotrain = "totto_train_data.jsonl"
Tottodev = "totto_dev_data.jsonl"
Tottotable = "table"
Tottovalue = "value"
Tottotablesectiontitle = "table_section_title"
Tottofinalsentence = "final_sentence"
Tottosentenceannotations = "sentence_annotations"

Logicnlg = "logicnlg"
Logicnlgpath = "../dataset/LogicNLG/data"
Logicnlgtrain = "train_lm.json"
Logicnlgtest = "test_lm.json"
Logicnlgval = "val_lm.json"

Sparc = "sparc"
Sparcpath = "../dataset/sparc"
Sparctrain = "train.json"
Sparctables = "tables.json"
Sparcdev = "dev.json"
Sparcdatabaseid = "database_id"
Sparcinteraction = "interaction"
Sparcquery = "query"
Sparcutterance = "utterance"
Sparcfinal = "final"
Sparctablename = "table_names"
Sparccolumnname = "column_names"
Sparcdbid = "db_id"

Cosql = "cosql"
Cosqlnotambiguous = "cosqlnotambiguous"
Cosqlpath = "../dataset/cosql_dataset"
Cosqltables = "tables.json"
Cosqldialogs = "cosql_all_info_dialogs.json"
Cosqldbid = "db_id"
Cosqlquerygoal = "query_goal"
Cosqlsql = "sql"
Cosqltablename = "table_names"
Cosqlcolumnname = "column_names"
Cosqltrain = "cosql_train.json"
Cosqldev = "cosql_dev.json"
Cosqluserintentpath = "../dataset/cosql_dataset/user_intent_prediction"
Cosqlutterance = "utterance"
Cosqlintent = "intent"
Cosqluserdbid = "database_id"
Cosqlambiguous = "AMBIGUOUS"

Alexa = "alexa"
Alexapath = "../dataset/Topical-Chat/conversations"
Alexatrain = "train.json"
Alexavalidfreq = "valid_freq.json"
Alexavalidrare = "valid_rare.json"
Alexatestfreq = "test_freq.json"
Alexatestrare = "test_rare.json"
Alexacontent = "content"
Alexamessage = "message"


Csv = 'csv'
Column = "column"
Table = "table"
Question = "question"
Outputpath = "./output.json"
Type1 = 'small talk'
Type2 = 'ambiguous'
Type3 = 'lack data'
Type4 = 'unanswerable by sql'
Type5 = 'answerable'
Train = "trainset"
Dev = "devset"
Test = "testset"
Type1json = "type1.json"
Type2json = "type2.json"
Type3json = "type3.json"
Type4json = "type4.json"
Type5json = "type5.json"
Trainportion = 0.64
Devportion = 0.8
Testportion = 1

Outtype = "type"
Outquestion = "question"
Outquestiondatasetid = "question_datasetid"
Outdatabaseiddatasetid = "databaseid_datasetid"
Outdatabaseid = "databaseid"
Outtables = "tables"

type1qdataset = [Msmarco, WikiQA, Coqa, Quac, Googlenq, Alexa]
type1dataset = [Spider, WikiSQL, Tablefact, HybridQA, Wikitable, Dbdomainnotambiguous, Dbdomainambiguous,
                    Totto, Logicnlg, Sparc, Cosql]
type2dataset = [Dbdomainambiguous, Cosql]
type3dataset = [Spider, WikiSQL, Sparc, Dbdomainnotambiguous, Cosqlnotambiguous, HybridQA, Spiderother]
type4dataset = [Tablefact, Totto, Wikitable, Logicnlg]
type5dataset = [Spider, WikiSQL, Sparc, Dbdomainnotambiguous, Cosqlnotambiguous, Spiderother]