# GECO2020 Operation & High Voltage Ramping Procedure

## 1. System Setup & Connection
1. Open **GECO2020** on the PC.
2. Click **File** $\rightarrow$ **Connect**.
3. Enter credentials:
   - **Username:** `admin`
   - **Password:** `admin`
4. Click **OK**.

---

## 2. Channel Configuration & Power-On

> **Hardware Configuration (1 bar / 1 cm setup):**
> - **CH0:** Grid
> - **CH4:** Anode
> - **CH5:** Window / Cathode

1. **Power On Channels:**
   - In row `CHANNEL00`, click the cell in the **Pw** column (it turns light green).
   - Click again and select **On** from the dropdown menu.
   - Repeat this process for `CHANNEL04` and `CHANNEL05`.
2. **Verify Ramp Speed:**
   - Confirm that the **RUp** and **RDwn** columns for all active channels are set to **10 Vps**.

---

## 3. Ramp-Up Sequence

> **Safety Caution:** Continuously monitor **IMon**—it must remain at **0 µA**. For each step, wait until the voltage on all channels stabilizes before advancing.

1. **Step 1 (Up to 400 V):** 
   - Ramp **CH5**, then **CH4** to **400 V** in **50 V steps**.
2. **Step 2 (Intermediate Adjustment):**
   - Ramp **CH5**, then **CH4** to **450 V**.
   - Ramp **CH0** to **430 V**.
3. **Step 3 (Up to 580 V):**
   - Ramp **CH5**, then **CH4** to **580 V** in **50 V steps** (the last step is **30 V**).
4. **Step 4 (Final Voltage):**
   - Ramp **CH5** to **1580 V** in one continuous run at **10 Vps**.

> **Final Target State:**
> - **Grid (CH0):** 430 V
> - **Anode (CH4):** 580 V
> - **Cathode / Window (CH5):** 1580 V

---

## 4. Ramp-Down Sequence

1. Lower **CH5** to **580 V**.
2. Lower **CH4** and **CH5** to **450 V** (set **CH4** first, followed by **CH5**).
3. Set voltage to **0 V** in the following order:
   1. **CH0**
   2. **CH4**
   3. **CH5**