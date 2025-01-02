import os
import subprocess

FileName = input('Название файла: ')
SubtitleName = input('Название субтитров: ')

FileNameBase = os.path.basename(FileName)
FileWithoutExtension, FileExtension = os.path.splitext(FileNameBase)
OutputFileName = FileWithoutExtension + "_SUB" + FileExtension
SubtitleNameBase = os.path.basename(SubtitleName)

cmd = f'ffmpeg -i "{FileNameBase}" -vf ass="{SubtitleNameBase}" "{OutputFileName}"'
subprocess.call(cmd, shell=True)
