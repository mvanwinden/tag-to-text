# tag-to-text
A simple Python script for extracting the contents of XML or HTML tags from a source file and writing them to a separate output file.

## Usage
``` bash
git https://github.com/mvanwinden/tag-to-text/
cd tag-to-text
python tag-to-text.py 'path_to_source_file' 'tag_name' 'output_file'
```

The script takes three command line arguments: 
* **path_to_source_file** is the path to the text file you want to compare with the source file.
* **tag_name** is the name of the tag you want to extract from the source file
* **output_file** is the path to the new file that will be created, containing the contents between the tags in the source file. If the output file is not defined, it defaults to the name of the source file (without the path), plus '_tags.txt'.
