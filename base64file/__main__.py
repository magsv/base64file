import os 
import base64
import logging
import click


@click.group()
def messages():
  pass

def list_files(folder):
    files=[]
    with os.scandir(folder) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.path)
    return files


def base64_handle_file(input,output,encode=False):
    file=open(input,'rb')
    data=file.read()
    processed_data=''
    if encode:
        #encode to base64
        processed_data=base64.encodestring(data)
    else:
        processed_data=base64.decodestring(data)
    file = open(output, 'wb')
    file.write(processed_data)
    file.close()
    logging.info('Encoded file:{} to base64 file:{}'.format(input,output))

def create_folder_if_not_exist(folder):
    if not os.path.exists(folder):
        logging.info('Creating folder:{}'.format(folder))
        os.makedirs(folder)

def build_output_name(input_file,output_folder,extension):
    name_in=os.path.basename(input_file)
    return os.path.join(output_folder,name_in+extension)

@click.command(name='encode',help='Command to encode a set of files to base64')
@click.option('--input',
              help='The path to the folder containing the files to encode to base64',
              required=True)
@click.option('--output',
              help='The path to the folder where encoded files should be stored',
              required=True)
@click.option('--output_extension',
              help='The output extension to use for encoded files default .encoded_b64',
              default='.encoded_b64',
              required=False)
def encode(input,output,output_extension):
    #create the output folder if not existing
    create_folder_if_not_exist(output)
    files=list_files(input)
    for item in files:
        output_name=build_output_name(item,output,output_extension)
        #encode it
        base64_handle_file(item,output_name,encode=True)

@click.command(name='decode',help='Command to decode a set of files from base64')
@click.option('--input',
              help='The path to the folder containing the files to decode from base64',
              required=True)
@click.option('--output',
              help='The path to the folder where decoded files should be stored',
              required=True)
@click.option('--output_extension',
              help='The output extension to use for decoded files default .decoded_b64',
              default='.decoded_b64',
              required=False)
def decode(input,output,output_extension):
    #create the output folder if not existing
    create_folder_if_not_exist(output)
    files=list_files(input)
    for item in files:
        output_name=build_output_name(item,output,output_extension)
        #encode it
        base64_handle_file(item,output_name,encode=False)

@click.command()
@click.pass_context
def help(ctx):
    print(ctx.parent.get_help())



messages.add_command(encode)
messages.add_command(decode)
messages.add_command(help)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    messages()