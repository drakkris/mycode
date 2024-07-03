#!/usr/bin/env python3
"""Alta3 Research | Moving and copying files"""

# import additional code to complete our task
import shutil
import os

def main():
    # move into the working directory
    os.chdir("/home/student/mycode/")

    # copy the filaA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire dirA to dirB
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
