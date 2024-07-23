import os
import sys

def restart_program():
    print("Restarting program...")
    # 重新执行当前脚本
    print(sys.executable, sys.executable, *sys.argv)
    os.execlp(sys.executable, sys.executable, *sys.argv)

if __name__ == "__main__":
    print("Original program")
    if len(sys.argv) > 1 and sys.argv[1] == "restarted":
        print("Program has been restarted")
    else:
        sys.argv.append("restarted")
        restart_program()
