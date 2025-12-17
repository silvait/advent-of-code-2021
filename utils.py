def get_input_filename(argv):
    if len(argv) < 2:
        return argv[0].replace(".py", ".txt")

    return argv[1]
