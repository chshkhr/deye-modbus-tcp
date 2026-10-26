from __future__ import annotations
from ..inverter_def import ComputedRegisterDef, InverterDef, RegisterDef

INVERTER = InverterDef(
    key="deye_sun6k_sg05lp1",
    name="Deye SUN-6K-SG05LP1 (Single Phase)",
    manufacturer="Deye",
    model="SUN-6K-SG05LP1",

    temp_registers={90}, # Температура DC

    registers=[
        # Справжні LP1-регістри для однофазників Deye:
        RegisterDef("Inverter Temperature",   90,  "°C",  0.1,  "int16",  "temperature", "measurement",      "mdi:thermometer"),
        RegisterDef("Battery Voltage",        183, "V",   0.01, "uint16", "voltage",     "measurement",      "mdi:flash"),
        RegisterDef("Battery SOC",            184, "%",   1,    "uint16", "battery",     "measurement",      "mdi:battery"),
        RegisterDef("Battery Power",          190, "W",   1,    "int16",  "power",       "measurement",      "mdi:battery-charging"),
        RegisterDef("Battery Current",        191, "A",   0.01, "int16",  "current",     "measurement",      "mdi:current-dc"),
        RegisterDef("Grid Voltage L1",        150, "V",   0.1,  "uint16", "voltage",     "measurement",      "mdi:flash"),
        RegisterDef("Grid Frequency",         151, "Hz",  0.01, "uint16", "frequency",   "measurement",      "mdi:sine-wave"),
        RegisterDef("Grid Power",             169, "W",   1,    "int16",  "power",       "measurement",      "mdi:transmission-tower"),
        RegisterDef("Grid CT Power",          172, "W",   1,    "int16",  "power",       "measurement",      "mdi:transmission-tower"),
        RegisterDef("Load Power",             178, "W",   1,    "uint16", "power",       "measurement",      "mdi:home-lightning-bolt"),
        RegisterDef("PV1 Power",              186, "W",   1,    "uint16", "power",       "measurement",      "mdi:solar-power"),
        RegisterDef("PV2 Power",              187, "W",   1,    "uint16", "power",       "measurement",      "mdi:solar-power"),
        RegisterDef("PV1 Voltage",            109, "V",   0.1,  "uint16", "voltage",     "measurement",      "mdi:flash"),
        RegisterDef("PV2 Voltage",            111, "V",   0.1,  "uint16", "voltage",     "measurement",      "mdi:flash"),
    ],

    computed_registers=[
        ComputedRegisterDef(
            name="PV Total Power",
            unit="W",
            device_class="power",
            state_class="measurement",
            icon="mdi:solar-power",
            sources=["PV1 Power", "PV2 Power"],
        ),
    ],

    # Блоки читання для діапазону 0-299
    read_blocks=[
        (90, 1),
        (109, 3),
        (150, 2),
        (169, 4),
        (178, 1),
        (183, 2),
        (186, 2),
        (190, 2),
    ],
)
