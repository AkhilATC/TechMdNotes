
# Regex in dateframe

### RegEx Replace values using Pandas

Pandas replace() function is used to replace a string regex, list, dictionary, series, number in a dataframe. 
we explain how to replace patterns using regex with examples.

#### Replace function for regex

For using pandas replace function with regex, you need to define 3 parameters: 

1. to_replace : Denotes the value that has to be replaced in the dataframe or series. In the case of regular expressions, a regex pattern has to be passed. 
This pattern represents a generic sequence of characters.
3. regex : For pandas to interpret the replacement as regular expression replacement, set it to __True__
4. value : This represents the value to be replaced in place of to_replace values.

