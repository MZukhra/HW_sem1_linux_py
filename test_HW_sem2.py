import subprocess


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout or text in result.stderr) and result.returncode != 0:
        return True
    else:
        return False


dir_in = "/home/zm/in"
dir_out = "/home/zm/out"
dir_ext = "/home/zm/unpacking"


def test_step1():
    assert checkout_negative(f'cd {dir_out}; 7z e 27CQW -o{dir_ext} -y', 'Can not open the file as archive'), "Test1 FAIL"


def test_step2():
    assert checkout_negative(f'cd {dir_out}; 7z t 27CQW', 'Can not open the file as archive'), "Test2 FAIL"
