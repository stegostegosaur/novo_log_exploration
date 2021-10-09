# novo_log_exploration
Exploratory analysis and descriptive statistics tasks conducted on the Novolanguage log-files of the PhD project called 'I can speak'. The following files are contained in this repository:

The file 'runPipeline.py' runs the analysis: it takes a user input for the directory where the log-files are located, and returns csv tables and barplots on the data. The analyses involved are defined in the followig scripts:

• main.py: contains functions for pre-processing the files, such as converting log files into JSON format and removing empty log files.

• makeOutput.py: generates csv tables and plots in a newly devised sub-directory within the working directory.

• getDescriptiveStats.py: calculates accuracy score and number of spoken instances of individual subjects on utterance, word and phone levels. Consecutively, it then writes the results into a single csv output.

• getBehaviourStats.py: collects data on the time-frame and input numbers associated with user activity. Generates a csv table and plots based on this.

• getNumberData.py: aggregates input numbers over lessons and prompts, then generates plots on these.

• getAccuracyData.py: Aggregates accuracy scores over lessons and prompts, then generates csv tables on these.
