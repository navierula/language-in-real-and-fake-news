import glob2

#######################################################################

# find all file names with a .txt extension
filenames = glob2.glob('data/political_news/fake_headlines/*.txt') 

# concatenate all individual files into one file
with open("fake_headlines.txt", "w", encoding="ISO-8859-1") as f:
    for file in filenames:
        with open(file, encoding="ISO-8859-1") as infile:
            # append 'fake' parameter at end of each line
            f.write(infile.read()+"\t"+"fake"+"\n")

########################################################################

# find all file names with a .txt extension
filenames = glob2.glob('data/political_news/real_headlines/*.txt') 

# concatenate all individual files into one file
with open("real_headlines.txt", "w", encoding="ISO-8859-1") as f:
    for file in filenames:
        with open(file, encoding="ISO-8859-1") as infile:
            # append 'fake' parameter at end of each line
            f.write(infile.read()+"\t"+"real"+"\n")

########################################################################