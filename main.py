import os

command = None
v_file = ""
o_file = ""
v_codec = ""
a_codec = ""
v_bitrate = ""
a_bitrate = ""
fps = ""
res = ""
duration_to_process = ""
start_time = ""
overwrite_if_exists = ""
vf = ""
correct_dir = False

print("Welcome to the FFmpeg command builder")

v_file = input("Filename of the video to edit: ")

v_file = f"-i {v_file}"

o_file = input("Name of the output file? ")

if input("Change video codec? y/n ") == "y":
    v_codec = input("New codec: ")
    v_codec = f"-c:v {v_codec}"
else:
    print("Not changing video codec")

if input("Change audio codec? y/n ") == "y":
    a_codec = input("New codec: ")
    a_codec = f"-c:a {a_codec}"
else:
    print("Not changing audio codec")

if input("Change video bitrate? y/n ") == "y":
    v_bitrate = input("New bitrate: ")
    v_bitrate = f"-b:v {v_bitrate}"
else:
    print("Not changing video bitrate")

if input("Change audio bitrate? y/n ") == "y":
    a_bitrate = input("New bitrate: ")
    a_bitrate = f"-b:a {a_bitrate}"
else:
    print("Not changing audio bitrate")

if input("Change video fps? y/n ") == "y":
    fps = input("New FPS: ")
    fps = f"-r {fps}"
else:
    print("Not changing FPS")

if input("New resolution? y/n ") == "y":
    res = input("New resolution: ")
    res = f"-s {res}"
else:
    print("Not changing resolution")

if input("Change duration to process? y/n ") == "y":
    duration_to_process = input("New duration to process: ")
    duration_to_process = f"-t {duration_to_process}"
else:
    print("Not changing duration to process")

if input("Change start time? y/n ") == "y":
    start_time = input("New start time: ")
    start_time = f"-ss {start_time}"
else:
    print("Not changing start time")

if input("Overwrite output if already exists? y/n ") == "y":
    overwrite_if_exists = "-y"
else:
    print("Will not overwrite output if already exists")

if input("Do you want to add video filters? y/n") == "y":
    vf = input("(You will have to do this manually, \
                I am not yet able validate your input) \
                Video filters: ")
    vf = f"-vf {vf}"
else:
    print("Not adding video filters")

command = f"{v_file} {o_file} {v_codec} {a_codec} {v_bitrate} {a_bitrate} \
        {fps} {res} {duration_to_process} {start_time} {overwrite_if_exists}" 

print(f"This is your current working directory: {os.getcwd()}")

if input("Do you want to change directories and automatically run the generated command? y/n ") == "y":
    while not correct_dir:
        dir_to_arrive = input("What directory do you want to get to (can be relative or absolute)? ")
        if input(f"Is this correct y/n? {dir_to_arrive} ") == "n":
            print("Trying again...")
        else:
            print("Sounds good, continuing")
            correct_dir = True
    os.chdir(dir_to_arrive)

print(f"Copy paste this command {command}")