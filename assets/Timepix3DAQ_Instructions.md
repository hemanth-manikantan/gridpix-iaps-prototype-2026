# Hardware Preparation and Acquisition

## Hardware preparation
1. **Low Voltage:** Use the All ON/OFF switcher.
2. **Power on** the FEC.

## Monitor opening
3. On the control PC, open a terminal in the `online-monitor` folder (bookmarked) and type:
   ```bash
   python start_tpx3_monitor.py
   ```
4. In the monitor window, select the **TPX3** tab.

## Control software
5. Open a new terminal window (in any folder).
6. Type:
   ```bash
   tpx3_gui
   ```
7. Once the GUI has been launched, click **Hardware init**.
8. Check that the ASIC is connected: the GUI should show a message saying: *"Connected to WF30-F11 (5 [6] active links)"*. If not, repeat Step 7.

## Acquisition
9. Click **Start readout** and set the desired acquisition time.
10. The monitor window should start showing the tracks.
11. Data will be saved to `Timepix3/data/hdf` (bookmarked).