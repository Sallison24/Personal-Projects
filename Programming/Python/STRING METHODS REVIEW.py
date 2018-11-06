"""
Excellent work! This lesson has shown you the vast variety of string methods and their power. Whatever the problem you are trying to solve, if you are working with strings then string methods are likely going to be part of the solution.

Over this lesson you've learned:

.upper(), .title(), and .lower() adjust the casing of your string.
.split() takes a string and creates a list of substrings.
.join() takes a list of strings and creates a string.
.strip() cleans off whitespace, or other noise from the beginning and end of a string.
.replace() replaces all instances of a character/string in a string with another character/string.
.find() searches a string for a character/string and returns the index value that character/string is found at.
.format() and f-strings allow you to interpolate a string with variables.

"""

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

###Splits the data set by ,
highlighted_poems_list=highlighted_poems.split(',')
print(highlighted_poems_list)
###iterates through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped
highlighted_poems_stripped=[]
for line in highlighted_poems_list:
  highlighted_poems_stripped.append(line.strip())
print(highlighted_poems_stripped)
###Iterates through highlighted_poems_stripped and split each string around the : characters
highlighted_poems_details=[]
for line in highlighted_poems_stripped:
  highlighted_poems_details.append(line.split(':'))
###Iterates through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates
titles=[]
poets=[]
dates=[]
for line in highlighted_poems_details:
  titles.append(line[0])
  poets.append(line[1])
  dates.append(line[2])
print(titles,poets,dates)
###loop that uses either f-strings or .format() to prints out the following string for each poem
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
