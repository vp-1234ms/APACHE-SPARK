# APACHE-SPARK


![WhatsApp Image 2024-09-30 at 2 21 28 PM](https://github.com/user-attachments/assets/0a2a701a-62c5-4e0a-a117-9897ccfbfd73)


![WhatsApp Image 2024-09-30 at 2 30 57 PM](https://github.com/user-attachments/assets/4b73f890-3064-41ce-818c-6ba2b98ff8da)




APACHE SPARK IS A IN MEMORY DATA PROCESSING FRAMEWORK DESIGNED FOR LARGE SCALE DATA PROCEESSING
IT HAS HIGHER EDGE THAN HADOOP MAP RDUCE DUE TO 
1) HADOOP LOW SPEED DUE TO DISK IO OPERATIONS WHILE SPARK DOES IN MEMORY PROCESSING WHICH MAKES IT "FASTER"
2) HADOOP SUPPORTS FOR ONLY BATHC PROCESSING WHICH LIMITS IT'S USE IN REAL TIME APPLICATION WHILE APACHE SPARK HANDLES "REAL TIME PROCESSING" WITH STREAMING CAPABILITY

APACHE SPARK CONSISTS OF 
1) SPARK SQL
2) SPRAK STREAMING 
3) MACHINE LEARNING LIBRARY(MLIB)
4) GRAPHX (GRAPH COMPUTATION)
APACHE SPARK CORE API SUPPORTS JAVA, PYTHON, SCALA, SQL, R



CHARACTERITESIC OF SPARK:
1) SPEED: DUES TO IN MEMORY COMPUTATION 
2) EASE OF USE: PROVIDES VARIOUS API SUPPORT IN JAVA, PYTHON, SCALA, SQL, R WHICH MAKES ACCESSIBLE TO DEVELOPERS WITH DIFFERENT SKILL SET 
3) MODULARITY: BUILT FOR DIFFERENT USE CASES SUACH AS SPARK SQL, SPARK STREAMING, MLIB AND GRAPHX
4) EXTENSIBILITY: IT IS HIGHLY FLEXIBLE MEANING YOU CAN ADD CUSTOM CUMPONENTS AND INTEGRATE WITH OTHER BUG DATA OOLS AND IT SUPPORTS WIDE RANGE OF DATA SOURCES LIKE MONGODB, NOSQL.



_____________________                              EXECUTOR 1
|                    |                           /
|     SPARK APP      |                          /       
|   ______________   |                         /
|  | SPARK DRIVER |  |        ________________/ 
|  |______________|  |        |CLIENT MANAGER|
|   ______________   |        |______________|
|  |SPARK SESSION |  |                        \
|  |______________|  |                         \
|____________________|                          \  EXECUTOR 2





SPARK APP: IT IS PROGRAM WRITTEN EG: WRITTEN IN PYTHON USING PYSPARK
SPARK DRIVER: MANAGES THE EXECUTION ON APPLICATION
SPARK SESSION THE ENTRY POINT FOR WORKING WITH SPARK USED TO WORK WITH DATA
CLUSTER MANAGER: MANAGES RESOURCES AND ALLOCATES TO DIFFERENT TASKS RUNNING ON CLUSTER
EXECUTOR: EXECUTE TASKS AND HANDLES DATA PROCESSING



PYSPARK:
PYSPARK IS PYTHOIN API FOR APACHE SPARK WHICH ALLOWS US TO USE SPARK'S POWERFUL DISTRIBUTED DATA PROCESSING USING PYTHON.

NOW WE CAN USE JUPYTER NOTEBOOK OR SPYDER OR PYCHARM AS IDE TO WRITE CODE FOR SPARK APPLICATIONIN PYTHON







                JOB                       TASK
             /
            / 
           /                              TASK
__________/
| DRIVER |
|________|\ - - JOB       STAGE           TASK
           \
            \
             \  JOB                       TASK




HERE WHENEVER WE CREATE SPARK APPLICATION, SPARK DRIVER AND SPARK SESSION IS CREATED
SPARK DRIVER MANAGES THE EXECURION OF APPLICATION , THIS SPARK APLICATION CAN CONSIST OF MULTIPLE JOBS EG: SPARK APPLICATION FOR FILETERING DATA CAN HAVE DATA PROCESSING , DATTA READING , DATA FILTERING ETC THIS JOBS ARE THEN DIVIDDED INTO STAGE BASED ON THERE PARALLEL EXECUTION THEN THIS STAGE ARE DIVIDED INTO TASK WHICH MANAGES PARALLEL EXECTUION ON CLUSTERS WHICH MAKES APACHE SPARK FASTER.
THIS FLOW IS IN FORM OF DAG(DIRECTED ACCLIC GRAPH) WHICH MAKES IT FASTER THAN HADOOP WHICH IS LINEAR


APACHE SPARK USES CONCEPT OF LAZY EVALUATION
LIKE THERE ARE TRANFORMATIOMN AND ACTION... FOR TRANSFORMATION IT DOES NOT REQUIRE ANY COMOPUTAION EG: GROUP BY, ORDER BY
SO IT DELAYS SUCH JOBS WHILE ACTIONS LIKE COUNT REQUIRES COMPUTAION IT PRITIZE SUCH JOBS USING DAG THIS MAKES IT FASTER.




RDD(RESILIENT DISTRIBUTED DATASET) AND DATAFRAME BOTH ARE USED FOR DATA PROCESSING
RDD IS SINCE SPARK RELASE WHICH HAD SOME CHALLENGES LIKE COMPLEXITY MORE COMPLEX CODE HARD TO USE
THEN IN LATER RELEASE DATAFRAME WAS USED WHICH REALLY MADE EASY TO PERFORM DATA OPERARTION USING SQL WITH SIMPLE SQL OPERATIONS 

IN RDD WE DIRECTLY START USING MAP REDUCE AND THEN LAMBDA FUNCTION TO PERFORM COMPUTATION
MEAN WHILE IN DATAFRAME WE CREATE SPARK SESSION AND THEN CREATE DTAAFRANE AND THEN START PERFORMING SQL OPERATIONS USING SPARK SQL.
 
SO OVERALL DATAFRAME PROVIDES STRUTURE TO OUR DATA AND OPTIMIZES OUR OPERATIONS





DATAFRAME VS DATASET

1) IN SIMPLE DATFRAM ARE UNSTRUTURED THERE IS NO DATA TYPE SPECIFIED, WHILE IN DATASET EACH COLUMN HAS DATATYPE SPECIFIED 
2) IN DATAFRAME IT IS SIMPLE TO USE BUT UNSAFE DUE TO DIFFEERENT UNKNOW COLUMN DATYPES WHILE DATSET ARE MORE SAFER DUE TO PREDEFINED DATATYPE
3) AS DATAFRAME DOES NOT REQUIRE ANY DATA TYPES DEFINED TO WORK IT CAN BE USED IN PYTHON,R,SCALA,JAVA WHILE DATASET REQUIRES PREDEFINED DATATYPES IT IS SUPPORTED ONLY IN SCALAA AND JAVA AS PYTHON AND R DOES NOT HAVE ANY DATATYPE SUPPORT.



WHEN TO USE RDD AND DATAFRAME:
RDD
1) WHEN YOU NEED FINE GRAINED CONTROL OVER DATA AND TRANSFORMATION
2) WHEN WORKING UNSTRUTRED DATA
3) WHEN YOU WANT TO ADD CUSTOM LOGIC AND FUNCTION
4) WHEN NEED FAULT TOLERANCE FOR COMPEX COMPUTATION

DATAFRAME:
1) WHEN WORKING SURETURED DATA
2) WHEN NEED PERFORMANCE OPTIMIZATION
3) FAMILALIR WITH SQL LIKE OPERATIONS EASY TO USE 
4) LOW CODE 





SPARK SQL:
SPARK SQL USES HIGHLY OPTIMIZE ENGINE WHICH CONSISTS OF
1) CATALYST OPTIMIZER: IS QUERY OPTIMIZER
2) TUNGSTEN OPTIMIZER: IS CPU AND MEMORY OPTIMIZER
THIS BOTH MAKES SPARK SQL FASTER.
SOAKR SQL ALSO CONSISTS OF JDBC AND ODBC CONNECTIORS WHICH ALLOWS SPAKR SQL TO CONNECT WITH VARIUOUS DATA SOURCES.



IN SPARK SQL WORK FLOW IS:
1) IMPORT REQUIRED PACKAGES EG: SPARK SESSION
2) CREATE SPARK SESSION BY SPECIFYING APPLICATION NAME
3) LOAD DATA BY SPECIFYING NAME AND PATH OF CSV FILE..IF WE DO INFER SCHEME TRUE IT WILLAUTOMZAITCALLY ASSIGN DATATYPE TO COLUMN THIS WILL CREATE SCHEMA
4) THEN WE CRETAE TEMP VIEW ON TOP OF DATA WHICH MAKES DATAFRAME AVAILABLE AS SQL VIEW TO PERFORM SQL OPERATIONS
5) THEN WE USE SPARK SQL TO PERFOMR SQL OPERATIONS

IN SPARK SQL WE HAVE MANAGE AND UNMANAGE TABLE
IN MANAGE TABLE -> SPARK MANAGES BOTH DATA AND METADATA 
IN UNMANAGE TABLE -> SPARK MANAGES ONLY META DATA WHILE DATA IS MANAGED BY USER OR STORED BY USER IN DIFFERENT DATA SOURCES


IN SPARK WE HAVE TEMP VIEW AND GLOBAL VIEW
VIEW-> IT IS CREATED ON TOP OF DATAFRAME SO IT IS VIRTUAL AND IS DOES NOT OCCUPY LARGE SPACE AND IS DELETED AFTER SESSSION ENDS
TEMP VIEW -> CAN BE USED IN CURRENT SESSION OF SPARK APPLICAION
GLOBAL VIEW -> CAN BE USED ACROSS ALL SESSION OF SPARK APPLICATION


>DATAFRAME READERS AND DATAFRAME WRITERS
THIS ARE USED TO READ AND WRITE FROM VARIOUS DATA SOURCES

>INTERACTING WITH EXTERNAL DATA SOURCES
WE CAN INTEGRATE WOTJ EXTERNAL DATA COURCES SUCH AS JDBC AND SQL DATABASES, POSTGRES, MYSQL, AZURE COSMOSDB AND MYSQL SERVER.



SO SUMMING UP SPARK SQL:
SPARK SQL IS MODULE IN APACHE SPARK THAT PROVIDES A INTEGRATIPONS OF SQL QUERIES WITH DATAFRAME AND DATASET APIS
IT ALLOWS US TO INGECT DATA FROM VARIOUS SOURCES BY LOADING NECESSARY PACKAGE LIKE SPARK SESSION TO CREATE SESSION THEN TRANFORMATION TO CREATE SCHEMA OR STURETURED DATA THEN CREATING TEMP VIEW THEN PERFORMAING DATA ANALYSIS WHICH ALLOWS US TO PERFORM SQL OPERATIONS ON THIS DATAFRAME AND THEN IT USES CATALYST AND TUNGSTEN OPTIMIZERS TO OPTIMIZE QUERY THEN SAVING FILES IN PARTION FORMAT OR VARIOUS TYPES WHICH INLCUDES CSV, JSON, PARQUET FORMAT.
THIS MAKES SPARK SQL A POWERFUL TOOL FOR LARGE SCALE DATA PROCESSING AND ANALYSIS





2) SPARK STREAMING

1) DEFINE INPUT SOURCE: HERE WE DEFINED INPUT SORCE WHICH IS SOCKET WHICH SETS UP THE APPLICATION TO LISTEM FOR INCOMING DATA ON A SPECIFIED HOST-> LOCAL HOST
AND SPECIFIED PORT -> 9999
2) TRANFRM DATA: HERE WE WANT TO SPLIT DATA INTO WORDS THAT IS EACH LINE OF IS TRANFORMED INTO ARRAY OF WORDS
3) DATA PROCESSING: HERE WE WANT OT COUTN BY GROUPING WORDS 
4) CHECKPOINT DIRECTORY : TO STORE INTERMEDIATE DIRECTORY FOR FAULT TOLERANCE
5) NOW COMFIRGURING FOR STARTING LIVE STREAMING OF DATA: SPECIFYING 
FORMAT-> CONSOLE
OUTPUT MODE-> CONSOLE
TRIGGER-> EVERY 1 SECOND WRITING OUTPUT
CHECKPOINT DIRECTORY -> PATH

THEN CONTINUING UNLESS UNITLL USER TERMINATES BY HIMSELF

THIS SPARK STREAMING APPLIATION CONTINUOUSLY READ DATA FROM A SOCKET(SENDER(CONSOLE) AND RECEIVER(SPARK STREAMING APPLICATION)) ON A PORT 9999. PROCESS THE DATA TO COUNT WORD OCCURENCES AND DIAPLAY THE RESULT IN REAL TIME ON CONSOLE. IT USES A ACHCKPOINT DIRECTORY TO ENSURE FAULT TOLERANCE AND MAINTAIN APPLICATION STATE.

THIS IS SIMPLE SPARK APPLICATION FOR DOING DATA PROCESSING AND DATA ANLYSIS ON SPARK STREAMING.



3) SPARK MLIB
SPARK PROVIDES MLIB FOR BUIDLING MACHINCE LEARNING MODELS
IT CONSISTS OF
1) TRNASFORMER : TRANSFORM INPUT DATAFRAME TO OUTPUT DATAFRAME WHICH INVOLES VARIOUS OPERATIONS ON INPUT DATAFRAME EG: SCALLING , ENCODING
2) ESTIMATOR : LEARN FROM DATA AND PRODUCE TRAINED MODEL
3) PIPELINES : CHAINING TOGETHER MULTIPLE TRANSFORMER AND ESTIMATOR TO STREAMLINE THE ML WORKFLOW

WE CAN EVEN BUILT ML MODELS INDEPENDENTLY BUT MLIB OF SPARK DIFFERS BY PROVIDNG
1) WE CAN TRAIN MODEL ON BIG DATA 
2) REAL TIME PROCESSING
3) BUILD COMPLEX DATA PIPLEINES
4) ADD DATA FROM MULTIPLE SOURCES
5) PROVIDES SCALABILITY 
6) PARALLEL PROCESSING
7) INTEGRATION WITH BIG DATA TOOLS
8) BUILT IN ALGORITHMS FOR LARGE SCALE ML
9) FAULT TOLERANCE






