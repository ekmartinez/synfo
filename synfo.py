import os
import platform
import psutil

class Info_sys:
    def __init__(self):
        """To access indinvidual variables at run time"""
        self.cpu = platform.processor()
        self.cores = psutil.cpu_count(logical=False)
        self.logical_cores = psutil.cpu_count(logical=True)
        self.ram_memory = f"{round(psutil.virtual_memory()[0] / float(1e+6)):,} MiB"
        self.used_ram = f"{round(psutil.virtual_memory()[3] / float(1e+6)):,} MiB"
        self.available_ram = f"{round(psutil.virtual_memory()[1] / float(1e+6)):,} MiB"
        self.percentage_used = f"{psutil.virtual_memory()[2]}%"
        self.swap_memory = f"{round(psutil.swap_memory()[0] / float(1e+6)):,} MiB"
        self.used_swap = f"{round(psutil.swap_memory()[1] / float(1e+6)):,} MiB"
        self.available_swap = f"{round(psutil.swap_memory()[2] / float(1e+6)):,} MiB"
        self.percentage_swap_used = f"{psutil.swap_memory()[3]}%"
        self.hd_total = f"{round(psutil.disk_usage('/')[0] / (2**30)):,} GiB"
        self.used_hd = f"{round(psutil.disk_usage('/')[1] / (2**30)):,} GiB"
        self.available_hd = f"{round(psutil.disk_usage('/')[2] / (2**30)):,} GiB"
        self.percentage_hd_used = f"{psutil.disk_usage('/')[3]}%"
        self.uname = os.getlogin()
        self.os_platform = f"{platform.platform()} {platform.architecture()[0]}"

    def cpu_summary(self):
        """Displays CPU information in terms of architecture,
        cores and logical cores."""
        cpu_info = f"\nCPU Summary\n{'-'*60}\n"
        cpu_info += f"CPU Type: {self.cpu}\n"
        cpu_info += f"Cores: {self.cores}\n"
        cpu_info += f"Logical Cores: {self.logical_cores}\n"
        cpu_info += f"{'-'*60}\n"
        return cpu_info
        
    def ram_summary(self):
        """Displays RAM and Swap information in terms of total, used and
        available memory."""
        ram_info = f"\nRAM Summary\n{'-'*60}\n"
        ram_info += f"Total Ram: {self.ram_memory}\n"
        ram_info += f"Ram Used: {self.used_ram}\n"
        ram_info += f"Available Ram: {self.available_ram}\n"
        ram_info += f"Percentage Used: {self.percentage_used}\n"
        ram_info += f"\nTotal Swap: {self.swap_memory}\n"
        ram_info += f"Used Swap: {self.used_swap}\n"
        ram_info += f"Available Swap: {self.available_swap}\n"
        ram_info += f"Percentage Swap Used: {self.percentage_swap_used}%\n"
        ram_info += f"{'-'*60}\n"
        return ram_info

    def hd_summary(self):
        """Displays hard disk drive information in terms of total, used & available
        drive space."""
        hd_info = f"\nHard Disk Summary\n{'-'*60}\n"
        hd_info += f"Total Disk Space: {self.hd_total}\n"
        hd_info += f"Used Disk Space: {self.used_hd}\n"
        hd_info += f"Available Disk Space: {self.available_hd}\n"
        hd_info += f"Percentage Disk Space Used: {self.percentage_hd_used}%\n"
        hd_info += f"{'-'*60}\n"
        return hd_info
    
    def os_summary(self):
        """Displays Operating System information in terms of vendor, type,
        & current user name."""
        os_info = f"\nOperating System Summary\n{'-'*60}\n"
        os_info += f"User Name: {self.uname}\n"
        os_info += f"Operating System: {self.os_platform}\n"
        os_info += f"{'-'*60}\n"
        return os_info
        

    

  