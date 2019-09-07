from os import system, listdir, path

input_path = rf"{input('Please enter the input path: ')}"
output_path = rf"{input('Please enter the output path: ')}"

command = 'ffmpeg -i {input_file}'

if input("Scale video? Y/n   ").lower() != 'n':
    command += f' -vf scale={input("Please enter the width: ")}x{input("Please enter the height: ")} -max_muxing_queue_size 9999'


if input("Remove audio tracks? Y/n   ").lower() != 'n':
    command += f' -map 0:0 -map 0:{input("Please enter the audio track: ")} -acodec copy'

command += ' {output_file}'

for file in listdir(input_path):
    settings = {
        'input_file': f'"{path.join(input_path, file)}"',
        'output_file': f'"{path.join(output_path, file)}"'
    }

    current_command = command.format(**settings)

    system(current_command)
