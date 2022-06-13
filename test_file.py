from synfo import Info_sys

"""Examples"""

info = Info_sys()

#Displaing individual variables
print(info.cpu)
print(info.ram_memory)
print(info.hd_total)
print(info.os_platform)

#Displaying system summaries
print(info.cpu_summary())
print(info.ram_summary())
print(info.hd_summary())
print(info.os_summary())
