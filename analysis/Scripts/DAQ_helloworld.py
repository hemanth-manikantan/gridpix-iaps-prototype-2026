'''This script intends to utilize the CLI for DAQ with a python script'''

'''#!/usr/bin/env python3'''
#!/home/ixpe_user/miniforge/envs/tpx3/bin python3

#!/usr/bin/env python3
import sys
import os
import time

# Ensure Python can find the tpx3 package components
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/ixpe_user/tpx3-daq/UI/CLI/')))

# Import the CLI function wrapper and the datalogger
from tpx3_cli import TPX3_CLI_function_call
from UI.tpx3_logger import TPX3_datalogger

def print_hardware_configuration():
    print("\n" + "="*50)
    print("      CURRENT TIMEPIX3 DETECTOR CONFIGURATION")
    print("="*50)
    
    # Extract structural metadata values cached inside the logger interface
    v_thresh = TPX3_datalogger.read_value(name='Vthreshold_combined')
    mask_file = TPX3_datalogger.read_value(name='Mask_path')
    equal_file = TPX3_datalogger.read_value(name='Equalisation_path')
    
    # Handle clean string printing for unset configurations
    mask_print = os.path.basename(mask_file) if mask_file else "No Active Mask (Unmasked)"
    equal_print = os.path.basename(equal_file) if equal_file else "No Uniform Equalization Loaded"
    
    print(f" Loaded Threshold DAC     : {v_thresh} (fine/coarse combined value)")
    print(f" Active Pixel Mask Map    : {mask_print}")
    print(f" Matrix Equalization Map  : {equal_print}")
    print("="*50 + "\n")

def print_chip_names():
    print("\n[2/4] Querying Connected Hardware Entities ('Who')...")
    print('Connected chips are:')
    
    # Replicates the exact behavior of the 'Who' / 'chip_names' CLI command
    chip_names = TPX3_datalogger.get_chipnames()
    if not chip_names:
        print("No chips currently detected in datalogger.")
        return

    for Chipname in chip_names:
        number_of_links = TPX3_datalogger.get_links(chipname=Chipname)
        if number_of_links == 1:
            print(Chipname + ' on ' + str(number_of_links) + ' active link')
        else:
            print(Chipname + ' on ' + str(number_of_links) + ' active links')

def main():
    print("--- Starting Automated GridPix Lab Execution ---")
    
    # Instantiate the standard CLI interaction class
    cli = TPX3_CLI_function_call()
    
    # 1. Initialize Hardware Framework
    print("\n[1/4] Dispatching Hardware Initialization...")
    # Directly calls the built-in Initialise_Hardware function
    chip_list = cli.Initialise_Hardware()
    
    # Store the firmware and link updates into the logger exactly as the CLI loop does
    if chip_list:
        try:
            TPX3_datalogger.write_value(name='firmware_version', value=chip_list.pop(0))
            TPX3_datalogger.write_value(name='hardware_links', value=chip_list.pop(0))
            for n in range(len(chip_list)):
                name = 'Chip' + str(n) + '_name'
                TPX3_datalogger.write_value(name=name, value=chip_list.pop(0))
        except IndexError:
            pass
        print("Hardware pipeline linked successfully.")

    # 2. Check and Print Chip Names & Active Link Connections Status
    print_chip_names()

    # 3. Print the Configuration Parameters (DAC, Mask, Equalization)
    # print("\n[3/4] Pulling Environment Configuration Logs...")
    # print_hardware_configuration()

    # 4. Handle Timed Data Take Runtime Processing Loop
    shutter_time = 100
    if len(sys.argv) > 1:
        try:
            shutter_time = int(sys.argv[1])
        except ValueError:
            print(f"Could not convert input argument to integer. Reverting to {shutter_time}s.")

    print(f"[4/4] Triggering Acquisition Window ('r') for {shutter_time} Seconds...")
    try:
        # Directly calls the built-in Run_Datataking function, passing the shutter time
        cli.Run_Datataking(scan_timeout=shutter_time)
        print("\n--- Sequence Execution Terminated Safely ---")
        
    except KeyboardInterrupt:
        print("\n[Aborted] Run broken via terminal kill instruction. Safe shutdown executed.")
        sys.exit(1)

if __name__ == "__main__":
    main()