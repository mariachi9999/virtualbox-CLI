import virtualbox
# from tools import IMachine


vbox = virtualbox.VirtualBox()
machines = vbox.machines
# for machine in machines:
#     print(machine.name)

options = ["Create", "Delete", "Open", "Close"]


print("CLI is running")
print("Please, select and type below your wanted option...")
for option in options:
    print(option)
command = input(">: ")


if command == "Open":
    print("Choose and type below on of the following existing machines...")
    for machine in machines:
        print(machine.name)
    sel_machine = input(">: ")
    print(sel_machine + " is opening")
    session = virtualbox.Session()
    machine = vbox.find_machine(sel_machine)
    # progress = machine.launch_vm_process(session, "gui", "")
    # For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()
    command = input(">: ")

if command == "Close":
    session.console.power_down()
    command = input(">: ")

