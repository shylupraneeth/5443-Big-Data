What language you choose, and why ?
-----
- I would like to use python language to convert the CSV files to JSON because my reaserch made me know that converting to JSON formats with python will be more easy and they are well organised.

Example : If you have an excel spreadsheet(saved as a csv file) of four columns. The first and third columns contain words,              the second and fourth columns contain frequency. So if it looks something like this:

                  word1, freq1, word2, freq2
                  word3, freq3, word4, freq4
                  
                
  Unfortunately python's DictReader isn't well suited for this use case, however little zip magic should help. 

  
  
  
  
 What file you choose to convert, and why? 
 -----------------------
 - I would like to prefer the CSV file to convert into JSON because :
    

    if you want to provide JSON-based results from the SQL, you are faced with a problem, because SQL Server doesn’t currently have native JSON-integration. You would normally  craft the SQL to do this ‘by hand’ for the specific job, using one of a variety of techniques. However, what if the developers needed to have large variety of results, though there will be a performance hit to using a generic solution that will produce JSON from any SQL. Until SQL Server provides ‘native’ JSON support it will be rather slow, but not difficult.

    if you want to provide JSON-based results from the SQL, you are faced with a problem, because SQL Server doesnâ€™t currently have native JSON-integration. You would normally  craft the SQL to do this â€˜by handâ€™ for the specific job, using one of a variety of techniques. However, what if the developers needed to have large variety of results, though there will be a performance hit to using a generic solution that will produce JSON from any SQL. Until SQL Server provides JSON support it will be rather slow, but not difficult.


    If you prefer converting xml to JSON i feel that the you need a large amount of size to store the data , as xml files are probably big in their size .So, i believe that converting CSV to JSON is easy and we get the results in more organised way .
    
 




-----------------------------------------------------------------------------------------------------------------------
Which of the files compresses the best using zip and gzip ?
--



ZIP and GZIP are two very popular methods of compressing files, in order to save space, or to reduce the amount of time needed to transmit the files across the network, or internet. In general, GZIP is much better compared to ZIP, in terms of compression, especially when compressing a huge number of files.

WHY ?
----


ZIP : These format are capable of both archiving and compressing the files together. These are two separate processes. 
Compression reduces the size of the file with the use of algorithms, while archiving combines multiple files, so that 
the output is a single file.

GZIP : This is purely a compression tool, and relies on another tool, commonly TAR, to archive the files.

-It might seem like a minor thing, but it can affect the experience of the user in certain instances

-In ZIP files, the individual files are compressed and then added to the archive, where GZIP is to archive all the      files into a single tarball before compression.
 so , When you want to pull a single file from a ZIP, it is simply extracted, then decompressed but With GZIP, the      whole file needs to be decompressed before you can extract the file you want from the archive


MAIN DIFFERENCES :
------

1. GZIP can achieve better compression compared to ZIP.

2. ZIP is capable of archiving and compressing multiple files, while GZIP is only capable of compression.

3. You can easily extract individual files from a large ZIP file, but not from a GZIP tarball.

4. ZIP is fairly popular on Windows, while GZIP is more popular on UNIX-like operating systems.


                                                      ----------
                                                      

| Type | Description                                  | Size    |Compressed size|   %   |
|------|----------------------------------------------|---------|---------------|------:|
| csv  |Comma seperated values                        | 484MB   |     59MB      | 87.8  |
| sql  |Structured Query Language (insert statements) | 467MB   |     60MB      | 87.1  |
| xml  |EXtensible Markup Language                    | 2.3GB   |     75MB      | 96.7  |
| yml  |Yet Another Markup Language                   | 771MB   |     61MB      | 92.0  |
| Json |Javascript Object Notation                    | 824MB   |               |       |

When we convert CSV file to Json file the file size is 824 MB


   

  
                                                      
                                                      


