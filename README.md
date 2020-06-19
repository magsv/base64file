# base64file

A small client library to process files in a folder and decode/encode to/from base64

The library uses Click as a command line parameter helper and as such Click need to be installed, e.g. using pip with command pip3 install click

The package can also be installed using the supplied setup.py command

## Decoding

python3 -m base64file decode --input='./inputfolder' --output='./decoded' --output_extension='.decoded_b64'


## Encoding

python3 -m base64file encode --input='./inputfolder' --output='./decoded' --output_extension='.encoded_b64'


## Encoding and remove default newlines

python3 -m base64file encode --input='./inputfolder' --output='./decoded' --output_extension='.encoded_b64' --clean_lines

