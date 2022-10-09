# Removing commentary* from a subtitle
# *examples: "(SCOFFS) Don't be ridiculous." or "(CHAINS RATTLING)"

print()
try:
    file = open(r'd:\Downloads\01.srt','r+')
    newFile = open(r'd:\Downloads\updated_sub.srt','x')  
    fileList = list(file)
    slicedList = []

    for i in range(len(fileList)):    
        sliced = fileList[i].split()   # cutting up the text
        slicedList.append(sliced)      # collecting the new/transformed items in a new list
        
    for i in slicedList:
        for k in i:
            if '(' in k and ')' in k:  # removing one word commentary from line like: "(SCOFFS) Don't be ridiculous."
                i.remove(k)
            elif '(' in k and ')' not in k: # removing multiple words commentary from lines like: "(CHAINS RATTLING)" 
                slicedList.remove(i)        # very small chance: there are lines where both previous conditions are true
                                            # and we remove a line with a non-commentary text

    for i in slicedList:             
        newFile.writelines(' '.join(i))  # add a space between the list items
        newFile.write('\n')              
    

    file.close()
    newFile.close()

    print()
    print('The new subtitle, named: updated_sub is created.')
    print()

except FileNotFoundError:
    print()
    print('The path is incorrect.')
    print()