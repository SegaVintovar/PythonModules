import sys
import os
import site

"""
site modules
This is a standard Python module
that is automatically imported when Python starts.
It handles how Python sets up the environment.
It tells Python where your installed packages are located.

os.getcwd()
get a path to current working directory

sys.prefix()
shows from where python is started
if it is outside the virt env then it is /usr
if inside it is /path_to_the_virt_env/bin/python3

sys.base_prefix()
the real Python installation
show the root dir where we have all user programs
normally it is /usr

site.getsitepackages()
This returns the site-packages directory inside your virtual environment.

if prefix and base_prefix are different - we are inside virt env
"""

def main() -> None:
    """
    if we are inside virtual enviroment, prefix shows a
    full path to the place where the venv works, and
    in this case

    """

    if os.getcwd() in sys.prefix:
        matrix_status = "Welcome to the construct\n"
        in_virt_env = True
        result = "SUCCESS: You're in an isolated environment!\n"\
                    "Safe to install packages without affecting "\
                    "the global system.\n"
        name = os.path.basename(sys.prefix)
        virt_env = f"{name}"

    elif sys.prefix == sys.base_prefix:
        in_virt_env = False
        matrix_status = "You are sill plugged it\n"
        result = "WARNING: You're in the global environment! " + \
        "The machines can see everything you install"
        virt_env = "None detected"

    current_python = sys.executable
    print("\nMATRIX STATUS: ", matrix_status)
    print("Current Python: ", current_python)
    print("Virtual Environment: ", virt_env)
    print(result)
    if in_virt_env is True:
        print("Package installation path:\n", site.getsitepackages()[0])
    else:
        print(
            "\nTo enter the construct, run:\n",
            "python -m venv matrix_env",
            "\nsource matrix_env/bin/activate "
        )
        print("\nThen run this program again")

    # if os.getcwd() in sys.prefix:
    #     print("we are inside Virtual enviroment")
    #     print(sys.prefix)
    # elif sys.prefix == sys.base_prefix:
    #     print("WARNING: You're in the global environment!"
    #           "The machines can see everything you install.\n")
    #     
        
    # print(sys.executable)
    # print(os.getcwd())
    # print(sys.base_prefix)
    # print(sys.prefix)
    # print(sys.modules)

if __name__ == "__main__":
    main()