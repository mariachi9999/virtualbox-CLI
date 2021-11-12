import virtualbox
import sys

message = "Create | Delete | Open | Close | Exit | Help "
print("CLI is running")
print("Please, select and type below your wanted option...")
print(message)


def cli_action():

    vbox = virtualbox.VirtualBox()
    machines = vbox.machines

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
        progress = machine.launch_vm_process(session, "headless", [])
        progress.wait_for_completion()
        print(sel_machine + " is running... To close it, type y below ")
        command = input(">: ")
        if command == "y":
            session.console.power_down()

    elif command == "Create":
        print("Choose below an OS to clone...")
        for machine in machines:
            print(machine.name)
        sel_machine = input(">: ")
        print("Choose a name for the new machine...")
        sel_name = input(">: ")
        print(sel_machine + " is creating...")
        machine_to_clone = vbox.find_machine(sel_machine)
        # session = virtualbox.Session()
        # progress = machine.launch_vm_process(session, "gui", [])
        # progress.wait_for_completion()
        # session.machine.take_snapshot(name="snapshot1",description="For study matters", pause=False)
        machine_to_clone.clone(name=sel_name)
        print(sel_name + " is created!")

    elif command == "Delete":
        print("Choose below an OS to remove...")
        for machine in machines:
            print(machine.name)
        sel_machine = input(">: ")
        print(sel_machine + " is being deleted...")
        machine_to_delete = vbox.find_machine(sel_machine)
        # session = virtualbox.Session()
        # progress = machine.launch_vm_process(session, "gui", [])
        # progress.wait_for_completion()
        # session.machine.take_snapshot(name="snapshot1",description="For study matters", pause=False)
        machine_to_delete.remove(delete=True)
        print(sel_machine + " has been deleted...")

    elif command == "Exit":
        sys.exit()

    elif command == "Help":
        print("Please, select and type below your wanted option...")
        print(message)

    else:
        print("Oops! It seems like your input isn't valid! Please, enter it again!")


while True:
    try:
        cli_action()
    except:
        print('Oops... It looks that something goes wrong!')
        print('Please, note that commands and vm are case sensitive')
        print('For more info, type Help on command line')
        cli_action()
