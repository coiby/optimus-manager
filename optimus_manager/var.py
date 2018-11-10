import optimus_manager.envs as envs


class VarError(Exception):
    pass


def read_startup_mode():

    try:
        with open(envs.STARTUP_MODE_FILE_PATH, 'r') as f:
            content = f.read()
            if content in ["intel", "nvidia", "inactive", "nvidia_once"]:
                mode = content
            else:
                raise VarError("Invalid value : %s" % content)
    except IOError:
        raise VarError("Cannot open or read %s" % envs.STARTUP_MODE_FILE_PATH)

    return mode


def write_startup_mode(mode):

    assert mode in ["intel", "nvidia", "inactive", "nvidia_once"]

    try:
        with open(envs.STARTUP_MODE_FILE_PATH, 'w') as f:
            f.write(mode)
    except IOError:
        raise VarError("Cannot open or write to %s" % envs.STARTUP_MODE_FILE_PATH)