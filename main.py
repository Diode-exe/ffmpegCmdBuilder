command = None
v_file = None
o_file = None

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

if input("Change video fps? y/n ")

print(f"Copy paste this command {command}")