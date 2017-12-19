In order to run the code make sure you have python 3.6.1 installed. Also you need to make sure you have Jupyter Notebook installed. If you do not have jupyter notebook I suggest installing Anaconda and then Jupiter notebook. Here is a link on installing the Jupyter notebook http://jupyter.readthedocs.io/en/latest/install.html.

To run the project notebook. 

1)	Open terminal or command line
2)	Navigate to the folder where the notebook is
3)	type in : ipython notebook
	Alternatively you can also type in jupyter notebook

This will lead to pop up a window on your browser which will have all files in your current directory listed. Make sure you have the following files in your current directory:
	* vectors.txt
	* Directory named DATA-NLP
	* Excel File named corpus_final.xls

The first file vectors.txt is the vectors of words created by using GloVe on our corpus.
The directory name DATA-NLP contains our dataset
The third file named corpus_final.xls is a list of classification of our files like which of them are plagiarised and by how much. We use this file for evaluation namely calculating precision, recall, F1 and accuracy.

After performing the above three steps make sure to click on kernel and the click on restart and run all cells. This will make sure that the code is executed in front of you and that it is working. 

You will also need all the imports to be installed on your system to run the file. 
