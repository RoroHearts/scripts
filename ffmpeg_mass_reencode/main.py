import ffmpeg
import os

ffmpeg_args = {
    "vcodec":"libx264",
    'preset':'medium',
    'crf':22
}

input_directory = "input"
output_directory = "output"

for filename in os.listdir(input_directory):

    input_name = os.path.join(input_directory, filename)
    output_name = os.path.join(output_directory, filename)

    stream = ffmpeg.input(input_name)
    stream = ffmpeg.output(stream, output_name, **ffmpeg_args)
    ffmpeg.run(stream)