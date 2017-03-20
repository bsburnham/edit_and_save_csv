#==============================================================================
# Created by Dr. Brian Burnham
# The University of Aberdeen
# School of Geosciences
#==============================================================================
# Code to delete rows of unused data and replace classified values of point 
#  cloud datasets containing XYZ and Intensity values.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Import functions into program for use
#------------------------------------------------------------------------------
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

#------------------------------------------------------------------------------
# Variables created for removing columns of data
#------------------------------------------------------------------------------
remove_from = 3
remove_to = 5

#------------------------------------------------------------------------------
# Function to open data file and write to new datafile
#------------------------------------------------------------------------------

def modify_data_and_update_file(filename, out_name):
    with open(filename, "r") as fp_in:
        reader = csv.reader(fp_in, delimiter=" ")
        with open(out_name, "w") as fp_out:
            writer = csv.writer(fp_out, delimiter=" ", lineterminator='\n')
            
#-------------------------------------------------------------------------------
# Removes the unnecessary columns from the file and replaces -100000 with 1 and
# everything else with a 0 and writes all rows and columns of data to text file
#-------------------------------------------------------------------------------
            for column in reader:
                del column[remove_from:remove_to]
                if column[3] != '-100000':  # NULL value VRGS produces
                    column[3] = '0'
                else:
                    column[3] = '1'
#                print(column)
                writer.writerow(column)
                
#------------------------------------------------------------------------------ 
# Prompts user to input file name and save filename with GUI   
#------------------------------------------------------------------------------    
Tk().withdraw()
filename = askopenfilename(title = "Please choose a file to open.")
#filename = input("Enter the filename: ")
out_name = asksaveasfilename(title = "Please choose a file name to save as.")
#out_name = input("What would you like to call the filename?: \n")

#Call the function modify_data_and_update_file
modify_data_and_update_file(filename, out_name)