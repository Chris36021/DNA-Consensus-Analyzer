"""This program reads DNA sequences from an input file and finds the
consensus sequence.  An output file is also created to store the
counts per column, so as to validate the consensus.
Add the corresponding code to accomplish the requested tasks
"""



##### ADD YOUR NAME, Student ID, and Section number #######
# NAME: Christopher Castillo    
# STUDENT ID: 802-18-8379
# SECTION: 036
###########################################################


def load_data(fileName):
    #Read DNA sequences from file and return them in a list.
    fhandle = open(fileName)
    # Assume the file to be open exist
    dataList = list()
    for line in fhandle:
        if not line.startswith(">"):
            dataList.append(line.strip()) #strip to get rid of the newline character "\n"
    fhandle.close()
    # Use dataList to save the the all data from the file 
    # If file opens successfully, loop over the contents and store sequences in list.
    # Skip description lines (lines that start with ">").

    return dataList


def count_nucl_freq(dataList):
    """Count the occurrences of characters by column."""
    countStruct = list() # Indexed by columns (List of what?)
    for num in range(len(dataList[0])):
        nuc_values = {"A":0,"T":0,"G":0,"C":0} 
        for seq in dataList:            #Create a list of dictionaries, (one for each position)
            b = seq[num]                #with the Nucleotides
            nuc_values[b] = nuc_values.get(b,0) + 1     #Modify the value for each nucleotide in the seq
        countStruct.append(nuc_values)
        
    return countStruct
    # Loop over the sequences in dataList to count the nucleotides
    # We'll need a nested loop to process every character in every sequence.
    # Recommend: Use outer loop for columns (characters) and inner loop for
    # rows (sequences), since countStruct only cares about the characters (not the seqs).
    

def find_consensus(countData):
    """Return the consensus sequence according to highest-occuring nucleotides"""
    consensusString = ""
    poslist = []
    for seqpos in countData:        #Create a list of lists to house tuples with 
        poslist.append([])          #the values of each dictionary (column)
    list_index = 0
    for seqpos in countData:
        for k,v in seqpos.items():
            poslist[list_index].append((v,k))      #append the keys and values of the nucleotides to a list
        poslist[list_index] = sorted(poslist[list_index], reverse = True) #sort list of nucs in sequence in decreasing order
        list_index +=1

    for seqpos in poslist:
        consensusString += seqpos[0][1]     #Create consensus sequence 

    return consensusString
    # Loop here to find highest-occuring nucleotide in each column
    # and concatenate them into consensusString


def process_results(countData, outFilename):
    """Print consensus to screen and store results in output file."""
    fhand = open(outFilename, "w")  #Create output file
    consensus = find_consensus(countData)
    print("Consensus: " + consensus)            
    fhand.write("Consensus: " + consensus + "\n")       #Write consensus in ouput file
    poslist = []
    for seqpos in countData:        
        poslist.append([])
    list_index = 0                  
    for seqpos in countData:            #Regain nucleotide data used in step 3
        for k,v in seqpos.items():
            poslist[list_index].append([v,k])
        poslist[list_index] = sorted(poslist[list_index], reverse = True)
        list_index += 1

    counter = 1
    for pos in poslist:
        fh = "Pos " + str(counter) + ": " +pos[0][1] +":" + str(pos[0][0]) + " "+pos[1][1] +":" + str(pos[1][0])
        lh = " " +pos[2][1] +":" + str(pos[2][0]) + " "+pos[3][1] +":" + str(pos[3][0])
        result_string = fh + lh
        fhand.write(result_string + "\n")
        print(result_string)                        #Iterate throughout each column and generate a
        counter +=1                                 #string that conatins the position and the 
                                                    #quantity of each nucleotide
                                                    #at the same time, write the position and number of 
                                                    #nucleotides in each column to the output file
    fhand.close()
    # Now open the output file, and write the consensus string.
    # Then loop, to print nucleotide count in non-increasing order.
    # Each row in the output file (except the first one) should
    # have the count data for a column, in order of columns.


def main():

    # File name "constants". Assume the names of the files don change.
    INPUTFILE  = "DNAInput.fasta"        #Test file name == "DNAInputT.txt"
    OUTPUTFILE = "DNAOutput.txt"         #Default file name == "DNAInput.fasta" 

    seqList = load_data(INPUTFILE)

    countData = count_nucl_freq(seqList)

    process_results(countData, OUTPUTFILE)

# The code below makes Python start from the main function
# whenever our program is invoked as a "standalone program"
# (as opposed to being imported as a module).
#if __name__ == "__main__":
#   main()
main()