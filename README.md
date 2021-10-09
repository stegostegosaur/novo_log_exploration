# novo_log_exploration
Exploratory analysis and descriptive statistics tasks conducted on the Novolanguage log-files of the PhD project called 'I can speak'. The following files are contained in this repository:

The analysis can be run with the script 'runPipeline.py'. Itt takes two user inputs: one for the directory where the log-files are located, and an optional list for participants to be removed. After conducting the analyses, it writes the resulting csv tables and barplots in a subfolder called 'Result of Analysis' inside the directory entered above.

• main.py: contains functions for pre-processing the files, such as converting log files into JSON format and removing empty log files.

• makeOutput.py: generates csv tables and plots in a newly devised sub-directory within the working directory.

• getDescriptiveStats.py: calculates accuracy score and number of spoken instances of individual subjects on utterance, word and phone levels. Consecutively, it then writes the results into a single csv output.

• getBehaviourStats.py: collects data on the time-frame and input numbers associated with user activity. Generates a csv table and plots based on this.

• getNumberData.py: aggregates input numbers over lessons and prompts, then generates plots on these.

• getAccuracyData.py: Aggregates accuracy scores over lessons and prompts, then generates csv tables on these.
